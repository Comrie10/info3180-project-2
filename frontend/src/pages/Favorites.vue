<script setup>
import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <div class="dashboard-layout">
    <!-- SIDEBAR -->
    <Sidebar />

    <!-- RIGHT SIDE -->
    <div class="main-area">
      <!-- NAVBAR -->
      <Navbar />

      <!-- CONTENT -->
      <main class="dashboard-content">
        <h1>Favorites</h1>

        <div class="card-grid">
          <div class="favorite-card">
            <img src="https://i.pravatar.cc/300?img=18" />

            <div class="favorite-content">
              <h3>Maya, 26</h3>
              <p>Montego Bay</p>
            </div>
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

/* RIGHT SIDE WRAPPER */
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

/* GRID */
.card-grid {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

/* CARD */
.favorite-card {
  width: 200px;
  background: var(--card);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.favorite-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.favorite-content {
  padding: 10px;
}
</style>