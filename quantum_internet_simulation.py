from qiskit import QuantumCircuit, transpile, Aer
from qiskit.visualization import plot_histogram
import numpy as np

def create_qubit_and_superposition():
    """
    Simula a criação de um qubit e o coloca em superposição.
    Um qubit em superposição pode ser 0 e 1 ao mesmo tempo.
    """
    qc = QuantumCircuit(1, 1) # 1 qubit, 1 bit clássico
    qc.h(0) # Aplica porta Hadamard para criar superposição
    qc.measure(0, 0) # Mede o qubit
    print("--- Criação de Qubit e Superposição ---")
    print("Circuito para superposição:")
    print(qc.draw())
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(transpile(qc, simulator), shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print(f"Resultados da medição (superposição): {counts}")
    print("Esperamos aproximadamente 50% de 0s e 50% de 1s, demonstrando a superposição.\n")
    return qc

def demonstrate_entanglement():
    """
    Demonstra o entrelaçamento entre dois qubits.
    Se um qubit é medido, o estado do outro é instantaneamente conhecido.
    """
    qc = QuantumCircuit(2, 2) # 2 qubits, 2 bits clássicos
    qc.h(0) # Coloca o primeiro qubit em superposição
    qc.cx(0, 1) # Aplica porta CNOT para entrelaçar os qubits
    qc.measure([0, 1], [0, 1]) # Mede ambos os qubits
    print("--- Demonstração de Entrelaçamento ---")
    print("Circuito para entrelaçamento:")
    print(qc.draw())
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(transpile(qc, simulator), shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print(f"Resultados da medição (entrelaçamento): {counts}")
    print("Esperamos apenas resultados '00' ou '11', demonstrando que os qubits estão entrelaçados.\n")
    return qc

def bb84_qkd_simulation(num_bits=10):
    """
    Simulação simplificada do protocolo BB84 para Distribuição de Chave Quântica (QKD).
    Alice envia qubits para Bob, que mede em bases aleatórias.
    Eles comparam bases publicamente para derivar uma chave secreta.
    Uma 'Eve' (espiã) é simulada para mostrar a detecção de intrusão.
    """
    print("--- Simulação do Protocolo BB84 (QKD) ---")
    print(f"Tentando gerar uma chave secreta de {num_bits} bits.")

    # 1. Alice gera bits aleatórios e bases aleatórias
    alice_bits = np.random.randint(0, 2, num_bits)
    alice_bases = np.random.randint(0, 2, num_bits) # 0 para base Z (computacional), 1 para base X (Hadamard)

    # 2. Alice prepara os qubits e os envia para Bob
    #    (Simulamos o envio criando o circuito para cada qubit)
    qubits_sent_by_alice = []
    for i in range(num_bits):
        qc = QuantumCircuit(1, 1)
        if alice_bits[i] == 1:
            qc.x(0) # Se o bit for 1, aplica porta X
        if alice_bases[i] == 1:
            qc.h(0) # Se a base for X, aplica porta Hadamard
        qubits_sent_by_alice.append(qc)

    # 3. Bob escolhe bases aleatórias para medição
    bob_bases = np.random.randint(0, 2, num_bits)

    # 4. Bob mede os qubits
    bob_measured_bits = []
    simulator = Aer.get_backend('qasm_simulator')

    # Simulação de Eve (opcional): Eve intercepta e mede
    eve_active = np.random.rand() < 0.5 # Eve está ativa em 50% das vezes
    eve_bases = np.random.randint(0, 2, num_bits) if eve_active else None
    eve_measured_bits = [] if eve_active else None

    for i in range(num_bits):
        qc_bob = qubits_sent_by_alice[i].copy() # Bob recebe o qubit de Alice

        if eve_active:
            # Eve intercepta, mede e reenvia (com sua própria base aleatória)
            qc_eve = qubits_sent_by_alice[i].copy()
            if eve_bases[i] == 1:
                qc_eve.h(0)
            qc_eve.measure(0, 0)
            job_eve = simulator.run(transpile(qc_eve, simulator), shots=1)
            result_eve = job_eve.result()
            eve_bit = int(list(result_eve.get_counts(qc_eve).keys())[0])
            eve_measured_bits.append(eve_bit)

            # Eve prepara um novo qubit com base no que ela mediu e reenvia para Bob
            qc_bob = QuantumCircuit(1, 1)
            if eve_bit == 1:
                qc_bob.x(0)
            if eve_bases[i] == 1:
                qc_bob.h(0)

        # Bob mede
        if bob_bases[i] == 1:
            qc_bob.h(0) # Se a base for X, aplica porta Hadamard
        qc_bob.measure(0, 0)
        job_bob = simulator.run(transpile(qc_bob, simulator), shots=1)
        result_bob = job_bob.result()
        bob_bit = int(list(result_bob.get_counts(qc_bob).keys())[0])
        bob_measured_bits.append(bob_bit)

    # 5. Alice e Bob comparam publicamente suas bases
    matching_indices = [i for i in range(num_bits) if alice_bases[i] == bob_bases[i]]

    alice_key_candidates = [alice_bits[i] for i in matching_indices]
    bob_key_candidates = [bob_measured_bits[i] for i in matching_indices]

    print("\n--- Comparação de Bases e Derivação da Chave ---")
    print(f"Bases de Alice: {alice_bases}")
    print(f"Bases de Bob:   {bob_bases}")
    print(f"Índices de bases correspondentes: {matching_indices}")

    # 6. Derivar a chave secreta e verificar a integridade
    final_alice_key = []
    final_bob_key = []
    for i in matching_indices:
        final_alice_key.append(alice_bits[i])
        final_bob_key.append(bob_measured_bits[i])

    print(f"Chave secreta de Alice (candidata): {final_alice_key}")
    print(f"Chave secreta de Bob (candidata):   {final_bob_key}")

    errors = sum(1 for a, b in zip(final_alice_key, final_bob_key) if a != b)
    error_rate = errors / len(final_alice_key) if len(final_alice_key) > 0 else 0

    print(f"Número de erros detectados: {errors}")
    print(f"Taxa de erro: {error_rate:.2f}")

    if eve_active:
        print("\n--- Simulação de Eve (Espiã) ---")
        print("Eve estava ativa e tentou interceptar a comunicação.")
        print("A presença de erros na chave final pode indicar a atividade de Eve.")
        if errors > 0:
            print("ERROS DETECTADOS! A presença de Eve foi revelada.")
        else:
            print("Nenhum erro detectado, mas Eve estava ativa. Isso pode acontecer se Eve tiver sorte com as bases.")
    else:
        print("\n--- Simulação de Eve (Espiã) ---")
        print("Eve não estava ativa nesta simulação.")
        if errors == 0:
            print("Nenhum erro detectado. A chave é segura (assumindo que Eve não estava ativa).")
        else:
            print("ERROS DETECTADOS MESMO SEM EVE ATIVA! Isso pode indicar ruído no canal ou um problema na simulação.")

    if errors == 0 and len(final_alice_key) > 0:
        print("\nChave secreta estabelecida com sucesso!")
        print(f"Chave: {final_alice_key}")
    elif len(final_alice_key) == 0:
        print("\nNão foi possível estabelecer uma chave secreta (poucos bits correspondentes).")
    else:
        print("\nChave comprometida devido a erros. A comunicação não é segura.")

    print("\n--- Conexão com o Mundo Real ---")
    print("Esta simulação demonstra os princípios por trás de projetos como:")
    print("- **Rede Rio Quântica:** A transmissão de qubits entre nós (instituições) para estabelecer comunicação segura.")
    print("- **Satélite Micius:** A capacidade de distribuir chaves quânticas de forma segura, mesmo em longas distâncias.")
    print("- **Quantum Internet Alliance:** O desenvolvimento de protocolos e a integração de componentes para uma rede quântica funcional.")
    print("A segurança da Internet Quântica reside na detecção de qualquer tentativa de espionagem, como demonstrado pela taxa de erro no BB84.")

if __name__ == "__main__":
    # Demonstração da criação de qubit e superposição
    create_qubit_and_superposition()

    # Demonstração de entrelaçamento
    demonstrate_entanglement()

    # Simulação do protocolo BB84 (QKD)
    bb84_qkd_simulation(num_bits=20) # Aumente num_bits para uma simulação mais robusta
