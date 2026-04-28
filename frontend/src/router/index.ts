import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../components/Dashboard.vue'
import HoaRegistry from '../views/HoaRegistry.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/hoa-management',
    name: 'HoaManagement',
    component: HoaRegistry
  },
  // We can add the Legal Workflow routes here later!
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router