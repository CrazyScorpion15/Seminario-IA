from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utilidad import obtener_emocion_texto, generar_respuesta
from deep_translator import GoogleTranslator

app = FastAPI()

# Cargar modelo entrenado en inglés
modelo = joblib.load("modelo_emociones.pkl")

class Message(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(msg: Message):
    # 🌐 Traducir mensaje del usuario de español a inglés
    try:
        text_en = GoogleTranslator(source='auto', target='en').translate(msg.text)
    except:
        text_en = msg.text  # fallback si falla traducción

    # 🔍 Clasificar emoción
    label = modelo.predict([text_en])[0]
    emocion = obtener_emocion_texto(label)
    respuesta = generar_respuesta(emocion)

    return {
        "emotion": emocion,
        "response": respuesta
    }
