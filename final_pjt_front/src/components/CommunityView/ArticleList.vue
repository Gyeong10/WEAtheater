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
  props: {
    category: String,
  },
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles', 'fetchCategoryArticles'])
  },
  // category 바뀔 때마다 list 갱신시켜주기
  watch: {
    'category'() {
      if (this.category === 'free' || this.category === 'movie') {
      this.fetchCategoryArticles(this.category)
      } else {
          this.fetchArticles()
      }
    }
  },
  // 처음 들어왔을 때, 새로고침 했을 때 category별로 list 출력
  created() {
    if (this.category === 'free' || this.category === 'movie') {
      this.fetchCategoryArticles(this.category)
    } else {
        this.fetchArticles()
    }
  }
}
</script>

<style>

</style>