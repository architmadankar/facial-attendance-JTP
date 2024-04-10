<template>
  <div class="py-5">
    <div class="row">
      <div class="col-md-6 mx-auto">
        <div class="card rounded-0">
          <div class="card-header">
            <h3 class="mb-0">Register</h3>
          </div>
          <div class="card-body">
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
            </div>
            <form @submit.prevent="registerUser" novalidate>
              <div class="form-group">
                <label for="username">Username</label>
                <input v-model="username" type="text" id="username" class="form-control rounded-0"
                  :class="{ 'is-invalid': !isUsernameValid && submitted }">
                <small v-if="!isUsernameValid && submitted" class="text-danger">Username is required (minimum 4 characters)</small>
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input v-model="password" type="password" id="password" class="form-control rounded-0"
                  :class="{ 'is-invalid': !isPasswordValid && submitted }">
                <small v-if="!isPasswordValid && submitted" class="text-danger">Password is required (minimum 8 characters, at least one letter & one number)</small>
              </div>
              <button :disabled="!isRegistrationFormValid" type="submit" class="btn btn-primary float-right">Register</button>
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
  name: 'UserSignup',
  data() {
    return {
      username: '',
      password: '',
      submitted: false,
      errorMsg: '',
      responseMsg: '',
      passwordPattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/
    };
  },
  computed: {
    isUsernameValid() {
      return !!this.username.trim() && this.username.length >= 4;
    },
    isPasswordValid() {
      return !!this.password.trim() && this.passwordPattern.test(this.password);
    },
    isRegistrationFormValid() {
      return this.isUsernameValid && this.isPasswordValid;
    }
  },
  methods: {
    async registerUser() {
      try {
        const res = await authService.registerUser({
          username: this.username,
          password: this.password
        });
        this.errorMsg = '';
        this.responseMsg = res.message;
      } catch (error) {
        console.error('Error registering user:', error);
        this.responseMsg = '';
        this.errorMsg = error.message || 'An error occurred during registration.';
      }
    }
  }
};
</script>

<style scoped>
/* Add your component styles here */
</style>