import { createApp } from 'vue'
import App from './App.vue'
import VueParticles from 'vue-particles'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createRouter,createWebHashHistory } from 'vue-router'
import 'font-awesome/css/font-awesome.min.css'

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        { path: '/item', component: ()=> import('./components/item.vue') },
        { path: '/order', component: ()=> import('./components/order.vue') },
        { path: '/crm', component: ()=> import('./components/crm.vue') },
        { path: '/answer', component: ()=> import('./components/answer.vue') },
    ]
})

const app=createApp(App)
app.use(VueParticles)
app.use(router)
app.use(VueAxios,axios)
app.mount('#app')
