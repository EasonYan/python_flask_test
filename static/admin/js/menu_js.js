$(function(){
  $(".nav_item").mouseover(function(){
    $(this).children("ul").slideDown(180);
  });
  $(".nav_item").mouseleave(function(){
    $(this).children("ul").slideUp(100);
  });
});