// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import "./assets/scss/theme.scss";
import axios from 'axios';

Vue.config.productionTip = true
Vue.use(VueMaterial)
Vue.prototype.$http = axios


const jwt = {
  accessToken: 'shit',
  refreshToken: null,
};

const apiUrl = "0.0.0.0:5001"

Vue.mixin({
  data() {
    return {
      jwt,
      apiUrl
    };
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
