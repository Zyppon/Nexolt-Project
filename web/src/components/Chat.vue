<template>
    <div class="container-fluid h-100">
      <div class="row h-100">
        <div class="col-3 bg-light border-right sidebar">
          <h4 class="text-center">Conversations</h4>
          <ul class="list-group">
            <li class="list-group-item" v-for="contact in contacts" :key="contact.id">
              {{ contact.name }}
            </li>
          </ul>
        </div>
        <div class="col-9 bg-white main-content">
          <div class="chat-window">
            <h4 class="text-center">Chat with {{ selectedContact.name }}</h4>
            <div class="messages" v-for="message in messages" :key="message.id">
              <div :class="{'text-right': message.sender === 'me'}">
                <p><strong>{{ message.sender }}:</strong> {{ message.text }}</p>
              </div>
            </div>
            <div class="input-group mt-3">
              <input type="text" class="form-control" v-model="newMessage" placeholder="Type a message..." @keyup.enter="sendMessage">
              <div class="input-group-append">
                <button class="btn btn-primary" @click="sendMessage">Send</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        contacts: [
          { id: 1, name: 'Alice' },
          { id: 2, name: 'Bob' },
          { id: 3, name: 'Charlie' },
        ],
        selectedContact: { id: 1, name: 'Alice' },
        messages: [],
        newMessage: ''
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim()) {
          this.messages.push({ id: Date.now(), sender: 'me', text: this.newMessage });
          this.newMessage = '';
        }
      }
    }
  };
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