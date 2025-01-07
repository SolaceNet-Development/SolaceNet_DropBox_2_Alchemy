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

describe('User Routes', () => {
  let userId;

  it('should create a new user', async () => {
    const res = await request(app)
      .post('/api/users')
      .send({
        username: 'testuser',
        password: 'testpassword',
        email: 'testuser@example.com',
      });
    expect(res.statusCode).toEqual(201);
    expect(res.body).toHaveProperty('_id');
    userId = res.body._id;
  });

  it('should get all users', async () => {
    const res = await request(app).get('/api/users');
    expect(res.statusCode).toEqual(200);
    expect(res.body).toBeInstanceOf(Array);
  });

  it('should get a user by ID', async () => {
    const res = await request(app).get(`/api/users/${userId}`);
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('_id', userId);
  });

  it('should update a user', async () => {
    const res = await request(app)
      .put(`/api/users/${userId}`)
      .send({ username: 'updateduser' });
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('username', 'updateduser');
  });

  it('should delete a user', async () => {
    const res = await request(app).delete(`/api/users/${userId}`);
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('message', 'User deleted successfully');
  });

  // New tests for user authentication and authorization
  it('should register a new user', async () => {
    const res = await request(app)
      .post('/api/auth/register')
      .send({
        username: 'newuser',
        password: 'newpassword',
        email: 'newuser@example.com',
      });
    expect(res.statusCode).toEqual(201);
    expect(res.body).toHaveProperty('token');
  });

  it('should login a user', async () => {
    const res = await request(app)
      .post('/api/auth/login')
      .send({
        username: 'newuser',
        password: 'newpassword',
      });
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('token');
  });

  it('should access a protected route', async () => {
    const loginRes = await request(app)
      .post('/api/auth/login')
      .send({
        username: 'newuser',
        password: 'newpassword',
      });
    const token = loginRes.body.token;

    const res = await request(app)
      .get('/api/protected')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('message', 'Protected route accessed');
  });
});
