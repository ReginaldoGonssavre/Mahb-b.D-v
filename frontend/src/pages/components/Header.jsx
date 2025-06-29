import React from 'react';

export default function Header({ onLoginClick }) {
  return (
    <header className="flex justify-between items-center p-4 bg-gray-800 text-white">
      <h1 className="text-2xl font-bold">AigroQuantumSaaS</h1>
      <button onClick={onLoginClick} className="bg-cyan-400 text-black py-2 px-4 rounded">Entrar</button>
    </header>
  );
}