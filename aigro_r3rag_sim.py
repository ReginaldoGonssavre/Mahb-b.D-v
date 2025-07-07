import difflib

# Dataset QA simples
dataset = [
    {"pergunta": "Quem descobriu o rádio?", "resposta_certa": "Marie Curie"},
    {"pergunta": "Capital do Brasil?", "resposta_certa": "Brasília"},
    {"pergunta": "Quem escreveu Dom Quixote?", "resposta_certa": "Miguel de Cervantes"},
]

# Documentos simulados
docs = [
    "Marie Curie descobriu o rádio e o polônio.",
    "A capital do Brasil é Brasília.",
    "Dom Quixote foi escrito por Miguel de Cervantes.",
    "Einstein criou a teoria da relatividade."
]

def recuperar_contexto(pergunta):
    return [d for d in docs if any(p.lower() in d.lower() for p in pergunta.lower().split())]

def modelo_responde(pergunta):
    if "rádio" in pergunta.lower():
        return "Marie Curie"
    elif "capital" in pergunta.lower():
        return "Brasília"
    elif "quixote" in pergunta.lower():
        return "Miguel de Cervantes"
    else:
        return "Não sei."

def calcular_recompensa(previsto, real, contexto):
    similaridade = difflib.SequenceMatcher(None, previsto.lower(), real.lower()).ratio()
    relevante = any(real.lower() in doc.lower() for doc in contexto)
    return 1 if similaridade > 0.6 or relevante else 0

def executar_simulacao():
    for item in dataset:
        print("\n📌 Pergunta:", item["pergunta"])
        contexto = recuperar_contexto(item["pergunta"])
        print("📚 Contexto:", contexto)
        resposta = modelo_responde(item["pergunta"])
        print("🤖 Resposta:", resposta)
        recompensa = calcular_recompensa(resposta, item["resposta_certa"], contexto)
        print("🏆 Recompensa:", recompensa, "✅" if recompensa == 1 else "❌")

executar_simulacao()
