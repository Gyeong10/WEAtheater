<template>
  <div id="card">
    <v-card
      class="mx-auto rounded-xl sub"
      max-width="220"
      height="100%"
    >
      <router-link :to="{ name: 'movieDetail', params: {moviePk: allMovie.id } }" class="link">
        <v-img
          class="rounded-t-xl"
          height="300px"
          :src="`https://image.tmdb.org/t/p/w500${allMovie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="link">
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
  display: inline-block;
  padding: 10px 20px;
  margin-right: 10px;
}
.link {
  color : #545775;
  font-size: 3vh;
  height: 6vh;
  text-align: q;
}
</style>