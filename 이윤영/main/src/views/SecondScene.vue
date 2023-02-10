<template>
  <transition>
    <div v-if="showFirstScene" class="second-scene">
      <div class="second-text">
        <transition name="fade">
          <p v-if="timedTrigger.Trigger1">
            시간이 지나고 당신은 <br />자리에서 일어났습니다.
          </p>
        </transition>
        <transition name="fade">
          <p v-if="timedTrigger.Trigger2">
            책상 앞에 앉아 창문 밖을 보니 <br />날이 벌써 어두워졌습니다.
          </p>
        </transition>
        <transition name="fade">
          <p v-if="timedTrigger.Trigger3">
            창문 밖에는 귀뚜라미 소리가 들립니다.
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
.second-scene {
  height: 100vh;
  background-image: url("../assets/images/example.jpg");
  color: #000;
  font-size: 18.5px;
  font-family: korFont2;
  position: relative;
  line-height: 1.5;
}
.second-text {
  display: inline-block;

  margin-top: 150px;
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
  margin-top: -411px;
  opacity: 30%;
}
p {
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
