<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="movie.poster_url" alt="poster">
    <review-list></review-list>
  </div>
</template>

<script>
import ReviewList from '@/components/MovieDetailView/ReviewList.vue'

import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'MovieDetailView',
  components: {
    ReviewList
  },
  computed: {
    ...mapGetters(['movie'])
  },
  methods: {
    ...mapActions(['movieDetail'])
  },
  created () {
    console.log(this.$route.params.moviePk)
    const payload = { moviePk : this.$route.params.moviePk }
    this.movieDetail(payload)
  }
}
</script>

<style>

</style>