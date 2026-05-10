<script setup>
import { reactive, ref } from "vue"
import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'

const filters = reactive({
  location: "Kingston, Jamaica",
  distance: 25,
  age: 35,
  gender: "All",
  interest: "Select interests"
})

const users = ref([
  {
    id: 1,
    name: "Emily",
    age: 23,
    location: "Kingston, Jamaica",
    interests: ["Reading", "Movies", "Travel"],
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400"
  },
  {
    id: 2,
    name: "Chris",
    age: 28,
    location: "Portmore, Jamaica",
    interests: ["Fitness", "Travel", "Food"],
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400"
  }
])
</script>

<template>
  <div class="dashboard-layout">

    <!-- SIDEBAR -->
    <Sidebar />

    <!-- MAIN -->
    <div class="main-area">

      <Navbar />

      <div class="content">

        <div class="topbar">
          <div>
            <h1>Search</h1>
            <p>Find people that match your preferences</p>
          </div>

          <img class="profile-avatar" src="https://i.pravatar.cc/40" />
        </div>

        <div class="search-layout">

          <!-- FILTERS -->
          <div class="filters">
            <h3>Filters</h3>

            <div class="form-group">
              <label>Location</label>
              <select v-model="filters.location">
                <option>Kingston, Jamaica</option>
                <option>Montego Bay</option>
                <option>Portmore</option>
              </select>
            </div>

            <div class="form-group">
              <label>Distance</label>
              <input type="range" min="1" max="50" v-model="filters.distance" />
              <div>{{ filters.distance }} miles</div>
            </div>

            <div class="form-group">
              <label>Age</label>
              <input type="range" min="18" max="50" v-model="filters.age" />
              <div>Up to {{ filters.age }}</div>
            </div>
          </div>

          <!-- CARDS -->
          <div class="cards-grid">

            <div class="card" v-for="user in users" :key="user.id">

              <div class="image-wrapper">
                <img :src="user.image" />
              </div>

              <div class="card-body">
                <h3>{{ user.name }}, {{ user.age }}</h3>
                <p>{{ user.location }}</p>

                <div class="tags">
                  <span v-for="tag in user.interests" :key="tag">
                    {{ tag }}
                  </span>
                </div>
              </div>

            </div>

          </div>

        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
/* keep your styles unchanged */
</style>