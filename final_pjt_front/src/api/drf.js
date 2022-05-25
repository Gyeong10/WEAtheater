const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'

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
    all_movie_list: () => HOST + MOVIES + 'movielist/',
    movie_detail: moviePk => HOST + MOVIES + `${moviePk}/`,
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,  // create
    review_list: moviePk => HOST + MOVIES + `${moviePk}/` + 'reviewlist/',  // review list
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,  // update or delete
    movie_like: moviePk => HOST + MOVIES + `${moviePk}/` + 'movie_like/',
    review_like: reviewPk => HOST + MOVIES + `${reviewPk}/` + 'review_like/',
    search: input => HOST + MOVIES + 'search/' + `${input}/`,
    search_datas: moviePk => HOST + MOVIES + 'search/' + `${moviePk}/`,
  },
  community: {
    community: () => HOST + COMMUNITY, // 목록 불러오기, create
    category_community: category => HOST + COMMUNITY + 'category/' + `${category}/`, // category 목록 불러오기
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`, // 상세 게시글 보기
    like_article: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    comments : articlePk => HOST + COMMUNITY + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/` + COMMENTS + `${commentPk}/`
  }
}