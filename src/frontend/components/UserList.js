import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get('/api/users');
        setUsers(response.data);
      } catch (error) {
        console.error('Error fetching users', error);
        setError('Failed to fetch users');
      }
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h1>User List</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {users.map(user => (
          <li key={user._id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
