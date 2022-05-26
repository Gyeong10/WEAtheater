<template>
  <div>
    <form @submit.prevent="onSubmit">
      <input class="inputbox" @keyup.enter="onSubmit" type="text" v-model="input" value="input">
      <button class="smallButton">검색</button>
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
  },
}
</script>

<style scoped>
  .inputbox {
    width: 500px;
    margin-bottom: 15px;
  }
</style>