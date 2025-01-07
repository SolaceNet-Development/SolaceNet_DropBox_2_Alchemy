const express = require('express');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const userRoutes = require('./routes/users');
const authMiddleware = require('./middleware/auth');

// Initialize the app
const app = express();

// Middleware
app.use(express.json());

// Connect to the database
mongoose.connect('mongodb://localhost:27017/solaceNet', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);

// Protected route example
app.get('/api/protected', authMiddleware, (req, res) => {
  res.status(200).json({ message: 'Protected route accessed' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

module.exports = app;