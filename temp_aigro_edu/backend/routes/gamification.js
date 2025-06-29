const express = require("express");
const router = express.Router();
const auth = require("../middleware/authMiddleware");
const UserProgress = require("../models/UserProgress");
const Achievement = require("../models/Achievement");

router.get("/progress", auth, async (req, res) => {
  try {
    const progress = await UserProgress.findOne({ userId: req.user.id });
    res.json(progress);
  } catch (err) {
    res.status(500).send("Erro no servidor");
  }
});

router.post("/add-xp", auth, async (req, res) => {
  const { xp } = req.body;
  try {
    const progress = await UserProgress.findOneAndUpdate(
      { userId: req.user.id },
      { $inc: { xp: xp }, $set: { lastLogin: new Date() } },
      { upsert: true, new: true }
    );
    res.json(progress);
  } catch (err) {
    res.status(500).send("Erro ao atualizar XP");
  }
});

module.exports = router;