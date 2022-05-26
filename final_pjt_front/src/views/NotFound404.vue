<template>
  <div>
    <h2>404</h2>
    <h1>PAGE NOT FOUND</h1>
    <br>
    <br>
    <h2>
      뒤로 돌아가거나 <router-link class="link" id="router" :to="{ name: 'home' }">HOME</router-link>으로 돌아가주세요
    </h2>
  </div>
</template>

<script>
export default {
  name: 'NotFound404',
}
</script>

<style scoped>
.link {
  color: white;
}
</style>