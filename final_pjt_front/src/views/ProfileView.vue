<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <h2>좋아요 누른 영화</h2>
    <ul>
      <li v-for="movie in profile.like_movies" :key="movie.pk">
        <router-link :to="{ name: 'movieDetail', params: { moviePk: movie.pk} }">
          <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>
    <hr>
    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
    <hr>
    <h2>작성한 댓글</h2>
    <ul>
      <li v-for="comment in profile.comments" :key="comment.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ comment.content }}  |  {{ comment.article }}
        </router-link>
      </li>
    </ul>
    <hr>
    <h2>좋아요한 게시글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods : {
    ...mapActions(['fetchProfile'])
  },
  created () {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }
}
</script>

<style>

</style>