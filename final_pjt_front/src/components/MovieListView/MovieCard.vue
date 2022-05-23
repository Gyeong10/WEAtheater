<template>
  <div>
    {{ allMovie.title }}
    {{ allMovie.like_users }}
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

<style>

</style>