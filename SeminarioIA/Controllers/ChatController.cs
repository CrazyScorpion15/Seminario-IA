using Microsoft.AspNetCore.Mvc;
using SeminarioIA.Models;
using Newtonsoft.Json;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Net.Mail;
using System.Net;

namespace SeminarioIA.Controllers
{
    public class ChatController : Controller
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public ChatController(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }
        public IActionResult Chat()
        {
            var userJson = HttpContext.Session.GetString("UsuarioChat");
            UsuarioChat user = null;

            if (!string.IsNullOrEmpty(userJson))
            {
                user = JsonConvert.DeserializeObject<UsuarioChat>(userJson);
            }

            ViewBag.Usuario = user;
            return View();
        }

        [HttpPost]
        public IActionResult GuardarDatos(string nombre, string nombreEmergencia, int numeroEmergencia, string correoEmergencia)
        {
            var usuario = new UsuarioChat
            {
                Nombre = nombre,
                NombreEmergencia = nombreEmergencia,
                NumeroEmergencia = numeroEmergencia,
                Email = correoEmergencia
            };

            HttpContext.Session.SetString("UsuarioChat", JsonConvert.SerializeObject(usuario));
            return RedirectToAction("Chat");
        }

        [HttpPost]
        public async Task<IActionResult> EnvioMensaje([FromBody] MensajeChat chat)
        {
            try
            {
                var client = _httpClientFactory.CreateClient();
                var content = new StringContent(System.Text.Json.JsonSerializer.Serialize(new { text = chat.Texto }),
                                                Encoding.UTF8, "application/json");

                var response = await client.PostAsync("http://127.0.0.1:8000/analyze", content);
                var responseBody = await response.Content.ReadAsStringAsync();

                using var doc = JsonDocument.Parse(responseBody);
                chat.Emocion = doc.RootElement.GetProperty("emotion").GetString();
                chat.Respuesta = doc.RootElement.GetProperty("response").GetString();

                int tristeza = HttpContext.Session.GetInt32("ContadorTristeza") ?? 0;
                int enojo = HttpContext.Session.GetInt32("ContadorEnojo") ?? 0;

                if (chat.Emocion == "tristeza")
                    HttpContext.Session.SetInt32("ContadorTristeza", ++tristeza);
                if (chat.Emocion == "enojo")
                    HttpContext.Session.SetInt32("ContadorEnojo", ++enojo);

                if (tristeza >= 3 || enojo >= 3)
                {
                    var usuarioJson = HttpContext.Session.GetString("UsuarioChat");
                    if (usuarioJson != null)
                    {
                        var usuario = JsonConvert.DeserializeObject<UsuarioChat>(usuarioJson);
                        EnviarCorreoAlerta(usuario);
                    }

                    // Reiniciar contadores para evitar spam
                    HttpContext.Session.SetInt32("ContadorTristeza", 0);
                    HttpContext.Session.SetInt32("ContadorEnojo", 0);
                }


                return Json(new { emocion = chat.Emocion, respuesta = chat.Respuesta });
            }
            catch (Exception)
            {
                chat.Emocion = "No hay emociones";
                chat.Respuesta = "No existe respuesta";
                return Json(new { emocion = chat.Emocion, respuesta = chat.Respuesta });
            }


        }

        private void EnviarCorreoAlerta(UsuarioChat usuario)
        {            
            string destinatario = usuario.Email;
            string asunto = $"🚨 Alerta emocional: {usuario.Nombre}";
            string cuerpo = $@"
Hola {usuario.NombreEmergencia},

El sistema detectó varias emociones negativas (como tristeza o enojo) en los mensajes recientes de {usuario.Nombre}.

Número de emergencia registrado: {usuario.NumeroEmergencia}
Hora de alerta: {DateTime.Now}

Este mensaje es automático. Considere ponerse en contacto si es necesario.

Atentamente,
MindBuddy";

            using var smtp = new SmtpClient("smtp.gmail.com")
            {
                Port = 587,
                Credentials = new NetworkCredential("edryanandre@gmail.com", "pkxrxssobkfjuwiy"),
                EnableSsl = true
            };

            var mail = new MailMessage("tucorreo@gmail.com", destinatario, asunto, cuerpo);
            smtp.Send(mail);
        }
    }
}
