import axios from 'axios';

const REGISTER_URL = 'http://localhost:5000/admin/signup';
const LOGIN_URL = 'http://localhost:5000/admin/login';

export default {
  registerUser(user) {
    return axios.post(REGISTER_URL, user);
  },

  loginUser(user) {
    return axios.post(LOGIN_URL, user);
  },

  loggedIn() {
    return !!localStorage.getItem('access_token');
  },

  logoutUser() {
    localStorage.removeItem('access_token');
    // Assuming you're using Vue Router
    this.$router.push('/login');
  },

  getToken() {
    return localStorage.getItem('access_token');
  }
};
