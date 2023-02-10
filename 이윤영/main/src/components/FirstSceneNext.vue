<template>
  <div v-if="firstNext1" class="first-scene-next">
    <div class="first-text">
      <transition name="fade">
        <p v-if="timedTrigger1.Trigger5">그리고 당신은 깊은 상상에 빠집니다.</p>
      </transition>
      <transition name="fade">
        <p v-if="timedTrigger1.Trigger6">
          상상 속 당신이 본 나무를 그려주세요.
        </p>
      </transition>
    </div>
    <transition enter-active-class="animate__animated animate__flash">
      <p v-if="timedTrigger1.Trigger7" class="touch-text">화면을 터치하세요</p>
    </transition>

    <div
      v-if="timedTrigger1.Trigger7"
      @click="moveToFirstPaint"
      class="touch-screen-two"
    ></div>
  </div>
  <transition enter-active-class="animate__animated animate__fadeIn">
    <FirstScenePaint v-if="firstPaint"></FirstScenePaint>
  </transition>
</template>

<script>
import { ref } from "vue";
import FirstScenePaint from "../components/FirstScenePaint.vue";
export default {
  name: "FirstSceneNext",
  components: { FirstScenePaint },
  methods: {
    moveToFirstPaint() {
      this.firstNext1 = !this.firstNext1;
      this.firstPaint = !this.firstPaint;
    },
  },
  setup() {
    const timedTrigger1 = ref({
      Trigger5: false,
      Trigger6: false,
      Trigger7: false,
    });
    setTimeout(() => {
      timedTrigger1.value.Trigger5 = true;
    }, 2000);
    setTimeout(() => {
      timedTrigger1.value.Trigger6 = true;
    }, 4000);
    setTimeout(() => {
      timedTrigger1.value.Trigger7 = true;
    }, 6000);
    return { timedTrigger1 };
  },
  data() {
    return { firstNext1: true, firstPaint: false };
  },
};
</script>

<style>
.first-scene-next {
  height: 100vh;
  background-image: url("../assets/images/example.jpg");
  color: #000;
  font-size: 18.5px;
  font-family: korFont2;
  position: relative;
  line-height: 1.5;
}
.touch-screen-two {
  height: 100vh;
  background-color: white;
  margin-top: -305px;
  opacity: 30%;
}
</style>
