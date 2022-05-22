<template>
  <div>
    {{ movie['name'] }}
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