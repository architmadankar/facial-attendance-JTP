import axios from 'axios';

export default {
  getDashboard() {
    return axios.get('http://localhost:5000/dashboard')
      .then(response => {
        if (response.status === 200) {
          return response.data;
        } else {
          throw new Error('Server responded with non-OK status');
        }
      })
      .catch(error => {
        if (error.response && error.response.status === 401) {
          return { error: error.response.data.message };
        } else if (error.request) {
          throw new Error('No response received from server');
        } else {
          throw error;
        }
      });
  }
};