<template>
  <div>
    <v-container>
    <v-row dense>
      <v-col cols="12" class="my-3">
      <v-card
        color="#6e74b9"
        class="rounded-pill"
      >
      <div id="recommend">
        <h2> WEATHER </h2>
          <div v-if="recommendMovies[2]" id="card">
            <recommend-movie-card
              v-for="(movie, idx) in recommendMovies[2]['weather']" :key="idx" :allMovie="movie"
            >
            </recommend-movie-card>
          </div>
      </div>
      </v-card>
    </v-col>
    <v-col cols="12" class="my-3">
    <v-card
      color="#7b7fa8"
      class="rounded-pill"
    >
    <div id="recommend">
      <h2> TOP10 </h2>
      <!-- <div class="swiper-button-prev"></div> -->
        <div v-if="recommendMovies[0]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[0]['top10']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
      <!-- <div class="swiper-button-next"></div> -->

    </div>
    </v-card>
    </v-col>
    <v-col cols="12" class="my-3">
    <v-card
      color="#52578f"
      class="rounded-pill"
    >
    <div id="recommend">
      <h2> ACTORS </h2>
        <div v-if="recommendMovies[1]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[1]['actor']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    
    <v-col cols="12" class="my-3">
    <v-card
      color="#284685"
      class="rounded-pill"
    >
    <div id="recommend">
      <h2> GENRE </h2>
        <div v-if="recommendMovies[3]" id="card">
          <recommend-movie-card
            v-for="(movie, idx) in recommendMovies[3]['genre']" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
        </div>
    </div>
    </v-card>
    </v-col>
    </v-row>
    </v-container>
  </div>
</template>

<script>
import RecommendMovieCard from '@/components/HomeView/RecommendMovieCard'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecommendationMovies',
  components: { RecommendMovieCard },
  // data () {
  //   return {
  //     mySwiper: new Swiper('.swiper-container', {
  //     // 슬라이드를 버튼으로 움직일 수 있습니다.
  //       navigation: {
  //         nextEl: '.swiper-button-next',
  //         prevEl: '.swiper-button-prev',
  //       },
  //     })
  //   }
  // },
  computed: {
    ...mapGetters(['recommendMovies']),
  },
  methods: {
    ...mapActions(['getRecommendMovies']),
  },
  created() {
    this.getRecommendMovies()
  }
}

</script>

<style scoped>
#recommend {
  white-space:nowrap; 
  overflow-x: hidden; 
  text-align:center;
  padding: 3vh;
}
</style>