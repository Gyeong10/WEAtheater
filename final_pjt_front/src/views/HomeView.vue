<template>
  <div>
    <h1>WEAtheater</h1>
    <h3>날씨에 맞춰 영화 추천</h3>
    <br>
    <br>
    <!-- <search-bar @input-change="onInputChange"></search-bar> -->
    <search-bar></search-bar>
    <br>
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
h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 70px;
}
</style>
