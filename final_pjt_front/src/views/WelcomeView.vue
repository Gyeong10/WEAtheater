<template>
  <div>
    <h2> 영화 취향을 알려주세요! </h2>
        <!-- <div v-for="(movie, idx) in allMovieList.slice(0, 19)" :key="idx">
    <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
        <v-img
          class="rounded-t-xl"
          height="500px"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="text-decoration-none">
          {{ movie.title }} 
          <v-btn
              color="primary"
              @click="hidden = !hidden, likeMovie({moviePk: movie.pk})"
            >
              {{ hidden ? '취소' : '선택' }}
            </v-btn>
        </v-card-subtitle>
    </v-card>
    </div>
        </div> -->
    <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step
        :complete="e1 > 1"
        step="1"
      >
        영화 선택 1
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        :complete="e1 > 2"
        step="2"
      >
        영화 선택 2
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3">
        영화 선택 3
      </v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-card
          class="mb-12"
          height="1300px"
          width="1500px"
        >
        <v-container class="d-flex">
        <div v-for="(movie, idx) in allMovieList.slice(0, 6)" :key="idx">
    <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
        <v-img
          class="rounded-t-xl"
          height="500px"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="text-decoration-none">
          {{ movie.title }} 
          <v-btn
          color="primary"
          @click="e1 = 2, likeMovie({moviePk: movie.pk})"
        >
          선택
        </v-btn>
        </v-card-subtitle>
    </v-card>
    </div>
        </div>
        
        </v-container>
        </v-card>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          height="1300px"
          width="1500px"
        >
        <v-container class="d-flex">
        <div v-for="(movie, idx) in allMovieList.slice(7, 13)" :key="idx">
    <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
        <v-img
          class="rounded-t-xl"
          height="500px"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="text-decoration-none">
          {{ movie.title }} 
          <v-btn
          color="primary"
          @click="e1 = 3, likeMovie({moviePk: movie.pk})"
        >
          선택
        </v-btn>
        </v-card-subtitle>
    </v-card>
    </div>
        </div>
        
        </v-container>
        </v-card>

      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          height="1300px"
          width="1500px"
        >
        <v-container class="d-flex">
        <div v-for="(movie, idx) in allMovieList.slice(14, 19)" :key="idx">
    <div id="card">
    <v-card
      class="mx-auto rounded-xl"
      max-width="300"
    >
        <v-img
          class="rounded-t-xl"
          height="500px"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
        >
        </v-img>
        <v-card-subtitle class="text-decoration-none">
          {{ movie.title }} 
          <v-btn
          color="primary"
          @click="likeMovie({moviePk: movie.pk})"
        >
          <router-link :to="{ name: 'home' }" class="text-decoration-none white--text">선택</router-link>
        </v-btn>
        </v-card-subtitle>
    </v-card>
    </div>
        </div>
        
        </v-container>
        </v-card>

      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'WelcomeView',
  data() {
    return {

      e1: 1,
    
    }
  },
  computed: {
    ...mapGetters(['allMovieList']),
  },
  methods: {
    ...mapActions(['getAllMovies', 'likeMovie']),
  },
  created() {
    this.getAllMovies()
  }
}
</script>

<style scoped>
.d-flex {
  flex-flow: row wrap;
  justify-content: center;
}

#id {
  margin: 1rem;
}
</style>