function sendCommand(action) {
    fetch('/control', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ action: action })
    })
    .then(res => res.json())
    .then(data => {
      console.log("Command sent:", data.sent);
    });
  }
  
  function fetchStatus() {
    fetch('/status')
      .then(res => res.json())
      .then(data => {
        document.getElementById('status').innerText = data.status;
      });
  }
  
  setInterval(fetchStatus, 2000);
  