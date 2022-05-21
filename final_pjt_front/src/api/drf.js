const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    movie_list: () => HOST + MOVIES,
    movie_detail: moviePk => HOST + MOVIES + `${moviePk}/`,
    review_create: moviePk => HOST + MOVIES + `${moviePk}/` + 'review/',
    review_delete: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'review/' + `${reviewPk}/`,
    movie_like: moviePk => HOST + MOVIES + `${moviePk}/` + 'movie_like/',
    review_like: reviewPk => HOST + MOVIES + `${reviewPk}/` + 'review_like/',
  },
  community: {
    community: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    like_article: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    comments : articlePk => HOST + COMMUNITY + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/` + COMMENTS + `${commentPk}/`
  }
}