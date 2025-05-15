# Mapeo de etiquetas numéricas a texto
etiquetas = {
    0: "tristeza",
    1: "alegría",
    2: "amor",
    3: "enojo",
    4: "miedo",
    5: "sorpresa"
}

# Respuestas emocionales
respuestas = {
    "tristeza": "Siento que estés triste. Estoy aquí para escucharte. 💙",
    "alegría": "¡Me alegra que te sientas bien! 😊",
    "amor": "Eso suena muy especial ❤️",
    "enojo": "Está bien estar molesto a veces. ¿Quieres contármelo?",
    "miedo": "Parece que algo te preocupa. Estoy contigo. 🫶",
    "sorpresa": "¡Qué sorpresa! Cuéntame más."
}

def obtener_emocion_texto(label):
    return etiquetas.get(label, "desconocida")

def generar_respuesta(emocion):
    return respuestas.get(emocion, "Gracias por compartir cómo te sientes.")
