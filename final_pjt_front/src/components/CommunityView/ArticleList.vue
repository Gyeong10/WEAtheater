<template>
  <div>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        작성자 : {{ article.user.username }} / 

        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>

        댓글 : {{ article.comment_count }}
        좋아요 : {{ article.like_count }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleList',
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>