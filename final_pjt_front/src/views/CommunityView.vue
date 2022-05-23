<template>
  <div>
    <h1>커뮤니티</h1>
    <menu-bar></menu-bar>
    <top3-article-list></top3-article-list>
    <article-list :category="category"></article-list>
  </div>
</template>

<script>
import ArticleList from '@/components/CommunityView/ArticleList'
import MenuBar from '@/components/CommunityView/MenuBar'
import Top3ArticleList from '@/components/CommunityView/Top3ArticleList'


export default {
  name: 'CommunityView',
  components: { ArticleList, MenuBar, Top3ArticleList },
  data() {
    return {
      category: this.$route.params.category,
    }
  },
  // route가 변할 때마다 category값 변경
  watch: {
    '$route'() {
      this.category = this.$route.params.category
    }
  }
}
</script>

<style>

</style>