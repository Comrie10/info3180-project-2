<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'

import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'

const auth = useAuthStore()

/* =========================
   PROFILE STATE (FROM DB)
========================= */
const profile = ref({
  first_name: '',
  last_name: '',
  age: '',
  bio: '',
  city: '',
  country: '',
  occupation: '',
  education: '',
  looking_for: '',
  interests: [],
  profile_picture: ''
})

/* =========================
   INTERESTS
========================= */
const interestInput = ref('')

const interestOptions = [
  'Travel','Music','Reading','Hiking','Food','Photography','Fitness',
  'Art','Fashion','Gaming','Movies','Cooking','Dancing','Writing'
]

const filteredInterests = computed(() => {
  if (!interestInput.value) return []

  return interestOptions.filter(item =>
    item.toLowerCase().includes(interestInput.value.toLowerCase()) &&
    !profile.value.interests.includes(item)
  )
})

const addInterest = (i) => {
  if (!profile.value.interests.includes(i)) {
    profile.value.interests.push(i)
  }
  interestInput.value = ''
}

const removeInterest = (i) => {
  profile.value.interests = profile.value.interests.filter(x => x !== i)
}

/* =========================
   LOAD PROFILE FROM BACKEND
========================= */
onMounted(async () => {
  await auth.fetchUser()

  if (auth.profile) {
    profile.value = {
      ...auth.profile,
      interests: auth.profile.interests?.map(i => i.name || i) || []
    }
  }
})

/* =========================
   SAVE PROFILE
========================= */
const saveProfile = async () => {
  try {
    const res = await axios.put(
      `http://localhost:5000/profile/update`,
      profile.value,
      { withCredentials: true }
    )

    auth.profile = res.data.profile

    alert("Profile updated successfully 🎉")
  } catch (err) {
    console.error(err)
    alert("Failed to update profile ❌")
  }
}
</script>

<template>
  <div class="dashboard-layout">

    <Sidebar />

    <div class="main-area">

      <Navbar />

      <main class="dashboard-content">

        <div class="edit-profile-card">

          <h1>Edit Profile</h1>

          <div class="profile-grid">

            <!-- LEFT -->
            <div>

              <img
                class="profile-image"
                :src="profile.profile_picture || 'https://i.pravatar.cc/400'"
              />

              <input v-model="profile.city" placeholder="City" />
              <input v-model="profile.country" placeholder="Country" />
              <input v-model="profile.occupation" placeholder="Occupation" />

            </div>

            <!-- RIGHT -->
            <div>

              <input v-model="profile.first_name" placeholder="First Name" />
              <input v-model="profile.last_name" placeholder="Last Name" />
              <input v-model="profile.age" type="number" placeholder="Age" />

              <textarea v-model="profile.bio" placeholder="Bio"></textarea>

              <select v-model="profile.looking_for">
                <option disabled value="">Looking For</option>
                <option>Long-term</option>
                <option>Short-term</option>
                <option>Friends</option>
              </select>

              <!-- INTERESTS -->
              <div>
                <div class="tag-box">
                  <span v-for="i in profile.interests" :key="i">
                    {{ i }}
                    <button @click="removeInterest(i)">×</button>
                  </span>
                </div>

                <input v-model="interestInput" placeholder="Add interests" />

                <div v-if="filteredInterests.length">
                  <div
                    v-for="item in filteredInterests"
                    :key="item"
                    @click="addInterest(item)"
                  >
                    {{ item }}
                  </div>
                </div>
              </div>

              <button @click="saveProfile">
                Save Changes
              </button>

            </div>

          </div>

        </div>

      </main>

    </div>

  </div>
</template>

<style scoped>

.dashboard-layout {
  display: flex;
  min-height: 100vh;
  background: #f7f7f9;
}

.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.dashboard-content {
  flex: 1;
  padding: 35px;
}

.profile-wrapper {
  display: flex;
  gap: 30px;
  align-items: flex-start;
}

/* SIDEBAR */
.settings-sidebar {
  width: 220px;
  background: white;
  border-radius: 20px;
  padding: 18px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.menu-item {
  border: none;
  background: transparent;
  padding: 14px;
  border-radius: 12px;
  cursor: pointer;
  font-size: 14px;
  color: #666;
}

.menu-item:hover {
  background: #f5f5f7;
}

.menu-item.active {
  background: #fff0f5;
  color: #ff4f8b;
  font-weight: 600;
}

/* CARD */
.edit-profile-card {
  flex: 1;
  background: white;
  border-radius: 24px;
  padding: 35px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04);
}

.edit-profile-card h1 {
  font-size: 30px;
  margin-bottom: 30px;
}

/* GRID */
.profile-grid {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 35px;
}

/* IMAGE */
.profile-image-wrapper {
  height: 350px;
  border-radius: 22px;
  overflow: hidden;
  position: relative;
  margin-bottom: 25px;
}

.profile-image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.camera-btn {
  position: absolute;
  bottom: 15px;
  right: 15px;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  border: none;
  background: white;
}

/* FORM */
.form-group {
  margin-bottom: 22px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  font-size: 14px;
  color: #555;
}

input,
textarea,
select {
  width: 100%;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 13px;
  font-size: 14px;
  outline: none;
  background: white;
}

textarea {
  height: 120px;
  resize: none;
}

/* TAGS */
.tag-box {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
}

.tag {
  background: #fff0f5;
  color: #ff4f8b;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 13px;
  display: flex;
  gap: 6px;
  align-items: center;
}

.tag button {
  border: none;
  background: transparent;
  cursor: pointer;
  color: #ff4f8b;
  font-size: 14px;
}

/* SUGGESTIONS */
.suggestions {
  border: 1px solid #eee;
  border-radius: 10px;
  margin-top: 5px;
  background: white;
  max-height: 150px;
  overflow-y: auto;
}

.suggestion-item {
  padding: 10px;
  cursor: pointer;
  font-size: 14px;
}

.suggestion-item:hover {
  background: #fff0f5;
}

/* SAVE */
.save-btn {
  margin-top: 10px;
  background: #ff4f8b;
  color: white;
  border: none;
  border-radius: 12px;
  padding: 14px 30px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.save-btn:hover {
  background: #ff3c7d;
}

@media (max-width: 1000px) {
  .profile-wrapper {
    flex-direction: column;
  }

  .profile-grid {
    grid-template-columns: 1fr;
  }

  .settings-sidebar {
    width: 100%;
    flex-direction: row;
    overflow-x: auto;
  }
}

</style>