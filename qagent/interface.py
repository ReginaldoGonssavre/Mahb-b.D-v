class CommandLineInterface:
    def __init__(self, classical, quantum):
        self.classical = classical
        self.quantum = quantum

    def run(self):
        print("Digite seu comando (ou 'sair'):")
        while True:
            comando = input(" > ")
            if comando.lower() == 'sair':
                break
            elif comando.lower().startswith("q:"):
                print("⚛️ Quantum Result:", self.quantum.executar())
            else:
                print(" IA Responde:", self.classical.inferir(comando))