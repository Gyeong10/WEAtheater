<template>
  <div>
    <router-link :to="{name: 'searchDataMovie', params: {moviePk : movie.id} }">
      {{ movie.title }}
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

<style>

</style>