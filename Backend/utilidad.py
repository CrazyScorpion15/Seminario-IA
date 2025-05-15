import random

respuestas = {
    "tristeza": [
        "Lamento que te sientas así. ¿Qué te ha pasado?",
        "Estoy aquí para escucharte. No estás solo/a.",
        "Hablar de lo que sientes puede ayudarte un poco. ¿Quieres contarme?",
        "Parece que estás atravesando un momento difícil. Estoy contigo.",
        "A veces la tristeza es parte del proceso. Tómate tu tiempo.",
        "Estoy a tu lado, incluso si ahora no parece suficiente.",
        "Puedes compartir lo que estás sintiendo. Estoy para ti.",
        "¿Qué es lo que más te duele ahora mismo?",
        "Estoy contigo, sin juzgarte. ¿Qué te gustaría decir primero?",
        "Tus emociones son válidas. Aquí estoy para apoyarte."
    ],
    "alegría": [
        "¡Qué bien que estés así! ¿Qué fue lo que te hizo sentir tan feliz?",
        "Tu alegría me alegra a mí también. Cuéntame más.",
        "¡Eso es genial! ¿Con quién compartiste ese momento?",
        "Me encanta leer eso. Sigue disfrutando el momento 😊",
        "¿Qué fue lo mejor de tu día?",
        "¡Tu energía positiva se siente incluso por aquí!",
        "Cuéntame, ¿qué fue lo que te hizo sonreír hoy?",
        "¡Qué bonito! Me encantaría saber más.",
        "¡Guau! Se nota que estás pasando un gran momento.",
        "¿Te gustaría recordar este día dentro de un año?"
    ],
    "amor": [
        "Ese sentimiento es muy especial. ¿Cómo te diste cuenta?",
        "El amor puede transformar nuestra forma de ver todo.",
        "Se nota que esa persona es muy importante para ti.",
        "Qué hermoso es poder sentir algo tan profundo.",
        "¿Cómo te hace sentir estar cerca de esa persona?",
        "Hablar de amor es algo poderoso. Cuéntame más.",
        "¿Recuerdas cuándo empezó a crecer ese sentimiento?",
        "A veces el amor llega sin avisar, y es maravilloso.",
        "Es lindo que puedas expresar tus emociones así.",
        "Tu corazón parece lleno. Cuídalo bien."
    ],
    "enojo": [
        "Puedo entender que eso te cause enojo. ¿Qué fue lo que pasó?",
        "¿Qué te hizo sentir tan frustrado/a?",
        "Hablar de lo que te molesta puede ayudarte a soltarlo.",
        "Estoy aquí si necesitas desahogarte.",
        "¿Hay algo que puedas hacer para sentirte más en control?",
        "A veces expresar lo que sientes ya es un primer paso.",
        "El enojo también es válido. Vamos a entenderlo juntos.",
        "¿Te ha pasado antes algo así?",
        "¿Qué parte te molesta más? Estoy contigo.",
        "Respirar profundo puede ayudarte. ¿Quieres intentarlo juntos?"
    ],
    "miedo": [
        "Parece que hay algo que te preocupa mucho. ¿Qué es?",
        "Estoy aquí para ayudarte a sentirte más seguro/a.",
        "A veces hablar del miedo le quita poder.",
        "¿Hay algo que puedas hacer ahora para sentirte más tranquilo/a?",
        "Tu miedo es válido. No estás solo/a en esto.",
        "Vamos paso a paso. ¿Qué es lo que más te inquieta ahora?",
        "Estoy contigo. ¿Quieres que pensemos en soluciones juntos?",
        "A veces el miedo protege, pero no debe detenernos.",
        "Dime más sobre lo que sientes. Estoy para apoyarte.",
        "¿Qué crees que podría ayudarte en este momento?"
    ],
    "sorpresa": [
        "¡Eso sí que fue inesperado! ¿Cómo te sentiste al instante?",
        "¡Qué giro tan sorprendente! ¿Qué pasó después?",
        "¡No me lo habría imaginado! Cuéntame más.",
        "¡Wow! ¿Te impactó de forma positiva o negativa?",
        "A veces la vida nos lanza sorpresas. ¿Te gustó?",
        "¡Qué inesperado! ¿Cómo reaccionaste tú?",
        "¿Te preparaste para algo así o fue repentino?",
        "Suena como algo que no pasa todos los días.",
        "¡Eso debió tomarte por sorpresa! ¿Qué hiciste?",
        "¡Guau! A veces las sorpresas son oportunidades disfrazadas."
    ]
}

etiquetas = {
    0: "tristeza",
    1: "alegría",
    2: "amor",
    3: "enojo",
    4: "miedo",
    5: "sorpresa"
}

def obtener_emocion_texto(label):
    return etiquetas.get(label, "desconocida")

def generar_respuesta(emocion):
    lista = respuestas.get(emocion, ["Gracias por compartir cómo te sientes."])
    return random.choice(lista)
