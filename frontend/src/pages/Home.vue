<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

/* =========================
   THEME STATE
========================= */
const isDark = ref(false)

/* APPLY THEME */
const applyTheme = () => {
  if (isDark.value) {
    document.body.classList.add('dark')
  } else {
    document.body.classList.remove('dark')
  }
}

/* TOGGLE THEME */
const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
  applyTheme()
}

/* LOAD SAVED THEME */
onMounted(() => {
  const saved = localStorage.getItem('theme')

  isDark.value = saved === 'dark'
  applyTheme()
})

/* LOGOUT */
const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<template>
  <div class="home-page">

    <!-- NAVBAR -->
    <header class="navbar">

      <div class="logo">
        ❤ DriftDater
      </div>

      <nav class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/features">Features</router-link>
      </nav>

      <div class="nav-buttons">

        <!-- THEME TOGGLE -->
        <button @click="toggleTheme" class="theme-btn">
          {{ isDark ? "☀️ Light Mode" : "🌙 Dark Mode" }}
        </button>

        <router-link to="/login" class="login-btn">
          Login
        </router-link>

        <router-link to="/register" class="register-btn">
          Register
        </router-link>

      </div>

    </header>

    <!-- HERO -->
    <section class="hero">

      <div class="overlay"></div>

      <div class="hero-content">

        <h1>
          Find Your Perfect
          <span>Match Today</span>
        </h1>

        <p>
          Join thousands of singles looking for meaningful
          connections and lasting relationships.
        </p>

        <div class="hero-buttons">

          <router-link to="/register" class="primary-btn">
            Get Started
          </router-link>

          <router-link to="/login" class="secondary-btn">
            Login
          </router-link>

        </div>

      </div>

    </section>

  </div>
</template>

<style scoped>

/* =========================
   LIGHT THEME (NEW STYLE)
========================= */
:global(:root) {
  --bg: linear-gradient(135deg, #fff0f6, #f3e8ff, #e9f0ff);
  --text: #3b2f4a;
  --nav: rgba(255, 255, 255, 0.75);
  --hero-text: #2d1b3d;
}

/* =========================
   DARK THEME
========================= */
:global(body.dark) {
  --bg: #121212;
  --text: #ffffff;
  --nav: #1a1a1a;
  --hero-text: #ffffff;
}

/* =========================
   PAGE
========================= */
.home-page {
  min-height: 100vh;
  font-family: Arial, sans-serif;

  background: var(--bg);
  background-attachment: fixed;

  color: var(--text);

  transition: 0.3s ease;
}

/* =========================
   NAVBAR
========================= */
.navbar {
  height: 90px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 0 70px;

  background: var(--nav);
  backdrop-filter: blur(10px);
}

.logo {
  font-size: 28px;
  font-weight: 800;
  color: #ff4d8d;
}

.nav-links {
  display: flex;
  gap: 42px;
}

.nav-links a {
  text-decoration: none;
  color: var(--text);
  font-weight: 500;
}

/* =========================
   BUTTONS
========================= */
.nav-buttons {
  display: flex;
  gap: 15px;
  align-items: center;
}

.theme-btn {
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid #ccc;
  background: transparent;
  cursor: pointer;
  font-weight: 600;
  color: var(--text);
}

.login-btn {
  padding: 12px 26px;
  border-radius: 12px;
  border: 1px solid #ddd;
  text-decoration: none;
  color: var(--text);
}

.register-btn {
  padding: 12px 26px;
  border-radius: 12px;
  text-decoration: none;
  background: #ff4d8d;
  color: white;
  font-weight: 600;
}

/* =========================
   HERO
========================= */
.hero {
  min-height: calc(100vh - 90px);
  display: flex;
  align-items: center;
  padding: 40px 80px;

  position: relative;
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.45);
}

.hero-content {
  max-width: 580px;
  position: relative;
  z-index: 2;
}

.hero-content h1 {
  font-size: 78px;
  line-height: 1.05;
  font-weight: 800;
  color: var(--hero-text);
}

.hero-content span {
  color: #ff7bab;
  display: block;
}

.hero-content p {
  margin-top: 28px;
  font-size: 20px;
  line-height: 1.8;
  color: var(--hero-text);
}

/* HERO BUTTONS */
.hero-buttons {
  display: flex;
  gap: 18px;
  margin-top: 42px;
}

.primary-btn {
  background: #ff4d8d;
  color: white;
  padding: 17px 34px;
  border-radius: 14px;
  text-decoration: none;
  font-weight: 600;
}

.secondary-btn {
  background: rgba(255,255,255,0.15);
  color: white;
  border: 2px solid white;
  padding: 17px 34px;
  border-radius: 14px;
  text-decoration: none;
}

/* =========================
   RESPONSIVE
========================= */
@media (max-width: 768px) {
  .navbar {
    padding: 0 25px;
  }

  .nav-links {
    display: none;
  }

  .hero {
    padding: 40px 25px;
  }

  .hero-content h1 {
    font-size: 46px;
  }

  .hero-buttons {
    flex-direction: column;
  }
}
</style>