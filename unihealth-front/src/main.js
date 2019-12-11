// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMaterial from 'vue-material'
import VueCookies from 'vue-cookies'
import 'vue-material/dist/vue-material.min.css'
import "./assets/scss/theme.scss";
import axios from 'axios';

Vue.config.productionTip = true
Vue.use(VueMaterial)
Vue.use(VueCookies)

axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://0.0.0.0:5001"
Vue.prototype.$http = axios

Vue.mixin({
  data() {
    return {};
  },
  methods: {
    tryRefreshAccessTokenAndDo(error, func) {
      if (error.response.status == 401) {
        this.$http.put("/auth/token", {
          'refresh_token': this.$cookies.get('refresh_token')
        }).then(response => {
          that.$cookies.set("access_token", response.data.access_token);
          that.$cookies.set("refresh_token", response.data.refresh_token);
          func();
        }).catch(error => {
          console.log(error);
        })
      }
    }
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>'
})
