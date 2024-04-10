import axios from 'axios';

const REGISTER_URL = 'http://localhost:5000/admin/signup';
const LOGIN_URL = 'http://localhost:5000/admin/login';

export default {
  registerUser(user) {
    return axios.post(REGISTER_URL, user);
  },

  loginUser(user) {
    return new Promise((resolve, reject) => {
      axios.post(LOGIN_URL, user)
        .then(response => {
          if (response.data.success) {
            // Store the user's information in localStorage
            localStorage.setItem('user', JSON.stringify(response.data.user));
            resolve(response.data.user);
          } else {
            reject(new Error(response.data.message));
          }
        })
        .catch(error => {
          reject(error);
        });
    });
  },

  loggedIn() {
    // Check if the user's information is in localStorage
    return localStorage.getItem('user') !== null;
  },

  logoutUser() {
    // Remove the user's information from localStorage
    localStorage.removeItem('user');
  },

  getUser() {
    // Retrieve the user's information from localStorage
    return JSON.parse(localStorage.getItem('user'));
  }
};