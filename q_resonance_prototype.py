from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms.linear_solvers import HHL
from qiskit.algorithms.linear_solvers.observables import MatrixFunctional
from qiskit.algorithms.linear_solvers.numpy_linear_solver import NumPyLinearSolver
from qiskit.algorithms.linear_solvers.linear_solver_result import LinearSolverResult
from qiskit.algorithms.linear_solvers.linear_system_problem import LinearSystemProblem
from qiskit.quantum_info import Statevector
import numpy as np

# 1. Definir matriz A e vetor b (Ax = b)
A = np.array([[1, -1/3], [-1/3, 1]])
b = np.array([1, 0])

# 2. Criar o problema linear
problem = LinearSystemProblem(matrix=A, vector=b)

# 3. Definir o backend quântico simulado
quantum_instance = QuantumInstance(backend=Aer.get_backend('aer_simulator_statevector'))

# 4. Resolver com HHL
hhl = HHL(quantum_instance=quantum_instance)
result: LinearSolverResult = hhl.solve(problem)

# 5. Mostrar resultado
print("Resultado aproximado do sistema Ax = b (via HHL):")
print(result.solution)

# Resultado clássico para comparação
classic_result = np.linalg.solve(A, b)
print("\nResultado clássico (numpy):")
print(classic_result)