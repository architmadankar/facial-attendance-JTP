<template>
  <div class="mt-5">
    <div v-if="responseMsg" class="alert alert-success" role="alert">
      {{ responseMsg }}
      <button type="button" class="close" @click="responseMsg = ''">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div v-if="errorMsg" class="alert alert-danger" role="alert">
      {{ errorMsg }}
      <button type="button" class="close" @click="errorMsg = ''">
        <span aria-hidden="true">&times;</span>
      </button>
      <div>
    <h1>Welcome, {{ user.username }}</h1>
    <!-- Add more user information here -->
  </div>
    </div>
  </div>
</template>

<script>
import dashboardService from '@/services/dashboard.service';
import authService from '@/services/auth.service';

export default {
  name: 'UserDashboard',
  data() {
    return {
      responseMsg: '',
      errorMsg: '',
      user: authService.getUser()
    };
  },
  created() {
    this.fetchDashboard();
  },
  methods: {
    fetchDashboard() {
      dashboardService.getDashboard()
        .then(data => {
          if (data.error) {
            this.errorMsg = data.error;
          } else {
            this.responseMsg = data.message;
          }
        })
        .catch(error => {
          console.error('Error fetching dashboard:', error);
        });
    }
  }
};
</script>

<style scoped>
/* Add your component styles here */
</style>