import torch
from transformers import AutoTokenizer, AutoModel
import pinecone
import os

class RAGModule:
    def __init__(self, api_key: str, environment: str, index_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        pinecone.init(api_key=api_key, environment=environment)
        self.index = pinecone.Index(index_name)

    def embed_text(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            embeddings = self.model(**inputs).last_hidden_state.mean(dim=1)
        return embeddings

    def upsert_vector(self, unique_id: str, text: str):
        vector = self.embed_text(text)
        self.index.upsert([({"id": unique_id, "values": vector[0].tolist()})])

    def query_vectors(self, query_text: str, top_k: int = 5):
        query_vector = self.embed_text(query_text)
        return self.index.query(vector=query_vector[0].tolist(), top_k=top_k, include_metadata=True)

# Exemplo de uso (para demonstração, as chaves devem vir de variáveis de ambiente ou configuração)
if __name__ == "__main__":
    # Certifique-se de definir estas variáveis de ambiente
    # export PINECONE_API_KEY="YOUR_API_KEY"
    # export PINECONE_ENVIRONMENT="YOUR_ENVIRONMENT"
    # export PINECONE_INDEX_NAME="YOUR_INDEX_NAME"

    api_key = os.getenv("PINECONE_API_KEY", "YOUR_API_KEY")
    environment = os.getenv("PINECONE_ENVIRONMENT", "YOUR_ENVIRONMENT")
    index_name = os.getenv("PINECONE_INDEX_NAME", "my-index")

    rag_module = RAGModule(api_key, environment, index_name)

    # Exemplo de upsert
    rag_module.upsert_vector("doc1", "O Qiskit é um framework de código aberto para computação quântica.")
    rag_module.upsert_vector("doc2", "O Algoritmo de Deutsch-Jozsa é um algoritmo quântico.")

    # Exemplo de query
    results = rag_module.query_vectors("O que é Qiskit?")
    print("Resultados da busca:", results)
