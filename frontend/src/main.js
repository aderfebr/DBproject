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
        { path: '/staff', component: ()=> import('./components/Staff.vue') },
        { path: '/area', component: ()=> import('./components/Area.vue') },
        { path: '/device', component: ()=> import('./components/Device.vue') },
        { path: '/security', component: ()=> import('./components/Security.vue') },
        { path: '/maintain', component: ()=> import('./components/Maintain.vue') },
        { path: '/alarm', component: ()=> import('./components/Alarm.vue') },
    ]
})

const app=createApp(App)
app.use(VueParticles)
app.use(router)
app.use(VueAxios,axios)
app.mount('#app')
