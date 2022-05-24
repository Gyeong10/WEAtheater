<template>
  <div>
    <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input v-model="context" id="review" type="text" required>
      <p>평점 <input v-model="score" type="text" required></p>
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
      context: '',
      score: '',
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.pk, context: this.context, score: this.score })
      // 리뷰 만들고 폼 초기화
      this.context = ''
      this.score = ''
    }
  }
}
</script>

<style>

</style>