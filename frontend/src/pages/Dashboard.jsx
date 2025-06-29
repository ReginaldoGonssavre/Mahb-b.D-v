import React, { useEffect, useState } from "react";
import Features from "../components/Features"; // Importar o componente Features

export default function Dashboard() {
  const [courses, setCourses] = useState([]);
  const [user, setUser] = useState(null);
  const [selectedModule, setSelectedModule] = useState("financial"); // Estado para o módulo selecionado

  const modules = [
    { id: "financial", name: "Análise Financeira" },
    { id: "robotics", name: "Robótica Avançada" },
    { id: "embedded-systems", name: "Sistemas Embarcados" },
    { id: "space-navigation", name: "Navegação Espacial" },
    { id: "machine-automation", name: "Automação de Máquinas" },
    { id: "electrical-energy", name: "Energia Elétrica" },
    { id: "digital-products", name: "Produtos Digitais" },
    { id: "quantum-tech", name: "Tecnologia Quântica" },
    { id: "ai-engineering", name: "Engenharia de Prompts" },
  ];

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        // Redirecionar para login se não houver token
        window.location.href = "/login"; // Redireciona para a nova rota de login
        return;
      }

      // Fetch user data
      try {
        const userRes = await fetch("http://localhost:5000/api/auth/me", {
          headers: { "x-auth-token": token },
        });
        const userData = await userRes.json();
        setUser(userData);
      } catch (err) {
        console.error("Erro ao buscar dados do usuário:", err);
        // Tratar erro, talvez redirecionar para login
      }

      // Fetch courses
      try {
        const coursesRes = await fetch("http://localhost:5000/api/courses", {
          headers: { "x-auth-token": token },
        });
        const coursesData = await coursesRes.json();
        setCourses(coursesData);
      } catch (err) {
        console.error("Erro ao buscar cursos:", err);
      }
    };
    fetchData();
  }, []);

  const handleDownload = async (resourceId) => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Você precisa estar logado para baixar recursos.");
      return;
    }

    try {
      const res = await fetch(`http://localhost:5000/api/downloads/${resourceId}`, {
        headers: { "x-auth-token": token },
      });
      const data = await res.json();
      if (res.ok) {
        alert(data.msg + "\nConteúdo: " + data.content); // Exibir o conteúdo simulado
      } else {
        alert(data.msg || "Erro ao baixar o recurso.");
      }
    } catch (err) {
      console.error("Erro ao baixar recurso:", err);
      alert("Erro ao comunicar com o servidor para download.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 p-6 text-white">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      {user && (
        <div className="mb-8 p-4 bg-gray-800 rounded">
          <h2 className="text-xl font-bold mb-2">Bem-vindo, {user.name}!</h2>
          <p>Status: {user.isPremium ? "Premium" : "Gratuito"}</p>
          {!user.isPremium && (
            <p>Horas de Trial Restantes: {user.freeTrialHoursLimit - user.freeTrialHoursUsed}</p>
          )}
          {user.isPremium && (
            <div className="mt-4">
              <h3 className="text-lg font-bold mb-2">Downloads Premium</h3>
              <button onClick={() => handleDownload("resource-a")} className="bg-green-500 text-white py-2 px-4 rounded mr-2 hover:bg-green-600">Download Recurso A</button>
              <button onClick={() => handleDownload("resource-b")} className="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">Download Recurso B</button>
              <button onClick={() => handleDownload("ebook-ia-quantica")} className="bg-green-500 text-white py-2 px-4 rounded ml-2 hover:bg-green-600">Download E-book IA Quântica</button>
            </div>
          )}
        </div>
      )}

      <div className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Módulos de IA</h2>
        <div className="flex flex-wrap gap-2">
          {modules.map((module) => (
            <button
              key={module.id}
              onClick={() => setSelectedModule(module.id)}
              className={`py-2 px-4 rounded-md ${selectedModule === module.id ? "bg-cyan-400 text-gray-900" : "bg-gray-700 text-white"} hover:bg-cyan-500 transition duration-300`}
            >
              {module.name}
            </button>
          ))}
        </div>
      </div>

      {selectedModule && <Features moduleType={selectedModule} />}

      <h2 className="text-2xl font-bold mb-4 mt-8">Seus Cursos</h2>
      <ul className="space-y-4">
        {courses.map((course, i) => (
          <li key={i} className="p-4 border rounded bg-gray-800">
            <h3 className="text-xl">{course.title}</h3>
            <p>{course.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}