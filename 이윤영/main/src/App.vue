<template>
  <nav><router-link to="/"></router-link></nav>
  <transition
    leave-active-class="animate__animated animate__fadeOut animate__slower"
  >
    <router-view @clickedNext1="onClickTransition" v-if="showMainPage" />
  </transition>
  <transition
    enter-active-class="animate__animated animate__fadeIn animate__slower"
  >
    <FirstScene v-if="showFirst"></FirstScene>
  </transition>
</template>

<script>
import FirstScene from "./views/FirstScene.vue";

export default {
  name: "App",
  components: { FirstScene },
  data() {
    return { showMainPage: true, showFirst: false };
  },
  methods: {
    onClickTransition() {
      this.showMainPage = !this.showMainPage;
      this.showFirst = !this.showFirst;
    },
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  background-color: #151515;
  position: relative;
}

body {
  margin: 0px;
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
</style>
