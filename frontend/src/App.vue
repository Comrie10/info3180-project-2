<script setup>
import { RouterView } from 'vue-router'
import AppHeader from "./components/AppHeader.vue"
import AppFooter from "./components/AppFooter.vue"
</script>

<template>
  <div class="app-layout">

   <AppHeader /> 

    <main class="app-main">
      <RouterView />
    </main>

    <AppFooter />

  </div>
</template>

<style>

/* =========================
   GLOBAL THEME VARIABLES
========================= */
:root {
  --bg: #f9f9f9;
  --text: #333333;
  --card: #ffffff;
  --border: #eeeeee;
}

/* DARK MODE */
[data-theme="dark"] {
  --bg: #121212;
  --text: #ffffff;
  --card: #1e1e1e;
  --border: #333333;
}

/* =========================
   APP LAYOUT
========================= */
.app-layout {
  min-height: 100vh;

  display: flex;
  flex-direction: column;

  background: var(--bg);
  color: var(--text);

  transition: 0.3s ease;
}

.app-layout > *:first-child {
  margin-top: 0;
  padding-top: 0;
}

/* MAIN CONTENT */
.app-main {
  flex: 1;
  padding-top: 80px; /* replaces body padding-top fix */
  background: var(--bg);
  color: var(--text);
}

/* REMOVE OLD BODY FIX */
body {
  margin: 0;
}
</style>