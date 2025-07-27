from typing import Callable, Dict, Any, List
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

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
)def create_qiskit_circuit_and_observables(num_qubits: int, hadamard_qubit: int, cx_control: int, cx_target: int, observable_labels: List[str]) -> Dict[str, Any]:    """Creates a simple Qiskit quantum circuit and defines observables.    Args:        num_qubits (int): The number of qubits in the circuit.        hadamard_qubit (int): The qubit to apply a Hadamard gate to.        cx_control (int): The control qubit for the CNOT gate.        cx_target (int): The target qubit for the CNOT gate.        observable_labels (List[str]): A list of Pauli strings (e.g., ["IZ", "XX"]) for observables.    Returns:        Dict[str, Any]: A dictionary containing the text drawing of the circuit and the created observables.    """    qc = QuantumCircuit(num_qubits)    qc.h(hadamard_qubit)    qc.cx(cx_control, cx_target)    observables = [SparsePauliOp(label) for label in observable_labels]    return {        "circuit_text_drawing": qc.draw("text"),        "observables_count": len(observables),        "first_observable_label": str(observables[0]) if observables else None    }qiskit_tool = AgentTool(    name="qiskit_circuit_and_observables",    description="Creates a Qiskit quantum circuit and defines observables based on parameters.",    func=create_qiskit_circuit_and_observables,    parameters={        "type": "object",        "properties": {            "num_qubits": {"type": "integer", "description": "The number of qubits in the circuit.", "minimum": 1},            "hadamard_qubit": {"type": "integer", "description": "The qubit to apply a Hadamard gate to.", "minimum": 0},            "cx_control": {"type": "integer", "description": "The control qubit for the CNOT gate.", "minimum": 0},            "cx_target": {"type": "integer", "description": "The target qubit for the CNOT gate.", "minimum": 0},            "observable_labels": {"type": "array", "items": {"type": "string"}, "description": "A list of Pauli strings (e.g., [\"IZ\", \"XX\"]) for observables."}        },        "required": ["num_qubits", "hadamard_qubit", "cx_control", "cx_target", "observable_labels"]    })# List of all available toolsAVAILABLE_TOOLS = {    calculator_tool.name: calculator_tool,    web_search_tool.name: web_search_tool,    qiskit_tool.name: qiskit_tool,}
