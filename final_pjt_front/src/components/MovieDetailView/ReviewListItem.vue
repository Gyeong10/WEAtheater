<template>
  <div>
    <div class="review">
      <v-container class="d-flex m-5">
        <v-col class="col-1">
          <router-link class="link" :to="{ name: 'profile', params: { username: review.user.username} }">
            {{ review.user.username }}
          </router-link>
        </v-col>
      <v-col class="col-1">
        <span v-if="!isEditing">
          <i class="fa fa-star"></i> {{ review.score }}
        </span>
        <span v-if="isEditing">
          <i class="fa fa-star"></i><input class="scorebox" type="text" v-model="payload.score">
        </span>
      </v-col>
        
        <v-col class="col-8">
          <span v-if="!isEditing">
            {{ review.context }}
          </span>
          <span v-if="isEditing">
            내용 <input class="editbox" type="text" v-model="payload.context">
          </span>
        </v-col>
        
        <v-col class="col-2">
          <span v-if="isEditing">
            <button @click="onUpdate">Update</button> |
            <button @click="switchIsEditing">Cancel</button>
          </span>
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
.scorebox {
  border: 1px solid #dbcfb0;
  width: 50px;
  margin: 1rem 3rem;
  padding: 10px;
  border-radius: 10px;
  color: #dbcfb0;
}

.editbox {
  border: 1px solid #dbcfb0;
  width: 50vw;
  margin: 1rem 3rem;
  padding: 10px;
  border-radius: 10px;
  color: #dbcfb0;
}
</style>