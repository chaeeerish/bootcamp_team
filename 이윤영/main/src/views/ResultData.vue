<template>
  <div class="results-data">
    <h1>Results</h1>
    <button>Click here</button>
    <div v-if="isShow" class="modal-container">
      <p>그림을 이대로 제출하시겠습니까?</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultData",
  components: {},
  data() {
    return {};
  },
  methods: {},
  setup() {},
};
</script>

<style>
.results-data {
  height: calc(var(--vh, 1vh) * 100);
}
h1 {
  margin: 0;
  padding: 0;
}
</style>
