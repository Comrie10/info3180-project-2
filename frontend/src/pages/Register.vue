<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'
import api from '../services/api'

const auth = useAuthStore()
const router = useRouter()

/* =========================
   STEP STATE
========================= */
const step = ref(1)

/* =========================
   THEME STATE
========================= */
const isDark = ref(false)

const applyTheme = () => {
  if (isDark.value) {
    document.body.classList.add('dark')
  } else {
    document.body.classList.remove('dark')
  }
}

const toggleTheme = () => {
  isDark.value = !isDark.value

  localStorage.setItem(
    'theme',
    isDark.value ? 'dark' : 'light'
  )

  applyTheme()
}

onMounted(() => {
  const saved = localStorage.getItem('theme')

  isDark.value = saved === 'dark'

  applyTheme()
})

/* =========================
   FORM
========================= */
const form = ref({
  full_name: '',
  email: '',
  age: '',
  password: '',
  confirm_password: '',
  bio: '',
  location: '',
  interests: [],
  looking_for: ''
})

/* =========================
   INTEREST OPTIONS
========================= */
const interestOptions = [
  'Travel',
  'Music',
  'Movies',
  'Fitness',
  'Gaming',
  'Cooking',
  'Photography',
  'Art',
  'Fashion',
  'Sports'
]

/* =========================
   TOGGLE INTERESTS
========================= */
const toggleInterest = (interest) => {
  if (form.value.interests.includes(interest)) {
    form.value.interests =
      form.value.interests.filter(
        i => i !== interest
      )
  } else {
    form.value.interests.push(interest)
  }
}

/* =========================
   STEPS
========================= */
const nextStep = () => {
  if (
    !form.value.full_name ||
    !form.value.email ||
    !form.value.age ||
    !form.value.password
  ) {
    alert('Please fill out all fields')
    return
  }

  if (
    form.value.password !==
    form.value.confirm_password
  ) {
    alert('Passwords do not match')
    return
  }

  step.value = 2
}

const prevStep = () => {
  step.value = 1
}

/* =========================
   REGISTER
========================= */
const register = async () => {
  try {
    await api.post(
      '/auth/register',
      form.value
    )

    router.push('/login')

  } catch (error) {
    console.error(error)
    alert('Registration failed')
  }
}

/* =========================
   LOGOUT
========================= */
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
        DriftDater
        <span class="pink-heart">❤</span>
      </div>

      <nav class="nav-links">
        <router-link to="/">
          Home
        </router-link>

        <router-link to="/about">
          About
        </router-link>

        <router-link to="/features">
          Features
        </router-link>
      </nav>

      <div class="nav-buttons">

        <button
          @click="toggleTheme"
          class="theme-btn"
        >
          {{ isDark
            ? "☀️ Light Mode"
            : "🌙 Dark Mode"
          }}
        </button>

      </div>

    </header>

    <!-- AUTH PAGE -->
    <div class="auth-page">

      <div class="auth-card">

        <!-- STEPS -->
        <div class="steps">

          <div
            class="step"
            :class="{ active: step === 1 }"
          >
            1
          </div>

          <div class="line"></div>

          <div
            class="step"
            :class="{ active: step === 2 }"
          >
            2
          </div>

        </div>

        <!-- STEP 1 -->
        <div v-if="step === 1">

          <h1 class="welcome-title">
            Create your account
            <span class="pink-heart">❤</span>
          </h1>

          <p class="subtitle">
            Join thousands of singles
            looking for love
          </p>

          <div class="input-group">
            <label>Full Name</label>

            <input
              v-model="form.full_name"
            />
          </div>

          <div class="input-group">
            <label>Email</label>

            <input
              v-model="form.email"
              type="email"
            />
          </div>

          <div class="input-group">
            <label>Age</label>

            <input
              v-model="form.age"
              type="number"
            />
          </div>

          <div class="input-group">
            <label>Password</label>

            <input
              v-model="form.password"
              type="password"
            />
          </div>

          <div class="input-group">
            <label>
              Confirm Password
            </label>

            <input
              v-model="form.confirm_password"
              type="password"
            />
          </div>

          <button @click="nextStep">
            Continue
          </button>

        </div>

        <!-- STEP 2 -->
        <div v-if="step === 2">

          <h1 class="welcome-title">
            Complete your profile
            <span class="pink-heart">❤</span>
          </h1>

          <p class="subtitle">
            Tell people more about yourself
          </p>

          <div class="input-group">
            <label>Location</label>

            <input
              v-model="form.location"
            />
          </div>

          <div class="input-group">

            <label>
              Looking For
            </label>

            <select
              v-model="form.looking_for"
            >
              <option value="">
                Select preference
              </option>

              <option>
                Friendship
              </option>

              <option>
                Relationship
              </option>

              <option>
                Casual Dating
              </option>
            </select>

          </div>

          <div class="input-group">

            <label>Bio</label>

            <textarea
              v-model="form.bio"
            ></textarea>

          </div>

          <div class="input-group">

            <label>
              Interests
            </label>

            <div class="interests">

              <button
                v-for="interest in interestOptions"
                :key="interest"
                type="button"
                class="interest-btn"
                :class="{
                  selected:
                  form.interests.includes(
                    interest
                  )
                }"
                @click="
                  toggleInterest(interest)
                "
              >
                {{ interest }}
              </button>

            </div>

          </div>

          <div class="button-group">

            <button
              class="secondary-btn"
              @click="prevStep"
            >
              Back
            </button>

            <button @click="register">
              Create Account
            </button>

          </div>

        </div>

        <p class="login-link">

          Already have an account?

          <router-link to="/login">
            Login
          </router-link>

        </p>

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
   DARK MODE
