let map;
let marker;

function initMap() {
  const initialPos = [37.4221, -122.0841];

  map = L.map('map').setView(initialPos, 18);

  // Use OpenStreetMap tiles
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  marker = L.marker(initialPos).addTo(map).bindPopup('Tracked Object').openPopup();
}

function fetchLocation() {
  fetch('/location')
    .then(res => res.json())
    .then(data => {
      const pos = [data.lat, data.lon];
      marker.setLatLng(pos);
      map.setView(pos);
      console.log("Updated marker to:", pos);
    });
}

window.onload = () => {
  initMap();
  setInterval(fetchLocation, 2000);
};
