<template>
  <div>
    <hr>
    <h3>Top10</h3>
    <router-link :to="{ name: 'movieDetail', params: { moviePk : recommendMovies[0].top10[0].id } }">
      <p>
        {{ recommendMovies[0].top10[0].title }}
        <img :src="`https://image.tmdb.org/t/p/w500${recommendMovies[0].top10[0].poster_url}`" alt="">
      </p>
    </router-link>
    <hr>
    {{ recommendMovies[1] }}
    <hr>
    {{ recommendMovies[2].weather[0] }}
    <hr>
    {{ recommendMovies[3] }}
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