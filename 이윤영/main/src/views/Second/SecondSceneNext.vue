<template>
  <transition name="first">
    <div v-if="secondNext1" class="second-scene">
      <button v-if="isPlaying" @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeon.png" />
      </button>
      <button v-else @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeoff.png" />
      </button>
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger5">
            그리고 당신은 또 다시 <br />
            깊은 상상에 빠져듭니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger6">
            상상 속 당신이 본<br />
            집을 그려주세요.
          </p>
        </transition>
      </div>
      <transition enter-active-class="animate__animated animate__flash">
        <p v-if="timedTrigger1.Trigger7" class="touch-text">
          화면을 터치하세요
        </p>
      </transition>

      <div
        v-if="timedTrigger1.Trigger7"
        @click="moveToSecondPaint"
        class="touch-screen"
      ></div>
    </div>
  </transition>

  <PaintingPageSecond
    v-if="secondPaint"
    v-bind:isPlaying="isPlaying"
    @toggleSound1="toggleSound"
    @turnOffSound="turnOffSound"
  ></PaintingPageSecond>
</template>

<script>
import { ref } from "vue";
import PaintingPageSecond from "./PaintingPageSecond.vue";
export default {
  name: "SecondSceneNext",
  components: { PaintingPageSecond },
  props: ["isPlaying"],
  methods: {
    moveToSecondPaint() {
      this.secondNext1 = false;
      this.secondPaint = true;
    },
    toggleSound() {
      this.$emit("toggleSound");
    },
    turnOffSound() {
      this.$emit("turnOffSound");
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
