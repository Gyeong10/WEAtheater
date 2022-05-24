<template>
  <div>
    <search-bar></search-bar>
    서치결과
    <movie-item
      v-for="(movie, idx) in searchData['results']" :key="idx" :movie="movie"
    ></movie-item>
  </div>
</template>

<script>
import MovieItem from '@/components/SearchView/MovieItem'
import SearchBar from '@/components/HomeView/SearchBar'

import { mapGetters } from 'vuex'

export default {
  name: 'SearchView',
  components: { MovieItem, SearchBar },
  computed: {
    ...mapGetters(['searchData', 'searchInput']),
  },
}
</script>

<style>

</style>