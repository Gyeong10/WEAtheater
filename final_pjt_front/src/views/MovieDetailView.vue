<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
    <p>{{ movie.genres }}</p>
    <p>{{ movie.overview }}</p>
    <button @click="likeMovie(payload)">좋아요</button>
    <p>좋아요 누른 사람: {{ movie.like_users }}</p>
    <review-list :reviews="reviews"></review-list>
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
  data () {
    return {
      payload: ({ moviePk : this.$route.params.moviePk }),
    }
  },
  computed: {
    ...mapGetters(['movie', 'reviews'])
  },
  methods: {
    ...mapActions(['movieDetail', 'likeMovie', 'getAllReviews'])
  },
  created () {
    // console.log(this.$route.params.moviePk)
    // const payload = { moviePk : this.$route.params.moviePk }
    this.movieDetail(this.payload)
    this.getAllReviews(this.payload)
  }
}
</script>

<style>

</style>