// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    movies : [],
    movie: {},

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

    SET_RECOMMEND_MOVIES: (state, recommendMovies) => state.recommendMovies = recommendMovies,
  },
  actions: {
    movieDetail({ getters, commit }, { moviePk }) {
      axios({
        url: drf.movies.movie_detail(moviePk),
        method: 'get',
        header: getters.authHeader
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.log(err.response.data))
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