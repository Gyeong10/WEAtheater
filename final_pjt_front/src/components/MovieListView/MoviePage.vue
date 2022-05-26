<template>
  <div>
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
  data() {
    return {
      page: 1,
      putPage: 1,
    }
  },
  computed: {
    ...mapGetters(['allMovieList']),
  },
  methods: {
    ...mapActions(['getAllMovies']),
  },
  created() {
    this.getAllMovies()
  },
}
</script>

<style scoped>
.d-flex {
  flex-flow: row wrap;
  justify-content: center;
}
</style>