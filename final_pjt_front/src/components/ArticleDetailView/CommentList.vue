<template>
  <div class="comment-list mx-3">
    <ul>
      <comment-list-item
        v-for="comment in comments"
        :comment="comment"
        :key="comment.pk">
      </comment-list-item>
      <hr>
    </ul>
    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentForm from '@/components/ArticleDetailView/CommentForm'
import CommentListItem from '@/components/ArticleDetailView/CommentListItem'

export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>