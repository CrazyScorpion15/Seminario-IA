using Microsoft.AspNetCore.Mvc;
using SeminarioIA.Models;
using Newtonsoft.Json;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

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
        public IActionResult GuardarDatos(string nombre, string nombreEmergencia, int numeroEmergencia)
        {
            var usuario = new UsuarioChat
            {
                Nombre = nombre,
                NombreEmergencia = nombreEmergencia,
                NumeroEmergencia = numeroEmergencia
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

                return Json(new { emocion = chat.Emocion, respuesta = chat.Respuesta });
            }
            catch (Exception)
            {
                chat.Emocion = "No hay emociones";
                chat.Respuesta = "No existe respuesta";
                return Json(new { emocion = chat.Emocion, respuesta = chat.Respuesta });
            }
        }


    }
}
