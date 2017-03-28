$(function(){
  $.getJSON("data.json", function(data){
      console.log(data[0]);
      status_print(data[0]);
  }) 
}) 

function status_print(json_data){
  if(json_data == 0) {
    $('.content').html('システムは正常です);
  }else{
    $('.content').html('システムに異常が発生しています');
  }
}
