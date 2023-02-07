import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../views/MainPage.vue";
import FirstScene from "../views/FirstScene.vue";

const routes = [
  {
    path: "/",
    name: "main",
    component: MainPage,
  },
  {
    path: "/first",
    name: "first",
    component: FirstScene,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
