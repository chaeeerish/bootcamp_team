import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../views/MainPage.vue";
import FirstScene from "../views/FirstScene.vue";
import SecondScene from "../views/SecondScene.vue";
import ResultData from "../views/ResultData.vue";

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
  {
    path: "/second",
    name: "second",
    component: SecondScene,
  },
  {
    path: "/result",
    name: "result",
    component: ResultData,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
