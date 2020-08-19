import Vue from 'vue'
import Router from 'vue-router'
import Asteroid from '@/components/Asteroid'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Asteroid',
      component: Asteroid
    }
  ]
})
