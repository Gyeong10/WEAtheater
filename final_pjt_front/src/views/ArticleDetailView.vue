<template>
  <div>
    <p class="title left p">| {{ article.category.name }} |</p>
    
    <v-btn tile v-if="!isAuthor" class="listbutton"><v-icon left>mdi-home</v-icon>
      <router-link class="link" :to="{ name: 'community', params: { category: 'all' } }">목록</router-link>
    </v-btn>
    <div class="buttons" v-if="isAuthor">
    
    <div>
      <v-btn tile class="editButton inline"><v-icon left>mdi-home</v-icon>
        <router-link class="link" :to="{ name: 'community', params: { category: 'all' } }">목록</router-link>
      </v-btn>
    </div>

    <div>
      <v-btn tile class="editButton inline">
        <v-icon left>
          mdi-pencil
        </v-icon>
        <router-link class="link" :to="{ name: 'articleEdit', params: {articlePk} }">EDIT</router-link>
      </v-btn>
      <v-btn depressed class="editButton inline" @click="deleteArticle(articlePk)"><v-icon left>
        mdi-delete
      </v-icon>DELETE</v-btn>
      </div>
    </div>

    <br>
    <h2 class="title left">제목 : {{ article.title }}</h2>
    <br>
    <pre class="content left">{{ article.content }}</pre>
    <br>
    <div>
      <button @click="likeArticle(articlePk)"><i class="fa fa-heart fa-2x"></i></button>
      {{ likeCount }}
    </div>
    <br>
    
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
  font-size: 30px;
  min-height: 300px;
}
.left {
    text-align: left;
}
.link {
  color: #545775;
}
.buttons {
  display: flex;
  justify-content: space-between;
  margin: 0 10vw;
}
.editButton {
  border: 1px solid #dbcfb0;
  width: 100px;
  height: 35px;
  padding: 6px 8px;
  margin: 0 1vw;
  border-radius: 50px;
  background-color: #dbcfb0;
  color: #545775;
  font-size: 15px;
  vertical-align: middle;
  text-align: center;
  align-content: center;
}
.listbutton {
  margin: 0 10vw;
  display: flex;

  border: 1px solid #dbcfb0;
  width: 100px;
  height: 35px;
  padding: 6px 8px;
  border-radius: 50px;
  background-color: #dbcfb0;
  color: #545775;
  font-size: 15px;
  vertical-align: middle;
  text-align: center;
  align-content: center;
}
.inline {
  display: inline;
}
</style>