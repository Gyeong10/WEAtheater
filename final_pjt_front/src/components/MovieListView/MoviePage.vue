<template>
  <div>
    moviePage
    <div class="text-center">
    <v-pagination
      v-model="page"
      :length="6"
    ></v-pagination>
  </div>
  </div>
</template>

<script>
export default {
  name: 'MoviePage',
  data() {
    return {
      page: 1,
    }
  },
}
</script>

<style>

</style>