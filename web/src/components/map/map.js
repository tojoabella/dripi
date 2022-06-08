/* INSTANTIATE */
var current_position;
var map;

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

function on_track_location_success(){
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

async function initMap() {
  /* INITIATE MAP */
  map = create_map(21.478252, -157.996700);
  let infoWindow = create_info_window();

  /* PAN BUTTON */
  let pan_button = document.getElementById('map_pan_button');
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(pan_button);
  pan_button.addEventListener("click", async () => {
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

  let response = await get_current_position();
  let pos = {
    lat: response.coords.latitude,
    lng: response.coords.longitude,
  };
  console.log(pos);
  set_current_position(pos);
  add_coordinates(current_position);
  mode_1(current_position, map);
  mode_2(current_position);
  mode_3(current_position);

  /*
    (success) => {
      const pos = {
        lat: success.coords.latitude,
        lng: success.coords.longitude,
      };

      set_current_position(pos);
      console.log(current_position);
      
    },
    (error) => {
      handleLocationError(error.message, infoWindow, map.getCenter());
    }
  );
  */

}

/*
add_coordinates(current_position);
mode_1(current_position, map);
mode_2(current_position);
mode_3(current_position);
*/
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

const add_coordinates = (pos) => {
  let latitude = pos["lat"];
  let longitude = pos["lng"];
  document.getElementById("coordinates").innerHTML = "Coordinates: " + latitude + ", " + longitude;
}

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

const mode_3 = (pos) => {
  /* get neighborhood */
  let latitude = pos["lat"];
  let longitude = pos["lng"];
  let url = "http://127.0.0.1:5000//get_neighborhood?lat=" + latitude + "&lng=" + longitude;
  let response = httpGet(url);
  response = JSON.parse(response);
  console.log(response);
  document.getElementById("neighborhood_name").innerHTML = "Neighborhood: " + response;
};

function round_number(num, dec) {
  return Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
}

function on_track_location_success(position){
  const pos = {
    lat: position.coords.latitude,
    lng: position.coords.longitude,
  };
  add_coordinates(pos);
  pos[lat] = round_number(pos[lat], 4);
  pos[lng] = round_number(pos[lng], 4);
  return pos;
}

/*
document.getElementById('start').addEventListener("click", () => {
  
  let current_position = get_current_position(
    (success) => {
      const pos = {
        lat: success.coords.latitude,
        lng: success.coords.longitude,
      };
      pos[lat] = round_number(pos[lat], 4);
      pos[lng] = round_number(pos[lng], 4);
      return pos;
    },
    (error) => {
      handleLocationError(error.message, infoWindow, map.getCenter());
    }
  );
  */
  
  /*
  let new_position = track_location(
    on_track_location_success,
    (error) => {
      handleLocationError(error.message, infoWindow, map.getCenter());
    }
  );
  */

/*
});
*/