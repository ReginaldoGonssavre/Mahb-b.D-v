import os
from supabase_manager import SupabaseManager
from my_agent import MyAgent
from input_data import InputData # New import

class AgentOrchestrator:
    def __init__(self):
        try:
            self.supabase_manager = SupabaseManager()
            print("AgentOrchestrator: SupabaseManager initialized.")
        except ValueError as e:
            print(f"AgentOrchestrator: Could not initialize SupabaseManager: {e}. Persistence will be disabled.")
            self.supabase_manager = None

    def process_request(self, agent_id: str, user_query: str, conversation_id: str | None = None):
        print(f"\n--- Processing Request for Agent '{agent_id}' ---")

        # 1. Load or Create Agent
        agent = MyAgent(agent_id, self.supabase_manager)
        print(f"Agent '{agent_id}' loaded/initialized.")

        # 2. Perceive Environment (User Query)
        input_data = InputData(text=user_query)
        rag_context = agent.perceive(input_data)

        # 3. Act (Generate Response)
        # For simplicity, we'll use a generic intention here.
        # In a real system, intention would be derived from user_query or agent's internal state.
        intention = f"Responder à pergunta do usuário: {user_query}"
        gemini_response = agent.act(intention, rag_context=rag_context)

        # 4. Save Agent State (if persistence is enabled)
        if self.supabase_manager:
            agent.save_state_to_db()
            print(f"Agent '{agent_id}' state saved to DB.")

        print(f"--- Request for Agent '{agent_id}' Processed ---")
        return gemini_response # Return the Gemini response


if __name__ == "__main__":
    # Ensure all necessary environment variables are set:
    # export SUPABASE_URL="YOUR_SUPABASE_URL"
    # export SUPABASE_KEY="YOUR_SUPABASE_KEY"
    # export PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    # export PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
    # export PINECONE_INDEX_NAME="my-index"
    # export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

    orchestrator = AgentOrchestrator()

    # Simulate a user request for product auditor agent
    print("\n--- Simulating Request for Product Auditor Agent ---")
    response1 = orchestrator.process_request("product_auditor_agent", InputData(text="Quais são os principais pontos de melhoria na usabilidade do Maḥbūb?"))
    print(f"Agent Response 1: {response1}")

    # Simulate another request for the same agent to show persistence
    print("\n--- Simulating Another Request for Product Auditor Agent (Persistence Test) ---")
    response2 = orchestrator.process_request("product_auditor_agent", InputData(text="Como podemos tornar a integração com o Gemini mais fluida?"))
    print(f"Agent Response 2: {response2}")

    # Simulate a request for a different agent
    print("\n--- Simulating Request for Marketing Agent ---")
    response3 = orchestrator.process_request("marketing_agent", InputData(text="Crie um slogan cativante para o Maḥbūb."))
    print(f"Agent Response 3: {response3}")

    # Simulate a request that should trigger a tool call (e.g., calculator)
    print("\n--- Simulating Request to Trigger Calculator Tool ---")
    response4 = orchestrator.process_request("math_agent", InputData(text="Qual é o resultado de 15 * 3 + 7?"))
    print(f"Agent Response 4 (Tool Use): {response4}")

    # Simulate a request that should trigger a tool call (e.g., web search)
    print("\n--- Simulating Request to Trigger Web Search Tool ---")
    response5 = orchestrator.process_request("research_agent", InputData(text="Pesquise sobre o que é Qiskit."))
    print(f"Agent Response 5 (Tool Use): {response5}")

    # Simulate a request that should trigger the Qiskit tool
    print("\n--- Simulating Request to Trigger Qiskit Tool ---")
    response6 = orchestrator.process_request("quantum_agent", InputData(text="Crie um circuito quântico com 2 qubits, um Hadamard no qubit 0 e um CNOT entre 0 e 1. Defina os observáveis 'IZ' e 'XX'."))
    print(f"Agent Response 6 (Qiskit Tool): {response6}")
