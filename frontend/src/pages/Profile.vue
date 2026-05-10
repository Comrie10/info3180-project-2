<script setup>
import { computed, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'

const auth = useAuthStore()

const profile = computed(() => auth.profile)

onMounted(async () => {
  if (!auth.profile) {
    await auth.fetchUser()
  }
})
</script>

<template>
  <div class="dashboard-layout">

    <!-- SIDEBAR -->
    <Sidebar />

    <!-- MAIN AREA -->
    <div class="main-area">

      <!-- NAVBAR -->
      <Navbar />

      <!-- CONTENT -->
      <main class="dashboard-content">

        <div class="profile-box">

          <!-- PROFILE IMAGE -->
          <img
            class="profile-image"
            :src="profile?.profile_picture || 'https://i.pravatar.cc/400'"
            alt="Profile Image"
          />

          <div class="profile-details">

            <!-- NAME -->
            <h1>
              {{ profile?.first_name }} {{ profile?.last_name }}
            </h1>

            <!-- LOCATION -->
            <p>
              {{ profile?.city }}, {{ profile?.country }}
            </p>

            <!-- BIO -->
            <div class="bio-box">
              {{ profile?.bio || 'No bio available yet.' }}
            </div>

            <!-- INTERESTS -->
            <div class="tags">
              <span
                v-for="(tag, index) in profile?.interests || []"
                :key="index"
              >
                {{ tag.name || tag }}
              </span>
            </div>

            <!-- EDIT BUTTON -->
            <router-link to="/edit-profile" class="primary-btn">
              Edit Profile
            </router-link>

          </div>

        </div>

      </main>

    </div>

  </div>
</template>



<style scoped>
/* =========================
   THEMES (FIXED CONSISTENT SYSTEM)
========================= */
:global(body) {
  --bg: #f9f9f9;
  --text1: #333;
  --text2: #666;
  --card: #fff;
  --nav: #fff;
}

:global(body.dark) {
  --bg: #121212;
  --text1: #ffffff;
  --text2: #cccccc;
  --card: #1e1e1e;
  --nav: #1a1a1a;
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
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

/* PROFILE CARD */
.profile-box {
  display: flex;
  gap: 30px;
  background: var(--card);
  padding: 25px;
  border-radius: 16px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  max-width: 700px;
  width: 100%;
}

/* IMAGE */
.profile-image {
  width: 180px;
  height: 180px;
  border-radius: 12px;
  object-fit: cover;
}

/* DETAILS */
.profile-details h1 {
  margin: 0;
}

.profile-details p {
  color: gray;
  margin: 5px 0 15px;
}

/* BIO */
.bio-box {
  margin: 10px 0;
  font-size: 14px;
  line-height: 1.4;
}

/* TAGS */
.tags {
  display: flex;
  gap: 8px;
  margin: 10px 0;
}

.tags span {
  background: #eaeaea;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 12px;
}

/* BUTTON */
.primary-btn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 15px;
  background: #4f46e5;
  color: white;
  border-radius: 8px;
  text-decoration: none;
}
</style>
