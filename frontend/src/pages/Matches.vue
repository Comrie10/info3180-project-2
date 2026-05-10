<script setup>
import Sidebar from '../components/Sidebar.vue'
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <div class="dashboard-layout">
    <!-- SIDEBAR -->
    <Sidebar />

    <div class="main-area">
      <!-- NAVBAR -->
      <Navbar />

      <!-- CONTENT -->
      <main class="dashboard-content">
        <h1>Your Matches</h1>

        <div class="match-list">
          <div class="match-user">
            <img src="https://i.pravatar.cc/150?img=11" />
            <h3>Sophia</h3>
          </div>

          <div class="match-user">
            <img src="https://i.pravatar.cc/150?img=12" />
            <h3>Maya</h3>
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

/* ✅ TOP-LEFT CONTENT */
.dashboard-content {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;   /* left align */
  justify-content: flex-start; /* top align */
}

/* MATCH LIST */
.match-list {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

/* MATCH CARD */
.match-user {
  background: var(--card);
  padding: 15px;
  border-radius: 12px;
  width: 120px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

/* CIRCLE IMAGE */
.match-user img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}
</style>