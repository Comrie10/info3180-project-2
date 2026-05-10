// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Discover from '../pages/Discover.vue'
import Matches from '../pages/Matches.vue'
import Messages from '../pages/Messages.vue'
import Favorites from '../pages/Favorites.vue'
import Profile from '../pages/Profile.vue'
import EditProfile from '../pages/EditProfile.vue'
import Settings from '../pages/Settings.vue'
import About from '../pages/About.vue'
import Features from '../pages/Features.vue'
import Search from '../pages/Search.vue'

const routes = [

  // HOME
  {
    path: '/',
    name: 'home',
    component: Home
  },

  // AUTH
  {
    path: '/login',
    name: 'login',
    component: Login
  },

  {
    path: '/register',
    name: 'register',
    component: Register
  },

  // APP PAGES
  {
    path: '/discover',
    name: 'discover',
    component: Discover
  },

  {
    path: '/matches',
    name: 'matches',
    component: Matches
  },

  {
    path: '/messages',
    name: 'messages',
    component: Messages
  },

  {
    path: '/favorites',
    name: 'favorites',
    component: Favorites
  },

  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },

  {
    path: '/edit-profile',
    name: 'edit-profile',
    component: EditProfile
  },

  {
    path: '/settings',
    name: 'settings',
    component: Settings
  },

  // STATIC PAGES
  {
    path: '/about',
    name: 'about',
    component: About
  },

  {
    path: '/features',
    name: 'features',
    component: Features
  },

  // SEARCH PAGE
  {
    path: '/search',
    name: 'search',
    component: Search
  },

  // 404 PAGE REDIRECT
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router