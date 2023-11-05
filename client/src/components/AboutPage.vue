<template>
  <div class="about-page">
    <div class="container">
      <h1>About Us</h1>
      <p>Learn more about our amazing company.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutPage'
}
</script>

<style scoped>
.about-page {
  background-color: #f9f9f9;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  text-align: center;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

p {
  font-size: 1.2em;
  color: #555;
  margin-bottom: 30px;
}
</style>
