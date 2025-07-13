import React from 'react';
import { useParams } from 'react-router-dom';

const articles = {
  1: {
    title: 'The Basics of Quantum Computing',
    content: `Quantum computing is a revolutionary type of computation that harnesses the principles of quantum mechanics to solve problems too complex for classical computers. Unlike classical bits, which can be a 0 or a 1, a quantum bit, or qubit, can be in a superposition of both states simultaneously. This allows quantum computers to perform a vast number of calculations at once. Another key concept is entanglement, a phenomenon where two qubits become linked in such a way that their fates are intertwined, no matter the distance separating them. These properties, governed by the laws of quantum physics, are the foundation upon which quantum algorithms are built.`
  },
  2: {
    title: 'Understanding Qubits',
    content: `A qubit is the fundamental unit of quantum information. While a classical bit is restricted to a single binary value (0 or 1), a qubit can exist in a complex combination of both. This state, called superposition, is often visualized as a point on the surface of a sphere (the Bloch sphere). When measured, a qubit collapses to a definite state of 0 or 1, but before measurement, it holds the potential for both. This probabilistic nature is what gives quantum computers their immense parallel processing power. The manipulation of qubits is done using quantum gates, which are the quantum equivalent of classical logic gates.`
  },
  3: {
    title: 'Quantum Supremacy: What It Means',
    content: `Quantum supremacy, or quantum advantage, is the milestone at which a programmable quantum computer can solve a problem that no classical computer could feasibly solve in a reasonable amount of time. It's a demonstration of the superior processing power of quantum systems for specific, often contrived, tasks. In 2019, Google claimed to have achieved this with its Sycamore processor. While a significant scientific achievement, it does not mean quantum computers are ready to replace classical ones. The problems they excel at are very specific, and building a fault-tolerant, general-purpose quantum computer remains a major challenge for the field.`
  },
};

const ArticleDetail = () => {
  const { id } = useParams();
  const article = articles[id];

  return (
    <div className="container mt-5">
      <div className="card card-custom p-4">
        <h1>{article.title}</h1>
        <p className="mt-3 fs-5">{article.content}</p>
      </div>
    </div>
  );
};

export default ArticleDetail;