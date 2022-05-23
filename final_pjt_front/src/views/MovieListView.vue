<template>
  <div>
    <h1>모든 영화 보기</h1>
    <movie-card
      v-for="(movie, idx) in allMovieList" :key="idx" :allMovie="movie"
    >
    </movie-card>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieListView/MovieCard'

import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MovieListView',
  components: { MovieCard },
  computed: {
    ...mapGetters(['allMovieList']),
  },
  methods: {
    ...mapActions(['getAllMovies']),
  },
  created() {
    this.getAllMovies()
  }
}
</script>

<style>

</style>