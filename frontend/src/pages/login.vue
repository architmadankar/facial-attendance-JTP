<template>
  <div class="py-5">
    <div class="row">
      <div class="col-md-6 mx-auto">
        <div class="card rounded-0">
          <div class="card-header">
            <h3 class="mb-0">Login</h3>
          </div>
          <div class="card-body">
            <div v-if="errorMsg" class="alert alert-danger" role="alert">
              {{ errorMsg }}
              <button type="button" class="close" @click="errorMsg = ''">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <form @submit.prevent="loginUser" novalidate>
              <div class="form-group">
                <label for="username">Username</label>
                <input v-model="username" type="text" id="username" class="form-control rounded-0"
                  :class="{ 'is-invalid': !isUsernameValid && isUsernameTouched }">
                <small v-if="!isUsernameValid && isUsernameTouched" class="text-danger">Username is required</small>
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input v-model="password" type="password" id="password" class="form-control rounded-0"
                  :class="{ 'is-invalid': !isPasswordValid && isPasswordTouched }">
                <small v-if="!isPasswordValid && isPasswordTouched" class="text-danger">Password is required</small>
              </div>
              <button :disabled="!isLoginFormValid" type="submit" class="btn btn-success float-right">Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from '@/services/auth.service';

export default {
  name: 'UserLogin',
  data() {
    return {
      username: '',
      password: '',
      isUsernameTouched: false,
      isPasswordTouched: false,
      errorMsg: ''
    };
  },
  computed: {
    isUsernameValid() {
      return !!this.username.trim();
    },
    isPasswordValid() {
      return !!this.password.trim();
    },
    isLoginFormValid() {
      return this.isUsernameValid && this.isPasswordValid;
    }
  },
  methods: {
    async loginUser() {
      try {
        const res = await authService.loginUser({
          username: this.username,
          password: this.password
        });
        this.errorMsg = '';
        localStorage.setItem('access_token', res.access_token);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Error logging in:', error);
        this.errorMsg = error.message || 'An error occurred during login.';
      }
    }
  }
};
</script>

<style scoped>
/* Add your component styles here */
</style>