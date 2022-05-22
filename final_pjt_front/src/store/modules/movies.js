// import router from '@/router'
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

  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    movies: state => state.movies,
    movie: state => state.movie,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),

    recommendMovies: state => state.recommendMovies,
  },
  mutations: {
    // SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => state.movie.reviews = reviews,
    SET_RECOMMEND_MOVIES: (state, recommendMovies) => state.recommendMovies = recommendMovies,
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
    updateReview({ getters, commit }, { articlePk, reviewPk, content }) {
      const review = { content }
      axios({
        url: drf.movies.review(articlePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
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
    createReview({ getters, commit }, { moviePk, content }) {
      const review = { content }
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
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

    // getSeachMovies({}) {}
  }
}