<template>
  <div>
    <review-form></review-form>
    <ul>
        <review-list-item v-for="review in reviews" :key="review.pk" :review="review"></review-list-item>
    </ul>
  </div>
</template>

<script>
import ReviewForm from '@/components/MovieDetailView/ReviewForm.vue'
import ReviewListItem from '@/components/MovieDetailView/ReviewListItem.vue'


export default {
  name: 'ReviewList',
  components: { ReviewForm, ReviewListItem },
  props: {
    reviews: Object,
  },

}
</script>

<style>

</style>