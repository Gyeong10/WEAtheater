<template>
  <div class="my-5">
    <div class="d-flex justify-space-between">
      <div class="d-flex">
        <li class="appTitle">
          <router-link class="link" id="router" :to="{ name: 'home' }">WEAtheater</router-link>
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
.appTitle {
  font-family: 'Oswald', sans-serif;
  font-size: 27px;
}
</style>