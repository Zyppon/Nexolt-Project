<template>
  <div class="register-page">
    <!-- Hero Section for Register -->
    <section class="hero d-flex justify-content-center align-items-center text-center text-white">
      <div class="register-form-container">
        <h2 class="display-4 mb-4">Register to Nexolt</h2>
        
        <!-- Form -->
        <form class="register-form" @submit.prevent="register">
          <!-- Username Field -->
          <div class="mb-3">
            <input v-model="username" type="text" class="form-control" placeholder="Username" required />
          </div>

          <!-- Email Field -->
          <div class="mb-3">
            <input v-model="email" type="email" class="form-control" placeholder="Email" required />
          </div>

          <!-- Password Field -->
          <div class="mb-3">
            <input v-model="password" type="password" class="form-control" placeholder="Password" required />
          </div>

          <!-- Submit Button -->
          <button type="submit" :disabled="loading" class="btn btn-primary btn-lg">{{ loading.value ? 'Loading...' : 'Register' }}</button>
        </form>

        <!-- Message Display -->
        <div v-if="message" class="alert alert-info mt-3">{{ message }}</div>

        <!-- Link to Login Page -->
        <h6>Already have an account? <router-link to="/login">Log In</router-link></h6>
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getCsrfToken } from '@/api/axios'; // Importă funcția de CSRF din axios.js
import axios from 'axios';  // Asigură-te că ai axios importat în fișier

export default {
  name: "Register",
  setup() {
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const message = ref('');
    const loading = ref(false);
    const router = useRouter();

    // Funcția de înregistrare
    const register = async () => {
      loading.value = true;

      if (!username.value || !email.value || !password.value) {
        message.value = 'All fields are required!';
        loading.value = false;
        return;
      }

      try {
        // Obține CSRF token
        const csrfToken = await getCsrfToken();
        const data = {
          username: username.value,
          email: email.value,
          password: password.value,
        };

        // Trimite cererea POST pentru înregistrare
        const response = await axios.post('http://localhost:8000/register/', data, {
          headers: {
            'X-CSRFToken': csrfToken,
          },
          withCredentials: true, // Permite trimiterea cookie-urilor
        });

        if (response.status === 201) {
          message.value = response.data.message;
          setTimeout(() => {
            router.push('/login');
          }, 1000);
        }
      } catch (error) {
        if (error.response) {
          console.error('Registration error response:', error.response);
          message.value = error.response?.data?.message || 'Something went wrong. Please try again.';
        } else {
          console.error('Error during registration:', error);
          message.value = 'An unexpected error occurred. Please try again.';
        }
      } finally {
        loading.value = false;
      }
    };

    return {
      username,
      email,
      password,
      message,
      loading,
      register,
    };
  },
};

</script>

<style scoped>
.register-page {
  background: linear-gradient(135deg, rgba(16, 24, 35, 0.9), rgba(72, 86, 112, 0.9)), url('https://source.unsplash.com/random') no-repeat center center fixed;
  background-size: cover;
  height: 100vh;
  color: white;
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}

/* Hero Section */
.hero {
  height: calc(100vh - 60px);
  background: rgba(16, 24, 35, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Register Form */
.register-form-container {
  background: rgba(16, 24, 35, 0.85);
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.register-form h2 {
  font-weight: bold;
}

.register-form .form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  transition: background 0.3s, border-color 0.3s;
}

.register-form .form-control:focus {
  background: rgba(255, 255, 255, 0.2);
  border-color: #5865f2;
  box-shadow: 0 0 5px rgba(88, 101, 242, 0.5);
}

.register-form .btn {
  width: 100%;
  padding: 15px;
  font-size: 1.1rem;
  border-radius: 8px;
  transition: background 0.3s;
}

.register-form .btn-primary {
  background-color: #5865f2;
  border-color: #5865f2;
}

.register-form .btn-primary:hover {
  background-color: #4752d0;
  border-color: #4752d0;
}

/* Success/Error Message */
.alert {
  font-size: 1rem;
  padding: 10px;
  border-radius: 8px;
  margin-top: 20px;
}

/* Footer */
footer {
  background: linear-gradient(135deg, rgba(16, 24, 35, 0.9), rgba(72, 86, 112, 0.9));
  color: white;
  padding: 20px 0;
  font-size: 0.9rem;
  text-align: center;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .hero h2 {
    font-size: 2rem;
  }

  .register-form .form-control {
    padding: 12px;
  }

  .register-form .btn {
    font-size: 1rem;
  }
}
</style>
