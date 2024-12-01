# Analisador de Conversas com IA

## Descrição do Projeto

Este projeto desenvolve um agente de inteligência artificial capaz de analisar textos provenientes de conversas de entrevistas, respostas a questionários ou dinâmicas de grupo. O agente identifica o sentimento predominante e avalia a coerência da comunicação, auxiliando profissionais de recursos humanos e recrutadores na análise eficiente de candidatos.

## Funcionalidades

- **Análise de Sentimento:** Determina se o texto possui um sentimento positivo, negativo ou neutro.
- **Avaliação de Coerência:** Avalia a clareza e a lógica da comunicação, fornecendo uma pontuação de 0 a 10.
- **Interface Intuitiva:** Permite a inserção fácil de textos para análise através de uma interface web simples.
- **Histórico de Análises:** Mantém o histórico das análises realizadas durante a sessão.

## Casos de Uso Testados e Resultados Observados

1. **Entrevistas de Recrutamento:**
   - **Entrada:** Transcrição de entrevista de um candidato.
   - **Resultado:** Identificação de sentimentos positivos na comunicação e alta coerência, indicando clareza nas respostas.
   
2. **Questionários de Avaliação:**
   - **Entrada:** Respostas a um questionário de personalidade.
   - **Resultado:** Sentimento neutro e coerência moderada, sugerindo respostas bem estruturadas mas sem expressar emoções fortes.

3. **Dinâmicas de Grupo:**
   - **Entrada:** Registro de interações durante uma dinâmica de grupo.
   - **Resultado:** Sentimentos mistos com coerência variada, destacando áreas de melhoria na comunicação do grupo.

### Exemplos de Resultados

- **Sentimento:** Positivo
- **Coerência:** 8.5

---

## Instruções para Execução do Código

### Pré-requisitos

- Python 3.7 ou superior
- Conta na [OpenAI](https://openai.com/) para obter uma chave de API

### Passos para Configuração e Execução

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/analisador-conversacional.git
   cd analisador-conversacional