const mongoose = require('mongoose');

const UserProgressSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  xp: { type: Number, default: 0 },
  lastLogin: { type: Date, default: Date.now }
});

module.exports = mongoose.model('UserProgress', UserProgressSchema);