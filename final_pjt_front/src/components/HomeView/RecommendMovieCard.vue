<template>
  <div id="card">
    <v-card
      class="mx-auto"
      max-width="200"
    >
      <router-link :to="{ name: 'movieDetail', params: {moviePk: allMovie.id } }" class="text-decoration-none">
        <v-img
          height="300px"
          :src="`https://image.tmdb.org/t/p/w500${allMovie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle>
          {{ allMovie.title }}
        </v-card-subtitle>
      </router-link>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'RecommendMovieCard',
  props: {
    allMovie: {
      type: Object,
    }
  }
}
</script>

<style scoped>
#card {
  margin: 1rem;
  display:inline-block; padding: 10px 20px; margin-right:10px;
}
</style>