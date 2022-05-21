const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOIVES = 'movies/'
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
    movie_list: () => HOST + MOIVES,
    movie_detail: movie_pk => HOST + movie_pk,
    review_create: movie_pk => HOST + movie_pk + 'review/',
    review_delete: (movie_pk, review_pk) => HOST + movie_pk + 'review/' + review_pk,
    movie_like: movie_pk => HOST + movie_pk + 'movie_like/',
    review_like: review_pk => HOST + review_pk + 'review_like/',
  },
  community: {
    community: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}`,
    like_article: articlePk => HOST + COMMUNITY + `${articlePk}` + 'like/',
    comments : articlePk => HOST + COMMUNITY + `${articlePk}` + COMMENTS,
    comment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}` + COMMENTS + `${commentPk}`
  }
}