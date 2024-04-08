import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/login.vue";
import Signup from "./pages/signup.vue";


const routes = [
    { path: "/login", component: Login },
    { path: "/signup", component: Signup },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
    });

export default router;