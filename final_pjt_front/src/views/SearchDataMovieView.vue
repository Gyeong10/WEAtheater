<template>
<div>
  <div class="card d-flex">

    <div>
      <div class="title">
        <h1 class="d-inline font">
          {{ searchMovieData.title }}
        </h1>
      <h3 class="my-3">Overview</h3>
      <div class="box">
        <h4>{{ searchMovieData.overview }}</h4>
      </div>
    </div>
    <v-btn 
      @click="goBack"
      outlined
      id="btn"
    >Main</v-btn>
    </div>
    <div>
      <v-card
          class="mx-auto rounded-xl"
          max-width="600"
        >
        <v-img
          class="rounded-t-xl"
          height="1000"
          :src="`https://image.tmdb.org/t/p/w500${searchMovieData.poster_path}`"
        >
        </v-img>
        </v-card>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchDataMovieView',
  data() {
    return {
      moviePk : this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['searchMovieData'])
  },
  methods: {
    ...mapActions(['getSearchDataMovie']),
    goBack() {
      this.$router.go(-1)
    }
  },
  created() {
    const payload = {moviePk : this.moviePk}
    this.getSearchDataMovie(payload)
  }
}
</script>

<style scoped>
.img {
  size: 10rem;
}
.title {
  width: 50vw;
  margin: 1vh 3vw;
  line-height: 150%;
}
.font {
  font-family: 'Hahmlet', serif;
}
.box {
  border: 1px solid #dbcfb0;
  width: 44vw;
  margin: 1rem auto 3rem;
  padding: 1rem;
  border-radius: 10px;
  color: #dbcfb0;
  line-height: 170%;
}
.card {
  justify-content: space-around;
}
#btn {
  color: #dbcfb0;
}
</style>