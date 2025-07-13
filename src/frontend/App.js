import React, { useState } from 'react';
import './App.css'; // Importa o arquivo CSS

function App() {
  const [token, setToken] = useState('');
  const [msg, setMsg] = useState('');
  const [user, setUser] = useState(null);

  async function register(e) {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
    const res = await fetch('/api/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    setMsg((await res.json()).msg || 'Erro');
  }

  async function login(e) {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (data.access_token) {
      setToken(data.access_token);
      setMsg('Login ok');
    } else {
      setMsg('Erro login');
    }
  }

  async function getMe() {
    const res = await fetch('/api/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    });
    setUser(await res.json());
  }

  async function quantum() {
    const prompt = window.prompt("Prompt para quantum (ex: superposição)?", "superposição");
    const res = await fetch('/api/ia', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({ module: 'quantum', prompt })
    });
    setMsg(JSON.stringify(await res.json(), null, 2));
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>AigroQuantumSaaS Frontend</h1>
        <p>Plataforma de Inovação Quântica e IA</p>
      </header>

      <main className="App-main">
        <section className="auth-section">
          <form onSubmit={register} className="auth-form">
            <h2>Registrar</h2>
            <input name="username" placeholder="Usuário" required />
            <input name="password" type="password" placeholder="Senha" required />
            <button type="submit">Registrar</button>
          </form>

          <form onSubmit={login} className="auth-form">
            <h2>Login</h2>
            <input name="username" placeholder="Usuário" required />
            <input name="password" type="password" placeholder="Senha" required />
            <button type="submit">Entrar</button>
          </form>
        </section>

        <section className="features-section">
          <button onClick={getMe} disabled={!token} className="action-button">Meus Dados</button>
          <button onClick={quantum} disabled={!token} className="action-button">Quantum Job</button>
        </section>

        <section className="message-section">
          <h3>Mensagens:</h3>
          <pre className="message-box">{msg}</pre>
          {user && (
            <>
              <h3>Dados do Usuário:</h3>
              <pre className="user-data-box">{JSON.stringify(user, null, 2)}</pre>
            </>
          )}
        </section>

        <section className="monetization-section">
          <h2>Apoie Nosso Projeto</h2>
          <div className="monetization-options">
            <div className="donation-card">
              <h3>Doações</h3>
              <p>Ajude-nos a continuar inovando com uma doação.</p>
              <button className="donate-button">Doar Agora</button>
              <p className="placeholder-text">(Integração com plataforma de pagamento)</p>
            </div>
            <div className="sponsorship-card">
              <h3>Patrocínio</h3>
              <p>Torne-se um patrocinador e apoie o futuro da tecnologia quântica.</p>
              <button className="sponsor-button">Saiba Mais</button>
              <p className="placeholder-text">(Informações para contato/proposta)</p>
            </div>
          </div>
        </section>
      </main>

      <footer className="App-footer">
        <p>&copy; 2025 AigroQuantumSaaS. Todos os direitos reservados.</p>
      </footer>
    </div>
  );
}

export default App;
