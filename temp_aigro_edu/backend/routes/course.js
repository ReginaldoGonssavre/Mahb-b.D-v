const express = require("express");
const router = express.Router();
const auth = require("../middleware/authMiddleware");
const Course = require("../models/Course");

router.get("/courses", auth, async (req, res) => {
  try {
    const courses = await Course.find();
    res.json(courses);
  } catch (err) {
    res.status(500).send("Erro no servidor");
  }
});

module.exports = router;