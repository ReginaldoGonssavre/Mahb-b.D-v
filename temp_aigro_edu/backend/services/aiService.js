const { GoogleGenerativeAI } = require("@google/generative-ai");

// Access your API key as an environment variable (e.g., from .env file)
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function callGeminiAPI(prompt) {
  try {
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    return text;
  } catch (error) {
    console.error("Erro ao chamar a API Gemini:", error);
    return "Erro ao processar sua solicitação com a IA.";
  }
}

module.exports = { callGeminiAPI };