<template>
  <div>
    서치서치
    <movie-item
      v-for="(movie, idx) in searchData['results']" :key="idx" :movie="movie"
    ></movie-item>
  </div>
</template>

<script>
import MovieItem from '@/components/SearchView/MovieItem'

import { mapGetters } from 'vuex'

export default {
  name: 'SearchView',
  components: { MovieItem },
  computed: {
    ...mapGetters(['searchData']),
  },
}
</script>

<style>

</style>