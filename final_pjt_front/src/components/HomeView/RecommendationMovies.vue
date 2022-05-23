<template>
  <div>
    <hr>
    <div v-if="recommendMovies[0]">
      <h3>Top10</h3>
      <router-link :to="{ name: 'movieDetail', params: { moviePk : recommendMovies[0].top10[0].id } }">
        <p>
          {{ recommendMovies[0].top10[0].title }}
          <img :src="`https://image.tmdb.org/t/p/w500${recommendMovies[0].top10[0].poster_url}`" alt="">
        </p>
      </router-link>
    </div>
    <hr>
    <div v-if="recommendMovies[1]">
      {{ recommendMovies[1] }}
    </div>
    <hr>
    <div v-if="recommendMovies[2]">
      {{ recommendMovies[2].weather[0] }}
    </div>
    <hr>
    <div v-if="recommendMovies[3]">
      {{ recommendMovies[3] }}
    </div>
    <hr>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecommendationMovies',
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

<style>

</style>