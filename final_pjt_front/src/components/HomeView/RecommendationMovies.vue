<template>
  <div>
    <v-container class="d-flex">
    <hr>
    <div v-if="recommendMovies[0]" id="card">
      <recommend-movie-card
        v-for="(movie, idx) in recommendMovies[0]['top10']" :key="idx" :allMovie="movie"
      >
      </recommend-movie-card>
    </div>
    </v-container>
    <!-- <hr>
    <div v-if="recommendMovies[1]">
      <recommend-movie-card
        v-for="(movie, idx) in recommendMovies[1]['actor']" :key="idx" :allMovie="movie"
      >
      </recommend-movie-card>
    </div>
    <hr>
    <div v-if="recommendMovies[2]">
      <recommend-movie-card
        v-for="(movie, idx) in recommendMovies[2]['weather']" :key="idx" :allMovie="movie"
      >
      </recommend-movie-card>
    </div>
    <hr>
    <div v-if="recommendMovies[3]">
      <recommend-movie-card
        v-for="(movie, idx) in recommendMovies[3]['genre']" :key="idx" :allMovie="movie"
      >
      </recommend-movie-card>
    </div>
    <hr> -->
  </div>
</template>

<script>
import RecommendMovieCard from '@/components/HomeView/RecommendMovieCard'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecommendationMovies',
  components: { RecommendMovieCard },
  computed: {
    ...mapGetters(['recommendMovies']),
  },
  methods: {
    ...mapActions(['getRecommendMovies']),
  },
  created() {
    this.getRecommendMovies()
  }
}
</script>

<style scoped>
.d-flex {
  
}
</style>