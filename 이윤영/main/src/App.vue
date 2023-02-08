<template>
  <router-view @clickedNext1="onClickTransition" v-slot="{ Component }">
    <transition :key="$route.fullPath" name="route1" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>

<script>
export default {
  name: "App",
  components: {},
  data() {
    return {};
  },
  methods: {
    onClickTransition() {
      this.$router.push("/first");
    },
    leave(event) {
      event.preventDefault();
      event.returnValue = "";
    },
  },

  // created() {
  //   this.$watch(
  //     () => this.$route.params,
  //     () => {
  //       // WATCH FOR ROUTE CHANGES
  //     }
  //   );
  // },

  mounted() {
    window.addEventListener("beforeunload", this.leave);
  },

  beforeUnmount() {
    window.removeEventListener("beforeunload", this.leave);
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

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
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

/* route transition */
.route1-enter-from {
  opacity: 0;
}
.route1-enter-active {
  transition: all 3s ease-in;
}
.route1-leave-to {
  opacity: 0;
}
.route1-leave-active {
  transition: all 3s ease-in;
}
</style>