========================= */
:global(body.dark) {
  --bg: #0d0d0d;
  --text: #0d0d0d;
  --text2: #1a1818;

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
  background: var(--bg);
  color: var(--text);
  transition: 0.3s ease;
  font-family: Arial, sans-serif;
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
   BUTTONS
========================= */
.theme-btn {
  padding: 10px 14px;

  border-radius: 10px;

  border: 1px solid var(--border);

  background: transparent;

  color: var(--text);

  cursor: pointer;
}

button {
  border: none;
  cursor: pointer;
}

/* =========================
   AUTH
========================= */
.auth-page {
  min-height: calc(100vh - 85px);

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 40px;
}

.auth-card {
  width: 500px;

  background: var(--card);

  border: 1px solid var(--border);

  border-radius: 25px;

  padding: 40px;
}



/* =========================
   STEPS
========================= */
.steps {
  display: flex;
  align-items: center;
  justify-content: center;

  margin-bottom: 30px;
}

.step {
  width: 40px;
  height: 40px;

  border-radius: 50%;

  background: #cccccc;

  display: flex;
  align-items: center;
  justify-content: center;

  font-weight: bold;
}

.step.active {
  background: #ff4d8d;
  color: white;
}

.line {
  width: 60px;
  height: 3px;

  background: #cccccc;
}

/* =========================
   INPUTS
========================= */
.input-group {
  margin-top: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 8px;
  color: var(--text);
}

.input-group input,
.input-group select,
.input-group textarea {
  width: 100%;

  padding: 14px;

  border-radius: 12px;

  border: 1px solid var(--border);

  background: var(--input);

  color: var(--text);

  outline: none;
}

textarea {
  min-height: 120px;
  resize: none;
}

/* =========================
   INTERESTS
========================= */
.interests {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;

  margin-top: 10px;
}

.interest-btn {
  padding: 10px 16px;

  border-radius: 999px;

  background: var(--input);

  border: 1px solid var(--border);

  color: var(--text);
}

.interest-btn.selected {
  background: #ff4d8d;
  color: white;
}

/* =========================
   BUTTON GROUP
========================= */
.button-group {
  display: flex;
  gap: 15px;

  margin-top: 25px;
}

.button-group button,
.auth-card > div button {
  width: 100%;

  padding: 15px;

  border-radius: 14px;

  background: #ff4d8d;

  color: white;

  font-weight: 700;
}

.secondary-btn {
  background: #666666 !important;
}

/* =========================
   LOGIN LINK
========================= */
.login-link {
  margin-top: 25px;
  text-align: center;
  color: var(--text2);
}

.login-link a {
  color: #ff4d8d;
  text-decoration: none;
  font-weight: bold;
}

/* =========================
   RESPONSIVE
========================= */
@media (max-width: 768px) {

  .navbar {
    padding: 0 20px;
  }

  .nav-links {
    display: none;
  }

  .auth-card {
    width: 100%;
  }

  .welcome-title {
    font-size: 30px;
  }
}
</style>