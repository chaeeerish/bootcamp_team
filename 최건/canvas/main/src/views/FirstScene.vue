<template>
  <transition leave-active-class="animate__animated animate__fadeOut">
    <div v-if="showFirstScene" class="first-scene">
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger1">
            당신은 깊은 잠에서 깨어났습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger2">
            눈 앞에는 벽난로가 있습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger3">
            벽 난로에는 장작이 타고 있으며 <br />당신의 몸을 따듯하게 녹여
            줍니다.
          </p>
        </transition>
      </div>
      <transition enter-active-class="animate__animated animate__flash">
        <p v-if="timedTrigger.Trigger4" class="touch-text">화면을 터치하세요</p>
      </transition>
      <div
        v-if="timedTrigger.Trigger4"
        @click="moveToFirstNext"
        class="touch-screen"
      ></div>
    </div>
  </transition>
  <transition enter-active-class="animate__animated animate__fadeIn">
    <FirstSceneNext v-if="firstNext"></FirstSceneNext>
  </transition>
</template>

<script>
import { ref } from "vue";
import FirstSceneNext from "../components/FirstSceneNext.vue";
export default {
  name: "FirstScene",
  components: { FirstSceneNext },
  setup() {
    const timedTrigger = ref({
      Trigger1: false,
      Trigger2: false,
      Trigger3: false,
      Trigger4: false,
    });
    setTimeout(() => {
      timedTrigger.value.Trigger1 = true;
    }, 1000);
    setTimeout(() => {
      timedTrigger.value.Trigger2 = true;
    }, 3000);
    setTimeout(() => {
      timedTrigger.value.Trigger3 = true;
    }, 5000);
    setTimeout(() => {
      timedTrigger.value.Trigger4 = true;
    }, 7000);
    return { timedTrigger };
  },
  data() {
    return { firstNext: false, showFirstScene: true };
  },
  methods: {
    moveToFirstNext() {
      this.showFirstScene = !this.showFirstScene;
      this.firstNext = !this.firstNext;
    },
  },
};
</script>

<style>
.first-scene {
  height: calc(var(--vh, 1vh) * 100);
  width: 100%;
  background-image: url("../assets/images/example.jpg");
  color: #000;
  font-size: 18.5px;
  font-family: korFont2;
  position: relative;
  line-height: 1.5;
  overflow: hidden;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.first-text {
  display: inline-block;

  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  top: 20%;
}
.touch-text {
  color: #dededeb9;
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  bottom: 10%;
  font-size: 17px;
}
.touch-screen {
  height: 100vh;
  background-color: white;
  opacity: 30%;
}
.texts {
  margin-top: 50px;
}
.fade-enter-from {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
.fade-enter-active {
  transition: all 1.5s ease;
}
.animate__animated.animate__flash {
  --animate-duration: 3.5s;
  --animate-repeat: 3;
}
.animate__animated.animate__fadeIn {
  --animate-duration: 3s;
}
</style>
