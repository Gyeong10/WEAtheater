<template>
  <div>
    <v-rating
        v-model="rating"
        background-color="white"
        color="yellow accent-4"
        dense
        half-increments
        hover
        size="18">
    </v-rating>
    <form @submit.prevent="onSubmit">
      <label for="review">  </label>
      <input class="inputlargebox" v-model="context" id="review" type="text" required>
      <button class="smallButton">작성</button>
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
      rating: 5,
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.pk, context: this.context, score: this.rating })
      // 리뷰 만들고 폼 초기화
      this.context = ''
      this.score = ''
    }
  }
}
</script>

<style>

</style>