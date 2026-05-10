<template>
  <div class="features-page">

    <section class="features-hero">
      <h1>Features</h1>
      <p>
        Discover powerful tools designed to help you connect, communicate,
        and build meaningful relationships on DriftDater.
      </p>
    </section>

    <section class="features-grid">

      <!-- LEFT COLUMN -->
      <div class="column">

        <div class="feature-item">
          <div class="icon">🔍</div>
          <div class="content">
            <h2>Smart Matching</h2>
            <p>
              Our intelligent matching system analyzes your interests, preferences,
              and activity to suggest highly compatible users, making it easier
              to find meaningful connections.
            </p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon">❤️</div>
          <div class="content">
            <h2>Likes & Matches</h2>
            <p>
              Express interest by liking profiles. When two users like each other,
              a match is created, unlocking private messaging and deeper interaction.
            </p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon">📍</div>
          <div class="content">
            <h2>Location-Based Discovery</h2>
            <p>
              Meet people near you or expand your search globally. DriftDater helps
              you connect with users based on distance preferences you control.
            </p>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN -->
      <div class="column">

        <div class="feature-item">
          <div class="icon">💬</div>
          <div class="content">
            <h2>Real-Time Chat</h2>
            <p>
              Communicate instantly with your matches through a smooth, real-time
              messaging system designed for natural and engaging conversations.
            </p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon">🛡️</div>
          <div class="content">
            <h2>Safety Controls</h2>
            <p>
              Stay protected with built-in safety tools including block, report,
              and user filtering features that help maintain a respectful environment.
            </p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon">⚡</div>
          <div class="content">
            <h2>Fast Performance</h2>
            <p>
              DriftDater is optimized for speed, ensuring smooth navigation,
              quick loading, and a seamless user experience across all devices.
            </p>
          </div>
        </div>

      </div>

    </section>

  </div>
</template>

<script setup>
// no logic needed
</script>

<style scoped>
.features-page {
  min-height: 100vh;
  padding: 60px 80px;
  font-family: Arial, sans-serif;
  background: #ffffff;
}

/* HERO */
.features-hero {
  text-align: center;
  margin-bottom: 50px;
}

.features-hero h1 {
  font-size: 52px;
  color: #ff4d8d;
}

.features-hero p {
  font-size: 18px;
  color: #555;
  max-width: 750px;
  margin: 12px auto 0;
  line-height: 1.7;
}

/* 2 COLUMN LAYOUT */
.features-grid {
  display: flex;
  gap: 30px;
}

/* EACH COLUMN */
.column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* FEATURE CARD */
.feature-item {
  display: flex;
  gap: 15px;

  padding: 20px;
  border-radius: 14px;
  background: #f9f9f9;

  box-shadow: 0 6px 16px rgba(0,0,0,0.06);
  transition: 0.3s;
}

.feature-item:hover {
  transform: translateY(-4px);
}

/* ICON */
.icon {
  font-size: 28px;
  width: 50px;
  height: 50px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: #ffe3ec;
  border-radius: 12px;
}

/* TEXT */
.content h2 {
  margin: 0;
  font-size: 18px;
  color: #222;
}

.content p {
  margin-top: 6px;
  font-size: 14px;
  color: #555;
  line-height: 1.6;
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .features-grid {
    flex-direction: column;
  }
}
</style>