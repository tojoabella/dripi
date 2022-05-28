//const { performance } = require('perf_hooks');
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

const get_current_position = (onSuccess, onError) => {
//const get_current_position = () => {
  //var startTime = performance.now();
  //console.time('doSomething')
  if (navigator.geolocation) {
    return navigator.geolocation.getCurrentPosition(onSuccess, onError);
  }
  return onError(new Error('Geolocation is not supported by your browser.'));
  //console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
  //console.timeEnd('doSomething');
};

function initMap() {
    let map = create_map(21.478252, -157.996700);

    let infoWindow = create_info_window();

    const locationButton = document.createElement("button");
    locationButton.textContent = "Pan to Current Location";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  
    
    locationButton.addEventListener("click", () => {
      get_current_position(
        (success) => {
          const pos = {
            lat: success.coords.latitude,
            lng: success.coords.longitude,
          };
          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);
          //map.setCenter(pos);
          //map.panTo(pos);
        },
        (error) => {
          handleLocationError(error.message, infoWindow, map.getCenter());
        }
      );
    });
  
    function handleLocationError(error_message, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(error_message);
      infoWindow.open(map);
    }
    
  
    const flightPlanCoordinates = [
      { lat: 37.772, lng: -122.214 },
      { lat: 21.291, lng: -157.821 },
      { lat: -18.142, lng: 178.431 },
      { lat: -27.467, lng: 153.027 },
    ];
    const flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: "#FF0000",
      strokeOpacity: 1.0,
      strokeWeight: 2,
    });
    flightPath.setMap(map);
  }
  
/*
function initMap(){
        //map options
        let options = {
          zoom: 14,
          center: {lat: 21.2871, lng: -157.8312}
        }
        //new map
        let map1 = new google.maps.Map(document.getElementById("map"), options);
        //markers
        addMarker({coords: {lat: 21.285, lng: -157.85}}, map1);

        function addMarker(properties, mapNum) {
          let marker = new google.maps.Marker(
          {
            position: properties.coords,
            map: mapNum
          });
        }
      }
*/
