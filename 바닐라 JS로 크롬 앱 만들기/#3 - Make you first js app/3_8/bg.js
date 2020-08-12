const body = document.querySelector("body");

const IMG_NUMBER = 30;

function paintImage(imgNumber){
    const image = new Image();
    root = `C:/Users/황준철/Desktop/개인공부_프로그래밍/NomadCoders/`;
    image.src = `${root}바닐라 JS로 크롬 앱 만들기/image/backgrounds/Large/${imgNumber + 1}.jpg`;
    image.classList.add("bgImage");
    body.prepend(image);
}

function getRandom(){
    const number = Math.floor(Math.random() * IMG_NUMBER);
    return number;
}

function init() {
    const randomNumber = getRandom();
    paintImage(randomNumber);
}

init();