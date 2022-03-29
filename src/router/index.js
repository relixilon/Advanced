import { createRouter, createWebHistory } from 'vue-router'
import home from '../components/home.vue'
import report from '../components/report/report.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path: '/report',
    name: 'Report',
    component: report
  }
]

const router = createRouter(
  {
    history: createWebHistory(process.env.BASE_URL),
    routes
  }
)

export default router