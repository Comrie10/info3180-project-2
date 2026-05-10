<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

// ✅ reactive user
const profile = computed(() => auth.profile)

// theme state
const isDark = ref(false)

const applyTheme = () => {
  document.body.classList.toggle('dark', isDark.value)
}

const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
  applyTheme()
}

onMounted(() => {
  const saved = localStorage.getItem('theme')
  isDark.value = saved === 'dark'
  applyTheme()
})

const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<template>
  <header class="navbar">

    <!-- LEFT -->
    <div class="left-section">
      <h1 class="logo">❤ DriftDater</h1>
    </div>

    <!-- CENTER -->
    <nav class="nav-links">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/features">Features</router-link>
    </nav>

    <!-- RIGHT -->
    <div class="right-section">

      <!-- SETTINGS -->
      <router-link to="/settings" class="icon-btn settings-btn">
        ⚙️
      </router-link>

      <!-- THEME -->
      <button class="theme-btn" @click="toggleTheme">
        {{ isDark ? "☀️ Light" : "🌙 Dark" }}
      </button>

      <!-- PROFILE (DYNAMIC 👇) -->
      <div class="profile-box">
  <img
    class="profile-image"
    :src="profile?.profile_picture || 'https://i.pravatar.cc/400'"
    alt="Profile Image"
  />
</div>

      <!-- LOGOUT -->
      <button class="logout-btn" @click="logout">
        Logout
      </button>

    </div>
  </header>
</template>

<style scoped>
.navbar {
  width: 100%;
  height: 80px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 30px;
  border-bottom: 1px solid #eee;
}

.logo {
  color: #ff2d75;
  font-size: 28px;
  font-weight: 700;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-links a {
  text-decoration: none;
  color: #333;
}

.right-section {
  display: flex;
  align-items: center;
  gap: 14px;
}

.icon-btn {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.theme-btn {
  padding: 10px 12px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  background: #eee;
}

.profile-box {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #fafafa;
  padding: 8px 14px;
  border-radius: 50px;
}

.profile-box img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.logout-btn {
  background: #ff2d75;
  color: white;
  border: none;
  padding: 12px 18px;
  border-radius: 12px;
  cursor: pointer;
}
</style>