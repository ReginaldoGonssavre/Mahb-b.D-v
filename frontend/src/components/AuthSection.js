import React from 'react';
import { useTranslation } from 'react-i18next';

const AuthSection = ({ register, login, getMe, quantum, token, msg, user,
  predictAerospaceTrajectory, predictAutomotiveMaintenance,
  assessMaritimeSupplyChainRisk, assessSpaceCybersecurity,
  optimizeAutomotiveCharging, designAeroMaterial,
  analyzeMaritimeStructuralIntegrity, enhanceSpaceNavigationPrecision,
  encryptPQC, decryptPQC, pqcPlaintext, setPqcPlaintext, pqcCiphertext, setPqcCiphertext, pqcAlgorithm, setPqcAlgorithm
}) => {
  const { t } = useTranslation();
  return (
    <section className="auth-section">
      <h1>AigroQuantumSaaS Frontend</h1>
      <form onSubmit={register}>
        <h2>Registrar</h2>
        <input name="username" placeholder="Usuário" />
        <input name="password" type="password" placeholder="Senha" />
        <button type="submit">Registrar</button>
      </form>
      <form onSubmit={login}>
        <h2>Login</h2>
        <input name="username" placeholder="Usuário" />
        <input name="password" type="password" placeholder="Senha" />
        <button type="submit">Entrar</button>
      </form>
      <button onClick={getMe} disabled={!token}>Meus Dados</button>
      <button onClick={quantum} disabled={!token}>Quantum Job</button>

      {/* New Product Demo Buttons */}
      <h2>Product Demos (Requires Login)</h2>
      <button onClick={predictAerospaceTrajectory} disabled={!token}>Predict Aerospace Trajectory</button>
      <button onClick={predictAutomotiveMaintenance} disabled={!token}>Predict Auto Maintenance</button>
      <button onClick={assessMaritimeSupplyChainRisk} disabled={!token}>Assess Maritime Risk</button>
      <button onClick={assessSpaceCybersecurity} disabled={!token}>Assess Space Security</button>
      <button onClick={optimizeAutomotiveCharging} disabled={!token}>Optimize Auto Charging</button>
      <button onClick={designAeroMaterial} disabled={!token}>Design Aero Material</button>
      <button onClick={analyzeMaritimeStructuralIntegrity} disabled={!token}>Analyze Maritime Integrity</button>
      <button onClick={enhanceSpaceNavigationPrecision} disabled={!token}>Enhance Space Nav Precision</button>

      {/* Post-Quantum Cryptography Section */}
      <h2>Post-Quantum Cryptography (PQC) Demo</h2>
      <div>
        <label>Plaintext:</label>
        <input type="text" value={pqcPlaintext} onChange={(e) => setPqcPlaintext(e.target.value)} />
      </div>
      <div>
        <label>Algorithm:</label>
        <select value={pqcAlgorithm} onChange={(e) => setPqcAlgorithm(e.target.value)}>
          <option value="dilithium">Dilithium</option>
          <option value="kyber">Kyber</option>
        </select>
      </div>
      <button onClick={encryptPQC} disabled={!token}>Encrypt (PQC)</button>
      <button onClick={decryptPQC} disabled={!token}>Decrypt (PQC)</button>
      {pqcCiphertext && <p>Ciphertext: {pqcCiphertext}</p>}

      <pre>{msg}</pre>
      {user && <pre>{JSON.stringify(user, null, 2)}</pre>}
    </section>
  );
};

export default AuthSection;