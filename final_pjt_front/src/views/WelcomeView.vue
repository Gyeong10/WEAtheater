<template>
  <div>
    <h2> 영화 취향을 알려주세요! (3개이상!) </h2>
    <ul>
      <li v-for="(movie, idx) in allMovieList.slice(0, 19)" :key="idx">
        <div>
          <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
          {{ movie.title }}
          <v-btn
              color="primary"
              @click="hidden = !hidden, likeMovie({moviePk: movie.pk})"
            >
              {{ hidden ? '취소' : '선택' }}
            </v-btn>
        </div>
      </li>
    </ul>
    <router-link :to="{ name: 'home' }">Home</router-link>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'WelcomeView',
  data() {
    return {
      hidden: false,
      // hidden: [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
    }
  },
  computed: {
    ...mapGetters(['allMovieList']),
  },
  methods: {
    ...mapActions(['getAllMovies', 'likeMovie']),
  },
  created() {
    this.getAllMovies()
  }
}
</script>

<style>

</style>