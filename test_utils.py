# test_utils.py

from utils import analyze_sentiment_text, evaluate_coherence_text

def main():
    user_input = input("Digite o texto para análise: ")

    print("Testando a função analyze_sentiment_text...")
    sentimento = analyze_sentiment_text(user_input)
    print(f"Sentimento: {sentimento}")

    print("\nTestando a função evaluate_coherence_text...")
    coerencia = evaluate_coherence_text(user_input)
    print(f"Coerência: {coerencia}/10")

if __name__ == "__main__":
    main()
