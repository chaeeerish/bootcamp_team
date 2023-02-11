import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faVolumeHigh,
  faMusic,
  faRotateRight,
} from "@fortawesome/free-solid-svg-icons";
import "animate.css";
library.add(faVolumeHigh, faMusic, faRotateRight);
createApp(App)
  .use(router)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
