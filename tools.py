from langchain.agents import Tool
from utils import analyze_sentiment_text, evaluate_coherence_text

# Ferramenta 1: Analisador de Sentimentos
sentiment_tool = Tool(
    name="Analisador de Sentimento",
    func=analyze_sentiment_text,
    description="Usado para determinar o sentimento (Positivo, Negativo ou Neutro) do texto fornecido."
)

# Ferramenta 2: Avaliador de Coerência
coherence_tool = Tool(
    name="Avaliador de Coerência",
    func=evaluate_coherence_text,
    description="Usado para avaliar a coerência do texto fornecido, retornando uma pontuação de 0 a 10."
)

