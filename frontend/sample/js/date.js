document.getElementById('date').innerHTML = getNow();

function getNow(){
  var now = new Date();
  var year = now.getFullYear();
  var month = now.getMonth()+1;
  var day = now.getDate();
  var hour = now.getHours();
  var min = now.getMinutes();
  var second = now.getSeconds();

  var all = year + "年" + month + "月" + day + "日" + hour + "時" + min + "分" + second +"秒";
  return all;

}