import React, { useState } from "react";

export default function Home() {
  const [showAuth, setShowAuth] = useState(true); // Sempre mostra o formulário de autenticação
  const [isRegister, setIsRegister] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleAuth = async (type) => {
    const endpoint = type === "login" ? "/api/auth/login" : "/api/auth/register";
    const body = type === "login" ? { email, password } : { name, email, password };

    try {
      const res = await fetch(`http://localhost:5000${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });
      const data = await res.json();
      if (data.token) {
        localStorage.setItem("token", data.token);
        window.location.href = "/dashboard";
      } else {
        alert(data.msg || "Erro na autenticação");
      }
    } catch (err) {
      alert("Erro ao comunicar com o servidor");
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
      {showAuth && (
        <div className="bg-gray-800 p-8 rounded-lg shadow-xl w-full max-w-md">
          <h2 className="text-3xl font-bold mb-6 text-center text-cyan-400">{isRegister ? "Registrar" : "Entrar"}</h2>
          {isRegister && (
            <input type="text" placeholder="Nome" value={name} onChange={(e) => setName(e.target.value)} className="w-full p-3 mb-4 bg-gray-700 text-white rounded-md border border-gray-600 focus:outline-none focus:border-cyan-400" />
          )}
          <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="w-full p-3 mb-4 bg-gray-700 text-white rounded-md border border-gray-600 focus:outline-none focus:border-cyan-400" />
          <input type="password" placeholder="Senha" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full p-3 mb-6 bg-gray-700 text-white rounded-md border border-gray-600 focus:outline-none focus:border-cyan-400" />
          <button onClick={() => handleAuth(isRegister ? "register" : "login")} className="w-full bg-cyan-400 text-gray-900 py-3 rounded-md font-bold text-lg hover:bg-cyan-500 transition duration-300">{isRegister ? "Registrar" : "Entrar"}</button>
          <button onClick={() => setIsRegister(!isRegister)} className="mt-4 text-sm text-gray-400 w-full text-center hover:text-cyan-400 transition duration-300">
            {isRegister ? "Já tem uma conta? Entrar" : "Não tem uma conta? Registrar"}
          </button>
        </div>
      )}
    </div>
  );
}