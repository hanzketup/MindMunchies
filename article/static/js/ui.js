
function more_sw(){
  var block = document.getElementById("more");
  console.log(block.style.display)
  if(block.style.display === "none") {
block.style.display = "block";
$('html,body').animate({
  scrollTop: $(".more").offset().top},'slow');
}
else {
  $('html,body').animate({
    scrollTop: $(".header").offset().top},'slow');
setTimeout(function(){
    block.style.display = "none";
  }, 750);

}}

function heart_sw(){

if ( document.getElementById("heart").classList.contains('fa-heart-o') ){
document.getElementById("heart").classList.remove('fa-heart-o');
document.getElementById("heart").classList.add('fa-heart');
document.getElementById("heart-drop").classList.add('drop-hover');
return;
}
  if ( document.getElementById("heart").classList.contains('fa-heart') ){
document.getElementById("heart").classList.remove('fa-heart');
document.getElementById("heart").classList.add('fa-heart-o');
document.getElementById("heart-drop").classList.remove('drop-hover');
return;
}

}

function done_sw(){

if ( document.getElementById("check").classList.contains('fa-check-circle-o') ){
document.getElementById("check").classList.remove('fa-check-circle-o');
document.getElementById("check").classList.add('fa-check-circle');
document.getElementById("check-drop").classList.add('drop-hover');
document.getElementById("check-text").innerHTML = "Munchie<br>Completed!";
return;
}
  if ( document.getElementById("check").classList.contains('fa-check-circle') ){
document.getElementById("check").classList.remove('fa-check-circle');
document.getElementById("check").classList.add('fa-check-circle-o');
document.getElementById("check-drop").classList.remove('drop-hover');
document.getElementById("check-text").innerHTML = "Complete<br>Munchie!";
return;
}

}

function show_pop(){

  var audio = new Audio('sounds/success.mp3');
  audio.volume = 0.5;
  audio.play();

document.getElementById("overlay").style.display = "block";

}

function hide_pop(){
document.getElementById("overlay").style.display = "none";
}

function show_noti(){

document.getElementById("noti").style.display = "block";

window.setTimeout(function(){
  document.getElementById("noti").classList.add('noti-show');
  document.getElementById("noti").classList.remove('noti-hide');
},1);


var audio = new Audio('sounds/ding.mp3');
audio.volume = 0.8;
audio.play();


window.setTimeout(hide_noti,5000);

}

function hide_noti(){

document.getElementById("noti").classList.remove('noti-show');
document.getElementById("noti").classList.add('noti-hide');

window.setTimeout(function(){
document.getElementById("noti").style.display = "none";
},600);

}