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
