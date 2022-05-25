<template>
  <div>
    {{ movie.known_for }}
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