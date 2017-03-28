$.ajax({
  type: 'GET',
  url: './data.json',
  dataType: 'json',
  beforeSend: function(data){
    data.overrideMimeType("text/html; charset=Shift_JIS") 
  },
  success: function(data){
    status_print(data[0]);
  },
  error: function(){
    console.log("json unreadable"); 
  },
});

function status_print(json_data){
  console.log("json status" + json_data);
  if(json_data == 0) {
    $('.content').html('OK:system is working properly');
  }else{
    $('.content').html('BAD: system is not working for some reason');
  }
}
