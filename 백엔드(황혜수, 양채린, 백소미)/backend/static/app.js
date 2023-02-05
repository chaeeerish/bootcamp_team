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
// canvas 그림 리셋
document.getElementById("jsReset").onclick=function(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";  
    ctx.fillRect(0, 0, canvas.width, canvas.height);
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
    // console.log();


    link.click();
  }  
if (jsSave) {
    jsSave.addEventListener("click", handleSaveClick);
  }  
//캔버스 내 이벤트들
if(canvas){
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", onMouseDown);
    canvas.addEventListener("mouseup", onMouseUp);
    canvas.addEventListener("mouseleave", stopPainting);
    canvas.addEventListener("contextmenu", handleCM); // 이벤트 추가

}

//선 크기 조절

if (range) {
    range.addEventListener("input", handleRangeChange);
}

function handleRangeChange(event) {
  const size = event.target.value;
  ctx.lineWidth = size;
}
