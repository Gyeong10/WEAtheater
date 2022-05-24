<template>
  <div>
    <input @keyup.enter="onInputKeyword" type="text" :value="searchInput">
    <button @keyup.enter="onInputKeyword">검색</button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      payload: { input: '' }
    }
  },
  computed : {
    ...mapGetters(['searchInput'])
  },
  // data() {
  //   return {
  //     inputText: null,
  //   }
  // },
  methods: {
    ...mapActions(['getSearchMovies']),
    onInputKeyword(event) {
      this.payload.input = event.target.value
      this.$emit('input-change', this.payload)
      this.getSearchMovies(this.payload)
    },
    // watch: {
    //   'searchInput' () {

    //   }
    // },
  },
}
</script>

<style>

</style>