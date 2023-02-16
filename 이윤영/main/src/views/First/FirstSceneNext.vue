<template>
  <transition name="first">
    <div v-if="firstNext1" class="first-scene">
      <button v-if="isPlaying" @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeon.png" />
      </button>
      <button v-else @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeoff.png" />
      </button>
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger5">
            그리고 당신은 깊은 <br />상상에 빠져듭니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger6">
            상상 속 당신이 본 <br />나무를 그려주세요.
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
        @click="moveToFirstPaint"
        class="touch-screen"
      ></div>
    </div>
  </transition>
  <PaintingPageFirst
    v-if="firstPaint"
    v-bind:isPlaying="isPlaying"
    @toggleSound1="toggleSound"
    @turnOffSound="turnOffSound"
    @ToSecondScene="ToSecondScene"
  ></PaintingPageFirst>
</template>

<script>
import { ref } from "vue";
import PaintingPageFirst from "./PaintingPageFirst.vue";

export default {
  name: "FirstSceneNext",
  components: { PaintingPageFirst },
  props: ["isPlaying"],
  methods: {
    ToSecondScene() {
      this.$emit("ToSecondScene");
    },
    toggleSound() {
      this.$emit("toggleSound");
    },
    moveToFirstPaint() {
      this.firstNext1 = false;
      this.firstPaint = true;
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
