import axios from 'axios';

// Setează `withCredentials: true` pentru toate cererile Axios
axios.defaults.withCredentials = true;

const API_URL = 'http://localhost:8000'; 
const instance = axios.create({
  baseURL: API_URL,
  timeout: 5000, 
  headers: { 'Content-Type': 'application/json' }, 
});


export const getCsrfToken = async () => {
  try {
    const response = await instance.get('/get_csrf_token/', { withCredentials: true });
    return response.data.csrfToken;  
  } catch (error) {
    console.error('Error getting CSRF token:', error);
    throw new Error('Unable to get CSRF token');
  }
};


getCsrfToken();

export default instance; 
