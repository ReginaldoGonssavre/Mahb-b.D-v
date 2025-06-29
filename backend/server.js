const express = require('express');
const cors = require('cors');
const multer = require('multer');
const mongoose = require('mongoose');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

// Import authentication routes and middleware
const { router: authRouter, protect } = require('./routes/auth');

// Middleware
app.use(cors());
app.use(express.json()); // For parsing application/json
app.use(express.urlencoded({ extended: true })); // For parsing application/x-www-form-urlencoded

// Multer setup for file uploads
const upload = multer({ dest: 'uploads/' });

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI || 'mongodb://mongo:27017/engenho', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected...'))
.catch(err => console.error(err));

// Mount authentication routes
app.use('/api/auth', authRouter);

// --- API Endpoints ---

// 1. Quantum Data Ingestion (File Upload)
app.post('/api/upload', upload.single('data'), protect, (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }
  console.log('File received:', req.file.originalname);
  // In a real application, process the file here (e.g., store, analyze, pass to quantum backend)
  res.json({ message: 'File uploaded successfully', filename: req.file.originalname, size: req.file.size });
});

// 3. Quantum Job Execution (General)
app.post('/api/ia', protect, (req, res) => {
  const { module, prompt } = req.body;
  console.log(`Quantum job request: Module - ${module}, Prompt - ${prompt}`);

  const jobDetails = {
    job_type: "quantum_algorithm",
    payload: { algorithm_name: module, params: prompt }
  };

  const pythonProcess = spawn('python3', ['./backend/quantum/run_quantum_job.py', JSON.stringify(jobDetails)]);

  let result = '';
  let error = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    error += data.toString();
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      console.error(`Python script exited with code ${code}, error: ${error}`);
      return res.status(500).json({ error: `Python script error: ${error}` });
    }
    try {
      const jsonResult = JSON.parse(result);
      res.json(jsonResult);
    } catch (e) {
      console.error('Failed to parse Python script output:', e, result);
      res.status(500).json({ error: 'Failed to parse Python script output.' });
    }
  });
});

// --- New Sector-Specific Placeholder Endpoints ---

// QuantumPredict Pro Endpoints
app.post('/api/predict/aerospace-trajectory', protect, (req, res) => {
  const { data } = req.body;
  console.log('Predicting aerospace trajectory with quantum algorithms:', data);
  res.json({ prediction: 'Optimized trajectory calculated (placeholder)' });
});

app.post('/api/predict/automotive-maintenance', protect, (req, res) => {
  const { sensorData } = req.body;
  console.log('Predicting automotive maintenance needs with QML:', sensorData);
  res.json({ prediction: 'Next maintenance due in X km (placeholder)' });
});

// QuantumRisk Guardian Endpoints
app.post('/api/risk/maritime-supply-chain', protect, (req, res) => {
  const { manifest, route } = req.body;
  console.log('Assessing maritime supply chain risk with quantum algorithms:', manifest, route);
  res.json({ risk_assessment: 'Low risk, optimized route (placeholder)' });
});

app.post('/api/risk/space-cybersecurity', protect, (req, res) => {
  const { systemId } = req.body;
  console.log('Assessing space cybersecurity posture with PQC:', systemId);
  res.json({ security_status: 'Post-quantum secure (placeholder)' });
});

// QuantumEco AI Endpoints
app.post('/api/eco/automotive-charging-optimization', protect, (req, res) => {
  const { vehicleId, location, time } = req.body;
  console.log('Optimizing EV charging for:', vehicleId, location, time);
  res.json({ optimal_charging_schedule: 'Charge from 2 AM to 4 AM (placeholder)' });
});

app.post('/api/eco/aero-material-design', protect, (req, res) => {
  const { materialSpecs } = req.body;
  console.log('Designing aerospace material with quantum simulation:', materialSpecs);
  res.json({ optimized_material_composition: 'New lightweight alloy (placeholder)' });
});

// QuantumSense Connect Endpoints
app.post('/api/sense/maritime-structural-integrity', protect, (req, res) => {
  const { sensorReadings } = req.body;
  console.log('Analyzing maritime structural integrity from quantum sensors:', sensorReadings);
  res.json({ integrity_report: 'No anomalies detected (placeholder)' });
});

app.post('/api/sense/space-navigation-precision', protect, (req, res) => {
  const { navData } = req.body;
  console.log('Enhancing space navigation precision with quantum sensor data:', navData);
  res.json({ enhanced_position: 'Lat: X, Lon: Y, Alt: Z (placeholder)' });
});

// --- Post-Quantum Cryptography Placeholder Endpoints ---
app.post('/api/pqc/encrypt', protect, (req, res) => {
  const { plaintext, public_key, algorithm } = req.body;
  console.log(`PQC encryption request: Algorithm - ${algorithm}, Plaintext - ${plaintext}`);

  const jobDetails = {
    job_type: "pqc_encrypt",
    payload: { plaintext, public_key, algorithm }
  };

  const pythonProcess = spawn('python3', ['./backend/quantum/run_quantum_job.py', JSON.stringify(jobDetails)]);

  let result = '';
  let error = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    error += data.toString();
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      console.error(`Python script exited with code ${code}, error: ${error}`);
      return res.status(500).json({ error: `Python script error: ${error}` });
    }
    try {
      const jsonResult = JSON.parse(result);
      res.json(jsonResult);
    } catch (e) {
      console.error('Failed to parse Python script output:', e, result);
      res.status(500).json({ error: 'Failed to parse Python script output.' });
    }
  });
});

app.post('/api/pqc/decrypt', protect, (req, res) => {
  const { ciphertext, private_key, algorithm } = req.body;
  console.log(`PQC decryption request: Algorithm - ${algorithm}, Ciphertext - ${ciphertext}`);

  const jobDetails = {
    job_type: "pqc_decrypt",
    payload: { ciphertext, private_key, algorithm }
  };

  const pythonProcess = spawn('python3', ['./backend/quantum/run_quantum_job.py', JSON.stringify(jobDetails)]);

  let result = '';
  let error = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    error += data.toString();
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      console.error(`Python script exited with code ${code}, error: ${error}`);
      return res.status(500).json({ error: `Python script error: ${error}` });
    }
    try {
      const jsonResult = JSON.parse(result);
      res.json(jsonResult);
    } catch (e) {
      console.error('Failed to parse Python script output:', e, result);
      res.status(500).json({ error: 'Failed to parse Python script output.' });
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Backend server listening at http://localhost:${port}`);
});