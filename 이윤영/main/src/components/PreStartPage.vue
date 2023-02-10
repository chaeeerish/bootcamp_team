<template>
  <div class="prepage">
    <button class="sound-btn">
      <font-awesome-icon class="icon-sound" icon="fa-solid fa-music" />
    </button>
    <div class="text1">
      <p>
        ※ 몰입감 있는 경험을 <br />위해 소리를 높여주세요
        <font-awesome-icon icon="fa-solid fa-headphones" />
      </p>
    </div>
    <button type="button" @click="onClickNext" class="start-btn">NEXT</button>
  </div>
</template>

<script>
export default {
  name: "PreStartPage",
  methods: {
    onClickNext() {
      this.$router.push({ name: "first" });
    },
  },
};
</script>

<style>
.prepage {
  background-color: #151515;
  height: 100vh;
}
.text1 {
  text-align: left;
  display: inline-block;
  padding-right: 20px;
  font-size: 20px;
  font-family: korFont2;
  margin-top: 60%;
}
.next-btn {
  font-family: korFontLight;
  font-size: 30px;
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  bottom: 6%;
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  cursor: pointer;
  outline: inherit;
}
.sound-btn {
  color: #ffffff;
  border: none;
  padding: 0;
  display: inline-block;
  background: none;
  position: absolute;
  top: 3%;
  right: 5%;
}
.icon-sound {
  height: 30px;
}
</style>
