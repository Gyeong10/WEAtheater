<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment">댓글: </label>
    <input class="inputlargebox" type="text" id="comment" v-model="content" required>
    <v-btn rounded><button>작성</button></v-btn>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content })
      this.content = ''
    }
  }
}
</script>

<style scoped>
  .button {
    padding: 5px 10px;
  }

</style>