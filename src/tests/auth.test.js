const request = require('supertest');
const app = require('../index');
const mongoose = require('mongoose');
const User = require('../models/User');

beforeAll(async () => {
  await mongoose.connect('mongodb://localhost:27017/solaceNetTest', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
});

afterAll(async () => {
  await mongoose.connection.close();
});

describe('Auth Routes', () => {
  let token;

  it('should register a new user', async () => {
    const res = await request(app)
      .post('/api/auth/register')
      .send({
        username: 'testuser',
        password: 'testpassword',
        email: 'testuser@example.com',
      });
    expect(res.statusCode).toEqual(201);
    expect(res.body).toHaveProperty('token');
    token = res.body.token;
  });

  it('should login a user', async () => {
    const res = await request(app)
      .post('/api/auth/login')
      .send({
        username: 'testuser',
        password: 'testpassword',
      });
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('token');
  });

  it('should access a protected route', async () => {
    const res = await request(app)
      .get('/api/protected')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('message', 'Protected route accessed');
  });
});
