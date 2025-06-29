const express = require('express');
const router = express.Router();
const { processFinancial, processAI } = require('../controllers/aiController');
const auth = require('../middleware/authMiddleware');
const freemium = require('../middleware/freemiumMiddleware');

router.post('/financial', auth, freemium, processFinancial);
router.post('/ai', auth, freemium, processAI);

module.exports = router;