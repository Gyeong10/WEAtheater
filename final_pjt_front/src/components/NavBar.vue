<template>
  <div>
    <!-- <v-card> -->
    <!-- <v-card class="overflow-hidden"> -->
      <!-- <v-toolbar
        class="#1A237E white--text"
        shrink-on-scroll
        scroll-target="#scrolling-techniques-2"
        src="@/assets/logo2.webp"
        prominent
      > 
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title>MOVIEmovie</v-toolbar-title>

      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template> -->
        <div class="d-flex justify-space-between">
            <div class="d-flex">
              <li>
                <router-link class="link" id="router" :to="{ name: 'home' }">HOME</router-link>
              </li>
              <li>
                <router-link class="link" id="router" :to="{ name: 'community', params: { category: 'all' } }">COMMUNITY</router-link>
              </li>
              <li>
                <router-link class="link" id="router" :to="{ name: 'movieList'}">All MOIVE</router-link>
              </li>
            </div>

            <div class="d-flex">
              <li v-if="!isLoggedIn">
                <router-link class="link" id="router" :to="{ name: 'login' }">LOGIN</router-link>
              </li>

              <li v-if="!isLoggedIn">
                <router-link class="link" id="router" :to="{ name: 'signup'}">SIGNUP</router-link>
              </li>

              <li v-if="isLoggedIn">
                <router-link class="link" id="router" :to="{ name: 'profile', params: {username} }">
                  {{ currentUser.username }}'s PROFILE
                </router-link>
              </li>

              <li v-if="isLoggedIn">
                <router-link class="link" id="router" :to="{ name: 'logout' }">LOGOUT</router-link>
              </li>
            </div>

        
      </div>
      <!-- </v-toolbar> -->
    <!-- </v-card> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
  },
}
</script>

<style scoped>
li {
  list-style: none;
  margin: 2vh 3vw 0;
}
.link {
  color: white;
  list-style: none;
}
/* #router {
  color: white;
} */
</style>