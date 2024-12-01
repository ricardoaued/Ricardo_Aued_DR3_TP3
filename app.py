# app.py

import streamlit as st
from agent import create_agent

def main():
    st.set_page_config(page_title="Analisador de Conversas para Entrevistas", layout="wide")
    st.title("Analisador de Conversas para Entrevistas")
    st.write("""
        Insira o texto da conversa (entrevista, questionário ou dinâmica de grupo) para analisar o sentimento e a coerência da comunicação.
    """)

    # Cria o agente
    agent = create_agent()

    user_input = st.text_area("Insira o texto para análise:", height=300)

    if st.button("Analisar"):
        if user_input.strip() == "":
            st.warning("Por favor, insira um texto para análise.")
        else:
            with st.spinner("Analisando..."):
                try:
                    # Executa o agente com a entrada do usuário
                    result = agent.run(user_input)
                    st.success("Análise Completa!")
                    st.markdown("### Resultado da Análise")

                    # Exibir o resultado bruto para depuração
                    st.write("**Resultado bruto do agente:**")
                    st.write(result)

                    # Processar o resultado
                    linhas = result.strip().split('\n')
                    sentimento = None
                    coerencia = None
                    for linha in linhas:
                        if 'Sentimento:' in linha:
                            sentimento = linha.split('Sentimento:')[1].strip()
                        elif 'Coerência:' in linha:
                            coerencia = linha.split('Coerência:')[1].strip()
                    if sentimento:
                        st.write(f"**Sentimento:** {sentimento}")
                    if coerencia:
                        st.write(f"**Coerência:** {coerencia}/10")
                    if not sentimento and not coerencia:
                        st.write("Nenhuma análise foi encontrada no resultado.")

                except Exception as e:
                    st.error(f"Ocorreu um erro durante a análise: {e}")

if __name__ == "__main__":
    main()
