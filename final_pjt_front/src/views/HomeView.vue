<template>
  <div>
    <h1>WEAtheater</h1>
    <br>
    <br>
    <!-- <search-bar @input-change="onInputChange"></search-bar> -->
    <search-bar></search-bar>
    <br>
    <recommend-weather></recommend-weather>
    <recommendation-movies></recommendation-movies>
    <recommend-actor></recommend-actor>
    <recommend-genre></recommend-genre>
  </div>
</template>

<script>
import RecommendationMovies from '@/components/HomeView/RecommendationMovies.vue'
import RecommendGenre from '@/components/HomeView/RecommendGenre.vue'
import RecommendWeather from '@/components/HomeView/RecommendWeather.vue'
import RecommendActor from '@/components/HomeView/RecommendActor.vue'
import SearchBar from '@/components/HomeView/SearchBar'

export default {
  name: 'HomeView',
  components: { RecommendationMovies, SearchBar, RecommendGenre, RecommendWeather, RecommendActor },
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
  font-size: 80px;
}
</style>
