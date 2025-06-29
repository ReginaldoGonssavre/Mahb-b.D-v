import React from 'react';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Seção de Cabeçalho */}
      <header className="p-6 bg-gray-800 shadow-lg">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-3xl font-bold text-cyan-400">AigroQuantumSaaS</h1>
          <nav>
            <a href="#features" className="text-white hover:text-cyan-400 mx-4">Recursos</a>
            <a href="#modules" className="text-white hover:text-cyan-400 mx-4">Módulos</a>
            <a href="#pricing" className="text-white hover:text-cyan-400 mx-4">Preços</a>
            <a href="/login" className="bg-cyan-400 text-gray-900 py-2 px-6 rounded-full hover:bg-cyan-500 transition duration-300">Login</a>
          </nav>
        </div>
      </header>

      {/* Seção Hero */}
      <section className="hero-section text-center py-20 bg-cover bg-center" style={{ backgroundImage: 'url(https://via.placeholder.com/1500x800?text=Fundo+Espacial+Qu%C3%A2ntico)' }}>
        <div className="container mx-auto">
          <h2 className="text-5xl font-extrabold mb-4 leading-tight text-shadow-lg">A Revolução Tecnológica ao Seu Alcance</h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">Plataforma SaaS de ponta com IA Generativa, Robótica, Navegação Espacial e Tecnologia Quântica para transformar sua indústria e residência.</p>
          <a href="#pricing" className="bg-cyan-400 text-gray-900 py-3 px-8 rounded-full text-lg font-bold hover:bg-cyan-500 transition duration-300 shadow-lg">Experimente Grátis</a>
        </div>
      </section>

      {/* Seção de Recursos (Features) */}
      <section id="features" className="py-20 bg-gray-800">
        <div className="container mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 text-cyan-400">Recursos Inovadores</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div className="feature-card bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300">
              <h3 className="text-2xl font-bold mb-4">IA Generativa Avançada</h3>
              <p>Crie, otimize e automatize com inteligência artificial de última geração.</p>
            </div>
            <div className="feature-card bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300">
              <h3 className="text-2xl font-bold mb-4">Robótica e Automação</h3>
              <p>Controle e programe robôs e sistemas automatizados com precisão.</p>
            </div>
            <div className="feature-card bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300">
              <h3 className="text-2xl font-bold mb-4">Tecnologia Quântica</h3>
              <p>Explore o poder da computação quântica simulada para problemas complexos.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Seção de Módulos (Detalhes) */}
      <section id="modules" className="py-20 bg-gray-900">
        <div className="container mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 text-cyan-400">Módulos Especializados</h2>
          <div className="space-y-16">
            {/* Módulo 1: Robótica e Sistemas Embarcados */}
            <div className="module-item flex flex-col md:flex-row items-center bg-gray-800 p-8 rounded-lg shadow-xl">
              <img src="https://via.placeholder.com/300x200?text=Rob%C3%B3tica" alt="Robótica" className="w-full md:w-1/3 rounded-lg mb-6 md:mb-0 md:mr-8" />
              <div className="text-left md:w-2/3">
                <h3 className="text-3xl font-bold mb-4 text-cyan-400">Robótica e Sistemas Embarcados</h3>
                <p className="text-lg mb-4">Desenvolva, simule e controle robôs autônomos e sistemas embarcados para aplicações industriais e residenciais. Integração com hardware e software de ponta.</p>
                <ul className="list-disc list-inside text-gray-300">
                  <li>Controle de braços robóticos e drones</li>
                  <li>Programação de microcontroladores</li>
                  <li>Visão computacional para robôs</li>
                </ul>
              </div>
            </div>

            {/* Módulo 2: Navegação Espacial e GPS Quântico */}
            <div className="module-item flex flex-col md:flex-row-reverse items-center bg-gray-800 p-8 rounded-lg shadow-xl">
              <img src="https://via.placeholder.com/300x200?text=Navega%C3%A7%C3%A3o+Espacial" alt="Navegação Espacial" className="w-full md:w-1/3 rounded-lg mb-6 md:mb-0 md:ml-8" />
              <div className="text-left md:w-2/3">
                <h3 className="text-3xl font-bold mb-4 text-cyan-400">Navegação Espacial e GPS Quântico</h3>
                <p className="text-lg mb-4">Soluções de posicionamento e navegação de ultra-precisão para veículos autônomos, drones e exploração espacial, utilizando princípios quânticos.</p>
                <ul className="list-disc list-inside text-gray-300">
                  <li>Sistemas de posicionamento global de próxima geração</li>
                  <li>Navegação autônoma para missões espaciais</li>
                  <li>Otimização de rotas em ambientes complexos</li>
                </ul>
              </div>
            </div>

            {/* Módulo 3: Automação de Máquinas e Energia Elétrica */}
            <div className="module-item flex flex-col md:flex-row items-center bg-gray-800 p-8 rounded-lg shadow-xl">
              <img src="https://via.placeholder.com/300x200?text=Automa%C3%A7%C3%A3o" alt="Automação" className="w-full md:w-1/3 rounded-lg mb-6 md:mb-0 md:mr-8" />
              <div className="text-left md:w-2/3">
                <h3 className="text-3xl font-bold mb-4 text-cyan-400">Automação de Máquinas e Energia Elétrica</h3>
                <p className="text-lg mb-4">Gerencie e otimize o consumo de energia, automatize processos industriais e residenciais com sistemas inteligentes e eficientes.</p>
                <ul className="list-disc list-inside text-gray-300">
                  <li>Monitoramento e controle de redes elétricas</li>
                  <li>Automação predial e industrial</li>
                  <li>Otimização de consumo energético com IA</li>
                </ul>
              </div>
            </div>

            {/* Módulo 4: Produtos Digitais e Tecnologia Quântica */}
            <div className="module-item flex flex-col md:flex-row-reverse items-center bg-gray-800 p-8 rounded-lg shadow-xl">
              <img src="https://via.placeholder.com/300x200?text=Produtos+Digitais" alt="Produtos Digitais" className="w-full md:w-1/3 rounded-lg mb-6 md:mb-0 md:ml-8" />
              <div className="text-left md:w-2/3">
                <h3 className="text-3xl font-bold mb-4 text-cyan-400">Produtos Digitais e Tecnologia Quântica</h3>
                <p className="text-lg mb-4">Acesse uma biblioteca exclusiva de e-books, cursos e ferramentas digitais, e mergulhe na vanguarda da tecnologia quântica aplicada.</p>
                <ul className="list-disc list-inside text-gray-300">
                  <li>E-books e guias especializados</li>
                  <li>Cursos interativos sobre IA e Quântica</li>
                  <li>Ferramentas de simulação quântica</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Seção de Preços (Pricing) */}
      <section id="pricing" className="py-20 bg-gray-800">
        <div className="container mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 text-cyan-400">Planos Flexíveis para Você</h2>
          <p className="text-xl text-center mb-12 max-w-2xl mx-auto">Escolha o plano que melhor se adapta às suas necessidades, do acesso gratuito para experimentação ao premium ilimitado.</p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            {/* Plano Freemium */}
            <div className="pricing-card bg-gray-700 p-8 rounded-lg shadow-xl border-2 border-cyan-400 transform hover:scale-105 transition duration-300">
              <h3 className="text-3xl font-bold mb-4 text-cyan-400">Freemium</h3>
              <p className="text-5xl font-extrabold mb-4">Grátis</p>
              <p className="text-lg mb-6">Ideal para começar e explorar as funcionalidades básicas.</p>
              <ul className="list-disc list-inside text-left mb-8 space-y-2">
                <li>Acesso limitado a módulos de IA</li>
                <li>X horas de uso gratuito por mês</li>
                <li>Suporte básico</li>
                <li>Acesso a e-books introdutórios</li>
              </ul>
              <a href="/register" className="bg-cyan-400 text-gray-900 py-3 px-8 rounded-full text-lg font-bold hover:bg-cyan-500 transition duration-300">Comece Grátis</a>
            </div>

            {/* Plano Premium */}
            <div className="pricing-card bg-gray-700 p-8 rounded-lg shadow-xl border-2 border-purple-500 transform hover:scale-105 transition duration-300">
              <h3 className="text-3xl font-bold mb-4 text-purple-500">Premium</h3>
              <p className="text-5xl font-extrabold mb-4">$99<span className="text-xl">/mês</span></p>
              <p className="text-lg mb-6">Acesso ilimitado a todos os recursos e suporte prioritário.</p>
              <ul className="list-disc list-inside text-left mb-8 space-y-2">
                <li>Acesso ilimitado a todos os módulos de IA</li>
                <li>Horas de uso ilimitadas</li>
                <li>Suporte prioritário 24/7</li>
                <li>Biblioteca completa de e-books e cursos</li>
                <li>Acesso a downloads exclusivos</li>
              </ul>
              <a href="#" className="bg-purple-500 text-white py-3 px-8 rounded-full text-lg font-bold hover:bg-purple-600 transition duration-300">Assinar Agora</a>
            </div>

            {/* Plano Enterprise */}
            <div className="pricing-card bg-gray-700 p-8 rounded-lg shadow-xl border-2 border-yellow-400 transform hover:scale-105 transition duration-300">
              <h3 className="text-3xl font-bold mb-4 text-yellow-400">Enterprise</h3>
              <p className="text-5xl font-extrabold mb-4">Personalizado</p>
              <p className="text-lg mb-6">Soluções customizadas para grandes indústrias e corporações.</p>
              <ul className="list-disc list-inside text-left mb-8 space-y-2">
                <li>Todos os recursos Premium</li>
                <li>Integração com sistemas existentes</li>
                <li>Desenvolvimento de módulos sob demanda</li>
                <li>Gerente de conta dedicado</li>
              </ul>
              <a href="#" className="bg-yellow-400 text-gray-900 py-3 px-8 rounded-full text-lg font-bold hover:bg-yellow-500 transition duration-300">Fale Conosco</a>
            </div>
          </div>
        </div>
      </section>

      {/* Seção de Chamada para Ação Final */}
      <section className="cta-final-section text-center py-20 bg-gray-900">
        <div className="container mx-auto">
          <h2 className="text-4xl font-bold mb-6 text-cyan-400">Pronto para a Transformação?</h2>
          <p className="text-xl mb-10 max-w-2xl mx-auto">Junte-se aos líderes de mercado que já estão utilizando a AigroQuantumSaaS para inovar e crescer.</p>
          <a href="#pricing" className="bg-cyan-400 text-gray-900 py-3 px-8 rounded-full text-lg font-bold hover:bg-cyan-500 transition duration-300 shadow-lg">Comece Sua Jornada</a>
        </div>
      </section>

      {/* Rodapé */}
      <footer className="py-10 bg-gray-800 text-gray-400 text-center">
        <div className="container mx-auto">
          <p>&copy; 2025 AigroQuantumSaaS. Todos os direitos reservados.</p>
          <div className="mt-4 space-x-4">
            <a href="#" className="hover:text-cyan-400">Termos de Serviço</a>
            <a href="#" className="hover:text-cyan-400">Política de Privacidade</a>
            <a href="#" className="hover:text-cyan-400">Contato</a>
          </div>
        </div>
      </footer>

      {/* Estilos Tailwind CSS (para ser incluído no index.css ou similar) */}
      <style jsx>{`
        .container {
          max-width: 1200px;
          padding-left: 1rem;
          padding-right: 1rem;
        }
        .text-shadow-lg {
          text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        }
        .hero-section {
          background-size: cover;
          background-position: center;
          min-height: 600px;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .feature-card, .pricing-card {
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
        }
        .pricing-card ul {
          width: 100%;
        }
        .pricing-card li {
          margin-left: 1.5rem;
        }
        .module-item img {
          object-fit: cover;
        }
      `}</style>
    </div>
  );
}