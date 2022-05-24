<template>
  <div>
    <v-toolbar
      dark
      prominent
    > 
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>MOVIEmovie</v-toolbar-title>

          <router-link :to="{ name: 'home' }">Home</router-link>

          <router-link :to="{ name: 'community', params: { category: 'all' } }">Community</router-link>

          <router-link :to="{ name: 'movieList' }">전체 영화 목록</router-link>

        <li v-if="!isLoggedIn">
          <router-link :to="{ name: 'login' }">Login</router-link>
        </li>

        <li v-if="!isLoggedIn">
          <router-link :to="{ name: 'signup'}">Signup</router-link>
        </li>

        <li v-if="isLoggedIn">
          <router-link :to="{ name: 'profile', params: {username} }">
            {{ currentUser.username }}'s profile
          </router-link>
        </li>

        <li v-if="isLoggedIn">
          <router-link :to="{ name: 'logout' }">Logout</router-link>
        </li>

    </v-toolbar>
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

</style>