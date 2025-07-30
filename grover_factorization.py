import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# --- Funções para o Oráculo de Fatoração (a parte "mágica") ---

def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    if a not in [2, 7, 8, 11, 13]:
        raise ValueError("'a' must be 2, 7, 8, 11 or 13")
    U = QuantumCircuit(4)
    for _iteration in range(power):
        if a in [2, 13]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
        if a in [7, 8]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
        if a == 11:
            U.swap(1, 3)
            U.swap(0, 2)
        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"
    c_U = U.control()
    return c_U

# --- Construção do Algoritmo de Grover ---

# 1. Definição do Problema
n_qubits_solution = 8  # Usaremos 8 qubits para representar os possíveis fatores (4 para 'a', 4 para 'b')
# O estado que queremos encontrar: 3 e 5 (0011 e 0101)
# Como o Qiskit lê os bits da direita para a esquerda, o estado é |0101 0011>
marked_state_str = "01010011"
marked_state_int = int(marked_state_str, 2)

# 2. Circuito Oráculo
# O oráculo marca o estado 'marked_state_str'
oracle = QuantumCircuit(n_qubits_solution)
# Para marcar um estado |s>, aplicamos uma porta Z controlada em |s>
# Isso é feito aplicando X nos qubits que são 0 em |s>,
# depois um MCZ (Multi-Controlled Z) em todos os qubits,
# e então desfazendo os gates X.
for qubit, bit in enumerate(reversed(marked_state_str)):
    if bit == '0':
        oracle.x(qubit)
oracle.h(n_qubits_solution - 1)
oracle.mct(list(range(n_qubits_solution - 1)), n_qubits_solution - 1)
oracle.h(n_qubits_solution - 1)
for qubit, bit in enumerate(reversed(marked_state_str)):
    if bit == '0':
        oracle.x(qubit)
oracle.name = "Oráculo"

# 3. Circuito Difusor (Amplificação)
diffuser = QuantumCircuit(n_qubits_solution)
diffuser.h(range(n_qubits_solution))
diffuser.x(range(n_qubits_solution))
diffuser.h(n_qubits_solution - 1)
diffuser.mct(list(range(n_qubits_solution - 1)), n_qubits_solution - 1)
diffuser.h(n_qubits_solution - 1)
diffuser.x(range(n_qubits_solution))
diffuser.h(range(n_qubits_solution))
diffuser.name = "Difusor"

# 4. Montagem do Circuito de Grover
# O número de iterações ideais é ~sqrt(2^n)
iterations = int(np.pi / 4 * np.sqrt(2**n_qubits_solution))
print(f"Número de qubits: {n_qubits_solution}")
print(f"Estado marcado (fatores 3 e 5): {marked_state_str}")
print(f"Número de iterações de Grover: {iterations}")

grover_circuit = QuantumCircuit(n_qubits_solution, n_qubits_solution)
grover_circuit.h(range(n_qubits_solution)) # Inicia a superposição

# Aplica Oráculo e Difusor repetidamente
for _ in range(iterations):
    grover_circuit.append(oracle, range(n_qubits_solution))
    grover_circuit.append(diffuser, range(n_qubits_solution))

grover_circuit.measure(range(n_qubits_solution), range(n_qubits_solution))

# --- Simulação e Resultados ---
print("\nExecutando o circuito no simulador quântico...")
backend = Aer.get_backend('qasm_simulator')
t_grover_circuit = transpile(grover_circuit, backend)
qobj = assemble(t_grover_circuit)
results = backend.run(qobj).result()
counts = results.get_counts()

# Extrai o resultado mais provável
most_likely_result = max(counts, key=counts.get)
factor_b_bin = most_likely_result[:4]
factor_a_bin = most_likely_result[4:]
factor_a = int(factor_a_bin, 2)
factor_b = int(factor_b_bin, 2)

print(f"\nResultado da medição mais provável: {most_likely_result}")
print(f"Fatores encontrados: a = {factor_a}, b = {factor_b}")
print(f"Verificação: {factor_a} * {factor_b} = {factor_a * factor_b}")

# Plota o histograma dos resultados
plot_histogram(counts)
plt.title("Resultados da Fatoração com Algoritmo de Grover")
plt.xlabel("Estados Medidos")
plt.ylabel("Contagens")
print("\nUm gráfico de histograma foi salvo como 'grover_factorization_results.png'")
plt.savefig('grover_factorization_results.png')
