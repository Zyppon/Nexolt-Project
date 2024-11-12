import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

// Importă componentele pentru fiecare pagină
import HelloWorld from './components/HelloWorld.vue';

// Definirea rutelor
const routes = [
 // { path: '/', component: AboutPage },
  { path: '/login' , component: HelloWorld}

];

// Crearea routerului
const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

// Folosirea routerului în aplicație
app.use(router);
app.mount('#app');
