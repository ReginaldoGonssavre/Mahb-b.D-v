const mongoose = require('mongoose');

const AchievementSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  name: { type: String, required: true },
  date: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Achievement', AchievementSchema);