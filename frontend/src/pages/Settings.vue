<script setup>
import Navbar from '../components/Navbar.vue'
import { ref, onMounted } from 'vue'

const darkMode = ref(false)
const notifications = ref(true)
const showOnline = ref(true)

/* APPLY THEME */
const applyTheme = () => {
  if (darkMode.value) {
    document.body.classList.add('dark')
  } else {
    document.body.classList.remove('dark')
  }
}

/* TOGGLE DARK MODE */
const toggleDarkMode = () => {
  darkMode.value = !darkMode.value
  localStorage.setItem('theme', darkMode.value ? 'dark' : 'light')
  applyTheme()
}

/* LOAD SAVED THEME */
onMounted(() => {
  const saved = localStorage.getItem('theme')
  darkMode.value = saved === 'dark'
  applyTheme()
})
</script>

<template>
  <div class="dashboard-layout">
    <Sidebar />

    <div class="main-area">
      <Navbar />

      <main class="dashboard-content">
        <h1>Settings</h1>

        <div class="settings-card">

          <!-- ACCOUNT -->
          <div class="section">
            <h3>Account</h3>
            <button class="btn">Change Password</button>
            <button class="btn danger">Delete Account</button>
          </div>

          <!-- PREFERENCES -->
          <div class="section">
            <h3>Preferences</h3>

            <label class="toggle">
              <span>Dark Mode</span>
              <input type="checkbox" :checked="darkMode" @change="toggleDarkMode" />
            </label>

            <label class="toggle">
              <span>Notifications</span>
              <input type="checkbox" v-model="notifications" />
            </label>

            <label class="toggle">
              <span>Show Online Status</span>
              <input type="checkbox" v-model="showOnline" />
            </label>
          </div>

          <!-- PRIVACY -->
          <div class="section">
            <h3>Privacy</h3>
            <button class="btn">Block Users</button>
            <button class="btn">Blocked List</button>
          </div>

        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* THEME */
:global(body) {
  --bg: #f9f9f9;
  --text1: #333;
  --card: #fff;
}

:global(body.dark) {
  --bg: #121212;
  --text1: #fff;
  --card: #1e1e1e;
}

/* LAYOUT */
.dashboard-layout {
  display: flex;
  min-height: 100vh;
  background: var(--bg);
  color: var(--text1);
}

.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* CONTENT */
.dashboard-content {
  flex: 1;
  padding: 20px;
}

/* CARD */
.settings-card {
  margin-top: 20px;
  background: var(--card);
  padding: 20px;
  border-radius: 16px;
  max-width: 600px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

/* SECTIONS */
.section {
  margin-bottom: 25px;
}

.section h3 {
  margin-bottom: 10px;
}

/* TOGGLES */
.toggle {
  display: flex;
  justify-content: space-between;
  margin: 10px 0;
}

/* BUTTONS */
.btn {
  display: block;
  margin: 8px 0;
  padding: 10px;
  border: none;
  border-radius: 8px;
  background: #eaeaea;
  cursor: pointer;
}

.btn:hover {
  background: #ddd;
}

.danger {
  background: #ff4d4d;
  color: white;
}

.danger:hover {
  background: #e60000;
}
</style>