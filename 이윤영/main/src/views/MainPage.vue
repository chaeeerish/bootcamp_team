<template>
  <transition name="fade">
    <div v-if="showMain" class="main">
      <div class="title">
        <p>내 그림, 그 속의 나</p>
        <p>
          내가 그린 그림으로 <br />
          확인해보는 심리 테스트
        </p>
      </div>
      <p @click="showMain = !showMain" class="start-btn">START</p>
    </div>
  </transition>

  <PreStartPage></PreStartPage>
</template>

<script>
import { ref } from "vue";
import PreStartPage from "./PreStartPage.vue";
export default {
  name: "MainPage",
  components: { PreStartPage },
  setup() {
    const showMain = ref(true);

    const triggerMain = () => {
      showMain.value = true;
      setTimeout(() => (showMain.value = false), 3000);
    };
    return { showMain, triggerMain };
  },
  data() {
    return {};
  },
};
</script>

<style>
.main {
  background-color: #8787ff;
  height: 100vh;
  color: #2c3e50;
}
.title {
  text-align: left;
  display: inline-block;
  padding-right: 20px;
  font-size: 30px;
  font-family: korFontRegular;
  margin-top: 50px;
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
}
</style>
