import Vue from 'vue'
import Router from 'vue-router'
import Landing from '@/view/Landing'
import Register from '@/view/Register'
import Login from '@/view/Login'

import Profile from '@/view/Profile'

import MainNavbar from '@/components/MainNavbar'

Vue.use(Router)

export default new Router({
  linkExactActiveClass: "active",
  routes: [{
      path: '/',
      name: 'landing',
      components: {
        header: MainNavbar,
        default: Landing
      }
    },
    {
      path: "/register",
      name: "register",
      components: {
        header: MainNavbar,
        default: Register
      }
    },
    {
      path: "/login",
      name: "login",
      components: {
        header: MainNavbar,
        default: Login
      }
    },
    {
      path: "/profile",
      name: "profile",
      components: {
        header: MainNavbar,
        default: Profile
      },
      children: [{
        path: "report",
      }, {
        path: "medication"
      }]
    }
  ]
})
