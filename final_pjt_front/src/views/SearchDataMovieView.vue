<template>
  <div>
    {{ searchMovieData.title }}
    <br>
    {{ searchMovieData.overview }}
    <br>
    <v-img :src="`https://image.tmdb.org/t/p/w500${searchMovieData.poster_path}`"></v-img>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchDataMovieView',
  data() {
    return {
      moviePk : this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['searchMovieData'])
  },
  methods: {
    ...mapActions(['getSearchDataMovie'])
  },
  created() {
    const payload = {moviePk : this.moviePk}
    this.getSearchDataMovie(payload)
  }
}
</script>

<style>

</style>