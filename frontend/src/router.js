import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/login.vue";
import Signup from "./pages/signup.vue";
import dashboard from "./pages/dashboard.vue";

const routes = [
    { path: "/login", component: Login },
    { path: "/signup", component: Signup },
    { path: "/", redirect: "/login" },
    { path: "/dashboard", component: dashboard },

];
const router = createRouter({
    history: createWebHistory(),
    routes,
    });

export default router;