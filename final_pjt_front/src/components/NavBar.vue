<template>
  <div>
    <v-card class="overflow-hidden">
      <v-toolbar
        class="deep-purple darken-3 white--text"
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
      </template>

        <div class="page">
          <li>
            <router-link id="router" :to="{ name: 'home' }">Home</router-link>
          </li>
          <li>
            <router-link id="router" :to="{ name: 'community', params: { category: 'all' } }">Community</router-link>
          </li>
          <li>
            <router-link id="router"  outer-link :to="{ name: 'movieList' }">전체 영화 목록</router-link>
          </li>
          <li v-if="!isLoggedIn">
            <router-link id="router" :to="{ name: 'login' }">Login</router-link>
          </li>

          <li v-if="!isLoggedIn">
            <router-link id="router" :to="{ name: 'signup'}">Signup</router-link>
          </li>

          <li v-if="isLoggedIn">
            <router-link id="router" :to="{ name: 'profile', params: {username} }">
              {{ currentUser.username }}'s profile
            </router-link>
          </li>

          <li v-if="isLoggedIn">
            <router-link id="router" :to="{ name: 'logout' }">Logout</router-link>
          </li>
        </div>

      </v-toolbar>
    </v-card>
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

<style>

#router {
  text-decoration: none;
  color: white;
}
</style>