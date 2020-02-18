// method

alert("Hello Front End Engneer Site")

var input = window.prompt("Put your name !")

if (input != ""){
  var userElem = document.getElementById("user_name")
  userElem.innerText = `Welcome ${input}`
}

let getRandomUserEmail = () => {
  $.ajax({
    url: 'https://randomuser.me/api/',
    dataType: 'json',
    success: function(data) {
      let user = document.getElementById("random_user")
      user.innerText = data.results[0].email
    }
  });
}

let getWeather = () => {
  $.ajax({
    url: 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010',
    dataType: 'json',
    success: function(data) {
      let weather = document.getElementById("weather")
      weather.innerText = data.forecasts[0].telop
    }
  });
}

new roughViz.Donut(
  {
    element: '#vis0',
    legend: false,
    data: {
      labels: ['JNCO Jeans', 'Sweat Pants', 'Jorts'],
      values: [20, 10, 2]
    },
    title: 'Pants I Got Clowned On For Wearing In High School',
    titleFontSize: '2rem',
    labels: 'letter',
    values: 'frequency',
    width: window.innerWidth,
    stroke: 'coral',
    strokeWidth: 3,
    color: 'pink',
    fillWeight: 1.5,
  }
);