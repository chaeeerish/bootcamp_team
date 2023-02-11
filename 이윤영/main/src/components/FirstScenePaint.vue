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
    onClickSecond() {
      this.$router.push({ name: "second" });
    },
  },
};
</script>

<style>
.first-scene-paint {
  height: calc(var(--vh, 1vh) * 100);
  position: relative;
  background-color: #2b2b2b;
}
</style>
