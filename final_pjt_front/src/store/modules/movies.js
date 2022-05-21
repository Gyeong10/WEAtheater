// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    movies : [],
    movie: {},

  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    movies: state => state.movies,
    movie: state => state.movie,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },
  mutations: {
    // SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie
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
    }
  }
}