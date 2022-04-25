import { createRouter, createWebHistory } from 'vue-router'
import home from '../components/home.vue'
import report from '../components/report/report.vue'
import login from '../components/login.vue'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: home
  },
  {
    path: '/report',
    name: 'Report',
    component: report
  },
  {
    path: '/',
    name: 'Login',
    component: login
  }
]

const router = createRouter(
  {
    history: createWebHistory(process.env.BASE_URL),
    routes
  }
)

export default router
