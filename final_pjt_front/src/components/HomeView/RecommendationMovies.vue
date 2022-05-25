<template>
  <div>
    <v-container>
    <v-row dense>
    <v-col cols="12">
    <v-card
      color="blue darken-2"
      dark
    >
    <div id="recommend">
      <hr>
        <div v-if="recommendMovies[0]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[0]['top10']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    <v-col cols="12">
    <v-card
      color="indigo darken-3"
      dark
    >
    <div id="recommend">
      <hr>
        <div v-if="recommendMovies[1]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[1]['actor']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    <v-col cols="12">
    <v-card
      color="cyan lighten-2"
      dark
    >
    <div id="recommend">
      <hr>
        <div v-if="recommendMovies[2]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[2]['weather']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    <v-col cols="12">
    <v-card
      color="teal lighten-1"
      dark
    >
    <div id="recommend">
      <hr>
        <div v-if="recommendMovies[3]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[3]['genre']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    </v-row>
    </v-container>
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
#recommend {
  white-space:nowrap; 
  overflow-x: auto; 
  text-align:center;
}
</style>