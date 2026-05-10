<script setup>
import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'

import { ref } from 'vue'

const activeChat = ref(0)

const chats = ref([
  {
    name: 'Sarah',
    last: 'Hey! How was your weekend?',
    time: '2m',
    unread: true,
    avatar: 'https://i.pravatar.cc/100?img=5'
  },
  {
    name: 'James',
    last: 'That sounds great!',
    time: '1h',
    unread: false,
    avatar: 'https://i.pravatar.cc/100?img=12'
  },
  {
    name: 'Aisha',
    last: 'See you there 👋',
    time: '2h',
    unread: true,
    avatar: 'https://i.pravatar.cc/100?img=32'
  },
  {
    name: 'Daniel',
    last: 'Thanks!',
    time: '1d',
    unread: false,
    avatar: 'https://i.pravatar.cc/100?img=22'
  },
  {
    name: 'Michael',
    last: 'Hi there!',
    time: '2d',
    unread: false,
    avatar: 'https://i.pravatar.cc/100?img=15'
  }
])

const messages = ref([
  { type: 'incoming', text: 'Hey there 👋', time: '10:30 AM' },
  { type: 'outgoing', text: 'Hi Sarah! How are you?', time: '10:31 AM' },
  { type: 'incoming', text: 'I’m good, thanks! How was your weekend?', time: '10:32 AM' },
  { type: 'outgoing', text: 'It was great! Went hiking with some friends. How about you?', time: '10:33 AM' },
  { type: 'incoming', text: 'Nice! I just relaxed and watched some movies. What kind of movies do you like?', time: '10:34 AM' }
])
</script>

<template>
  <div class="dashboard-layout">

    <Sidebar />

    <div class="main-area">

      <Navbar />

      <main class="messages-layout">

        <!-- LEFT -->
        <div class="chat-sidebar">

          <h3 class="title">Conversations</h3>

          <div
            v-for="(chat, index) in chats"
            :key="index"
            class="chat-user"
            :class="{ active: activeChat === index }"
            @click="activeChat = index"
          >

            <img :src="chat.avatar" />

            <div class="chat-info">
              <h4>
                {{ chat.name }}
                <span v-if="chat.unread" class="dot"></span>
              </h4>
              <p>{{ chat.last }}</p>
            </div>

            <span class="time">{{ chat.time }}</span>

          </div>

        </div>

        <!-- RIGHT -->
        <div class="chat-window">

          <!-- HEADER -->
          <div class="chat-header">
            <div class="user">
              <img src="https://i.pravatar.cc/100?img=5" />
              <div>
                <h4>Sarah</h4>
                <span>Online</span>
              </div>
            </div>

            <div class="menu">⋮</div>
          </div>

          <!-- MESSAGES -->
          <div class="messages">

            <div
              v-for="(msg, i) in messages"
              :key="i"
              class="message"
              :class="msg.type"
            >
              <p>{{ msg.text }}</p>
              <span class="msg-time">{{ msg.time }}</span>
            </div>

          </div>

          <!-- INPUT -->
          <div class="message-input">

            <input placeholder="Type a message..." />

            <button class="emoji">😊</button>

            <button class="send">➤</button>

          </div>

        </div>

      </main>

    </div>
  </div>
</template>

<style scoped>

/* LAYOUT */
.dashboard-layout {
  display: flex;
  height: 100vh;
  background: #f7f7f9;
}

.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.messages-layout {
  flex: 1;
  display: flex;
  overflow: hidden;
}

/* LEFT SIDEBAR */
.chat-sidebar {
  width: 300px;
  background: white;
  border-right: 1px solid #eee;
  padding: 20px;
  overflow-y: auto;
}

.title {
  font-size: 18px;
  margin-bottom: 15px;
  font-weight: 700;
}

.chat-user {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px;
  border-radius: 12px;
  cursor: pointer;
  position: relative;
}

.chat-user:hover {
  background: #f5f5f7;
}

.chat-user.active {
  background: #ffe4ec;
}

.chat-user img {
  width: 45px;
  height: 45px;
  border-radius: 50%;
}

.chat-info h4 {
  margin: 0;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.chat-info p {
  margin: 0;
  font-size: 12px;
  color: gray;
}

.time {
  margin-left: auto;
  font-size: 11px;
  color: gray;
}

.dot {
  width: 8px;
  height: 8px;
  background: red;
  border-radius: 50%;
}

/* CHAT WINDOW */
.chat-window {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* HEADER */
.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: white;
  border-bottom: 1px solid #eee;
}

.chat-header .user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.chat-header img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.chat-header span {
  font-size: 12px;
  color: green;
}

/* MESSAGES */
.messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.message {
  max-width: 60%;
  padding: 10px 14px;
  border-radius: 14px;
  position: relative;
  font-size: 14px;
}

.message p {
  margin: 0;
}

.msg-time {
  font-size: 10px;
  color: gray;
  display: block;
  margin-top: 5px;
}

.incoming {
  background: #eee;
  align-self: flex-start;
}

.outgoing {
  background: #ff4f8b;
  color: white;
  align-self: flex-end;
}

/* INPUT */
.message-input {
  display: flex;
  align-items: center;
  padding: 12px;
  background: white;
  border-top: 1px solid #eee;
  gap: 10px;
}

.message-input input {
  flex: 1;
  padding: 12px;
  border-radius: 20px;
  border: 1px solid #ddd;
  outline: none;
}

.emoji,
.send {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
}

.emoji {
  background: #f5f5f5;
}

.send {
  background: #ff4f8b;
  color: white;
}

</style>