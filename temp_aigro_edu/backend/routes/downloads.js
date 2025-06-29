const express = require('express');
const router = express.Router();
const { getDownload } = require('../controllers/downloadsController');
const auth = require('../middleware/authMiddleware');
const freemium = require('../middleware/freemiumMiddleware');

// @route   GET api/downloads/:resourceId
// @desc    Get a downloadable resource
// @access  Private (requires auth and freemium check)
router.get('/:resourceId', auth, freemium, getDownload);

module.exports = router;