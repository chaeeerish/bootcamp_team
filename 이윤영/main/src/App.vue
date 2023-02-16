<template>
  <desktop-scene v-if="desktop"></desktop-scene>
  <MainPage
    @ToFirstScene="ToFirstScene"
    @toggleSound="toggleSound"
    v-bind:isPlaying="isPlaying"
    v-if="mobile"
  ></MainPage>

  <FirstScene
    @ToSecondScene="ToSecondScene"
    @toggleSound="toggleSound"
    v-bind:isPlaying="isPlaying"
    v-if="showFirst"
  ></FirstScene>

  <SecondScene
    @toggleSound="toggleSound"
    v-bind:isPlaying="isPlaying"
    v-if="showSecond"
  ></SecondScene>
</template>

<script>
import DesktopScene from "./components/DesktopScene.vue";
import MainPage from "./views/Main/MainPage.vue";
import FirstScene from "./views/First/FirstScene.vue";
import SecondScene from "./views/Second/SecondScene.vue";

export default {
  name: "App",
  components: { DesktopScene, MainPage, FirstScene, SecondScene },
  data() {
    return {
      mobile: true,
      desktop: false,
      showFirst: false,
      showSecond: false,
      isPlaying: true,
    };
  },
  methods: {
    ToFirstScene() {
      this.mobile = false;
      this.showFirst = true;
    },
    ToSecondScene() {
      this.showFirst = false;
      this.showSecond = true;
    },

    leave(event) {
      event.preventDefault();
      event.returnValue = "";
    },
    checkMobile() {
      if (
        /iP(hone|od|ad)|Android|BlackBerry|IEMobile|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune|Lumia/g.test(
          navigator.userAgent
        )
      ) {
        this.device = "mobile";
      } else {
        this.device = "etc";
      }
      console.log(this.device);
    },
    toggleSound() {
      this.isPlaying = !this.isPlaying;
    },
  },
  created() {
    this.checkMobile();
    if (this.device === "mobile") {
      this.mobile = true;
      this.desktop = false;
    } else {
      this.mobile = false;
      this.desktop = true;
    }
  },
  mounted() {
    window.addEventListener("beforeunload", this.leave);
  },

  beforeUnmount() {
    window.removeEventListener("beforeunload", this.leave);
  },
};
</script>
<style>
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}
body {
  line-height: 1;
}
ol,
ul {
  list-style: none;
}
blockquote,
q {
  quotes: none;
}
blockquote:before,
blockquote:after,
q:before,
q:after {
  content: "";
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  background-color: #151515;
  position: relative;
}

body,
html {
  margin: 0;
  padding: 0;
}
* {
  box-sizing: border-box;
}

@font-face {
  font-family: korFontLight;
  src: url(./assets/fonts/SCDreamExtraLight.otf);
}
@font-face {
  font-family: korFontRegular;
  src: url(./assets/fonts/SCDreamRegular.otf);
}
@font-face {
  font-family: korFont2;
  src: url(./assets/fonts/micegothic.ttf);
}

.page-enter-active,
.page-leave-active {
  transition: opacity 0.5s;
}
.page-enter,
.page-leave-to {
  opacity: 0;
}
</style>
