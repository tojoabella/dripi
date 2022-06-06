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

function initMap() {
  /* INITIATE MAP */
    let map = create_map(21.478252, -157.996700);
    let infoWindow = create_info_window();

    /* PAN BUTTON */
    let pan_button = document.getElementById('map_pan_button');
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(pan_button);
    pan_button.addEventListener("click", () => {
      get_current_position(
        (success) => {
          const pos = {
            lat: success.coords.latitude,
            lng: success.coords.longitude,
          };
          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);
          map.panTo(pos);
          map.setZoom(13);
        },
        (error) => {
          handleLocationError(error.message, infoWindow, map.getCenter());
        }
      );
    });

    /* RESET MAP BUTTON */
    let reset_button = document.getElementById('map_reset_button');
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(reset_button);
    reset_button.addEventListener("click", () => {
      map.panTo({lat: 21.478252, lng: -157.996700});
      map.setZoom(10);
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

    const pos = {
      lat: 21.478252,
      lng: -157.996700,
    };
    mode_1(pos, map);
    mode_2(pos, map);
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

/* MODES */

const mode_1 = (pos, map) => {
  /* get road */
  let latitude = pos["lat"];
  let longitude = pos["lng"];
  let url = "http://127.0.0.1:5000//get_road?lat=" + latitude + "&lng=" + longitude;
  let response = httpGet(url);
  response = JSON.parse(response);
  console.log(response);
  let infoWindow = create_info_window();
  infoWindow.setPosition(pos);
  infoWindow.setContent(response);
  infoWindow.open(map);
  document.getElementById("road_name").innerHTML = "Road: " + response;
};

const mode_2 = (pos) => {
  /* get localities */
  let latitude = pos["lat"];
  let longitude = pos["lng"];
  let url = "http://127.0.0.1:5000//get_localities?lat=" + latitude + "&lng=" + longitude;
  let response = httpGet(url);
  response = JSON.parse(response);
  console.log(response);
  let text = "";
  for (let i = 0; i < response.length; i++) {
    if (i == response.length - 1){
      text += response[i];
    }
    else{
      text += response[i] + ", ";
    }
  }
  document.getElementById("locality_name").innerHTML = "Localities: " + text;
};
