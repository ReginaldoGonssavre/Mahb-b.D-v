import React from 'react';
import { Link } from 'react-router-dom';

const articles = [
  { id: 1, title: 'The Basics of Quantum Computing', summary: 'An introduction to the fundamental principles of quantum mechanics and how they apply to computing.' },
  { id: 2, title: 'Understanding Qubits', summary: 'A deep dive into the building blocks of quantum computers.' },
  { id: 3, title: 'Quantum Supremacy: What It Means', summary: 'Exploring the concept of quantum supremacy and its implications for the future.' },
];

const Articles = () => {
  return (
    <div className="container mt-5">
      <h1 className="mb-4">Articles</h1>
      <div className="row">
        {articles.map(article => (
          <div className="col-md-4 mb-4" key={article.id}>
            <div className="card h-100 card-custom">
              <div className="card-body">
                <h5 className="card-title">{article.title}</h5>
                <p className="card-text">{article.summary}</p>
                <Link to={`/articles/${article.id}`} className="btn btn-outline-light">Read More</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Articles;