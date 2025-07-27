import os
from collections import deque
from refactored_agent import IntelligentAgent, MLComponent, NeuralAgentComponent
from supabase_manager import SupabaseManager
from agent_tools import AVAILABLE_TOOLS # Import available tools
import json # For parsing tool calls

class MyAgent(IntelligentAgent):
    def __init__(self, agent_id: str, supabase_manager: SupabaseManager | None = None):
        super().__init__(agent_id, supabase_manager, tools=AVAILABLE_TOOLS) # Pass AVAILABLE_TOOLS to parent
        print(f"MyAgent '{agent_id}' initialized with RAG, Gemini, Supabase persistence, and Tool Use capabilities.")

    def perceive(self, environment: str):
        self.percepts.append(environment)
        print(f"Agent perceived: {environment}")

        # Use RAG to get relevant context based on the environment
        rag_context = ""
        if self.rag_module:
            print(f"Searching RAG for context related to: {environment}")
            results = self.rag_module.query_vectors(environment)
            if results and results.matches:
                # Concatenate relevant text from RAG results
                for match in results.matches:
                    # Assuming metadata contains 'text' field
                    if 'text' in match.metadata:
                        rag_context += match.metadata['text'] + "\n"
                print(f"RAG context found: {rag_context[:100]}...") # Print first 100 chars
            else:
                print("No RAG context found.")
        else:
            print("RAG module not initialized. Cannot retrieve context.")
        return rag_context

    def _get_tool_definitions_for_gemini(self) -> str:
        if not self.tools:
            return ""
        tool_definitions = []
        for tool_name, tool_obj in self.tools.items():
            tool_definitions.append(f"Tool Name: {tool_obj.name}\nDescription: {tool_obj.description}\nParameters: {json.dumps(tool_obj.parameters)}")
        return "\n\nAvailable Tools:\n" + "\n---\n".join(tool_definitions) + "\n\n"

    def act(self, intention: str, rag_context: str = "") -> str:
        print(f"Agent acting with intention: {intention}")

        if not self.gemini_client:
            print("Gemini client not initialized. Cannot generate response.")
            return "Error: Gemini client not initialized."

        tool_definitions_str = self._get_tool_definitions_for_gemini()

        # Construct a prompt for Gemini, including RAG context and tool definitions
        prompt = f"Based on the following context: {rag_context}\n\nAnd the intention: {intention}\n\n{tool_definitions_str}"
        prompt += "If a tool is needed, respond with a JSON object like: {\"tool_name\": \"tool_name_here\", \"parameters\": {\"param1\": \"value1\"}}.\nOtherwise, provide a concise and helpful response."

        print(f"Sending prompt to Gemini: {prompt[:500]}...") # Print first 500 chars
        gemini_response_text = self.gemini_client.generate_content(prompt)
        print(f"Gemini's raw response: {gemini_response_text}")

        # Attempt to parse Gemini's response as a tool call
        try:
            tool_call = json.loads(gemini_response_text)
            tool_name = next(iter(tool_call))
            parameters = tool_call[tool_name]

            if tool_name in self.tools:
                tool_obj = self.tools[tool_name]
                print(f"Executing tool: {tool_name} with parameters: {parameters}")
                tool_result = tool_obj(**parameters)
                print(f"Tool result: {tool_result}")

                # Optionally, send tool result back to Gemini for final response generation
                follow_up_prompt = f"Based on the original intention: {intention}\nAnd the tool result from {tool_name}: {tool_result}\n\nProvide a concise and helpful final response."
                final_gemini_response = self.gemini_client.generate_content(follow_up_prompt)
                return final_gemini_response
            else:
                return f"Gemini suggested unknown tool: {tool_name}"
        except json.JSONDecodeError:
            # Not a tool call, return Gemini's text response directly
            return gemini_response_text

    # Placeholder for abstract methods from IntelligentAgent
    def _update_desires(self):
        return "" # Simplified for example

    def _form_intention(self):
        return "" # Simplified for example


if __name__ == "__main__":
    # Set environment variables for Pinecone and Gemini before running
    # export PINECONE_API_KEY="YOUR_API_KEY"
    # export PINECONE_ENVIRONMENT="YOUR_ENVIRONMENT"
    # export PINECONE_INDEX_NAME="my-index"
    # export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

    # Example of populating Pinecone index (run this once or as needed)
    # from rag_module import RAGModule
    # rag_module_example = RAGModule(
    #     os.getenv("PINECONE_API_KEY"),
    #     os.getenv("PINECONE_ENVIRONMENT"),
    #     os.getenv("PINECONE_INDEX_NAME", "my-index")
    # )
    # rag_module_example.upsert_vector("doc1", "O Qiskit é um framework Python de código aberto para computação quântica.")
    # rag_module_example.upsert_vector("doc2", "O Algoritmo de Deutsch-Jozsa é um algoritmo quântico que determina se uma função é constante ou balanceada.")
    # rag_module_example.upsert_vector("doc3", "Maḥbūb é uma plataforma open-source modular para orquestração de agentes de IA autônomos.")

    try:
        supabase_manager = SupabaseManager()
        print("SupabaseManager initialized for example usage.")
    except ValueError as e:
        print(f"Could not initialize SupabaseManager: {e}. Skipping Supabase persistence demo.")
        supabase_manager = None

    agent_id = "my_test_agent"
    agent = MyAgent(agent_id, supabase_manager)

    # Simulate a perception and action cycle
    user_query = "O que é o Qiskit e qual a sua relação com o Maḥbūb?"
    context = agent.perceive(user_query)
    agent.act(f"Responder à pergunta do usuário sobre {user_query}", rag_context=context)
    if supabase_manager:
        agent.save_state_to_db()

    user_query_2 = "Explique o algoritmo de Deutsch-Jozsa."
    context_2 = agent.perceive(user_query_2)
    agent.act(f"Explicar o algoritmo de Deutsch-Jozsa para o usuário.", rag_context=context_2)
    if supabase_manager:
        agent.save_state_to_db()
