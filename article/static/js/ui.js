
function more_sw(){
$('html,body').animate({
  scrollTop: $(".more").offset().top},'slow');
}

function heart_sw(){

if ( document.getElementById("heart").classList.contains('fa-heart-o')){
document.getElementById("heart").classList.remove('fa-heart-o');
document.getElementById("heart").classList.add('fa-heart');
document.getElementById("heart-drop").classList.add('drop-hover');

var heart = document.getElementById("heart-drop")
savedpost('saved',
heart.getAttribute("data-pk"),
heart.getAttribute("data-usr"),
true,
"Munchie saved!");

return;}

  if ( document.getElementById("heart").classList.contains('fa-heart')){
document.getElementById("heart").classList.remove('fa-heart');
document.getElementById("heart").classList.add('fa-heart-o');
document.getElementById("heart-drop").classList.remove('drop-hover');

var heart = document.getElementById("heart-drop")
savedpost('saved',
heart.getAttribute("data-pk"),
heart.getAttribute("data-usr"),
false,
"Munchie un-saved!");

return;}

}

function done_sw(){

if ( document.getElementById("check").classList.contains('fa-check-circle-o') ){
document.getElementById("check").classList.remove('fa-check-circle-o');
document.getElementById("check").classList.add('fa-check-circle');
document.getElementById("check-drop").classList.add('drop-hover');
document.getElementById("check-text").innerHTML = "Munchie<br>Completed!";

var check = document.getElementById("heart-drop")
donepost('done',
check.getAttribute("data-pk"),
check.getAttribute("data-usr"),
true,
" ");

return;
}
  if ( document.getElementById("check").classList.contains('fa-check-circle') ){
document.getElementById("check").classList.remove('fa-check-circle');
document.getElementById("check").classList.add('fa-check-circle-o');
document.getElementById("check-drop").classList.remove('drop-hover');
document.getElementById("check-text").innerHTML = "Complete<br>Munchie!";

var check = document.getElementById("heart-drop")
donepost('done',
check.getAttribute("data-pk"),
check.getAttribute("data-usr"),
false,
" ");

return;
}

}

function show_pop(title="Awesome!",msg="Great job finishing this munchie! Keep it up!"){

  var audio = document.getElementById('success');
  audio.volume = 0.5;
  audio.play();

document.getElementById("overlay").style.display = "block";

document.getElementById("overlay-title").innerHTML = title;
document.getElementById("overlay-desc").innerHTML = msg;

}

function hide_pop(){
document.getElementById("overlay").style.display = "none";

document.getElementById("overlay-title").innerHTML = " ";
document.getElementById("overlay-desc").innerHTML = " ";

}




function show_noti(msg){

document.getElementById("noti").style.display = "block";
document.getElementById("noti-text").innerHTML = msg;


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

// AJAX POST
function donepost(type,art,usr,bool,msg){
    $.ajax({
        type: "POST",
        url: "/stat/",
        dataType: "json",
        data: { "type":type, "art":art, "usr":usr,"bool":bool },
        success: function(data) {

            if(bool == true){show_pop();}
            if(bool == false){show_noti("Munchie un-done!");}
        }
    });
}

    // AJAX POST
    function savedpost(type,art,usr,bool,msg){
        $.ajax({
            type: "POST",
            url: "/stat/",
            dataType: "json",
            data: { "type":type, "art":art, "usr":usr,"bool":bool },
            success: function(data) {
                show_noti(msg);
            }
        });
    }



    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
