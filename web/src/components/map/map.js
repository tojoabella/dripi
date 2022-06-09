/* INSTANTIATE */
let map;

/* HELPERS */
const create_map = ( lat, lng ) => {
  return new google.maps.Map(document.getElementById('map'), {
    center: { lat, lng },
    zoom: 10,
    mapTypeId: "terrain"
  });
};

const create_info_window = () => {
  return new google.maps.InfoWindow();
};

/* DEPRECATED: NOW USING PROMISES/ASYNC/AWAIT INSTEAD OF CALLBACKS
const get_current_position = (onSuccess, onError = () => {}) => {
  if (navigator.geolocation) {
    return navigator.geolocation.getCurrentPosition(onSuccess, onError);
  }
  return onError(new Error('Geolocation is not supported by your browser.'));
};

const track_location = (onSuccess, onError = () => { }) => {
  if (navigator.geolocation) {
    return navigator.geolocation.watchPosition(onSuccess, onError);
  }
  return onError(new Error('Geolocation is not supported by your browser.'));
};
*/

function get_current_position() {
  var options = {
    enableHighAccuracy: true,
    timeout:    5000,
    maximumAge: 0,
  };

  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(
      (pos) => { resolve(pos); }, 
      (err) => { reject(err); }, 
      options);
  });
}

function track_location(){
  return new Promise((resolve, reject) => {
    navigator.geolocation.watchPosition(
      (pos) => { resolve(pos) },
      (err) => { reject(err) }
    );
  });
}

const add_polylines = (coords, map) => {
  const flightPath = new google.maps.Polyline({
    path: coords,
    geodesic: true,
    strokeColor: "#FF0000",
    strokeOpacity: 1.0,
    strokeWeight: 2,
  });
  flightPath.setMap(map);
};

function set_current_position(pos) {
  current_position = pos;
}

/*
function httpGetAsync(theUrl, callback){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}
*/
function httpGet(theUrl) {
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", theUrl, false); 
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}

async function initMap() {
  /* INITIATE MAP */
  map = create_map(21.478252, -157.996700);
  let infoWindow;

  /* PAN BUTTON */
  let pan_button = document.getElementById('map_pan_button');
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(pan_button);
  pan_button.addEventListener("click", async () => {
    infoWindow = create_info_window();
    let response = await get_current_position();
    let pos = {
      lat: response.coords.latitude,
      lng: response.coords.longitude,
    };
    infoWindow.setPosition(pos);
    infoWindow.setContent("Location found.");
    infoWindow.open(map);
    map.panTo(pos);
    map.setZoom(13);
  });

  /* RESET MAP BUTTON */
  let reset_button = document.getElementById('map_reset_button');
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(reset_button);
  reset_button.addEventListener("click", () => {
    map.panTo({lat: 21.478252, lng: -157.996700});
    map.setZoom(10);
    if (infoWindow){
      infoWindow.close();
    }
  });

  function handleLocationError(error_message, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(error_message);
    infoWindow.open(map);
  }

  const polyline_coords = [
    { lat: 37.772, lng: -122.214 },
    { lat: 21.291, lng: -157.821 },
    { lat: -18.142, lng: 178.431 },
    { lat: -27.467, lng: 153.027 },
  ];
  add_polylines(polyline_coords, map);
}

window.initMap = initMap;