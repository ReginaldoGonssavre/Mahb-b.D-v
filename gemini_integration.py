import google.generativeai as genai
import os

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_content(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating content from Gemini: {e}"

# Exemplo de uso (para demonstração)
if __name__ == "__main__":
    # Defina a variável de ambiente GEMINI_API_KEY antes de executar
    # export GEMINI_API_KEY="SUA_CHAVE_API_GEMINI"
    try:
        gemini_client = GeminiClient()
        response = gemini_client.generate_content("Explique o conceito de computação quântica em uma frase.")
        print(response)
    except ValueError as e:
        print(e)
