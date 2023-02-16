<template>
  <div v-if="showMain" class="main">
    <div class="title">
      <p class="texts">마음 스케치</p>
      <p class="texts">
        내가 그린 그림으로 <br />
        확인해보는 심리 테스트
      </p>
    </div>
    <button
      type="button"
      @click="toggleMain"
      @ToFirstScene="$emit('ToFirstScene')"
      class="start-btn"
    >
      START
    </button>
  </div>

  <transition name="main">
    <PreStartPage
      v-bind:isPlaying="isPlaying"
      @ToFirstScene="ToFirstScene"
      @toggleSound="toggleSound"
      v-if="showPre"
    ></PreStartPage>
  </transition>
</template>

<script>
import PreStartPage from "./PreStartPage.vue";
export default {
  name: "MainPage",
  components: { PreStartPage },
  props: ["isPlaying"],
  data() {
    return {
      current: {},
      index: 0,
      showMain: true,
      showPre: false,
      sounds: [
        {
          title: "MainSound",
          src: require("../../assets/audio/start.mp3"),
        },
      ],
      player: new Audio(),
    };
  },
  created() {
    this.current = this.sounds[this.index];
    this.player.src = this.current.src;
  },
  methods: {
    ToFirstScene() {
      this.$emit("ToFirstScene");
    },
    toggleMain() {
      this.player.play();
      this.showMain = !this.showMain;
      this.showPre = !this.showPre;
    },
    toggleSound() {
      this.$emit("toggleSound");
    },
  },
  setup() {
    const setScreenSize = function () {
      let vh = window.innerHeight * 0.01;
      document.documentElement.style.setProperty("--vh", `${vh}px`); //핸드폰 화면에 맞게 vh 새로 설정
    };
    setScreenSize();
    window.addEventListener("resize", () => setScreenSize());
  },
};
</script>

<style>
.main {
  background-image: url("../../assets/images/example.jpg");
  height: calc(var(--vh, 1vh) * 100);
  color: #3c3c3c;
  overflow: hidden;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.title {
  text-align: left;
  display: inline-block;
  padding-right: 20px;
  font-size: 30px;
  font-family: korFontRegular;
  margin-top: 50px;
  font-weight: 1000;
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  top: 15%;
}
.title :nth-child(2) {
  font-size: 20px;
  font-family: korFontLight;
}
.start-btn {
  font-family: korFont2;
  font-size: 30px;
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  bottom: 10%;
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  cursor: pointer;
  outline: inherit;
}
.main-enter-from {
  opacity: 0;
  transform: translateY(500px);
}
.main-enter-active {
  transition: all 1s ease-out;
}
.main-leave-to {
  opacity: 0;
  transform: translateY(-500px);
}
.main-leave-active {
  transition: all 1s ease-in;
}
</style>
