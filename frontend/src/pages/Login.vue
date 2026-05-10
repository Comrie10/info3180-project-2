<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

/* =========================
   FORM
========================= */
const form = ref({
  email: '',
  password: ''
})

const loading = ref(false)

/* =========================
   LOGIN
========================= */
const login = async () => {
  loading.value = true

  try {
    const res = await auth.login(form.value.email, form.value.password)

    // store user from backend
    auth.user = res.user

    alert("Login successful 🎉")

    // go to profile page (NOT home)
    router.replace('/profile')

  } catch (err) {
    console.error(err)

    const message =
      err?.response?.data?.error || "Login failed ❌"

    alert(message)

  } finally {
    loading.value = false
  }
}

/* =========================
   THEME
========================= */
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
  isDark.value = localStorage.getItem('theme') === 'dark'
  applyTheme()
})
</script>

<template>
  <div class="home-page">

    <!-- NAVBAR -->
    <header class="navbar">

      <div class="logo">
        DriftDater <span class="pink-heart">❤</span>
      </div>

      <nav class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/features">Features</router-link>
      </nav>

      <div class="nav-buttons">
        <button @click="toggleTheme" class="theme-btn">
          {{ isDark ? "☀️ Light Mode" : "🌙 Dark Mode" }}
        </button>
      </div>

    </header>

    <!-- AUTH -->
    <div class="auth-page">

      <!-- LEFT -->
      <div class="auth-left">
        <div class="left-content">

          <h1 class="welcome-title">
            Welcome Back <span class="pink-heart">❤</span>
          </h1>

          <p>
            Log in to continue discovering meaningful connections
            and chatting with your matches.
          </p>

        </div>
      </div>

      <!-- RIGHT -->
      <div class="auth-right">

        <div class="auth-card">

          <h2>Login</h2>
          <p class="subtitle">Sign into your account</p>

          <div class="input-group">
            <label>Email</label>
            <input v-model="form.email" type="email" />
          </div>

          <div class="input-group">
            <label>Password</label>
            <input v-model="form.password" type="password" />
          </div>

          <button @click="login">Login</button>

          <!-- REGISTER LINK -->
          <p class="register-link">
            Don't have an account?
            <router-link to="/register">Register</router-link>
          </p>

        </div>

      </div>

    </div>

  </div>
</template>

<style scoped>

/* =========================
   LIGHT MODE
========================= */
:global(body) {
  --bg: #ffffff;
  --text: #111111;
  --text2: #555555;

  --nav: rgba(255, 255, 255, 0.95);
  --card: #ffffff;

  --border: rgba(0, 0, 0, 0.15);
  --input: #f5f5f5;
}

/* =========================
   DARK MODE (FIXED PROPERLY)
========================= */
:global(body.dark) {
  --bg: #0d0d0d;

  --text: #ffffff;
  --text2: #cccccc;

  --nav: #111111;
  --card: #1a1a1a;

  --border: rgba(255, 255, 255, 0.15);
  --input: #2a2a2a;
}

/* =========================
   PAGE
========================= */
.home-page {
  min-height: 100vh;
  font-family: Arial, sans-serif;

  background: var(--bg);
  color: var(--text);

  transition: 0.3s ease;
}

/* =========================
   NAVBAR
========================= */
.navbar {
  height: 85px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 0 60px;

  background: var(--nav);
  backdrop-filter: blur(10px);
}

.logo {
  font-size: 28px;
  font-weight: 800;

  color: var(--text);

  display: flex;
  align-items: center;
  gap: 8px;
}

.pink-heart {
  color: #ff4d8d;
}

.nav-links {
  display: flex;
  gap: 30px;
}

.nav-links a {
  text-decoration: none;
  color: var(--text);
}

/* =========================
   BUTTON
========================= */
.theme-btn {
  padding: 10px 14px;

  border-radius: 10px;

  border: 1px solid var(--border);

  background: transparent;

  color: var(--text);

  cursor: pointer;
}

/* =========================
   AUTH LAYOUT
========================= */
.auth-page {
  min-height: calc(100vh - 85px);

  display: grid;

  grid-template-columns: 1fr 1fr;
}

/* LEFT */
.auth-left {
  display: flex;
  align-items: center;
  justify-content: center;

  padding: 60px;
}

/* FIXED WELCOME TEXT */
.welcome-title {
  font-size: 60px;

  color: var(--text);

  display: flex;
  align-items: center;

  gap: 10px;

  white-space: nowrap;
}

.left-content p {
  margin-top: 20px;

  color: var(--text2);

  max-width: 450px;

  line-height: 1.7;
}

/* RIGHT */
.auth-right {
  display: flex;
  align-items: center;
  justify-content: center;

  padding: 40px;
}

/* CARD */
.auth-card {
  width: 420px;

  background: var(--card);

  border: 1px solid var(--border);

  padding: 45px;

  border-radius: 25px;
}

.auth-card h2 {
  font-size: 40px;
  color: var(--text);
}

.subtitle {
  color: var(--text2);
}

/* INPUT */
.input-group {
  margin-top: 20px;
}

.input-group label {
  color: var(--text);
}

.input-group input {
  width: 100%;

  padding: 14px;

  border-radius: 12px;

  border: 1px solid var(--border);

  background: var(--input);

  color: var(--text);

  outline: none;
}

/* BUTTON */
button {
  width: 100%;

  margin-top: 25px;

  padding: 15px;

  border: none;

  border-radius: 14px;

  background: #ff4d8d;

  color: white;

  font-weight: 700;

  cursor: pointer;
}

/* REGISTER LINK */
.register-link {
  margin-top: 20px;

  text-align: center;

  color: var(--text2);
}

.register-link a {
  color: #ff4d8d;

  font-weight: 700;

  text-decoration: none;
}


:global(body.dark) .welcome-title {
  color: var(--text) !important;
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .auth-page {
    grid-template-columns: 1fr;
  }

  .auth-left {
    display: none;
  }
  
}

</style>