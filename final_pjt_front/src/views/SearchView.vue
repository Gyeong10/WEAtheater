<template>
  <div>
    <search-bar></search-bar>
    <hr>
    <h2>영화 목록</h2>
    <movie-item
      v-for="(movie, idx) in searchData[0]" :key="idx" :movie="movie"
    ></movie-item>
    <hr>
    <div v-for="(searchmovie, i) in searchData[1]" :key="i">
      <h2>
        {{ searchmovie.name }}이(가)
        출연한 영화
      </h2>
      <movie-item
        v-for="(movie, idx) in searchmovie['known_for']" :key="idx" :movie="movie"
      ></movie-item>
    </div>
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