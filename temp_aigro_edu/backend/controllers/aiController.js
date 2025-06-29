const { callGeminiAPI } = require('../services/aiService');

exports.processFinancial = async (req, res) => {
  const { prompt } = req.body;
  try {
    const result = await callGeminiAPI(`Análise Financeira: ${prompt}`);
    res.json({ analysis: result, type: 'financial' });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
};

exports.processAI = async (req, res) => {
  const { prompt } = req.body;
  try {
    const result = await callGeminiAPI(`Engenharia de Prompts: ${prompt}`);
    res.json({ analysis: result, type: 'ai' });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
};