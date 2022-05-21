<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment">댓글: </label>
    <input type="text" id="comment" v-model="content" required>
    <button>작성</button>
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

<style>

</style>