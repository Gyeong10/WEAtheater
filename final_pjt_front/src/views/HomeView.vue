<template>
  <div>
    <h1>Home</h1>
    <search-bar @input-change="onInputChange"></search-bar>
    <recommendation-movies></recommendation-movies>
  </div>
</template>

<script>
import RecommendationMovies from '@/components/HomeView/RecommendationMovies.vue'
import SearchBar from '@/components/HomeView/SearchBar'

export default {
  name: 'HomeView',
  components: { RecommendationMovies, SearchBar },
  data() {
    return {
      inputValue: null,
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText
    },
  }
}
</script>

<style>

</style>