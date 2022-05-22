<template>
  <div>
    <input @keyup.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      inputText: null,
    }
  },
  methods: {
    ...mapActions(['getSearchMovies']),
    onInputKeyword(event) {
      this.$emit('input-change', event.target.value)
      this.inputText = event.target.value
      const payload = {
        input: this.inputText
      }
      this.getSearchMovies(payload)
    },
  },
}
</script>

<style>

</style>