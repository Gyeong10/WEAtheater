<template>
  <div>
    <h1>커뮤니티</h1>
    <menu-bar></menu-bar>
    <top3-article-list></top3-article-list>
    <article-list></article-list>
  </div>
</template>

<script>
import ArticleList from '@/components/CommunityView/ArticleList'
import MenuBar from '@/components/CommunityView/MenuBar'
import Top3ArticleList from '@/components/CommunityView/Top3ArticleList'

export default {
  name: 'CommunityView',
  components: { ArticleList, MenuBar, Top3ArticleList },

}
</script>

<style>

</style>