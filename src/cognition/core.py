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
