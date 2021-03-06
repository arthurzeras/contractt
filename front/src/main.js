import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'

import './assets/scss/app.scss'

Vue.config.productionTip = false

Vue.use(VueResource)

Vue.http.options.root = 'http://localhost:8000/api/'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
