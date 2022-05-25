<template>
  <div>
    <span v-if="isEditing">
      <div class="review">
        평점 : <input class="inputbox" type="text" v-model="payload.score">
        <br>
        내용 : <input class="editbox" type="text" v-model="payload.context">
        <br>
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancel</button>
      </div>
    </span>
    <div class="review">
      <v-container class="d-flex m-5">
        <v-col class="col-1">
          <router-link class="link" :to="{ name: 'profile', params: { username: review.user.username} }">
            {{ review.user.username }}
          </router-link>
        </v-col>
        <v-col class="col-1">
          <i class="fa fa-star"></i> {{ review.score }}
        </v-col>
        <v-col class="col-8">
          {{ review.context }}
        </v-col>
        <v-col class="col-2">
          <span v-if="currentUser.username === review.user.username && !isEditing">
            <button @click="switchIsEditing">Edit</button> |
            <button @click="deleteReview(payload)">Delete</button>
          </span>
        </v-col>
      </v-container>
    </div>
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
        context: this.review.context,
        score: this.review.score
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

<style scoped>
.review {
  width: 1000px;
  margin: 5px auto;
  border: 1px solid #dbcfb0;
  border-radius: 10px;
  color: #dbcfb0;
}

.box {
  border: 1px solid #dbcfb0;
  width: 500px;
  margin: 50px;
  padding: 10px;
  border-radius: 10px;
  color: #dbcfb0;
}

.editbox {
  border: 1px solid #dbcfb0;
  width: 800px;
  margin: 5px 50px;
  padding: 10px;
  border-radius: 10px;
  color: #dbcfb0;
}
</style>