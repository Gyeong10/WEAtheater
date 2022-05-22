<template>
  <div>
    <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input v-model="content" id="review" type="text" required>
      <button>작성</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewForm',
  data () {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.pk, content: this.content })
      // 리뷰 만들고 폼 초기화
      this.content = ''
    }
  }
}
</script>

<style>

</style>