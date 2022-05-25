<template>
  <div>
    <vue-star-rate 
      v-on:ratingSet="myRatingMethod"
      :rateRange="3"
      :maxIcon="5"
      :iconHeight="30"
      :iconWidth="30"
      :hasCounter="true"
      color="#FFFF99"
      iconColor="#FFFF99"
      iconColorHover="#FFFF99"
      iconShape="star"
    ></vue-star-rate>
    <form @submit.prevent="onSubmit">
      <!-- <p>평점 <input  v-model="score" type="text" required></p> -->
      <label for="review">리뷰 </label>
      <input class="inputlargebox" v-model="context" id="review" type="text" required>
      <button class="smallButton">작성</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import vueStarRate from "vue-js-star-rating"

export default {
  name: 'ReviewForm',
  components: { vueStarRate },
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
    myRatingMethod(rating) {
      this.score = rating
    },
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