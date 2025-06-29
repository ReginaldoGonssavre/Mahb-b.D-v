const express = require("express");
const cors = require("cors");
const connectDB = require("./config/db");
require("dotenv").config();

connectDB();

const app = express();
app.use(express.json());
app.use(cors());

// Rotas
app.use("/api/auth", require("./routes/auth"));
app.use("/api/courses", require("./routes/course"));
app.use("/api/gamification", require("./routes/gamification"));
app.use("/api/ai", require("./routes/ai"));
app.use("/api/downloads", require("./routes/downloads"));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));