# test_agent.py

from agent import create_agent

def main():
    agent = create_agent()
    user_input = input("Digite o texto para análise: ")

    print("Analisando...")
    result = agent.invoke(input=user_input)
    print("Resultado:")
    print(result)

if __name__ == "__main__":
    main()
