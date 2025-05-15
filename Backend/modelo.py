import pandas as pd
import kagglehub
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Descargar el dataset desde KaggleHub
print("Descargando dataset...")
dataset_path = kagglehub.dataset_download("nelgiriyewithana/emotions")

#Confirmar y cargar archivo correcto
file_path = os.path.join(dataset_path, "text.csv")
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

#Cargar dataset original
print("Cargando datos...")
df = pd.read_csv(file_path)  # ya tiene columnas: 'text' y 'label'

# (Opcional) Tomar una muestra para entrenamiento rápido
# df = df.sample(n=5000, random_state=42).reset_index(drop=True)

#Crear el pipeline con vectorización + Naïve Bayes
print("🔧 Entrenando modelo Naïve Bayes...")
modelo = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

modelo.fit(df["text"], df["label"])

#Guardar el modelo entrenado
joblib.dump(modelo, "modelo_emociones.pkl")
print("✅ Modelo entrenado y guardado como 'modelo_emociones.pkl'")
