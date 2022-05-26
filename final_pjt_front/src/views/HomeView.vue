<template>
  <div>
    <h1>Home(웹이름)</h1>
    <br>
    <!-- <search-bar @input-change="onInputChange"></search-bar> -->
    <search-bar></search-bar>
    <recommendation-movies></recommendation-movies>
  </div>
</template>

<script>
import RecommendationMovies from '@/components/HomeView/RecommendationMovies.vue'
import SearchBar from '@/components/HomeView/SearchBar'

export default {
  name: 'HomeView',
  components: { RecommendationMovies, SearchBar },
  // data() {
  //   return {
  //     inputValue: null,
  //   }
  // },
  // methods: {
  //   onInputChange(inputText) {
  //     this.inputValue = inputText
  //   },
  // }
}
</script>

<style scoped>

</style>
