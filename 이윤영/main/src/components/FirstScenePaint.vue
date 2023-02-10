<template>
  <div class="first-scene-paint"></div>
  <button type="button" @click="onClickSecond" class="start-btn">NEXT</button>
</template>

<script>
export default {
  name: "FirstScenePaint",
  components: {},
  data() {
    return {};
  },
  methods: {
    onClickSecond() {},
  },
};
</script>

<style>
.first-scene-paint {
  height: 100vh;
  position: relative;
  background-color: #2b2b2b;
}
</style>
