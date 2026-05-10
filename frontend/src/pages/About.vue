<template>
  <div class="about-page">

    <section class="about-hero">
      <h1>About DriftDater</h1>
      <p>
        DriftDater is a modern dating platform designed to help people build
        real, meaningful relationships through smart matching and simple design.
      </p>
    </section>

    <section class="about-content">

      <div class="card">
        <h2>💡 Our Mission</h2>
        <p>
          To connect people based on compatibility, interests, and genuine intent—
          not just swipes.
        </p>
      </div>

      <div class="card">
        <h2>❤️ Why DriftDater?</h2>
        <p>
          We focus on authenticity, safety, and simplicity so users can focus on
          real connections instead of distractions.
        </p>
      </div>

      <div class="card">
        <h2>🌍 Our Vision</h2>
        <p>
          A world where online dating feels natural, respectful, and human again.
        </p>
      </div>

    </section>

  </div>
</template>

<script setup>
// no JS needed
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  padding: 60px 80px;
  font-family: Arial, sans-serif;
  background: #f9f9f9;
}

.about-hero {
  text-align: center;
  margin-bottom: 50px;
}

.about-hero h1 {
  font-size: 52px;
  color: #ff4d8d;
  margin-bottom: 15px;
}

.about-hero p {
  font-size: 18px;
  max-width: 700px;
  margin: auto;
  line-height: 1.7;
  color: #444;
}

.about-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
}

.card {
  background: white;
  padding: 25px;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

.card h2 {
  margin-bottom: 12px;
  color: #222;
}

.card p {
  color: #555;
  line-height: 1.6;
}
</style>