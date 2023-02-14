<template>
  <div v-if="firstNext1" class="first-scene">
    <div class="first-text">
      <transition name="fade">
        <p class="texts" v-if="timedTrigger1.Trigger5">
          그리고 당신은 깊은 상상에 빠집니다.
        </p>
      </transition>
      <transition name="fade">
        <p class="texts" v-if="timedTrigger1.Trigger6">
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
      class="touch-screen"
    ></div>
  </div>
  <transition enter-active-class="animate__animated animate__fadeIn">
    <PaintingPageFirst v-if="firstPaint"></PaintingPageFirst>
  </transition>
</template>

<script>
import { ref } from "vue";
import PaintingPageFirst from "../components/PaintingPageFirst.vue";

export default {
  name: "FirstSceneNext",
  components: { PaintingPageFirst },
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
/*
.first-scene-next {
  
}
*/
.touch-screen-two {
  height: 100vh;
  background-color: white;
  margin-top: -305px;
  opacity: 30%;
}
</style>
