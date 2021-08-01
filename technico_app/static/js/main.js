  
  //NAVIGATION

window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
  if (window.matchMedia('screen and (max-width: 768px)').matches){

  }else{
    document.getElementById("navbar").style.top = "0";
    document.getElementById("nav").style.display = "none";
  }} else {
  if (window.matchMedia('screen and (max-width: 768px)').matches){

  }else{
    document.getElementById("navbar").style.top = "-85px";
    document.getElementById("nav").style.display = "block";
    }
  }
}

var count=0;
function opennav(){
if(count==0){
document.getElementById("nav").style.height="300px";
document.getElementById("icon").style.color="#3399ff";
count++;
}else{
document.getElementById("nav").style.height="45px";
document.getElementById("icon").style.color="#000";
count=0;
}
}



// text type
const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");

const textArray = ["Website Development","New Computer System", "Computer Repaire ","Laptop Repaire" ,"Computer Softwear","CCTV" ,"Computer Accessories"];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
  	setTimeout(erase, newTextDelay);
  }
}

function erase() {
	if (charIndex > 0) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
    charIndex--;
    setTimeout(erase, erasingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if(textArrayIndex>=textArray.length) textArrayIndex=0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function() { // On DOM Load initiate the effect
  if(textArray.length) setTimeout(type, newTextDelay + 250);
});




