<template>
  <transition>
    <div v-if="showFirstScene" class="first-scene">
      <button v-if="isPlaying" @click="toggleSound" class="sound-btn">
        <img class="icon-sound" src="../assets/images/volumeon.png" />
      </button>
      <button v-else @click="toggleSound" class="sound-btn">
        <img class="icon-sound" src="../assets/images/volumeoff.png" />
      </button>
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger1">
            당신은 깊은 잠에서 깨어났습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger2">
            눈 앞에는 벽난로가 있습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger3">
            벽 난로에는 장작이 타고 있으며 <br />당신의 몸을 따듯하게 녹여
            줍니다.
          </p>
        </transition>
      </div>
      <transition>
        <p v-if="timedTrigger.Trigger4" class="touch-text">화면을 터치하세요</p>
      </transition>
      <div
        v-if="timedTrigger.Trigger4"
        @click="moveToFirstNext"
        class="touch-screen"
      ></div>
    </div>
  </transition>
  <transition>
    <FirstSceneNext
      v-if="firstNext"
      v-bind:isPlaying="isPlaying"
      @toggleSound="toggleSound"
      @turnOffSound="turnOffSound"
    ></FirstSceneNext>
  </transition>
</template>

<script>
import { ref } from "vue";
import FirstSceneNext from "../components/FirstSceneNext.vue";
export default {
  name: "FirstScene",
  components: { FirstSceneNext },
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
  created() {
    this.current = this.sounds[this.index];
    this.player.src = this.current.src;
    this.player.loop = true;
    setTimeout(() => {
      this.player.play();
    }, 1000); //1초 후에 오디오 실행
  },
  data() {
    return {
      isPlaying: true,
      firstNext: false,
      showFirstScene: true,
      current: {},
      index: 0,
      sounds: [
        {
          title: "MainSound",
          src: require("../assets/audio/fireplace.mp3"),
        },
      ],
      player: new Audio(),
    };
  },
  methods: {
    toggleSound() {
      this.isPlaying = !this.isPlaying;
      if (this.isPlaying === !true) {
        this.player.pause();
      } else if (this.isPlaying === true) {
        this.player.play();
      }
    }, //음소거
    moveToFirstNext() {
      this.showFirstScene = !this.showFirstScene;
      this.firstNext = !this.firstNext;
    },
    turnOffSound() {
      this.player.pause();
    },
  },
};
</script>

<style>
.first-scene {
  height: calc(var(--vh, 1vh) * 100);
  width: 100%;
  background-image: url("../assets/images/fireplace.jpg");
  color: #000;
  font-size: 18.5px;
  font-family: korFont2;
  position: relative;
  line-height: 1.5;
  overflow: hidden;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.first-text {
  display: inline-block;

  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  top: 20%;
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
  font-size: 17px;
}
.touch-screen {
  height: 100vh;
  background-color: white;
  opacity: 30%;
}
.texts {
  margin-top: 50px;
}
.fade-enter-from {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
.fade-enter-active {
  transition: all 1.5s ease;
}
.animate__animated.animate__flash {
  --animate-duration: 3.5s;
  --animate-repeat: 3;
}
.animate__animated.animate__fadeIn {
  --animate-duration: 3s;
}
</style>
