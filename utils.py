import os
import openai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

import openai

def analyze_sentiment_text(text):
    prompt = f"Analise o sentimento do seguinte texto e responda apenas com 'Positivo', 'Negativo' ou 'Neutro':\n\n{text}"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que analisa o sentimento de textos."},
            {"role": "user", "content": prompt}
        ],
    )
    sentiment = completion.choices[0].message.content.strip()
    return sentiment


def evaluate_coherence_text(text):
    prompt = (
        f"Avalie a clareza e coerência do seguinte texto e responda apenas com um número de 0 a 10, "
        f"onde 10 representa máxima coerência:\n\n{text}"
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que avalia a coerência de textos."},
            {"role": "user", "content": prompt}
        ],
    )
    score_str = completion.choices[0].message.content.strip()
    try:
        score = float(score_str)
    except ValueError:
        score = 0  # Valor padrão caso a conversão falhe
    return score

