# Notas de Pesquisa para Simulação de Internet Quântica

## Artigo da USP: "Internet Quântica: o futuro que chegará antes dos computadores quânticos"

- **Conceito Principal:** A Internet Quântica não é apenas uma versão mais rápida da internet clássica, mas uma rede que utiliza os princípios da mecânica quântica (superposição, entrelaçamento) para comunicação intrinsecamente segura e, futuramente, para conectar computadores quânticos.
- **Prioridade:** A segurança da comunicação (QKD) é o primeiro e mais imediato benefício da Internet Quântica, antes mesmo da computação quântica distribuída.
- **Tecnologias Mencionadas:** Distribuição de Chave Quântica (QKD), teletransporte quântico.

## Satélite Micius (China)

- **Pioneirismo:** Primeiro satélite a demonstrar QKD em escala global (distâncias de milhares de quilômetros).
- **Tecnologia:** Utiliza fótons entrelaçados para estabelecer chaves secretas entre estações terrestres distantes.
- **Relevância:** Prova a viabilidade da comunicação quântica de longa distância, superando as limitações de perda de sinal em fibras ópticas.

## Quantum Internet Alliance (QIA)

- **Objetivo:** Consórcio europeu focado no desenvolvimento de uma Internet Quântica funcional.
- **Foco:** Pesquisa em hardware (repetidores quânticos), software e protocolos para construir uma rede quântica escalável e robusta.
- **Protocolos:** Desenvolvimento de protocolos para roteamento de qubits, correção de erros quânticos e gerenciamento de rede.

## Rede Rio Quântica (Brasil)

- **Localização:** Rio de Janeiro, Brasil.
- **Instituições Envolvidas:** UFRJ, UFF, CBPF, PUC-Rio, IME (futuramente).
- **Infraestrutura:** Combinação de enlaces por fibra óptica e um feixe de laser verde (6,8 km entre UFF e CBPF).
- **Objetivo:** Primeira rede de comunicação quântica do Brasil, focada em estabelecer uma infraestrutura nacional de comunicações quânticas seguras.
- **Significado:** Marca a entrada do Brasil na corrida global pela tecnologia de Internet Quântica, demonstrando a aplicação prática de QKD em ambiente urbano/regional.

## Conceitos Chave para a Simulação

- **Qubit:** Unidade básica de informação quântica. Pode estar em superposição de 0 e 1.
- **Superposição:** Um qubit pode existir em múltiplos estados simultaneamente até ser medido.
- **Entrelaçamento:** Dois ou mais qubits tornam-se intrinsecamente ligados, de modo que a medição de um instantaneamente afeta o estado do outro, independentemente da distância.
- **Distribuição de Chave Quântica (QKD - Protocolo BB84):**
    1.  **Geração de Qubits:** Alice gera qubits em estados aleatórios (0, 1, +, -).
    2.  **Escolha de Base:** Alice escolhe aleatoriamente uma base de medição (computacional ou Hadamard) para cada qubit.
    3.  **Transmissão:** Alice envia os qubits para Bob.
    4.  **Medição de Bob:** Bob mede cada qubit em uma base escolhida aleatoriamente.
    5.  **Comparação de Bases:** Alice e Bob comparam publicamente as bases que usaram (mas não os resultados das medições).
    6.  **Chave Secreta:** Os qubits medidos nas bases correspondentes formam a chave secreta. Qualquer tentativa de espionagem (Eve) introduzirá erros detectáveis.

## Desafios e Limitações da Simulação

- **Hardware Físico:** A simulação não replica o hardware físico (lasers, detectores, fibras ópticas) ou os desafios de engenharia (perda de sinal, decoerência real).
- **Escalabilidade:** A simulação é conceitual e não aborda a escalabilidade de uma rede quântica real com múltiplos repetidores quânticos.
- **Ruído e Erros:** Embora o Qiskit permita simular ruído básico, a complexidade do ruído em sistemas quânticos reais é muito maior.
