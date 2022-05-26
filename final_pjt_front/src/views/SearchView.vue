<template>
  <div>
    <h1>movies & actors</h1>
    <search-bar></search-bar>
    <div v-if="searchData[0].length > 0">
    <br>
      <h2>영화 목록</h2>
      <div class="box">
        <movie-item
          v-for="(movie, idx) in searchData[0]" :key="idx" :movie="movie"
        ></movie-item>
      </div>
    <br>
    </div>
    
    <br>
    <div v-for="(searchmovie, i) in searchData[1]" :key="i">
      <h2>
        <router-link id="movies" :to="{name:'searchDataPerson', params:{personPk: searchmovie.id} }">
        {{ searchmovie.name }}
        </router-link>
        이(가)
        출연한 영화
      </h2>
      <div class="box">
        <movie-item
          v-for="(movie, idx) in searchmovie['known_for']" :key="idx" :movie="movie"
        ></movie-item>
      </div>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/SearchView/MovieItem'
import SearchBar from '@/components/HomeView/SearchBar'

import { mapGetters } from 'vuex'

export default {
  name: 'SearchView',
  components: { MovieItem, SearchBar },
  computed: {
    ...mapGetters(['searchData', 'searchInput']),
  },
}
</script>

<style scoped>

#movies {
  text-decoration: none;
  font-size: 1.5rem;
  color: #dbcfb0;
}
.box {
  border: 1px solid #dbcfb0;
  width: 44vw;
  margin: 1rem auto 3rem;
  padding: 1rem;
  border-radius: 10px;
  color: #dbcfb0;
  line-height: 170%;
  text-align: start;
}
</style>