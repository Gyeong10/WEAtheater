<template>
  <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
      <router-link :to="{ name: 'movieDetail', params: {moviePk: allMovie.pk } }" class="text-decoration-none">
        <v-img
          class="rounded-t-xl"
          height="500px"
          :src="`https://image.tmdb.org/t/p/w500${allMovie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="text-decoration-none">
          {{ allMovie.title }}
        </v-card-subtitle>
      </router-link>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
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
}
</style>