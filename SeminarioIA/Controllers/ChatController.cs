using Microsoft.AspNetCore.Mvc;

namespace SeminarioIA.Controllers
{
    public class ChatController : Controller
    {
        public IActionResult Chat()
        {
            return View();
        }
    }
}
