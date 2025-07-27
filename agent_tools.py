from typing import Callable, Dict, Any

class AgentTool:
    def __init__(self, name: str, description: str, func: Callable, parameters: Dict[str, Any]):
        self.name = name
        self.description = description
        self.func = func
        self.parameters = parameters # Dictionary describing expected parameters for the tool

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# --- Example Tools ---

def simple_calculator(expression: str) -> str:
    """Calculates the result of a simple mathematical expression."""
    try:
        # WARNING: Using eval() is generally unsafe with untrusted input.
        # For a real application, use a safer math expression parser.
        return str(eval(expression))
    except Exception as e:
        return f"Error calculating: {e}"

calculator_tool = AgentTool(
    name="calculator",
    description="A simple calculator for mathematical expressions.",
    func=simple_calculator,
    parameters={
        "type": "object",
        "properties": {
            "expression": {"type": "string", "description": "The mathematical expression to evaluate."}
        },
        "required": ["expression"]
    }
)

def simulated_web_search(query: str) -> str:
    """Simulates a web search and returns a predefined result."""
    if "Qiskit" in query:
        return "Qiskit is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules."
    elif "Maḥbūb" in query:
        return "Maḥbūb is an open-source modular platform for orchestrating autonomous AI agents."
    else:
        return "No relevant information found for your query in the simulated search."

web_search_tool = AgentTool(
    name="web_search",
    description="Simulates a web search to find information.",
    func=simulated_web_search,
    parameters={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query."}
        },
        "required": ["query"]
    }
)

# List of all available tools
AVAILABLE_TOOLS = {
    calculator_tool.name: calculator_tool,
    web_search_tool.name: web_search_tool,
}
