import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue'; 
import Login from '@/components/Login.vue'; 
import Register from '@/components/Register.vue';
import ChatApp from '@/components/Chat.vue';
import Blog from '@/components/Blog.vue';
import Contact from '@/components/Contact.vue';
import Support from '@/components/Support.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {title : 'Nexolt'}
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresAuth: false },
  },
  {
    path: '/register',
    name: 'Register',
    component : Register ,
    meta: {requiresAuth: false}
  },
  {
    path:'/chat',
    name:'Chat',
    component:ChatApp,
    meta: {requiresAuth:true},
  
      
  },
  {
    path: '/support',
    name: 'Support',
    component : Support ,
    meta: {requiresAuth: false}
  },
  {
    path: '/blog',
    name: 'Blog',
    component : Blog ,
    meta: {requiresAuth: false}
  },
  {
    path: '/contact',
    name: 'Contact',
    component : Contact ,
    meta: {requiresAuth: false}
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  console.log('Navigating to:', to.name);
  if (to.meta.requiresAuth) {
    console.log('Checking authentication for:', to.name);
    if (localStorage.getItem('access_token')) {
      console.log('Access token exists, proceeding to:', to.name);
      next(); // Allow access to the route
    } else {
      console.log('No access token, redirecting to Login');
      next({ name: 'Login' }); // Redirect to Login if no token exists
    }
  } else {
    console.log('No authentication required, proceeding to:', to.name);
    next(); // Allow access to routes that do not require authentication
  }
});

export default router;
