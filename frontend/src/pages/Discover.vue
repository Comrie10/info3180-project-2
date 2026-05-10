<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'

import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'

const auth = useAuthStore()

const users = ref([])
const loading = ref(false)
const error = ref(null)

const selectedUser = ref(null)

/* =========================
   ONLY SHOW OTHER USERS
========================= */
const filteredUsers = computed(() => {
  if (!auth.user?.id) {
    return users.value
  }

  return users.value.filter(user => {
    return (
      user.user_id !== auth.user.id &&
      user.id !== auth.user.id
    )
  })
})

/* =========================
   FETCH USERS
========================= */
const fetchUsers = async () => {
  try {
    loading.value = true
    error.value = null

    console.log('Fetching profiles...')

    const response = await axios.get(
      'http://127.0.0.1:5000/api/profiles',
      {
        withCredentials: true
      }
    )

    console.log('API RESPONSE:', response.data)

    const fetchedUsers =
      response.data?.profiles ??
      response.data?.data?.profiles ??
      response.data ??
      []

    users.value = Array.isArray(fetchedUsers)
      ? fetchedUsers
      : []

  } catch (err) {
    console.error('Fetch error:', err)

    error.value =
      err?.response?.data?.message ||
      err.message ||
      'Failed to load users'

  } finally {
    loading.value = false
  }
}

/* =========================
   OPEN / CLOSE PROFILE
========================= */
const openProfile = (user) => {
  selectedUser.value = user
}

const closeProfile = () => {
  selectedUser.value = null
}

/* =========================
   LIKE USER
========================= */
const likeUser = async (user) => {
  try {
    if (!auth.user?.id) {
      console.error('No logged in user')
      return
    }

    await axios.post(
      `http://127.0.0.1:5000/api/profiles/${user.id}/action`,
      {
        action: 'like'
      },
      {
        withCredentials: true
      }
    )

    users.value = users.value.filter(
      u => u.id !== user.id
    )

    closeProfile()

  } catch (err) {
    console.error('Like error:', err)
  }
}

/* =========================
   DISLIKE USER
========================= */
const dislikeUser = async (user) => {
  try {
    if (!auth.user?.id) {
      console.error('No logged in user')
      return
    }

    await axios.post(
      `http://127.0.0.1:5000/api/profiles/${user.id}/action`,
      {
        action: 'dislike'
      },
      {
        withCredentials: true
      }
    )

    users.value = users.value.filter(
      u => u.id !== user.id
    )

    closeProfile()

  } catch (err) {
    console.error('Dislike error:', err)
  }
}

onMounted(fetchUsers)
</script>

<template>

  <div class="dashboard-page">

    <Navbar />

    <div class="dashboard-layout">

      <Sidebar />

      <main class="dashboard-content">

        <div class="discover-container">

          <!-- HEADER -->
          <div class="discover-header">
            <h1>Discover</h1>
            <p>Find people you may be interested in</p>
          </div>

          <!-- LOADING -->
          <div v-if="loading" class="status">
            Loading profiles...
          </div>

          <!-- ERROR -->
          <div v-else-if="error" class="status error">
            {{ error }}
          </div>

          <!-- EMPTY -->
          <div v-else-if="users.length === 0" class="status">
            No users found.
          </div>

          <!-- GRID -->
          <div v-else class="card-grid">

            <div
              v-for="user in users"
              :key="user.id"
              class="discover-card"
              @click="openProfile(user)"
            >

              <!-- IMAGE (FIXED SAFE FALLBACK) -->
              <div class="image-wrapper">

                <img
                  :src="user.profile_picture || 'https://via.placeholder.com/300'"
                  :alt="user.first_name || 'User'"
                />

                <div class="online-dot"></div>

              </div>

              <!-- CONTENT -->
              <div class="card-content">

                <h3>
                  {{ user.first_name }} {{ user.last_name }}
                </h3>

                <p class="bio">
                  {{ user.bio }}
                </p>

              </div>

            </div>

          </div>

        </div>

      </main>

    </div>

    <!-- MODAL -->
    <div v-if="selectedUser" class="profile-modal">

      <div class="modal-card">

        <button class="close-btn" @click="closeProfile">×</button>

        <img
          :src="selectedUser.profile_picture || 'https://via.placeholder.com/300'"
          class="modal-image"
        />

        <div class="modal-info">

          <h2>
            {{ selectedUser.first_name }} {{ selectedUser.last_name }}
          </h2>

          <p class="modal-bio">
            {{ selectedUser.bio }}
          </p>

        </div>

        <div class="swipe-actions">

          <button
            class="swipe-btn dislike-btn"
            @click.stop="dislikeUser(selectedUser)"
          >
            ✕
          </button>

          <button
            class="swipe-btn like-btn"
            @click.stop="likeUser(selectedUser)"
          >
            ❤
          </button>

        </div>

      </div>

    </div>

  </div>

</template>

<style scoped>
/* (your CSS stays EXACTLY the same — no changes needed) */
</style>