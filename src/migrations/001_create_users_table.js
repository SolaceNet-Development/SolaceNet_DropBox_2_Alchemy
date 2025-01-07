const mongoose = require('mongoose');
const User = require('../models/User');

const createUsersTable = async () => {
  await mongoose.connect('mongodb://localhost:27017/solaceNet', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  const users = [
    { username: 'user1', password: 'password1', email: 'user1@example.com' },
    { username: 'user2', password: 'password2', email: 'user2@example.com' },
    { username: 'user3', password: 'password3', email: 'user3@example.com' },
    { username: 'user4', password: 'password4', email: 'user4@example.com' },
  ];

  try {
    await User.insertMany(users);
    console.log('Users table created and seeded');
  } catch (error) {
    console.error('Error seeding users table:', error);
  } finally {
    await mongoose.connection.close();
  }
};

createUsersTable().catch(console.error);
