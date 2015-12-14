$(document).ready(function(){
    $('.more a').click(function(){
       $(this).parentsUntil('.person').siblings('.operation').slideToggle();
    });
});