import pandas as pd
import kagglehub
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Paso 1: Descargar y cargar dataset
print("Descargando dataset...")
dataset_path = kagglehub.dataset_download("nelgiriyewithana/emotions")
file_path = os.path.join(dataset_path, "text.csv")

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

print("Cargando datos...")
df = pd.read_csv(file_path)  # columnas: text, label

# Paso 2: Balancear el dataset (igualar número de ejemplos por emoción)
print("Balanceando dataset...")
min_clases = df["label"].value_counts().min()
df_balanced = df.groupby("label").apply(lambda x: x.sample(min_clases, random_state=42)).reset_index(drop=True)

print("Dataset balanceado:")
print(df_balanced["label"].value_counts())

# Paso 3: Entrenar modelo con TfidfVectorizer
print("Entrenando modelo con Tfidf...")
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(df_balanced["text"], df_balanced["label"])

# Paso 4: Guardar el modelo
joblib.dump(pipeline, "modelo_emociones.pkl")
print("✅ Modelo guardado como 'modelo_emociones.pkl'")
