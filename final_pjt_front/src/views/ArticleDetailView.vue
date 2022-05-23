<template>
  <div class="article-detail-view">
    <h1>{{ article.title }}</h1>
    <p>{{ article.category.name }}</p>
    <p>{{ article.content }}</p>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: {articlePk} }">
        <button>Edit</button>
      </router-link>

      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>
    <div>
      Like:
      <button @click="likeArticle(articlePk)">{{ likeCount }}</button>
    </div>
    <div>
      <router-link :to="{ name: 'community' , params: { category: 'all' } }">목록</router-link>
    </div>
    <hr />
    <comment-list :comments="article.comments"></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/ArticleDetailView/CommentList.vue'


import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleDetailView',
  components: { CommentList },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'article']),
    likeCount() {
      return this.article.like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'fetchArticle',
      'likeArticle',
      'deleteArticle',
    ])
  },
  created() {
    this.fetchArticle(this.articlePk)
  },
}
</script>

<style>

</style>