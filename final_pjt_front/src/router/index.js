import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleEditView from '@/views/ArticleEditView'
import ArticleNewView from '@/views/ArticleNewView'
import CommunityView from '@/views/CommunityView'
import HomeView from '@/views/HomeView'
import SearchView from '@/views/SearchView'
import MovieDetailView from '@/views/MovieDetailView'
import MovieListView from '@/views/MovieListView'

import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView'
import SignupView from '@/views/SignupView'
import ProfileView from '@/views/ProfileView'
import WelcomeView from '@/views/WelcomeView'
import NotFound404 from '@/views/NotFound404'

import SearchDataMovieView from '@/views/SearchDataMovieView'
import SearchDataPersonView from '@/views/SearchDataPersonView'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/:moviePk',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/movielist',
    name: 'movieList',
    component: MovieListView
  },
  {
    path: '/search/:input',
    name: 'search',
    component: SearchView
  },
  {
    path: '/searchdata/movie/:moviePk',
    name: 'searchDataMovie',
    component: SearchDataMovieView
  },
  {
    path: '/searchdata/person/:personPk',
    name: 'searchDataPerson',
    component: SearchDataPersonView
  },
  {
    path: '/community/:category',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/community/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/welcome',
    name: 'welcome',
    component: WelcomeView
  },
  {
    path: '/404',
    name: 'notFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// Navigation Guard
router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'home' })
  }
})

export default router
