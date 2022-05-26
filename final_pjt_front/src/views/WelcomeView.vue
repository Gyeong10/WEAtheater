<template>
  <div>
    <v-stepper v-model="e1">
      <v-stepper-header class="grey darken-1">
        <v-stepper-step
          :complete="e1 > 1"
          step="1"
          color="grey darken-3"
        >
      </v-stepper-step>

      <v-divider></v-divider>

        <v-stepper-step
          :complete="e1 > 2"
          step="2"
          color="grey darken-3"
        >
        </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        :complete="e1 > 3"
        step="3"
        color="grey darken-3"
      >
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step 
        :complete="e1 > 3"
        step="4"
        color="grey darken-3"
      >
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step 
        step="5"
        color="grey darken-3"
      >
      </v-stepper-step>
      
      </v-stepper-header>
      
      <v-stepper-items class="grey lighten-5">
        <v-stepper-content step="1">
          <v-alert
            shaped
            outlined
            type="success"
            color="grey darken-4"
          >
            반가워요, 이용자님! 이용자님께 영화 추천을 해드리기 위해 영화 선호도를 알아보고 있어요! 준비가 다 되었다면 시작버튼을 눌러주세요!
          </v-alert>
          <v-btn
            @click="e1 = 2"
            class="ma-2"
            outlined
            color="grey darken-4"
          >
            시작!
          </v-btn>
        </v-stepper-content>


        <v-stepper-content step="2">
          <v-alert
            shaped
            outlined
            type="success"
            color="grey darken-4"
          >
            선호하는 영화를 선택해 주세요!
          </v-alert>
          <v-container class="d-flex">
          <div v-for="(movie, idx) in allMovieList.slice(0, 6)" :key="idx">
            <div id="card">
              <v-card
                class="mx-3 my-3 rounded-xl"
                max-width="300"
              >
                <v-img
                  class="rounded-t-xl"
                  height="500px"
                  :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
                >
                </v-img>
                <v-card-subtitle class="text-decoration-none"> 
                  <v-btn
                  class="ma-2"
                  outlined
                  color="grey darken-4"
                  @click="e1 = 3, likeMovie({moviePk: movie.pk})"
                >
                  {{ movie.title }}
                </v-btn>
                </v-card-subtitle>
              </v-card>
            </div>
          </div>
          </v-container>
        </v-stepper-content>


        <v-stepper-content step="3">
          <v-alert
            shaped
            outlined
            type="success"
            color="grey darken-4"
          >
            한개 더!
          </v-alert>
          <v-container class="d-flex">
          <div v-for="(movie, idx) in allMovieList.slice(7, 13)" :key="idx">
            <div id="card">
              <v-card
                class="mx-3 my-3 rounded-xl"
                max-width="300"
              >
              <v-img
                class="rounded-t-xl"
                height="500px"
                :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
              >
              </v-img>
              <v-card-subtitle class="text-decoration-none"> 
                <v-btn
                  class="ma-2"
                  outlined
                  color="grey darken-4"
                  @click="e1 = 4, likeMovie({moviePk: movie.pk})"
                >
                {{ movie.title }}
                </v-btn>
              </v-card-subtitle>
              </v-card>
            </div>
          </div>
          </v-container>
        </v-stepper-content>


        <v-stepper-content step="4">
          <v-alert
            shaped
            outlined
            type="success"
            color="grey darken-4"
          >
            이제 마지막이에요!
          </v-alert>
          <v-container class="d-flex">
            <div v-for="(movie, idx) in allMovieList.slice(14, 20)" :key="idx">
              <div id="card">
                <v-card
                  class="mx-3 my-3 rounded-xl"
                  max-width="300"
                >
                <v-img
                  class="rounded-t-xl"
                  height="500px"
                  :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`"
                >
                </v-img>
                <v-card-subtitle class="text-decoration-none">
                  <v-btn
                  class="ma-2"
                  outlined
                  color="grey darken-4"
                  @click="e1 = 5, likeMovie({moviePk: movie.pk})"
                >
                {{ movie.title }}
                </v-btn>
                </v-card-subtitle>
                </v-card>
              </div>
            </div>
          </v-container>
        </v-stepper-content>


          <v-stepper-content step="5">
            <v-alert
            shaped
            outlined
            type="success"
            color="grey darken-4"
          >
            잘하셨어요! 이제 시작해볼까요?
          </v-alert>
            <v-btn
              class="ma-2"
              outlined
              color="grey darken-4"
            >
            <router-link :to="{ name: 'home' }" class="text-decoration-none indigo--text">네!</router-link>
            </v-btn>
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

.color1 {
  background-color: #dbcfb0;
}
</style>