from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.quantum_info import get_clifford_gate_names

basis_gates = get_clifford_gate_names() + ['t', 'tdg']
pm = generate_preset_pass_manager(basis_gates=basis_gates)
qc = QuantumCircuit(1)
qc.rx(0.8, 0)
qct = pm.run(qc)
print(qct.count_ops())