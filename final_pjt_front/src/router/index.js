import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

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
    path: '/movies/movielist',
    name: 'movieList',
    component: MovieListView
  },
  {
    path: '/search/:input',
    name: 'search',
    component: SearchView
  },
  // {
  //   path: '/recommendation/:category',
  //   name: 'recommendation',
  //   component: RecommendationView
  // },
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

export default router
