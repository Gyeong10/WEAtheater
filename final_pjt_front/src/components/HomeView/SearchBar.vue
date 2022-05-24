<template>
  <div>
    <form @submit.prevent="onSubmit">
      <input class="inputbox" @keyup.enter="onSubmit" type="text" v-model="input" value="input">
      <button class="button">검색</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      input: this.searchInput,
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
    onSubmit() {
      this.getSearchMovies(this.input)
    }
    // onInputKeyword(event) {
    //   // this.inputValue = event.target.value
    //   // this.$emit('input-change', this.inputValue)
    //   // const payload = { input: this.inputValue}
    //   this.payload.input = event.target.value
      // this.getSearchMovies(this.payload)
    // },
    // watch: {
    //   'searchInput' () {
    //     this.getSearchMovies(this.payload)
    //   }
    // },
  },
}
</script>

<style scoped>
  .button {
    padding: 5px 10px;
  }
  .inputbox {
    width: 500px;
    margin-bottom: 15px;
  }
</style>