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
        { path: '/wuliao', component: ()=> import('./components/wuliao.vue') },
        { path: '/kucun', component: ()=> import('./components/kucun.vue') },
        { path: '/tiaopei', component: ()=> import('./components/tiaopei.vue') },
        { path: '/mps', component: ()=> import('./components/mps.vue') },
    ]
})

const app=createApp(App)
app.use(VueParticles)
app.use(router)
app.use(VueAxios,axios)
app.mount('#app')
