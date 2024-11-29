// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue'; // Pagină de exemplu
import UserLogin from '@/components/Login.vue'; // Pagină de login
import Register from '@/components/Register.vue';
import Chat from '@/components/Chat.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  //  meta: { requiresAuth: true }, // Această rută necesită autentificare
    meta: {title : 'Nexolt'}
  },
  {
    path: '/login',
    name: 'Login',
    component: UserLogin,
    meta: { requiresAuth: false }, // Login nu necesită autentificare
  },
  {
    path: '/register',
    name: 'Register',
    component : Register ,
    meta: {requiresAuth: false}
  },
  {
    path:'/chat',
    name:'ChatApp',
    component:Chat,
    meta: {requiresAuth:true},
   // beforeEnter:(to , from , next) => {
    //  const token = local.Storage.getItem('acces_token')
    //  if (token) {
    //    next();
    //  }else {
    //    next('/login');
    //  }
   // }
      
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Adaugă beforeEach pentru a verifica autentificarea
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token'); // Verifică dacă utilizatorul are un token
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login'); // Redirecționează la pagina de login
  } else {
    next(); // Permite accesul
  }
});


export default router;
