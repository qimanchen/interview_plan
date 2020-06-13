$(document).ready(function(){   
  
    $("ul.sub-menu").parent().append("<span></span>"); //Only shows drop down trigger when js is enabled (Adds empty span tag after ul.sub-menu*)   
  
    $("ul.menu li a").mouseover(function() { //When trigger is clicked...   
  
        //Following events are applied to the sub-menu itself (moving sub-menu up and down)   
        $(this).parent().find("ul.sub-menu").slideDown('fast').show(); //Drop down the sub-menu on click   
  
        $(this).parent().hover(function() {   
        }, function(){   
            $(this).parent().find("ul.sub-menu").slideUp('slow'); //When the mouse hovers out of the sub-menu, move it back up   
        });   
  
        //Following events are applied to the trigger (Hover events for the trigger)   
        }).hover(function() {   
            $(this).addClass("subhover"); //On hover over, add class "subhover"   
        }, function(){  //On Hover Out   
            $(this).removeClass("subhover"); //On hover out, remove class "subhover"   
    });   
  
});  


$(document).ready(function(){
  $("#imgPlay").mouseover(function(){
  $(this).children("div.next").stop(true, true).fadeIn('300');
  });
  $("#imgPlay").mouseout(function(){
  $(this).children("div.next").stop(true, true).fadeOut('300');
  });
    $("#imgPlay").mouseover(function(){
  $(this).children("div.prev").stop(true, true).fadeIn('300');
  });
  $("#imgPlay").mouseout(function(){
  $(this).children("div.prev").stop(true, true).fadeOut('300');
  });
});

//<![CDATA[
$(document).ready(function () {
//Append a div with hover class to all the LI
$('#navigation li').append('<div class="hover"><\/div>');
$('#navigation li').hover(
//Mouseover, fadeIn the hidden hover class
function() {
$(this).children('div').stop(true, true).fadeIn('1000');
},
//Mouseout, fadeOut the hover class
function() {
$(this).children('div').stop(true, true).fadeOut('1000');
}).click (function () {
//Add selected class if user clicked on it
$(this).addClass('selected');
});
});
//]]> 


//<![CDATA[
$(document).ready(function () {
//Append a div with hover class to all the LI
$('.main2 .new_tu li').append('<div class="hover2"><\/div>');
$('.main2 .new_tu li').hover(
//Mouseover, fadeIn the hidden hover class
function() {
$(this).children('.hover2').stop(true, true).fadeOut('300');
},
//Mouseout, fadeOut the hover class
function() {
$(this).children('.hover2').stop(true, true).fadeIn('300');
}).click (function () {
//Add selected class if user clicked on it
$(this).addClass('selected');
});

});
//]]> 

