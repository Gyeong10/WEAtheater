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
    <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              @input="handlePage"
              :length="categoryCount[this.payload.category]"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleList',
  data() {
    return {
      page: 1,
      payload : {category: this.category, page: this.page}
    }
  },
  props: {
    category: String,
  },
  computed: {
    ...mapGetters(['articles', 'categoryCount'])
  },
  methods: {
    ...mapActions(['fetchArticles', 'fetchCategoryArticles', 'getCategoryCount']),
    handlePage() {
      this.payload.page = this.page
      if (this.category === 'free' || this.category === 'movie') {
        this.fetchCategoryArticles(this.payload)
      } else {
        this.fetchArticles(this.page)
      }
    }
  },
  // category 바뀔 때마다 list 갱신시켜주기
  watch: {
    'category'() {
      this.page = 1
      this.payload.category = this.$route.params.category
      this.payload.page = 1
      this.getCategoryCount()
      if (this.category === 'free' || this.category === 'movie') {
      this.fetchCategoryArticles(this.payload)
      } else {
          this.fetchArticles(this.page)
      }
    }
  },
  // 처음 들어왔을 때, 새로고침 했을 때 category별로 list 출력
  created() {
    if (this.category === 'free' || this.category === 'movie') {
      this.fetchCategoryArticles(this.payload)
    } else {
        this.fetchArticles(this.page)
    }
    this.getCategoryCount()
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