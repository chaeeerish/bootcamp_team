<template>
  <div v-if="secondNext1" class="second-scene">
    <div class="first-text">
      <transition name="fade">
        <p class="texts" v-if="timedTrigger1.Trigger5">
          그리고 당신은 또 다시 <br />
          깊은 상상에 빠집니다.
        </p>
      </transition>
      <transition name="fade">
        <p class="texts" v-if="timedTrigger1.Trigger6">
          상상 속 당신이 본 집을 그려주세요.
        </p>
      </transition>
    </div>
    <transition enter-active-class="animate__animated animate__flash">
      <p v-if="timedTrigger1.Trigger7" class="touch-text">화면을 터치하세요</p>
    </transition>

    <div
      v-if="timedTrigger1.Trigger7"
      @click="moveToSecondPaint"
      class="touch-screen"
    ></div>
  </div>
  <transition enter-active-class="animate__animated animate__fadeIn">
    <PaintingPageSecond v-if="secondPaint"></PaintingPageSecond>
  </transition>
</template>

<script>
import { ref } from "vue";
import PaintingPageSecond from "../components/PaintingPageSecond.vue";
export default {
  name: "SecondSceneNext",
  components: { PaintingPageSecond },
  methods: {
    moveToSecondPaint() {
      this.secondNext1 = !this.secondNext1;
      this.secondPaint = !this.secondPaint;
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
    return { secondNext1: true, secondPaint: false };
  },
};
</script>

<style></style>
