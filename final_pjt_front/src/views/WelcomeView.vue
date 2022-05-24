<template>
  <div>
    <h2> 영화 취향을 알려주세요! (3개이상!) </h2>
    <ul>
      <li v-for="(movie, idx) in allMovieList.slice(0, 19)" :key="idx">
        <div>
          <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
          {{ movie.title }}
          <div v-if="userData in movie.like_users">
            <button @click="likeMovie({moviePk : movie.pk})">
              선택 해제
            </button>
          </div>
          <div v-else>
            <button @click="likeMovie({moviePk : movie.pk})">
              선택{{ movie.like_users }}, {{ currentUser.pk }}, {{ currentUser.username }}
            </button>
          </div>
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
      userData: {
        pk: this.currentUser.pk,
        username: this.currentUser.username
      }
    }
  },
  computed: {
    ...mapGetters(['allMovieList', 'currentUser']),
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