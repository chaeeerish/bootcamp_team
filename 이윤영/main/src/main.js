import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueCookies from "vue-cookies";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faVolumeHigh,
  faMusic,
  faRotateRight,
} from "@fortawesome/free-solid-svg-icons";
library.add(faVolumeHigh, faMusic, faRotateRight);

createApp(App)
  //쿠키를 사용한다.
  .use(VueCookies)
  .use(router)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");

//   //쿠키를 사용한다.
// App.use(VueCookies);
// //쿠키의 만료일은 7일이다. (글로벌 세팅)
// App.$cookies.config("7d");
