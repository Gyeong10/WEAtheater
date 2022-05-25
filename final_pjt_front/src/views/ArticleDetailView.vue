<template>
  <div class="article-detail-view">
    <p>| {{ article.category.name }} |</p>
    <h1>{{ article.title }}</h1>
    <pre class="content">{{ article.content }}</pre>

    <div v-if="isAuthor">
      <router-link class="link" :to="{ name: 'articleEdit', params: {articlePk} }">
        EDIT
      </router-link>

      <button @click="deleteArticle(articlePk)">DELETE</button>
    </div>
    <div>
      <button @click="likeArticle(articlePk)"><i class="fa fa-heart fa-2x"></i></button>
      {{ likeCount }}
    </div>
    <div>
      <router-link class="link" :to="{ name: 'community' , params: { category: 'all' } }">목록</router-link>
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

<style scoped>
.content {
  border: 1px solid #dbcfb0;
  margin: 4vh 10vw;
  padding: 5px 8px;
  border-radius: 10px;
  color: #dbcfb0;
}
</style>