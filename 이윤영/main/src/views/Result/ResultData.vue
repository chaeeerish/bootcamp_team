<template>
  <div class="results-data">
    <h1 class="userName">{{ name }}님의 결과입니다.</h1>
    <div class="first-result"></div>
    <p>{{ name }}님의 나무 그림</p>
    <img class="first-image" src="../../assets/images/window.png" />
    <p class="first-result-text">
      {{ firstResultText }}
    </p>
  </div>
  <div class="second-result"></div>
</template>

<script>
export default {
  name: "ResultData",
  props: ["data"],
  components: {},
  data() {
    return {
      name: "이겸희",
      firstResultText: `나무의 줄기가 얇은 것을 봤을때 현재 당신은 지친 상태에 있습니다. 나무의
      뿌리가 또한 땅 속에 밖혀있지 않고 밖으로 나와있는데, 이는 현재 휴식이
      필요하다는 것을 의미하며...`,
    };
  },
  methods: {},
  setup() {},
};
</script>

<style>
.results-data {
  height: calc(var(--vh, 1vh) * 100);
  display: inline-block;
  font-family: korFont2;
}
.userName {
  font-size: 25px;
  margin-top: 15%;
}
.first-result {
  margin-top: 50px;
}
.first-result:first-child {
  font-size: 15px;
}
.first-image {
  margin-top: 25px;
  width: 250px;
}
.first-result-text {
  width: 80%;
  margin: 50px auto;
}
</style>
