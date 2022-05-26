<template>
  <div>
    <hr>
    <v-container class="d-flex">
      <div class="col-2">
        <router-link class="link" :to="{ name: 'profile', params: { username: comment.user.username} }">
          {{ comment.user.username }}
        </router-link>
      </div>

      <div class="col-7">
        <span v-if="!isEditing">{{ payload.content }}</span>

        <span v-if="isEditing">
          <input class="inputbox"  type="text" v-model="payload.content">
        </span>
      </div>

      <div class="col-3">
        <span v-if="isEditing">
          <button @click="onUpdate">완료</button> |
          <button @click="switchIsEditing">취소</button>
        </span>
        <span v-if="currentUser.username === comment.user.username && !isEditing">
          <button @click="switchIsEditing">수정</button> | 
          <button @click="deleteComment(payload)">삭제</button>
        </span>
      </div>
  </v-container>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style scoped>
.link {
  color: white;
}
.inputbox {
  width: 40vw;
  color: white;
}
</style>