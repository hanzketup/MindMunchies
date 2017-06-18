
function more_sw(){
$('html,body').animate({
  scrollTop: $(".more").offset().top},'slow');
}

function heart_sw(){

if ( document.getElementById("heart").classList.contains('fa-heart-o')){
document.getElementById("heart").classList.remove('fa-heart-o');
document.getElementById("heart").classList.add('fa-heart');
document.getElementById("heart-drop").classList.add('drop-hover');



return;}

  if ( document.getElementById("heart").classList.contains('fa-heart')){
document.getElementById("heart").classList.remove('fa-heart');
document.getElementById("heart").classList.add('fa-heart-o');
document.getElementById("heart-drop").classList.remove('drop-hover');



return;}

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

  var audio = document.getElementById('success');
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


var audio = document.getElementById('ding');
audio.volume = 0.8;
audio.play();


notitime = window.setTimeout(hide_noti,5000);

}

function hide_noti(){

clearTimeout(notitime);
document.getElementById("noti").classList.remove('noti-show');
document.getElementById("noti").classList.add('noti-hide');

window.setTimeout(function(){
document.getElementById("noti").style.display = "none";
},600);

}

function filt(v) {
    var list = document.querySelectorAll(".grid-item");
    for(i of list) {

      if(v == 0){
        i.style.display = 'flex';
      }

      if(v == 1){
      if(i.getAttribute("data-saved") == 'True') {
        i.style.display = 'flex';}
        else {i.style.display = 'none';}
    }


      if(v == 2){
      if(i.getAttribute("data-done") == 'True') {
        i.style.display = 'flex';}
        else {i.style.display = 'none';}
        }

  }

if(v == 0){
  document.getElementById("filter0").classList.add("drop-hover");
  document.getElementById("filter1").classList.remove("drop-hover");
  document.getElementById("filter2").classList.remove("drop-hover");
}
if(v == 1){
  document.getElementById("filter1").classList.add("drop-hover");
  document.getElementById("filter0").classList.remove("drop-hover");
  document.getElementById("filter2").classList.remove("drop-hover");
}
if(v == 2){
  document.getElementById("filter2").classList.add("drop-hover");
  document.getElementById("filter0").classList.remove("drop-hover");
  document.getElementById("filter1").classList.remove("drop-hover");
}



}
