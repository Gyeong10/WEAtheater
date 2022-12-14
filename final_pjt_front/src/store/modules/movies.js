import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'



export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    movies : [],
    movie: {},

    recommendMovies: [],
    searchData: [],
    searchInput: '',
    allMovieList: [],
    reviews: [],

    searchMovieData: [],
    searchPersonData: [],

    genreRecom: [],
    weatherRecom: [],
    actorRecom: [],

    weatherIcon: [],
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    movies: state => state.movies,
    movie: state => state.movie,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),

    recommendMovies: state => state.recommendMovies,
    searchData: state => state.searchData,
    searchInput: state => state.searchInput,
    allMovieList: state => state.allMovieList,
    reviews: state => state.reviews,
    // allReviewList: state => state.allReviewList,
    searchMovieData: state => state.searchMovieData,
    searchPersonData: state => state.searchPersonData,

    genreRecom: state => state.genreRecom,
    weatherRecom: state => state.weatherRecom,
    actorRecom: state => state.actorRecom,

    weatherIcon: state => state.weatherIcon,
  },
  mutations: {
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => state.reviews = reviews.reverse(),
    SET_RECOMMEND_MOVIES: (state, recommendMovies) => state.recommendMovies = recommendMovies,
    SET_SEARCH_DATA: (state, searchData) => state.searchData = searchData,
    SET_ALL_MOVIE_LIST: (state, allMovieList) => state.allMovieList = allMovieList,
    SET_SEARCH_INPUT: (state, input) => state.searchInput = input,
    SET_SEARCH_DATAS: (state, searchDatas) => state.searchDatas = searchDatas,
    SET_SEARCH_MOVIE_DATA: (state, searchMovieData) => state.searchMovieData = searchMovieData,
    SET_SEARCH_PERSON_DATA: (state, searchPersonData) => state.searchPersonData = searchPersonData,

    SET_GENRE_RECOM: (state, genreRecom) => state.genreRecom = genreRecom,
    SET_WEATHER_RECOM: (state, weatherRecom) => state.weatherRecom = weatherRecom,
    SET_ACTOR_RECOM: (state, actorRecom) => state.actorRecom = actorRecom,

    SET_WEATHER_ICON: (state, weatherIcon) => state.weatherIcon = weatherIcon,
  },
  actions: {
    movieDetail({ getters, commit }, { moviePk }) {
      axios({
        url: drf.movies.movie_detail(moviePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    likeMovie({ getters, commit }, { moviePk }) {
      axios({
        url: drf.movies.movie_like(moviePk),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    updateReview({ getters, commit }, { moviePk, reviewPk, context, score }) {
      const review = { context, score }
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => {
          console.error(err.response)
          alert('????????? 0 ~ 5, ????????? ??????????????????!')
        })
    },
    deleteReview({ getters, commit }, { moviePk, reviewPk }) {
      if (confirm('????????? ?????????????????????????')) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    },
    createReview({ getters, commit }, { moviePk, username, context, score }) {
      const review = { username, context, score }
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => {
          console.error(err.response)
          alert('????????? ????????? ??????????????????!')
        })
    },
    getRecommendMovies({ commit, getters }) {

      axios({
        url : drf.movies.movie_list(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_RECOMMEND_MOVIES', res.data))
        .catch(err => {
          console.error(err.response)
        })
    },

    getSearchMovies({ commit, getters }, input ) {
      
      axios({
        url: drf.movies.search(input),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_SEARCH_INPUT', input)
          commit('SET_SEARCH_DATA', res.data)
          router.push({
            name: 'search',
            params: { input: getters.searchData }
          })
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getAllMovies({ commit, getters }, page) {
      
      axios({
        url: drf.movies.all_movie_list() + '?page=' + page ,
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ALL_MOVIE_LIST', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getAllReviews({commit, getters}, { moviePk }) {

      axios({
        url: drf.movies.review_list(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getSearchDataMovie({commit, getters}, {moviePk}) {

      axios({
        url: drf.movies.searchDataMovie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SEARCH_MOVIE_DATA', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getSearchDataPerson({commit, getters}, {personPk}) {
  
      axios({
        url: drf.movies.searchDataPerson(personPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SEARCH_PERSON_DATA', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getGenreRecom({commit, getters}) {

      axios({
        url : drf.movies.genre_list(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_GENRE_RECOM', res.data))
        .catch(err => {
          console.error(err.response)
        })
    },

    getWeatherRecom({commit, getters}) {

      axios({
        url : drf.movies.weather_list(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_WEATHER_RECOM', res.data))
        .catch(err => {
          console.error(err.response)
        })
    },

    getActorRecom({commit, getters}) {

      axios({
        url : drf.movies.actor_list(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ACTOR_RECOM', res.data))
        .catch(err => {
          console.error(err.response)
        })
    },

    getWeatherIcon({commit, getters}) {

      axios({
        url: drf.movies.weather_icon(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_WEATHER_ICON', res.data))
        .catch(err => {console.error(err.response)})
    }
  }
}