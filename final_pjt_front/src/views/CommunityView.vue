<template>
  <div>
    <h1>COMMUNITY</h1>
    <br>
    <menu-bar></menu-bar>
    <br>
    <article-list :category="category"></article-list>
  </div>
</template>

<script>
import ArticleList from '@/components/CommunityView/ArticleList'
import MenuBar from '@/components/CommunityView/MenuBar'



export default {
  name: 'CommunityView',
  components: { ArticleList, MenuBar },
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