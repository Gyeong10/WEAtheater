<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <br>
    <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
    <div>
      |
      <span v-for="(genre, idx) in movie.genres" :key="idx">
      {{ genre.name }} |
      </span>

    </div>
    <div class="box">
      <p>{{ movie.overview }}</p>
    </div>
    <button @click="likeMovie(payload)"><i class="fa fa-heart fa-3x"></i></button>
    <p>{{ likeCount }}</p>
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
    ...mapGetters(['movie', 'reviews']),
    likeCount() {
      return this.movie.like_users?.length
    }
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
.fa {
  color: #dbcfb0;
}
.box {
  border: 1px solid #dbcfb0;
  margin: 5px 50px;
  padding: 8px;
  border-radius: 10px;
  color: #dbcfb0;
}
</style>