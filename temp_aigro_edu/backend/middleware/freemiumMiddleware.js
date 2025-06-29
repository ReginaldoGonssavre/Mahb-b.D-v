const User = require('../models/User');

module.exports = async function (req, res, next) {
  try {
    const user = req.user; // User object attached by authMiddleware

    if (user.isPremium) {
      return next(); // Premium users have full access
    }

    // Check free trial hours
    if (user.freeTrialHoursUsed < user.freeTrialHoursLimit) {
      // Increment used hours (this is a simplified example, you might want to track actual usage time)
      user.freeTrialHoursUsed += 1; // Increment by 1 for each AI call
      await user.save();
      return next();
    } else {
      return res.status(403).json({ msg: 'Free trial hours exhausted. Please upgrade to premium.' });
    }
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
};