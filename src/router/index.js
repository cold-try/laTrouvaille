import { createRouter, createWebHashHistory } from 'vue-router'
import Accueil from '../views/Accueil.vue'
import AnnonceDetail from '../views/AnnonceDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Accueil',
    component: Accueil
  },
  {
    path: '/annonce_detail/:pk',
    name: 'AnnonceDetail',
    component: AnnonceDetail
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router