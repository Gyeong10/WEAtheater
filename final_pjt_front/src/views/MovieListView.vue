<template>
  <div>
    <h1>모든 영화 보기</h1>
    <v-container class="d-flex">
      <movie-card
        v-for="(movie, idx) in allMovieList" :key="idx" :allMovie="movie"
      >
      </movie-card>
    </v-container>
    <!-- <router-link class="link" :to="{ name: 'movieList', query: { page: putPage } }" >{{ putPage }}</router-link> -->
    <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              @input="handlePage"
              :length="498"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieListView/MovieCard'

import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MovieListView',
  components: { MovieCard },
  data() {
    return {
      page: 1,
    }
  },
  computed: {
    ...mapGetters(['allMovieList']),
  },
  methods: {
    ...mapActions(['getAllMovies']),
    handlePage() {
      this.getAllMovies(this.page)
    }
  },
  created() {
    this.getAllMovies(this.page)
  },
  // watch: {
  //   'page' () {
  //     this.putPage = this.page
  //   }
  // }
}
</script>

<style scoped>
.d-flex {
  flex-flow: row wrap;
  justify-content: center;
}
</style>