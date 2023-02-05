<template>
  <transition name="pre">
    <div v-if="showMain" class="prePage">
      <div class="text1">
        <p>더욱 깊이 있는 경험을 원하신다면 소리 볼륨을 높여주세요</p>
        <font-awesome-icon icon="fa-solid fa-headphones" />
      </div>
      <p @click="showMain = !showMain" class="start-btn">START</p>
    </div>
  </transition>
</template>

<script>
export default {
  name: "PreStartPage",
};
</script>

<style>
.prePage {
  background-color: #151515;
}
</style>
