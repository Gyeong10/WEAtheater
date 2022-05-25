<template>
  <div>
    <form @submit.prevent="onSubmit">
      <AwesomeVueStarRating 
      :star="this.star" 
      :disabled="this.disabled" 
      :maxstars="this.maxstars" 
      :starsize="this.starsize" 
      :hasresults="this.hasresults"
      :hasdescription="this.hasdescription"
      :ratingdescription="this.ratingdescription" />
      <p>평점 <input  v-model="score" type="text" required></p>
      <label for="review">review: </label>
      <input class="inputlargebox" v-model="context" id="review" type="text" required>
      <button>작성</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AwesomeVueStarRating from 'awesome-vue-star-rating'

export default {
  name: 'ReviewForm',
  components: { AwesomeVueStarRating },
  data () {
    return {
      context: '',
      score: '',
      star: 5, // default star
      ratingdescription: [
        {
          text: 'Poor',
          class: 'star-poor'
        },
        {
          text: 'Below Average',
          class: 'star-belowAverage'
        },
        {
          text: 'Average',
          class: 'star-average'
        },
        {
          text: 'Good',
          class: 'star-good'
        },
        {
          text: 'Excellent',
          class: 'star-excellent'
        }
      ],
      hasresults: true,
      hasdescription: true,
      starsize: 'lg', //[xs,lg,1x,2x,3x,4x,5x,6x,7x,8x,9x,10x],
      maxstars: 5,
      disabled: false
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
.star {
  color: yellow;
}
.star.active {
  color: yellow;
}
/* .list, .list.disabled {
  &:hover {
    .star {
      color: red !important;
    }
    .star.active {
      color: red;
    }
  }
} */
</style>