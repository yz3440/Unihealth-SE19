// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import "./assets/scss/theme.scss";
import axios from 'axios';
import store from "./store"

Vue.config.productionTip = true
Vue.use(VueMaterial)

axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://0.0.0.0:5001"
Vue.prototype.$http = axios

Vue.mixin({
  computed: {
    currentDate() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth() + 1; //Because January is 0
      var yyyy = today.getFullYear();

      if (dd < 10) dd = "0" + dd;
      if (mm < 10) mm = "0" + mm;

      today = yyyy + "-" + mm + "-" + dd;
      return today;
    }
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
