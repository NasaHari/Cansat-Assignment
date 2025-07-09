function fetchTemp() {
    fetch('/data')
      .then(response => response.json())
      .then(data => {
        console.log("Got data:", data);
        document.getElementById('temp').innerText = data.temp;
      });
  }
  
  setInterval(fetchTemp, 2000);
  