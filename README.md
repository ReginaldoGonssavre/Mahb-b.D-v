#  AigroQuantumSaaS - Plataforma Educacional com IA

Plataforma educacional para estudantes de Engenharia da Computação, com correção automática de código, análise de desempenho e gamificação.

## ️ Tecnologias

| Camada | Tecnologia |
|--------|------------|
| Frontend | React.js + Tailwind CSS |
| Backend | Node.js + Express |
| Banco | MongoDB |
| IA | OpenAI API |
| Deploy | GitHub Actions |

##  Estrutura do Projeto

```
AigroQuantumSaaS-EduTech-IA/
├── frontend/
├── backend/
├── ai/
├── tests/
├── .github/workflows/deploy.yml
└── README.md
```

##  Como Rodar Localmente

1. Clone o repositório  
2. Configure `.env`  
3. Suba os serviços:
   ```bash
   docker-compose up
   ```
4. Abra http://localhost:3000