<template>
  <div>
    <span v-if="isEditing">
      <input type="text" v-model="payload.context">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancel</button>
    </span>

    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
    <router-link :to="{ name: 'profile', params: { username: review.user.username} }">
      {{ review.user.username }}
    </router-link>
    {{ review }}
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie_id,
        reviewPk: this.review.pk,
        context: this.review.context
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>

</style>