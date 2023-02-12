<template>
  <div>

      <div id="canvas_Wrapper">
          <canvas ref="jsCanvas" id="jsCanvas" class="canvas" ></canvas>
      </div>
      <div class="controls">
          <div class="controls__range">
              <input type="range" id="jsRange" min="0.1" max="5" step="0.1" v-model="size"/>
          </div>
          <div class="controls__btns">
              <button id="jsSave" @click="handleSaveClick">Save</button>
              <button id="jsReset" @click="resetCanvas">Reset</button>
          </div>
          <div class="controls__colors" id="jsColors" ref="jsColors">
              <div
              class="controls__color jsColor " @click="handleColorClick"
              style="background-color:#2c2c2c"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:white"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#FF3B30"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#FF9500"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#FFCC00"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#4CD963"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#5AC8FA"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#0579FF"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#5856D6"
              ></div>
              <div
              class="controls__color jsColor" @click="handleColorClick"
              style="background-color:#884d1d"
              ></div>

          </div>
      </div>
  </div>
  </template>
  <script>

  export default {

      components: {},
      data() {
          return {
            ctx : null,
            painting : false,
            isMobile : false,
            size : 2.5,
            color : "#2c2c2c"




          }
      },
      setup() {},
      created() {
        this.checkMobile();
        const colors = this.$refs.jsColors;

      },
      mounted() {
        //모바일
        if(this.isMobile){
          this.$refs.jsCanvas.width=310;
          this.$refs.jsCanvas.height=465.3;

          this.ctx = this.$refs.jsCanvas.getContext('2d');
          this.ctx.fillStyle = "white";
          this.ctx.fillRect(0, 0, 700, 700);


          this.ctx.strokeStyle = "#2c2c2c";
          this.ctx.fillStyle = "#2c2c2c";
          this.ctx.lineWidth = 2.5;

          this.$refs.jsCanvas.addEventListener("touchmove", this.touchMove, false);
          this.$refs.jsCanvas.addEventListener("touchstart", this.touchStart, false);
          this.$refs.jsCanvas.addEventListener("touchend", this.touchEnd, false);
         }

        else{
          //PC 버전
          this.$refs.jsCanvas.width=700;
          this.$refs.jsCanvas.height=700;

          this.ctx = this.$refs.jsCanvas.getContext('2d');
          this.ctx.fillStyle = "white";
          this.ctx.fillRect(0, 0, 700, 700);


          this.ctx.strokeStyle = "#2c2c2c";
          this.ctx.fillStyle = "#2c2c2c";
          this.ctx.lineWidth = 2.5;

          this.$refs.jsCanvas.addEventListener("mousemove", this.onMouseMove);
          this.$refs.jsCanvas.addEventListener("mousedown", this.onMouseDown);
          this.$refs.jsCanvas.addEventListener("mouseup", this.onMouseUp);
        }



      },
      unmounted() {},
      methods:{
      onMouseMove(event){
          const x = event.offsetX;
          const y = event.offsetY;


          if (!this.painting){
              this.ctx.beginPath();
              this.ctx.moveTo(x,y);
          }else {
              this.ctx.lineTo(x, y); // lineTo는 path의 이전 위치에서 지금 위치까지 선을 만드는 것
              this.ctx.stroke();
          }

      },
      onMouseDown(event){
          this.painting = true;
      },
      onMouseUp(event){
          this.painting = false;
      },
      stopPainting(){
          this.painting = false;
      },
      checkMobile(){
          if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
              this.isMobile = true;
              // this.$refs.jsCanvas.width=700;
              // this.$refs.jsCanvas.height=700;

          }else{
              this.isMobile = false;
              // this.$refs.jsCanvas.style.width=700;
              // this.$refs.jsCanvas.style.height=700;
          }
      },
      resetCanvas(){
        this.ctx = this.$refs.jsCanvas.getContext('2d');
        this.ctx.clearRect(0, 0, 700, 700);
        this.ctx.fillStyle = "white";
        this.ctx.fillRect(0, 0, 700, 700);
      },
      getTouchPos(e) {
        return {
            x: (e.targetTouches[0].clientX - e.target.offsetLeft),
            y: (e.targetTouches[0].clientY - e.target.offsetTop + document.documentElement.scrollTop)
        }
      },
      touchStart(e) {
          e.preventDefault();
          this.painting = true;
          const { x, y } = this.getTouchPos(e);
          this.startX = x;
          this.startY = y;
      },
      touchMove(e) {
          if(!this.painting) return;
          const { x, y } = this.getTouchPos(e);
          this.ctx.lineTo(x, y);
          this.ctx.stroke();
          this.startX = x;
          this.startY = y;
      },
      touchEnd(e) {
      if(!this.painting) return;
          this.ctx.beginPath();
          const { x, y } = this.getTouchPos(e);
          this.startX = x;
          this.startY = y;
          this.ctx.arc(this.startX, this.startY, this.ctx.lineWidth/2, 0, 2*Math.PI);
          this.ctx.fillStyle = this.ctx.strokeStyle;
          this.ctx.fill();
          this.painting = false;
      },
      handleColorClick(e){
        this.color = e.target.style.backgroundColor;
        this.ctx.strokeStyle = this.color;
      },
      handleSaveClick() {
      const image = this.$refs.jsCanvas.toDataURL();
      const link = document.createElement("a");
      link.href = image;
      link.download = "drawImage";
      link.click();
      }


      },
      // size 변경을 감지하면 양방향 데이터 바인딩을 통해 사이즈 변경 값으로 선 굵기 변경
      watch: {
              size(){
                this.ctx.lineWidth = this.size;
              },
              color(){
                this.ctx.strokeStyle = this.color;
              }
          }

  }

  </script>
  <style>
  /* http://meyerweb.com/eric/tools/css/reset/
     v2.0 | 20110126
     License: none (public domain)
  */
  /*
      브라우저마다 기존 값들이 달라서 내가 만든 화면과 다른 화면이 만들어질 수 있어서
      설정값들을 전부 초기화 하는 것 같음.
   */
   html, body, div, span, applet, object, iframe,
  h1, h2, h3, h4, h5, h6, p, blockquote, pre,
  a, abbr, acronym, address, big, cite, code,
  del, dfn, em, img, ins, kbd, q, s, samp,
  small, strike, strong, sub, sup, tt, var,
  b, u, i, center,
  dl, dt, dd, ol, ul, li,
  fieldset, form, label, legend,
  table, caption, tbody, tfoot, thead, tr, th, td,
  article, aside, canvas, details, embed,
  figure, figcaption, footer, header, hgroup,
  menu, nav, output, ruby, section, summary,
  time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
  }
  /* HTML5 display-role reset for older browsers */
  article, aside, details, figcaption, figure,
  footer, header, hgroup, menu, nav, section {
    display: block;
  }
  body {
    line-height: 1;
  }
  ol, ul {
    list-style: none;
  }
  blockquote, q {
    quotes: none;
  }
  blockquote:before, blockquote:after,
  q:before, q:after {
    content: '';
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
    background-color: white;
    padding: 5px 0px;
    width: 80px;
    text-align: center;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
    border: 2px solid rgba(0, 0, 0, 0.2);
    color: rgba(0, 0, 0, 0.7);
    text-transform: uppercase;
    font-weight: 800;
    font-size: 12px;
  }

  .controls__btns  button:active  {
    transform: scale(0.98);
  }

  .controls .controls__range {
    margin-bottom: 30px;
  }
  html {
    cursor: url(../assets/cursor.png) 0 32, auto;
  }

  /* 핸드폰 사이즈*/
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