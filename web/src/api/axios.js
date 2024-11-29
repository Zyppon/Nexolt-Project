import axios from 'axios'



const API_URL = 'http://localhost:8000/';

const instance  = axios.create({
    baseURL : API_URL,
    withCredentials : true,
})


async function setCSRFToken() {
    try {
      const response = await axios.get('/get-csrf-token/');
      const csrfToken = response.data.csrfToken;
      instance.defaults.headers.common['X-CSRFToken'] = csrfToken;
    } catch (error) {
      console.error('Failed to fetch CSRF token:', error);
    }
  }
  
  // Call this function once during application initialization
  setCSRFToken();
export default instance

