from collections import deque
from typing import Dict, Any, Optional
from supabase_manager import SupabaseManager

class MemoryManager:
    def __init__(self, agent_id: str, supabase_manager: Optional[SupabaseManager] = None):
        self.agent_id = agent_id
        self.supabase_manager = supabase_manager
        self.short_term_memory = deque(maxlen=100)  # Percepts, recent interactions
        self.episodic_memory = deque(maxlen=50)   # Specific events, experiences
        self.semantic_memory: Dict[str, Any] = {} # Facts, concepts, knowledge
        self.long_term_memory: Dict[str, Any] = {} # Persistent state, goals, beliefs

        if self.supabase_manager:
            self.load_from_db() # Attempt to load persistent memory

    def add_short_term_memory(self, percept: Any):
        self.short_term_memory.append(percept)

    def add_episodic_memory(self, episode: Any):
        self.episodic_memory.append(episode)

    def add_semantic_memory(self, key: str, value: Any):
        self.semantic_memory[key] = value

    def add_long_term_memory(self, key: str, value: Any):
        self.long_term_memory[key] = value

    def get_short_term_memory(self) -> deque:
        return self.short_term_memory

    def get_episodic_memory(self) -> deque:
        return self.episodic_memory

    def get_semantic_memory(self, key: str) -> Optional[Any]:
        return self.semantic_memory.get(key)

    def get_long_term_memory(self, key: str) -> Optional[Any]:
        return self.long_term_memory.get(key)

    def load_from_db(self):
        if self.supabase_manager:
            print(f"MemoryManager: Attempting to load memory for agent {self.agent_id} from Supabase...")
            agent_data = self.supabase_manager.get_agent_definition(self.agent_id)
            if agent_data:
                self.long_term_memory = agent_data.get("long_term_memory", {})
                self.semantic_memory = agent_data.get("semantic_memory", {})
                print(f"MemoryManager: Memory for agent {self.agent_id} loaded from Supabase.")
            else:
                print(f"MemoryManager: No existing memory found for agent {self.agent_id} in Supabase. Initializing new.")

    def save_to_db(self):
        if self.supabase_manager:
            print(f"MemoryManager: Saving memory for agent {self.agent_id} to Supabase...")
            memory_state = {
                "long_term_memory": self.long_term_memory,
                "semantic_memory": self.semantic_memory
            }
            self.supabase_manager.update_agent_definition(self.agent_id, memory_state)
            print(f"MemoryManager: Memory for agent {self.agent_id} saved to Supabase.")

