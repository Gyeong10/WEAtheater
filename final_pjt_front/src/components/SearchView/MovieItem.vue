<template>
  <div>
    <router-link id="movies" class="" :to="{name: 'searchDataMovie', params: {moviePk : movie.id} }">
      <p>{{ movie.title }}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object,
    }
  }
}
</script>

<style scoped>

#movies {
  text-decoration: none;
  font-size: 1.5rem;
  color: #dbcfb0;
}

</style>