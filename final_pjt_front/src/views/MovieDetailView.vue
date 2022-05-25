<template>
  <div>
    <div class="card d-flex justify-center">
      <div>
        <img class="img" :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
      </div>
      <div>
        <div>
          <h1 class="d-inline">{{ movie.title }}</h1>
          <h2 class="d-inline"> ( {{ movie.release_date.slice(0, 4) }} )</h2>
        </div>
        <div>
          |
          <span v-for="(genre, idx) in movie.genres" :key="idx">
          {{ genre.name }} |
          </span>
        </div>
        <br>
        <div>
          출연 배우
          <br>
          |
          <span v-for="(actor, idx) in movie.actors.slice(0, 3)" :key="idx"> {{ actor.name }} |</span >
        </div>
        <div class="box">
          <p>{{ movie.overview }}</p>
        </div>
        <div>
          <button @click="likeMovie(payload)"><i class="fa fa-heart fa-3x"></i></button>
          <p>{{ likeCount }}</p>
        </div>
      </div>
    </div>
    <br>
    <div class="my-5">
      <h2> Review </h2>
      <br>
      <review-list :reviews="reviews"></review-list>
    </div>
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
/* .card {
  color: #dbcfb0;
  background-color: #545775;
} */
.fa {
  color: #dbcfb0;
}
.box {
  border: 1px solid #dbcfb0;
  width: 500px;
  margin: 50px;
  padding: 10px;
  border-radius: 10px;
  color: #dbcfb0;
}
.img {
  height: 33rem;
}
</style>