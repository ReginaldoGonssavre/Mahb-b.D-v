const mongoose = require('mongoose');
const User = require('../models/User');
const Course = require('../models/Course');
const bcrypt = require('bcryptjs');
require('dotenv').config({ path: '../.env' }); // Carrega as variáveis de ambiente do .env do backend

const coursesData = [
  {
    title: "Introdução à Robótica Avançada",
    description: "Aprenda os fundamentos da robótica, desde a cinemática até o controle de robôs industriais.",
    content: "Link para o conteúdo do curso de robótica."
  },
  {
    title: "Sistemas Embarcados com IA",
    description: "Desenvolva sistemas embarcados inteligentes para diversas aplicações, utilizando microcontroladores e algoritmos de IA.",
    content: "Link para o conteúdo do curso de sistemas embarcados."
  },
  {
    title: "Navegação Espacial e GPS Quântico",
    description: "Explore os princípios da navegação espacial e as inovações do GPS quântico para posicionamento de alta precisão.",
    content: "Link para o conteúdo do curso de navegação espacial."
  },
  {
    title: "Automação de Máquinas Industriais",
    description: "Domine as técnicas de automação para otimizar processos em ambientes industriais, com foco em eficiência e segurança.",
    content: "Link para o conteúdo do curso de automação de máquinas."
  },
  {
    title: "Gestão de Energia Elétrica Inteligente",
    description: "Entenda como a IA pode ser aplicada na gestão e otimização do consumo de energia elétrica em residências e indústrias.",
    content: "Link para o conteúdo do curso de energia elétrica."
  },
  {
    title: "Criação de Produtos Digitais e E-books",
    description: "Aprenda a criar e comercializar produtos digitais, incluindo e-books e cursos online, com estratégias de marketing digital.",
    content: "Link para o conteúdo do curso de produtos digitais."
  },
  {
    title: "Fundamentos da Tecnologia Quântica",
    description: "Uma introdução aos conceitos da mecânica quântica e suas aplicações emergentes em computação e comunicação.",
    content: "Link para o conteúdo do curso de tecnologia quântica."
  }
];

const seedDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB Conectado para Seed!');

    // Limpar dados existentes
    await User.deleteMany({});
    await Course.deleteMany({});
    console.log('Dados existentes limpos.');

    // Criar um usuário de exemplo
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash('password123', salt);
    const adminUser = new User({
      name: 'Admin User',
      email: 'admin@example.com',
      password: hashedPassword,
      isPremium: true, // Usuário premium para testes
    });
    await adminUser.save();
    console.log('Usuário Admin criado.');

    const freeUser = new User({
      name: 'Free User',
      email: 'free@example.com',
      password: hashedPassword,
      isPremium: false,
      freeTrialHoursUsed: 0,
      freeTrialHoursLimit: 5, // 5 horas de trial para o usuário gratuito
    });
    await freeUser.save();
    console.log('Usuário Gratuito criado.');

    // Inserir cursos
    await Course.insertMany(coursesData);
    console.log('Cursos inseridos.');

    console.log('Banco de dados populado com sucesso!');
    process.exit(0);
  } catch (err) {
    console.error('Erro ao popular o banco de dados:', err);
    process.exit(1);
  }
};

seedDB();