import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    articles: [],
    article: {},
    category: {'free': 2, 'movie': 3},
    categoryCount : [],
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
    category: state => state.category,
    categoryCount: state => state.categoryCount,
  },

  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => state.article.comments = comments,
    SET_CATEGORY_COUNT: (state, categoryCount) => state.categoryCount = categoryCount,
  },

  actions: {
    // 전체 게시글 목록 받아오기
    fetchArticles({ commit, getters }, page) {
    
      axios({
        url: drf.community.community() + '?page=' + page,
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_ARTICLES', res.data)
      })
        .catch(err => console.error(err.response))
    },

    // category별 게시글 받아오기
    fetchCategoryArticles({ commit, getters }, payload) {
      const cat = getters.category[payload.category]
      axios({
        url: drf.community.category_community(cat) + '?page=' + payload.page,
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_ARTICLES', res.data)
        })
        .catch(err => console.error(err.response))
    },

    // 단일 게시글 받아오기
    fetchArticle({ commit, getters }, articlePk) {
    
      axios({
        url: drf.community.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    // 게시글 생성
    createArticle({ commit, getters }, article) {

      axios({
        url: drf.community.community(),
        method: 'post',
        data: article,
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
        .catch(err => {
          console.error(err.response)
          alert('게시판을 선택해주세요!')
        }
      )
    },

    // 게시글 수정
    updateArticle({ commit, getters }, {pk, title, content}) {

      axios({
        url: drf.community.article(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    // 게시글 삭제
    deleteArticle({ commit, getters }, articlePk) {
      
      if (confirm('삭제하시겠습니까?')) {
        
        axios({
          url: drf.community.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'community' })
          })
          .catch(err => console.error(err.response))
      }
    },

    // 게시글 좋아요
    likeArticle({ commit, getters }, articlePk) {

      axios({
        url: drf.community.like_article(articlePk),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },

    // 댓글 생성
    createComment({ commit, getters }, { articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.community.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    // 댓글 삭제
    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.comment(articlePk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    },
    
    updateComment({ commit, getters }, {articlePk, commentPk, content}) {
      const comment = { content }

      axios({
        url: drf.community.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    getCategoryCount({commit, getters}) {

      axios({
        url: drf.community.category_count(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_CATEGORY_COUNT', res.data)
        })
        .catch(err => console.error(err.response))
    },
  },
}