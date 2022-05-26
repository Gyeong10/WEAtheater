<template>
  <div>
    <p class="title left p">| {{ article.category.name }} |</p>
    <h2 class="title left">{{ article.title }}</h2>
    <div class="buttons" v-if="isAuthor">
      <div class="editButton">
        <router-link class="link" :to="{ name: 'articleEdit', params: {articlePk} }">
          EDIT
        </router-link>
      </div>

      <button class="editButton" @click="deleteArticle(articlePk)">DELETE</button>
    </div>

    <pre class="content left">{{ article.content }}</pre>

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
.p {
  font-size: 3px;
}
.title {
  margin-left: 10vw;
}
.content {
  border: 1px solid #dbcfb0;
  margin: 1vh 10vw 4vh;
  padding: 4px 20px;
  border-radius: 10px;
  color: #dbcfb0;
  font-size: 15px;
}
.left {
    text-align: left;
}
.link {
  color: #545775;
}
.buttons {
  display: flex-end;
  justify-content: right;
  margin: 0 10vw;
}
.editButton {
  border: 1px solid #dbcfb0;
  width: 80px;
  height: 35px;
  padding: 6px 8px;
  margin: 0 1vw;
  border-radius: 10px;
  background-color: #dbcfb0;
  color: #545775;
  font-size: 15px;
  vertical-align: middle;
  text-align: center;
  align-content: center;
}
</style>