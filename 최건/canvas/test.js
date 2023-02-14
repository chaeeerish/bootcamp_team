// 캔버스
const canvas = document.getElementById("jsCanvas");
// 선
const ctx = canvas.getContext("2d");
// 색깔
const range = document.getElementById("jsRange");

//컨버스 크기
canvas.width = 700;
canvas.height = 700;
//일단 흰색으로 채우고 시작 (기존 canvas가 흰색으로 보여도 데이터 상으로는 0으로 되어 있다고 한다)
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);


ctx.strokeStyle = "#2c2c2c"; // 우리가 그릴 선들은 모두 이 색을 갖는다
ctx.fillStyle = "#2c2c2c";
ctx.lineWidth = 2.5; // 라인의 너비가 2.5


let painting = false;
function stopPainting(){
    painting = false;
}
//모바일 PC를 구별하기
let device = "";
function checkMobile(){
    var mobileFlag = /Mobile|iP(hone|od)|Windows (CE|Phone)|Minimo|Opera M(obi|ini)|BlackBerry|Nokia/;
        //모바일일경우
      if (navigator.userAgent.match(/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune|Lumia/)) {
        device = "mobile";
    }
        //테블릿일 경우

    else if ((/iPad|tablet|Tablet|Kindle|Tab|Galaxy Tab/).test(navigator.userAgent)) {
        device = "tablet";
    }
        //그 외의 경우 모두 pc로 취급
    else {
        device = "etc";

    }
};
    // if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
    //     isMobile = true;
    // }else{
    //     isMobile = false;
    // }

checkMobile();
console.log(device);
if(isMobile){
    // 모바일 버전
    canvas.addEventListener("touchmove", touchMove, false);
    canvas.addEventListener("touchstart", touchStart, false);
    canvas.addEventListener("touchend", touchEnd, false);
}else{
    // pc버전

    if(canvas){
        canvas.addEventListener("mousemove", onMouseMove);
        canvas.addEventListener("mousedown", onMouseDown);
        canvas.addEventListener("mouseup", onMouseUp);
        canvas.addEventListener("mouseleave", stopPainting);
        canvas.addEventListener("contextmenu", handleCM); // 이벤트 추가

    }
}



// canvas 그림 리셋
document.getElementById("jsReset").onclick=function(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}
///////////  모바일///////////////////////////
// 모바일 터치 좌표 구하기
function getTouchPos(e) {
    return {
        x: e.targetTouches[0].clientX - e.target.offsetLeft,
        y: e.targetTouches[0].clientY - e.target.offsetTop + document.documentElement.scrollTop
    }
}

function touchStart(e) {
    e.preventDefault();
    painting = true;
    const { x, y } = getTouchPos(e);
    startX = x;
    startY = y;
}

function touchMove(e) {
    if(!painting) return;
    const { x, y } = getTouchPos(e);
    ctx.lineTo(x, y);
    ctx.stroke();
    startX = x;
    startY = y;
}

function touchEnd(e) {
    if(!painting) return;
    ctx.beginPath();
    const { x, y } = getTouchPos(e);
    startX = x;
    startY = y;
    ctx.arc(startX, startY, ctx.lineWidth/2, 0, 2*Math.PI);
    ctx.fillStyle = ctx.strokeStyle;
    ctx.fill();
    painting = false;
}

///////////////////////PC//////////////////////////
//  마우스 움직일 때
function onMouseMove(event){
    const x = event.offsetX;
    const y = event.offsetY;

    if (!painting){
        ctx.beginPath();
        ctx.moveTo(x,y);
    }else {
        ctx.lineTo(x, y); // lineTo는 path의 이전 위치에서 지금 위치까지 선을 만드는 것
        ctx.stroke();
      }

}
// 마우스를 누르고 있을 때
function onMouseDown(event){
    painting = true;
}
// 마우스를 누르지 않고 있을 때
function onMouseUp(event){
    painting = false;
}
// 마우스가 벗어나면 그리지 않도록
function onMouseLeave(event){
    painting = false;
}

//선 크기 조절
if (range) {
    range.addEventListener("input", handleRangeChange);
}
function handleRangeChange(event) {
  const size = event.target.value;
  ctx.lineWidth = size;
}
// 색깔 바꾸기
const colors = document.getElementsByClassName("jsColor");

for(var i=0; i<colors.length; i++){
    colors[i].addEventListener("click",handleColorClick)
}
//  두 개는 같은 의미
// Array.from(colors).forEach((color) =>
//     color.addEventListener("click",handleColorClick)
//     );
function handleColorClick(e){
    const color = e.target.style.backgroundColor;
    ctx.strokeStyle = color;
}




// canvas 그림 저장
function handleCM(event) {
    event.preventDefault();
  }

function handleSaveClick() {
    const image = canvas.toDataURL();
    const link = document.createElement("a");
    link.href = image;
    link.download = "PaintJS";
    link.click();
  }
if (jsSave) {
    jsSave.addEventListener("click", handleSaveClick);
  }