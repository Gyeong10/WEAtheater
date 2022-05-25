<template>
  <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
      <router-link class="link" :to="{ name: 'movieDetail', params: {moviePk: allMovie.pk } }">
        <v-img
          class="rounded-t-xl"
          height="500"
          :src="`https://image.tmdb.org/t/p/w400${allMovie.poster_url}`"
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
.link {
  color : #545775;
  font-size: 17px;
}
</style>