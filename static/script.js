setInterval(displayTime, 1000);
    function displayTime() {
      let currentTime = new Date();
      let hours = currentTime.getHours();
      let minutes = currentTime.getMinutes();
      let secondes = currentTime.getSeconds();

      if (hours < 10) {
        hours = "0" + hours;
      }
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      if (secondes < 10) {
        secondes = "0" + secondes;
      }

      document.getElementById("time").innerHTML = hours + ':' + minutes + '.' + secondes;
    }