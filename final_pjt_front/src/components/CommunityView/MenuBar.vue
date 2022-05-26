<template>
  <div>
    <router-link class="link" :to="{ name: 'community', params: { category: 'all' } }" >전체 게시판</router-link> | 
    <router-link class="link" :to="{ name: 'community', params: { category: 'free' } }">자유 게시판</router-link> | 
    <router-link class="link" :to="{ name: 'community', params: { category: 'movie' } }">영화 게시판</router-link>
    <div>
      <br>
      <v-btn large rounded id="vtn"
      color="grey lighten-1" @click="goNew"><v-icon left>
        mdi-pencil
      </v-icon>게시글 작성</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  methods: {
    goNew() {
      this.$router.push({ name: 'articleNew'})
    },
  },
  // data () {
  //   return {
  //     all: "all",
  //     free: "free",
  //   }
  // }
}
</script>

<style scoped>
.link {
  color: #dbcfb0;;
}
#vtn {
  width: 1000px;
}
</style>