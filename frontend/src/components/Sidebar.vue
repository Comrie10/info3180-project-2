<template>
  <aside class="sidebar">

    <div class="logo-area">
      <h1>Activity</h1>
    </div>

    <nav class="nav-links">
      <router-link to="/profile">My Profile</router-link>
      <router-link to="/discover">Discover</router-link>
      <router-link to="/matches">Matches</router-link>
      <router-link to="/messages">Messages</router-link>
      <router-link to="/favorites">Favorites</router-link>
      <router-link to="/search">Search</router-link>

    </nav>

  </aside>
</template>

<script setup>
// no JS needed — theme handled globally
</script>

<style scoped>
/* =========================
   SIDEBAR (THEME AWARE)
========================= */
.sidebar {
  width: 250px;
  height: 100vh;

  background: var(--nav);
  color: var(--text1);

  display: flex;
  flex-direction: column;

  padding: 20px;
  transition: 0.3s ease;
}

/* LOGO */
.logo-area h1 {
  color: #ff4d8d;
  font-size: 22px;
  margin-bottom: 30px;
}

/* LINKS */
.nav-links {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.nav-links a {
  text-decoration: none;
  color: var(--text1);
  font-weight: 500;
  transition: 0.2s;
}

/* HOVER */
.nav-links a:hover {
  color: #ff4d8d;
}
</style>

