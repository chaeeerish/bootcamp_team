<template>
  <div class="first-scene">
    <div class="first-text">
      <p>당신은 깊은 잠에서 깨어났습니다.</p>
      <p>눈 앞에는 벽난로가 있습니다.</p>
      <p>
        벽 난로에는 장작이 타고 있으며 <br />당신의 몸을 따듯하게 녹여 줍니다.
      </p>
    </div>
    <p class="touch-text">화면을 터치하세요</p>
    <div class="touch-screen"></div>
  </div>
</template>

<script>
export default {
  name: "FirstScene",
  components: {},
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
p {
  margin-top: 25px;
}
</style>
