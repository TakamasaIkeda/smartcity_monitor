$(function(){
  $.getJSON("data.json", function(data){
      console.log(data[0]);
      status_print(data[0]);
  }) 
}) 

function status_print(json_data){
  if(json_data == 0) {
    $('.content').html('System is operating on normally');
  }else{
    $('.content').html('Something happening on system');
  }
}
