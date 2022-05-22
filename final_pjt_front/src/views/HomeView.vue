<template>
  <div>
    <h1>Home</h1>
    <input type="text">
    <recommendation-movies></recommendation-movies>
  </div>
</template>

<script>
import RecommendationMovies from '@/components/HomeView/RecommendationMovies.vue'

export default {
  name: 'HomeView',
  components: { RecommendationMovies },
}
</script>

<style>

</style>