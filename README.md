# Seminario-IA
# MindBuddy – Asistente emocional con detección de sentimientos

**MindBuddy** es un chatbot desarrollado en ASP.NET MVC y Python (FastAPI) que proporciona respuestas empáticas a los usuarios analizando sus emociones a partir del texto que escriben. Está diseñado especialmente para apoyar emocionalmente a jóvenes mediante conversaciones seguras y humanas.

---

## Características principales

- Detección de emociones en tiempo real (tristeza, alegría, amor, enojo, miedo y sorpresa)
- Respuestas empáticas y variadas por emoción
- Backend en Python (FastAPI) con un modelo Naïve Bayes entrenado con el dataset de Kaggle
- Traducción automática del texto (español → inglés) para aprovechar un modelo entrenado en inglés
- Contador de emociones negativas para activar alertas
- Envío automático de correo al contacto de emergencia si se detectan patrones de riesgo emocional

---

## Tecnologías utilizadas

- Frontend: **ASP.NET MVC (.NET Core)**  
- Backend: **FastAPI + scikit-learn**
- Dataset: [Kaggle - Emotion Detection](https://www.kaggle.com/datasets/nelgiriyewithana/emotions)
- Traducción: `deep-translator` (Google Translate API)
- Sesiones: ASP.NET Core Session Middleware
- Correo SMTP: `System.Net.Mail`

---

## ¿Cómo funciona?

1. El usuario llena un formulario inicial con su nombre y contacto de emergencia.
2. Ingresa mensajes en el chat.
3. Cada mensaje se envía al backend (FastAPI), donde se:
   - Traduce al inglés (si está en español).
   - Clasifica la emoción con el modelo Naïve Bayes.
   - Devuelve una respuesta empática seleccionada aleatoriamente.
4. Si se detectan **5 emociones negativas seguidas (tristeza o enojo)**, se activa una alerta por correo electrónico.

---
