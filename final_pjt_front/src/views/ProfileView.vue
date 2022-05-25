<template>
  <div>
    <h1>{{ profile.username }}'s PROFILE</h1>

    <h2>관심있는 영화</h2>
    <ul>
      <!-- <li v-for="movie in profile.like_movies" :key="movie.pk">
        <router-link :to="{ name: 'movieDetail', params: { moviePk: movie.pk} }">
          <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_url}`" alt="poster">
          {{ movie.title }}
        </router-link>
      </li> -->
      <li>
      <v-container class="d-flex">
        <movie-card
          v-for="(movie, idx) in profile.like_movies" :key="idx" :allMovie="movie"
        >
        </movie-card>
      </v-container>
      </li>
    </ul>
    <br>
    <h2>작성한 글</h2>
    <div class="box">
      <ul>
        <li v-for="(article, idx) in profile.articles" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx+1 }}
          </div>
            <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          <div>
          {{ article.created_at }}
          </div>
        </li>
      </ul>
    </div>
    <br>
    <h2>작성한 댓글</h2>
    <div class="box">
      <ul>
        <li v-for="(comment, idx) in profile.comments" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx + 1 }}
          </div>
        <router-link class="link" :to="{ name: 'article', params: { articlePk: comment.article } }">
          {{ comment.content }}
        </router-link>
        <div>
          {{ comment.created_at }}
        </div>
      </li>
    </ul>
    </div>
    <br>
    <h2>좋아요 누른 게시글</h2>
    <div class="box">
      <ul>
      <li v-for="(article, idx) in profile.like_articles" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx+1 }}
          </div>
        <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      <div>
          {{ article.created_at }}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCard from '@/components/MovieListView/MovieCard'

export default {
  name: 'ProfileView',
  components: { MovieCard },
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

<style scoped>
h2 {
  text-align: left;
  margin: auto 6vw;
}
li {
  list-style: none;
}
.link {
  color: white;
}
.box {
  border: 1px solid #dbcfb0;
  margin: 1vh 5vw;
  padding: 5px 8px;
  border-radius: 10px;
  color: #dbcfb0;
  line-height: 200%;
}
</style>