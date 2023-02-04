<template>
  <nav><router-link to="/"></router-link></nav>
  <router-view />
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  background-color: #2c3e50;
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
