import { createApp } from 'vue'
import App from './App.vue'
import VueParticles from 'vue-particles'
import { createRouter,createWebHashHistory } from 'vue-router'
import 'font-awesome/css/font-awesome.min.css'

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        { path: '/', component: ()=> import('./components/Staff.vue') },
    ]
})

const app=createApp(App)
app.use(VueParticles)
app.use(router)
app.mount('#app')
