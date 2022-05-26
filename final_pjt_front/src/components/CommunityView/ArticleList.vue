<template>
  <div>
    <ul>
      <li class="article" v-for="article in articles" :key="article.pk">
        <div class="col-2">
          {{article.pk}} |  
          <router-link class="link" :to="{ name: 'profile', params: { username: article.user.username} }">
            {{ article.user.username }}
          </router-link>

        </div>
        <div class="col-7">
          <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
            {{ article.title }}
          </router-link>
        </div>
        <div class="col-3">
        댓글  {{ article.comment_count }}
        좋아요  {{ article.like_count }}
        </div>
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

<style scoped>
li {
  list-style: none;
}
.link {
  color: #dbcfb0;
}
.article {
  display: flex;
  width: 80vw;
  height: 7vh;
  margin: 3vh auto;
  border: 1px solid #dbcfb0;
  border-radius: 10px;
  color: #dbcfb0;
  align-items: center;
}
</style>