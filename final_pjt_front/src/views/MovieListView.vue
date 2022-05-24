<template>
  <div>
    <h1>모든 영화 보기</h1>
    <v-container class="d-flex">
      <movie-card
        v-for="(movie, idx) in allMovieList" :key="idx" :allMovie="movie"
      >
      </movie-card>
    </v-container>
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

<style scoped>
.d-flex {
  flex-flow: row wrap;
  justify-content: center;
}
</style>