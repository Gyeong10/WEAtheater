<template>
  <div>
    <article-form :article="article" :action="action"></article-form>
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
        category: null,
      },
      action: "create",
    }
  },
}
</script>

<style>

</style>