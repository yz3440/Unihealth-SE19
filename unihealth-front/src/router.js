import Vue from "vue";
import Router from "vue-router";
import Landing from "./views/Landing.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";
import MainNavbar from "./layout/MainNavbar.vue";

Vue.use(Router);

export default new Router({
  routes: [{
      path: "/",
      name: "index",
      components: {
        default: Landing,
        header: MainNavbar,
      },
      props: {
        header: {
          colorOnScroll: 400
        },
        footer: {
          backgroundColor: "black"
        }
      }
    },
    {
      path: "/login",
      name: "login",
      components: {
        default: Login,
        header: MainNavbar,
      },
      props: {
        header: {
          colorOnScroll: 400
        }
      }
    }, {
      path: "/register",
      name: "register",
      components: {
        default: Register,
        header: MainNavbar,
      },
      props: {
        header: {
          colorOnScroll: 400,
        }
      }
    },
    {
      path: "/profile",
      name: "profile",
      components: {
        default: Profile,
        header: MainNavbar,
      },
      props: {
        header: {
          colorOnScroll: 400
        },
        footer: {
          backgroundColor: "black"
        }
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return {
        selector: to.hash
      };
    } else {
      return {
        x: 0,
        y: 0
      };
    }
  }
});