#!/bin/bash

# Etapa 4: Criar o arquivo requirements.txt
echo "Criando o arquivo requirements.txt com as dependências do projeto..."
cat << EOF > requirements.txt
google-generativeai
fastapi
uvicorn[standard]
redis
psycopg2-binary
numpy
pandas
langchain
crewai
autogen
lama-index
EOF

# Etapa 1: Salvar as alterações no Git
echo "Adicionando todas as alterações ao Git e criando um commit..."
git add .
git commit -m "refactor: Implementa a arquitetura agêntica de 8 camadas no Maḥbūb"

# Etapa 2: Implementar a Camada de Cognição
echo "Criando o CognitiveCore em src/cognition/core.py..."
cat << 'EOF' > src/cognition/core.py
# src/cognition/core.py
import os
import google.generativeai as genai

class CognitiveCore:
    """
    Gerencia a interação com o LLM Gemini.
    Este é o 'cérebro' central do agente.
    """
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("A variável de ambiente GEMINI_API_KEY não foi definida.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def reason(self, prompt: str) -> str:
        """
        Envia um prompt para o LLM e retorna a resposta.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Erro durante a chamada ao LLM: {e}")
            return "Erro: Não foi possível obter uma resposta do modelo."
EOF

# Etapa 3: Criar um Agente de Teste na Camada de Aplicação
echo "Criando um ponto de entrada de teste em src/application/main.py..."
cat << 'EOF' > src/application/main.py
# src/application/main.py
import sys
import os

# Adiciona a raiz do projeto ao path do Python para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.cognition.core import CognitiveCore

def run_test_agent():
    """
    Um agente de teste simples que usa o CognitiveCore para responder a uma pergunta.
    """
    print("Inicializando o Agente de Teste...")
    
    # Para este teste, garanta que você definiu a variável de ambiente:
    # export GEMINI_API_KEY="SUA_CHAVE_API"
    if not os.getenv("GEMINI_API_KEY"):
        print("\nErro: A variável de ambiente GEMINI_API_KEY não está definida.")
        print("Por favor, defina-a para executar o agente de teste.")
        return

    try:
        cognitive_core = CognitiveCore()
        prompt = "Explique o papel da camada de Cognição em uma arquitetura de IA Agêntica em uma frase."
        
        print(f"\nEnviando prompt: '{prompt}'")
        response = cognitive_core.reason(prompt)
        
        print("\nResposta do Cognitive Core:")
        print("-" * 30)
        print(response)
        print("-" * 30)
        
        print("\nAgente de Teste finalizado.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    run_test_agent()
EOF

# Tornar o script executável
chmod +x setup_mahbub_architecture.sh

echo "\nScript 'setup_mahbub_architecture.sh' criado com sucesso."
echo "Para executar os próximos passos, use o comando: ./setup_mahbub_architecture.sh"
