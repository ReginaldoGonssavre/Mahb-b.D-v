import React, { useState } from "react";

export default function Features({ moduleType }) {
  const [prompt, setPrompt] = useState("");
  const [output, setOutput] = useState("");

  async function handleSend() {
    setOutput("Processando...");
    const token = localStorage.getItem("token");
    if (!token) {
      setOutput("Erro: Usuário não autenticado.");
      return;
    }

    let endpoint = "";
    let defaultPrompt = "";

    switch (moduleType) {
      case "financial":
        endpoint = "http://localhost:5000/api/ai/financial";
        defaultPrompt = "Gerar relatório financeiro detalhado para o último trimestre.";
        break;
      case "robotics":
        endpoint = "http://localhost:5000/api/ai/robotics";
        defaultPrompt = "Simular o movimento de um braço robótico para montagem de peças.";
        break;
      case "embedded-systems":
        endpoint = "http://localhost:5000/api/ai/embedded-systems";
        defaultPrompt = "Gerar código para um sistema embarcado de monitoramento de temperatura.";
        break;
      case "space-navigation":
        endpoint = "http://localhost:5000/api/ai/space-navigation";
        defaultPrompt = "Calcular a trajetória ideal para uma sonda espacial até Marte.";
        break;
      case "machine-automation":
        endpoint = "http://localhost:5000/api/ai/machine-automation";
        defaultPrompt = "Otimizar o ciclo de produção de uma linha de montagem automatizada.";
        break;
      case "electrical-energy":
        endpoint = "http://localhost:5000/api/ai/electrical-energy";
        defaultPrompt = "Prever o consumo de energia elétrica de uma indústria para o próximo mês.";
        break;
      case "digital-products":
        endpoint = "http://localhost:5000/api/ai/digital-products";
        defaultPrompt = "Gerar um esboço de e-book sobre 'Introdução à IA Quântica'.";
        break;
      case "quantum-tech":
        endpoint = "http://localhost:5000/api/ai/quantum-tech";
        defaultPrompt = "Simular um algoritmo quântico para otimização de portfólio.";
        break;
      case "ai-engineering":
      default:
        endpoint = "http://localhost:5000/api/ai/ai";
        defaultPrompt = "Como a IA pode otimizar processos de manufatura?";
        break;
    }

    if (!prompt) {
      setPrompt(defaultPrompt);
    }

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-auth-token": token,
        },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setOutput(JSON.stringify(data, null, 2));
    } catch (e) {
      setOutput("Erro ao consultar backend.");
    }
  }

  const getTitle = (type) => {
    switch (type) {
      case "financial": return "Análise Financeira com IA";
      case "robotics": return "Robótica Avançada";
      case "embedded-systems": return "Sistemas Embarcados Inteligentes";
      case "space-navigation": return "Navegação Espacial e GPS Quântico";
      case "machine-automation": return "Automação de Máquinas";
      case "electrical-energy": return "Gestão de Energia Elétrica";
      case "digital-products": return "Criação de Produtos Digitais";
      case "quantum-tech": return "Tecnologia Quântica Aplicada";
      case "ai-engineering": return "Engenharia de Prompts com IA";
      default: return "Módulo de IA";
    }
  };

  return (
    <section className="py-20 px-4 bg-gray-900 text-white">
      <h2 className="text-3xl font-bold text-center mb-12 text-cyan-400">{getTitle(moduleType)}</h2>
      <div className="max-w-2xl mx-auto bg-gray-800 p-8 rounded-lg shadow-xl">
        <textarea
          className="w-full p-3 rounded bg-gray-700 text-white mb-4 border border-gray-600 focus:outline-none focus:border-cyan-400"
          rows="5"
          placeholder={defaultPrompt}
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        ></textarea>
        <button
          onClick={handleSend}
          className="bg-cyan-400 text-gray-900 py-2 px-4 rounded-md font-bold hover:bg-cyan-500 transition duration-300"
        >
          Enviar Prompt
        </button>
        <pre className="bg-gray-700 p-4 rounded-md mt-4 text-white overflow-auto border border-gray-600" style={{ minHeight: "150px" }}>
          {output}
        </pre>
      </div>
    </section>
  );
}