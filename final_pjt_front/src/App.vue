<template>
  <v-app id="app">
    <div id="body-wrapper">
      <nav-bar></nav-bar>
      <router-view id="body-content"></router-view>
      <foot-bar></foot-bar>
    </div>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import FootBar from '@/components/FootBar.vue'
import { mapActions } from 'vuex'

export default ({
  name: 'App',
  components: { NavBar, FootBar },
  methods : {
    ...mapActions(['fetchCurrentUser'])
  },
  created() {
    this.fetchCurrentUser()
  }
})
</script>

<style>
#app {
  font-family: 'Noto Serif KR', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #dbcfb0;
  background-color: black;
  margin: 0;
  padding: 0;
  height: 100%;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#body-wrapper {
  min-height: 100%;
  position: relative;
}

#body-content {
  margin-top: 100px;
  padding-bottom: 100px;
}

.link {
  text-decoration: none;
  color: #dbcfb0;
}

.inputbox {
  border: 1px solid #dbcfb0;
  margin: 4px;
  padding: 5px 8px;
  border-radius: 10px;
  color: #dbcfb0;
}

.button {
  border: 1px solid #dbcfb0;
  background-color: #dbcfb0;
  color: #545775;
  margin: 4px;
  padding: 2px 100px;
  border-radius: 10px;
}

.inputlargebox {
  color: #dbcfb0;
  border: 1px solid #dbcfb0;
  border-radius: 10px;
  margin: 20px;
  padding: 5px 8px;
  width: 700px;
  height: 50px;
}

.smallButton {
  border: 1px solid #dbcfb0;
  background-color: #dbcfb0;
  color: #545775;
  padding: 5px 10px;
  margin: 4px;
  border-radius: 10px;
}
h1 {
  font-size: 50px;
}
</style>
