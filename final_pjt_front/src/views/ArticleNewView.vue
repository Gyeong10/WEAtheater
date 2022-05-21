<template>
  <div>
    <h1>게시글 생성</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/CommunityView/ArticleForm'

export default {
  name: 'ArticleNewView',
  components: { ArticleForm },
  data() {
    return {
      article: {
        pk: null,
        title: '',
        content: '',
      }
    }
  },
}
</script>

<style>

</style>