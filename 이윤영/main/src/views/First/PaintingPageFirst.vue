<template>
  <transition name="first">
    <div class="painting-page">
      <div class="painting-content">
        <div id="canvas_Wrapper">
          <canvas ref="jsCanvas" id="jsCanvas" class="canvas"></canvas>
        </div>
        <div class="controls">
          <div class="controls-container">
            <div class="controls__range">
              <input
                type="range"
                id="jsRange"
                min="0.1"
                max="5"
                step="0.1"
                v-model="size"
              />
            </div>
            <div class="controls__btns">
              <button
                type="button"
                class="reset-btn"
                id="jsReset"
                @click="resetCanvas"
              >
                <font-awesome-icon
                  class="reset-icon"
                  icon="fa-solid fa-rotate-right"
                />
              </button>
            </div>
            <button
              v-if="isPlaying"
              @click="$emit('toggleSound1')"
              class="sound-btn1"
            >
              <img class="icon-sound1" src="../../assets/images/volumeon.png" />
            </button>
            <button v-else @click="$emit('toggleSound1')" class="sound-btn1">
              <img
                class="icon-sound1"
                src="../../assets/images/volumeoff.png"
              />
            </button>
          </div>
          <div class="controls__colors" id="jsColors" ref="jsColors">
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #2c2c2c"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: white"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #ff3b30"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #ff9500"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #ffcc00"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #4cd963"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #5ac8fa"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #0579ff"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #5856d6"
            ></div>
            <div
              class="controls__color jsColor"
              @click="handleColorClick"
              style="background-color: #884d1d"
            ></div>
          </div>
        </div>
      </div>
      <button type="button-next" @click="toggleModal" class="button-next">
        NEXT
      </button>
    </div>
  </transition>

  <transition name="zoom">
    <div v-show="showModal" class="overlay">
      <div v-show="showModal" class="modal-container">
        <div class="modal-content">
          <p>
            ????????? ????????? <br />
            ?????????????????????????
          </p>
        </div>
        <div class="modal-btn-grid">
          <button @click="toggleModal" class="modal-btn left">??????</button>
          <button @click="onClickSecond" class="modal-btn">??????</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "PaintingPageFirst",
  components: {},
  props: ["isPlaying"],
  data() {
    return {
      ctx: null,
      painting: false,
      size: 2.5,
      color: "#2c2c2c",
      showModal: false,
      device: null,
    };
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    }, //?????? ?????? ???
    onClickSecond() {
      this.$emit("turnOffSound");

      var canvasContents = this.$refs.jsCanvas.toDataURL();
      var cookie_userid = this.$cookies.get("userid");
      var file = JSON.stringify({ 'image': canvasContents, 'userid':cookie_userid });
      fetch("http://localhost:3000/tree/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: file,
      })
        .then((response) => response.json())
        .then((data) => console.log(data));

      this.$emit("ToSecondScene");
    }, //????????? ?????? ???????????? ???????????? ??????
    onMouseMove(event) {
      const x = event.offsetX;
      const y = event.offsetY;

      if (!this.painting) {
        this.ctx.beginPath();
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y); // lineTo??? path??? ?????? ???????????? ?????? ???????????? ?????? ????????? ???
        this.ctx.stroke();
      }
    },
    onMouseDown() {
      this.painting = true;
    },
    onMouseUp() {
      this.painting = false;
    },
    stopPainting() {
      this.painting = false;
    },
    checkMobile() {
      if (
        /iP(hone|od)|Android.*Mobile|BlackBerry|IEMobile|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune|Lumia/g.test(
          navigator.userAgent
        )
      ) {
        this.device = "mobile";
      } else {
        this.device = "etc";
      }
    },
    resetCanvas() {
      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.clearRect(0, 0, 700, 700);
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);
    },
    getTouchPos(e) {
      return {
        x: e.targetTouches[0].clientX - e.target.offsetLeft,
        y:
          e.targetTouches[0].clientY -
          e.target.offsetTop +
          document.documentElement.scrollTop,
      };
    },
    touchStart(e) {
      e.preventDefault();
      this.painting = true;
      const { x, y } = this.getTouchPos(e);
      this.startX = x;
      this.startY = y;
    },
    touchMove(e) {
      if (!this.painting) return;
      const { x, y } = this.getTouchPos(e);
      this.ctx.lineTo(x, y);
      this.ctx.stroke();
      this.startX = x;
      this.startY = y;
    },
    touchEnd(e) {
      if (!this.painting) return;
      this.ctx.beginPath();
      const { x, y } = this.getTouchPos(e);
      this.startX = x;
      this.startY = y;
      this.ctx.arc(
        this.startX,
        this.startY,
        this.ctx.lineWidth / 2,
        0,
        2 * Math.PI
      );
      this.ctx.fillStyle = this.ctx.strokeStyle;
      this.ctx.fill();
      this.painting = false;
    },
    handleColorClick(e) {
      this.color = e.target.style.backgroundColor;
      this.ctx.strokeStyle = this.color;
    },
  },

  mounted() {
    this.checkMobile();
    // this.ctx = this.$refs.jsCanvas.getContext("2d");
    // this.ctx.fillStyle = "white";
    // this.ctx.fillRect(0, 0, 700, 700);

    // this.ctx.strokeStyle = "#2c2c2c";
    // this.ctx.fillStyle = "#2c2c2c";
    // this.ctx.lineWidth = 2.5;

    // this.$refs.jsCanvas.addEventListener("mousemove", this.onMouseMove);
    // this.$refs.jsCanvas.addEventListener("mousedown", this.onMouseDown);
    // this.$refs.jsCanvas.addEventListener("mouseup", this.onMouseUp);

    if (this.device === "mobile") {
      // ????????? ??????
      this.$refs.jsCanvas.width = 310;
      this.$refs.jsCanvas.height = 465.3;

      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);

      this.ctx.strokeStyle = "#2c2c2c";
      this.ctx.fillStyle = "#2c2c2c";
      this.ctx.lineWidth = 2.5;

      this.$refs.jsCanvas.addEventListener("touchmove", this.touchMove, false);
      this.$refs.jsCanvas.addEventListener(
        "touchstart",
        this.touchStart,
        false
      );
      this.$refs.jsCanvas.addEventListener("touchend", this.touchEnd, false);
    } else {
      this.$refs.jsCanvas.width = 700;
      this.$refs.jsCanvas.height = 700;

      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);

      this.ctx.strokeStyle = "#2c2c2c";
      this.ctx.fillStyle = "#2c2c2c";
      this.ctx.lineWidth = 2.5;

      this.$refs.jsCanvas.addEventListener("mousemove", this.onMouseMove);
      this.$refs.jsCanvas.addEventListener("mousedown", this.onMouseDown);
      this.$refs.jsCanvas.addEventListener("mouseup", this.onMouseUp);

      //??????????????? ????????? ????????? ?????????????????? ?????????, PC??? ?????? ????????? ?????? ???????????????.
      this.$refs.jsCanvas.addEventListener("touchmove", this.touchMove, false);
      this.$refs.jsCanvas.addEventListener(
        "touchstart",
        this.touchStart,
        false
      );
      this.$refs.jsCanvas.addEventListener("touchend", this.touchEnd, false);
    }
  },

  // size ????????? ???????????? ????????? ????????? ???????????? ?????? ????????? ?????? ????????? ??? ?????? ??????
  watch: {
    size() {
      this.ctx.lineWidth = this.size;
    },
    color() {
      this.ctx.strokeStyle = this.color;
    },
  },
};
</script>
<style scoped>
/* http://meyerweb.com/eric/tools/css/reset/
   v2.0 | 20110126
   License: none (public domain)
*/
/*
    ?????????????????? ?????? ????????? ????????? ?????? ?????? ????????? ?????? ????????? ???????????? ??? ?????????
    ??????????????? ?????? ????????? ?????? ??? ??????.
 */
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}
body {
  line-height: 1;
}
ol,
ul {
  list-style: none;
}
blockquote,
q {
  quotes: none;
}
blockquote:before,
blockquote:after,
q:before,
q:after {
  content: "";
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
body {
  background-color: #f6f9fc;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px 0px;
}
.painting-page {
  height: calc(var(--vh, 1vh) * 100);
  position: relative;
  background-color: #121212;
}
.painting-content {
  padding-top: 30px;
}
.canvas {
  width: 700px;
  height: 700px;
  background-color: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}

.controls {
  margin-top: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.controls-container {
  display: flex;
  flex-direction: row;
}

.controls .controls__colors {
  display: flex;
}

.controls__colors .controls__color {
  width: 50px;
  height: 50px;
  border-radius: 25px;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}
.controls .controls__btns {
  margin-bottom: 30px;
}

.controls__btns button {
  all: unset;
  cursor: pointer;
  text-align: center;
  padding-left: 10px;
}

.controls__btns button:active {
  transform: scale(0.98);
}

.controls .controls__range {
  margin-bottom: 30px;
}
html {
  cursor: url("../../assets/images/cursor.png") 0 32, auto;
}
.sound-btn1 {
  color: #ffffff;
  border: none;
  padding: 0;
  display: inline-block;
  background: none;
  margin-top: -10px;
  padding-left: 5px;
}
.icon-sound1 {
  height: 40px;
  color: #fff;
}
.button-next {
  font-family: korFont2;
  font-size: 30px;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  cursor: pointer;
  outline: inherit;
  width: 80px;
  top: 13px;
}
.reset-btn {
  border: none;
  padding: 0;
  margin: 0;
  display: inline-block;
  background: transparent;
}
.reset-icon {
  color: #ffffff;
  height: 30px;
}
.overlay {
  position: fixed; /* Positioning and size */
  top: 0;
  left: 0;
  width: 100vw;
  height: 100%;
}
.modal-container {
  display: inline-block;
  position: fixed;
  width: 250px;
  background-color: #fff;
  border-radius: 10px;
  text-align: center;
  color: #000;
  font-family: korFont2;
  top: 40%;
  left: 0;
  right: 0;
  margin-left: auto;
  margin-right: auto;
  -webkit-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  -moz-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.3);
}
.modal-container p {
  margin: 30px;
}
.modal-content {
  border-bottom: 1px solid #d0d0d0;
  line-height: 1.5;
}
.modal-btn-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  overflow: hidden;
}
.modal-btn {
  border-radius: 0 0 10px 0;
  color: #5490ff;
  background-color: #fff;
  border: 0;
  font-size: 1rem;
  cursor: pointer;
  outline: none;
  min-height: 50px;
  font-weight: 1000;
}
.modal-btn.left {
  border-radius: 0 0 0 10px;
  border-right: 1px solid #d0d0d0;
}

.results-data {
  height: calc(var(--vh, 1vh) * 100);
}

.zoom-enter-active,
.zoom-leave-active {
  animation-duration: 0.21s;
  animation-fill-mode: both;
  animation-name: zoom;
}
.zoom-leave-active {
  animation-direction: reverse;
}
@keyframes zoom {
  from {
    opacity: 0;
    transform: scale3d(1.1, 1.1, 1.1);
  }
  100% {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}
/* ????????? ?????????*/
@media screen and (max-width: 450px) {
  body {
    align-items: center;
    background-color: #333333;
  }
  .canvas {
    width: 310px;
    height: 465.3px;
  }
  .controls {
    margin-top: 10px;
  }
  .controls .controls__range {
    margin-bottom: 10px;
  }
  .controls .controls__btns {
    margin-bottom: 10px;
  }
  .controls .controls__colors {
    display: flex;
    width: 90%;
  }
  .controls__colors .controls__color {
    width: 36px;
    height: 40px;
    border-radius: 0px;
  }
}
</style>
