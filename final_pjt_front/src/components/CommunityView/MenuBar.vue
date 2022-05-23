<template>
  <div>
    <router-link :to="{ name: 'community', params: { category: 'all' } }" >전체 게시판</router-link> | 
    <router-link :to="{ name: 'community', params: { category: 'free' } }">자유 게시판</router-link> | 
    <router-link :to="{ name: 'community', params: { category: 'movie' } }">영화 게시판</router-link>
    <div>
      <button @click="goNew">게시글 작성</button>
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

<style>

</style>