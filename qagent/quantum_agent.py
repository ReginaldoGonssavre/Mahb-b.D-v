from qiskit import QuantumCircuit, transpile, Aer, execute

class QuantumAgent:
    def __init__(self):
        self.circuit = QuantumCircuit(2, 2)
        self._setup()

    def _setup(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.measure([0, 1], [0, 1])

    def executar(self):
        simulator = Aer.get_backend('qasm_simulator')
        compiled = transpile(self.circuit, simulator)
        job = execute(compiled, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts()
        return counts