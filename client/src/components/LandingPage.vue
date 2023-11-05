<template>
  <div class="landing-page">
    <div class="container">
      <h1>Test to Our Website</h1>
      <p>Discover amazing features and content.</p>
      <router-link to="/about" class="cta-button">Learn more</router-link>
      <router-link to="/chatbot">Chatbot</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage'
}
</script>

<style scoped>
.landing-page {
  background-color: #f4f4f4;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  text-align: center;
}

h1 {
  font-size: 3em;
  margin-bottom: 20px;
}

p {
  font-size: 1.2em;
  color: #555;
  margin-bottom: 30px;
}

.cta-button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 1.2em;
  text-decoration: none;
  color: #fff;
  background-color: #007BFF;
  border-radius: 5px;
}
</style>
