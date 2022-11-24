// 현재 data값 갱신

function refresh() {
  const curTemp = document.getElementById("cur-temp");
  const curHum = document.getElementById("cur-hum");
  console.log(curTemp.innerHTML);
  console.log(curHum.innerHTML);
  $.ajax({
    url: 'json',
    type: 'GET',
    datatype: 'json',
    success: function(data){
      curTemp.innerHTML = `${data[99].temp}℃`
      curHum.innerHTML = `${data[99].humid}%`
    }

  });

}


setInterval(refresh, 5000);

refresh();