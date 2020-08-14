const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");

// 화면상에 보여지는 canvas는 css로 작성하여 나왔기때문에 canvas에 픽셀 사이즈를 줄 필요가 있음
canvas.width = 700;
canvas.height = 700;

ctx.strokeStyle = "#2c2c2c";
ctx.lineWidth = 2.5;

let painting = false;

function stopPainting() {
  painting = false;
}

function startPainting() {
  painting = true;
}

function onMouseMove(event) {
  const x = event.offsetX; // offsetX : 캔버스 내의 x 좌표
  const y = event.offsetY; // offsetY : 캔버스 내의 y 좌표

  if (!painting) {
    ctx.beginPath();
    ctx.moveTo(x, y);
  } else {
    ctx.lineTo(x, y);
    ctx.stroke();
  }
}

function onMouseDown(event) {
  painting = true;
}

if (canvas) {
  canvas.addEventListener("mousemove", onMouseMove);
  canvas.addEventListener("mousedown", startPainting);
  canvas.addEventListener("mouseup", stopPainting);
  canvas.addEventListener("mouseleave", stopPainting);
}
