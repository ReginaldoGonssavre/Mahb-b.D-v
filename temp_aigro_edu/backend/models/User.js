const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  date: { type: Date, default: Date.now },
  isPremium: { type: Boolean, default: false },
  freeTrialHoursUsed: { type: Number, default: 0 },
  freeTrialHoursLimit: { type: Number, default: 100 } // Exemplo: 100 horas de trial
});

module.exports = mongoose.model('User', UserSchema);