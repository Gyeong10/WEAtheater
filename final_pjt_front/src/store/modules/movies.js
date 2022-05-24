import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'



export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    movies : [],
    movie: {},
    // movieLike: null,

    recommendMovies: [],
    searchData: [],
    searchInput: '',
    allMovieList: [],
    reviews: [],
    // allReviewList: [],

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
  },
  mutations: {
    // SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_RECOMMEND_MOVIES: (state, recommendMovies) => state.recommendMovies = recommendMovies,
    SET_SEARCH_DATA: (state, searchData) => state.searchData = searchData,
    SET_ALL_MOVIE_LIST: (state, allMovieList) => state.allMovieList = allMovieList,
    SET_SEARCH_INPUT: (state, input) => state.searchInput = input,
    // SET_ALL_REVIEW_LIST: (state, allReviewList) => state.allReviewList = allReviewList,
  },
  actions: {
    movieDetail({ getters, commit }, { moviePk }) {
      axios({
        url: drf.movies.movie_detail(moviePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          // console.log(res.data)
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
          // console.log(res.data)
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
          alert('평점은 숫자만 입력해주세요!')
        })
    },
    deleteReview({ getters, commit }, { moviePk, reviewPk }) {
      if (confirm('리뷰를 삭제하시겠습니까?')) {
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
          alert('평점은 숫자만 입력해주세요!')
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

    getSearchMovies({ commit, getters }, { input } ) {
      
      axios({
        url: drf.movies.search(input),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_SEARCH_INPUT', input)
          commit('SET_SEARCH_DATA', res.data)
          // console.log(getters.searchData)
          router.push({
            name: 'search',
            params: { input: getters.searchData }
          })
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    getAllMovies({ commit, getters }) {
      
      axios({
        url: drf.movies.all_movie_list(),
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
  }
}