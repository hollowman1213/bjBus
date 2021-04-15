import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import axios from 'axios'
import qs from 'qs'
import store from './store'

Vue.config.productionTip = false
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
