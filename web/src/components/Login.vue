<template>
  <div class="login-page">

    <!-- Navbar --
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">ModernApp</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link btn btn-primary text-white ms-2" href="#">Sign Up</a>
            </li>
          </ul>
        </div>
      </div>
    </nav> -->

    <!-- Hero Section for Login -->
    <section class="hero d-flex justify-content-center align-items-center text-center text-white">
      <div class="login-form-container">
        <h2 class="display-4 mb-4">Login to Nexolt</h2>
        <form class="login-form" @submit.prevent="login">
          <div class="mb-3">
            <input v-model="email" type="email" class="form-control" placeholder="Email" required />
          </div>
          <div class="mb-3">
            <input v-model="password" type="password" class="form-control" placeholder="Password" required />
          </div>
          <button type="submit" class="btn btn-primary btn-lg">Login</button>
        </form>
        <div v-if="message" class="alert alert-info mt-3">{{ message }}</div>
        <h6>New to Nexolt?<router-link to="/register">Create a new account</router-link></h6>
      </div>
    </section>

    <!-- Footer --
    <footer>
      <p>&copy; 2024 ModernApp. All rights reserved.</p>
    </footer> -->
  </div> 
</template>
<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
export default {
  name: "Login",
  setup() {
    const email = ref('');
    const password = ref('');
    const message = ref('');
    const loading = ref(false);
    const router = useRouter();

    const login = async () => {
        loading.value = true;
        try {
        const response = await axios.post('http://127.0.0.1:8000/login/', {
          email: email.value,
          password: password.value,
        }, { withCredentials: true });


        if (response.status === 200) {
      // Save tokens in localStorage
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          localStorage.setItem('username', response.data.username);
          message.value = "Login successful!";

          setTimeout(() => {
            router.push('/chat'); // Redirect to chat after login
          }, 1000); // Add a timeout to allow the message to show
        }
        } catch (error) {
        message.value = error.response?.data?.message || 'Invalid credentials.';
        console.error(error);

      } finally {
        loading.value = false;

      }

    };
    return {

      email,
      password,
      message,
      loading,
      login,
    };

  },

};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Apply dynamic background */
.login-page {
  background: linear-gradient(135deg, rgba(16, 24, 35, 0.9), rgba(72, 86, 112, 0.9)), url('https://source.unsplash.com/random') no-repeat center center fixed;
  background-size: cover;
  height: 100vh; /* Full viewport height */
  color: white;
  font-family: 'Arial', sans-serif;
  margin: 0; /* Remove margin */
  padding: 0; /* Remove padding */
}

/* Hero Section */
.hero {
  height: calc(100vh - 60px); /* Adjust height to take full screen, minus navbar height */
  background: rgba(16, 24, 35, 0.7); /* Dark overlay for better text visibility */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Login Form Styling */
.login-form-container {
  background: rgba(16, 24, 35, 0.85);
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.login-form h2 {
  font-weight: bold;
}

.login-form .form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  transition: background 0.3s, border-color 0.3s;
}

.login-form .form-control:focus {
  background: rgba(255, 255, 255, 0.2);
  border-color: #5865f2;
  box-shadow: 0 0 5px rgba(88, 101, 242, 0.5);
}

.login-form .btn {
  width: 100%;
  padding: 15px;
  font-size: 1.1rem;
  border-radius: 8px;
  transition: background 0.3s;
}

.login-form .btn-primary {
  background-color: #5865f2;
  border-color: #5865f2;
}

.login-form .btn-primary:hover {
  background-color: #4752d0;
  border-color: #4752d0;
}

/* Footer Styling */
footer {
  background: linear-gradient(135deg, rgba(16, 24, 35, 0.9), rgba(72, 86, 112, 0.9));
  color: white;
  padding: 20px 0; /* Adjust footer padding */
  font-size: 0.9rem;
  text-align: center;
}

footer p {
  margin: 0;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .hero h2 {
    font-size: 2rem;
  }

  .login-form .form-control {
    padding: 12px;
  }

  .login-form .btn {
    font-size: 1rem;
  }
}
</style>