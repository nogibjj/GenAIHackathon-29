import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './components/LandingPage.vue';
import AboutPage from './components/AboutPage.vue';
import ChatbotPage from './components/ChatbotPage.vue';


const routes = [
    { path: '/', component: LandingPage },
    { path: '/about', component: AboutPage },
    {
        path: '/chatbot',
        name: 'Chatbot',
        component: ChatbotPage
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
