<template>
  <div>
    <div class="card d-flex justify-center">
      <div>
        <img class="img" :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
      </div>
      <div>
        <div class="title">
          <h1 class="d-inline font">{{ movie.title }}</h1>
          <h2 class="d-inline font"> ( {{ movie.release_date.slice(0, 4) }} )</h2>
        </div>
        <div>
          |
          <span v-for="(genre, idx) in movie.genres" :key="idx">
          {{ genre.name }} |
          </span>
        </div>
        <br>
        <div>
          <h3>ACTOR</h3>
          |
          <span v-for="(actor, idx) in movie.actors.slice(0, 3)" :key="idx"> {{ actor.name }} |</span >
        </div>
        <div class="mt-5">
          <h3 class="d-inline me-2">평점</h3>
          <h3 v-if="avgScore" class="d-inline me-5">{{ avgScore }}</h3>
          <h3 v-else class="d-inline me-5">-</h3>
          <button @click="likeMovie(payload)" class="d-inline ms-5"><i class="fa fa-heart fa-2x"></i></button>
          <h3 class="d-inline ms-2">{{ likeCount }}</h3>
        </div>
        <br>
        <h3>Overview</h3>
        <div class="box">
          <h4>{{ movie.overview }}</h4>
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
    },
    avgScore() {
      const reviews = this.movie.reviews
      if (reviews) {
        var sumScore = 0
        reviews.forEach(review => {
          sumScore += review.score
        });
        return Math.round(sumScore / reviews.length *100) / 100
      } else {
        return 0
      }
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

<style scoped>
/* .card {
  color: #dbcfb0;
  background-color: #545775;
} */
.fa {
  color: #dbcfb0;
}
.box {
  border: 1px solid #dbcfb0;
  width: 44vw;
  margin: 1rem auto 3rem;
  padding: 1rem;
  border-radius: 10px;
  color: #dbcfb0;
  line-height: 170%;
}
.img {
  height: 33rem;
}
.title {
  width: 50vw;
  margin: 1vh 3vw;
  line-height: 150%;
}
.font {
  font-family: 'Hahmlet', serif;
}
</style>