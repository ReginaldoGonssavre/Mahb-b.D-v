
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import os

# Supondo que agent_orchestrator.py e suas dependências estão no mesmo diretório
from agent_orchestrator import AgentOrchestrator

# --- Validação de Dados ---
# Modelo Pydantic para a requisição do Telegram
class TelegramWebhook(BaseModel):
    message: dict

# --- Inicialização ---
app = FastAPI(
    title="Maḥbūb Webhook Server",
    description="Recebe webhooks de serviços externos para interagir com os agentes Maḥbūb.",
    version="0.1.0"
)

# Instancia o orquestrador de agentes uma vez na inicialização
# Isso garante que o SupabaseManager e outros recursos não sejam reinicializados a cada requisição
try:
    orchestrator = AgentOrchestrator()
    print("Webhook Server: AgentOrchestrator carregado com sucesso.")
except Exception as e:
    print(f"Erro crítico ao inicializar o AgentOrchestrator: {e}")
    orchestrator = None

# --- Endpoints da API ---
@app.post("/webhooks/telegram/{agent_id}")
async def receive_telegram_webhook(agent_id: str, webhook_data: TelegramWebhook, request: Request):
    """
    Recebe uma notificação de webhook do Telegram e a encaminha para o agente apropriado.
    """
    if not orchestrator:
        raise HTTPException(status_code=500, detail="Erro interno: Orquestrador de agentes não está disponível.")

    # Validação de Segurança (Simples)
    # Em produção, você DEVE validar o token secreto do Telegram aqui
    # telegram_secret_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
    # if not telegram_secret_token or telegram_secret_token != os.getenv("TELEGRAM_SECRET_TOKEN"):
    #     raise HTTPException(status_code=403, detail="Acesso negado: Token secreto inválido.")

    try:
        # Extrai a mensagem do usuário do payload do Telegram
        user_query = webhook_data.message.get("text")
        chat_id = webhook_data.message.get("chat", {}).get("id")

        if not user_query or not chat_id:
            raise HTTPException(status_code=400, detail="Payload inválido: 'text' ou 'chat.id' não encontrados.")

        print(f"Webhook recebido para o agente '{agent_id}' do chat ID '{chat_id}': '{user_query}'")

        # Processa a requisição usando o orquestrador
        agent_response = orchestrator.process_request(
            agent_id=agent_id,
            user_query=user_query,
            conversation_id=f"telegram_{chat_id}" # Cria um ID de conversação único
        )

        # A resposta para o Telegram geralmente é enviada por outra chamada de API ao bot,
        # não diretamente na resposta do webhook. Aqui, apenas confirmamos o recebimento.
        # O ideal seria ter uma função para enviar a `agent_response` de volta para o `chat_id`.
        print(f"Resposta do agente: {agent_response}")
        return {"status": "success", "message": "Webhook processado.", "agent_response": agent_response}

    except Exception as e:
        print(f"Erro ao processar o webhook do Telegram: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno ao processar o webhook: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Servidor de Webhooks Maḥbūb está no ar."}

# --- Execução ---
if __name__ == "__main__":
    # Para rodar este servidor:
    # 1. Instale as dependências: pip install fastapi uvicorn python-multipart
    # 2. Configure as variáveis de ambiente (SUPABASE_URL, etc.)
    # 3. Execute o comando: uvicorn webhook_server:app --host 0.0.0.0 --port 8000 --reload
    print("Para iniciar o servidor, execute: uvicorn webhook_server:app --host 0.0.0.0 --port 8000 --reload")
