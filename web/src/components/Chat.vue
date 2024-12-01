<template>
  <h1>welcome to the chat {{ username }}</h1>
<button @click="logout">Log Out</button>
 
 </template>
  
  <script>

export default {
  name: 'ChatApp',
  

}



  </script>
  
  <style>
  .sidebar {
    height: 100vh;
    overflow-y: auto;
  }
  .main-content {
    height: 100vh;
    overflow-y: auto;
  }
  .chat-window {
    padding: 15px;
    height: 100%;
  }
  .messages {
    margin-bottom: 15px;
  }
  </style>