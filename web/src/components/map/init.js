/* initMap won't work if there are other imports */

 var map;

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

function initMap() {
  map = create_map(21.478252, -157.996700);
}

window.initMap = initMap;


/*
function initMap() {
  map = create_map(21.478252, -157.996700);
  let infoWindow = create_info_window();

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
  set_current_position(pos);
  add_coordinates(current_position);

}
*/