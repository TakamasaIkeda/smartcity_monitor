$.ajax({
  type: 'GET',
  url: './data.json',
  dataType: 'json',
  beforeSend: function(data){
    data.overrideMimeType("text/html; charset=Shift_JIS"); 
  },
  success: function(data){
    var status_array = [];
    var ok = "現在システムは正常に稼働しています";
    var ng = "現在システムはご利用になれません";
    for(i in data)status_array.push(Object.values(data[i])[0]);
    var status_flag = status_array.indexOf(1);
    status_flag >= 0 ? $('.content').html(ng) : $('.content').html(ok);
    console.log("status_array:" + status_array);
    console.log("status_flag:" + status_flag);
  },
  error: function(){
    console.log("json unreadable"); 
  },
});
