<template>
  <div class="chatbot-page">
    <div class="chat-container">
      <div class="chatbox" ref="chatbox"></div>
      <div class="input-container">
        <input v-model="message" class="message-input" placeholder="Type a message...">
        <button @click="sendMessage" class="send-button">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatbotPage',
  data() {
    return {
      message: ''
    };
  },
  methods: {
    sendMessage() {
      if (this.message.trim() !== '') {
        axios.post(`http://localhost:5000/get_dish`, `prompt=${this.message}`, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          }
        })
        .then(response => this.displayMessage(response.data))
        .catch(error => console.error('Error:', error));
      }
      this.message = '';
    },
    displayMessage(message) {
      this.$refs.chatbox.innerHTML += `<div class="message">${message}</div>`;
      this.$refs.chatbox.scrollTop = this.$refs.chatbox.scrollHeight;
    }
  }
}
</script>

<style scoped>
.chatbot-page {
  font-family: 'Arial', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.chat-container {
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.chatbox {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 300px;
  overflow-y: scroll;
  padding: 10px;
  margin-bottom: 10px;
}

.input-container {
  display: flex;
  align-items: center;
}

.message-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.send-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.2s;
}

.send-button:hover {
  background-color: #0056b3;
}
</style>
