<template>
  <div class="first-scene">
    <div class="first-text">
      <p v-if="timedTrigger.Trigger1">당신은 깊은 잠에서 깨어났습니다.</p>
      <p v-if="timedTrigger.Trigger2">눈 앞에는 벽난로가 있습니다.</p>
      <p v-if="timedTrigger.Trigger3">
        벽 난로에는 장작이 타고 있으며 <br />당신의 몸을 따듯하게 녹여 줍니다.
      </p>
    </div>
    <p v-if="timedTrigger.Trigger4" class="touch-text">화면을 터치하세요</p>
    <div v-if="timedTrigger.Trigger4" class="touch-screen"></div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  name: "FirstScene",
  components: {},
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
    return {};
  },
};
</script>

<style>
.first-scene {
  height: 100vh;
  background-image: url("../assets/images/fireplace.png");
  color: #f2f2f2;
  font-size: 18px;
  font-family: korFont2;
  position: relative;
}
.first-text {
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
  font-size: 19px;
}
.touch-screen {
  height: 100vh;
  background-color: white;
  z-index: 1;
  position: absolute;
}
p {
  margin-top: 25px;
}
</style>
