import os
from supabase import create_client, Client
from typing import Dict, Any, List

class SupabaseManager:
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        if not url or not key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set.")
        self.supabase: Client = create_client(url, key)

    # --- Agent Definitions (e.g., 'agents' table) ---
    def get_agent_definition(self, agent_id: str) -> Dict[str, Any] | None:
        response = self.supabase.from_('agents').select('*').eq('id', agent_id).single().execute()
        return response.data

    def create_agent_definition(self, agent_data: Dict[str, Any]) -> Dict[str, Any] | None:
        response = self.supabase.from_('agents').insert(agent_data).execute()
        return response.data[0] if response.data else None

    def update_agent_definition(self, agent_id: str, updates: Dict[str, Any]) -> Dict[str, Any] | None:
        response = self.supabase.from_('agents').update(updates).eq('id', agent_id).execute()
        return response.data[0] if response.data else None

    # --- Agent Memory (e.g., 'agent_memory' table) ---
    def get_agent_memory(self, agent_id: str, user_id: str) -> List[Dict[str, Any]]:
        response = self.supabase.from_('agent_memory').select('*').eq('agent_id', agent_id).eq('user_id', user_id).order('timestamp', desc=False).execute()
        return response.data

    def add_to_agent_memory(self, memory_data: Dict[str, Any]) -> Dict[str, Any] | None:
        # memory_data should include agent_id, user_id, content, timestamp
        response = self.supabase.from_('agent_memory').insert(memory_data).execute()
        return response.data[0] if response.data else None

    # --- Conversation State (e.g., 'conversations' table) ---
    def get_conversation_state(self, conversation_id: str) -> Dict[str, Any] | None:
        response = self.supabase.from_('conversations').select('*').eq('id', conversation_id).single().execute()
        return response.data

    def update_conversation_state(self, conversation_id: str, updates: Dict[str, Any]) -> Dict[str, Any] | None:
        response = self.supabase.from_('conversations').update(updates).eq('id', conversation_id).execute()
        return response.data[0] if response.data else None

    def create_conversation_state(self, conversation_data: Dict[str, Any]) -> Dict[str, Any] | None:
        response = self.supabase.from_('conversations').insert(conversation_data).execute()
        return response.data[0] if response.data else None

# Exemplo de uso (para demonstração)
if __name__ == "__main__":
    # Certifique-se de definir as variáveis de ambiente:
    # export SUPABASE_URL="YOUR_SUPABASE_URL"
    # export SUPABASE_KEY="YOUR_SUPABASE_KEY"

    try:
        manager = SupabaseManager()
        print("SupabaseManager initialized successfully.")

        # Exemplo: Criar uma definição de agente
        # new_agent = manager.create_agent_definition({"id": "my-first-agent", "name": "My First Agent", "config": {"model": "gemini-pro"}})
        # print(f"Created agent: {new_agent}")

        # Exemplo: Obter uma definição de agente
        # agent_def = manager.get_agent_definition("my-first-agent")
        # print(f"Retrieved agent: {agent_def}")

        # Exemplo: Adicionar à memória do agente
        # memory_entry = manager.add_to_agent_memory({"agent_id": "my-first-agent", "user_id": "user123", "content": "Hello, agent!", "timestamp": "2025-07-26T10:00:00Z"})
        # print(f"Added to memory: {memory_entry}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
