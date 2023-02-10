<template>
  <div class="second-scene-paint"></div>
  <button type="button" @click="onClickSecond" class="start-btn">NEXT</button>
</template>

<script>
export default {
  name: "SecondScenePaint",
  components: {},
  data() {
    return {};
  },
  methods: {
    onClickSecond() {
      this.$router.push({ name: "result" });
    },
  },
};
</script>

<style>
.second-scene-paint {
  height: 100vh;
  position: relative;
  background-color: #2b2b2b;
}
</style>
