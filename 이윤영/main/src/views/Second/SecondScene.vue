<template>
  <transition name="first">
    <div v-if="showSecondScene" class="second-scene">
      <button v-if="isPlaying" @click="toggleSound" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeon.png" />
      </button>
      <button v-else @click="toggleSound" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeoff.png" />
      </button>
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger1">
            시간이 지나고 당신은 <br />자리에서 일어났습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger2">
            책상 앞에 앉아 창문 밖을 보니 <br />날이 벌써 어두워졌습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger.Trigger3">
            창문 밖에는 귀뚜라미 <br />소리가 들립니다.
          </p>
        </transition>
      </div>
      <transition enter-active-class="animate__animated animate__flash">
        <p v-if="timedTrigger.Trigger4" class="touch-text">화면을 터치하세요</p>
      </transition>
      <div
        v-if="timedTrigger.Trigger4"
        @click="moveToSecondNext"
        class="touch-screen"
      ></div>
    </div>
  </transition>

  <SecondSceneNext
    v-if="secondNext"
    v-bind:isPlaying="isPlaying"
    @toggleSound="toggleSound"
    @turnOffSound="turnOffSound"
  ></SecondSceneNext>
</template>

<script>
import { ref } from "vue";
import SecondSceneNext from "./SecondSceneNext.vue";
export default {
  name: "FirstScene",
  components: { SecondSceneNext },
  props: ["isPlaying"],
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
    if (this.isPlaying === true) {
      setTimeout(() => {
        this.player.play();
      }, 2000); //2초 후에 오디오 실행
    }
  },
  data() {
    return {
      secondNext: false,
      showSecondScene: true,
      current: {},
      index: 0,
      sounds: [
        {
          title: "MainSound",
          src: require("../../assets/audio/night.mp3"),
        },
      ],
      player: new Audio(),
    };
  },
  methods: {
    toggleSound() {
      this.$emit("toggleSound");
      if (this.isPlaying === true) {
        this.player.pause();
      } else if (this.isPlaying === false) {
        this.player.play();
      }
    }, //음소거
    moveToSecondNext() {
      this.showSecondScene = false;
      this.secondNext = true;
    },
    turnOffSound() {
      this.player.pause();
    },
  },
};
</script>

<style>
.second-scene {
  height: calc(var(--vh, 1vh) * 100);
  width: 100%;
  background-image: url("../../assets/images/night2.jpg");
  color: #ffffff;
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
.second-text {
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
  font-size: 17px;
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

.first-enter-from {
  opacity: 0;
}
.first-enter-to {
  opacity: 1;
}
.first-enter-active {
  transition: all 1s ease;
}
.first-leave-from {
  opacity: 1;
}
.first-leave-to {
  opacity: 0;
}
.first-leave-active {
  transition: all 1s ease;
}
</style>
