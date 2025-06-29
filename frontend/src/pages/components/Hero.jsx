import React from 'react';

export default function Hero({ onGetStarted }) {
  return (
    <section className="text-center py-20 px-4">
      <h2 className="text-4xl font-bold mb-4">Aprenda Engenharia da Computação com IA</h2>
      <p className="text-lg mb-8">Nossa plataforma oferece cursos interativos, correção de código e gamificação para impulsionar seu aprendizado.</p>
      <button onClick={onGetStarted} className="bg-cyan-400 text-black py-3 px-6 rounded text-lg font-bold">Comece Agora</button>
    </section>
  );
}