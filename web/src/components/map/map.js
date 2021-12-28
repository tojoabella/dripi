//const { performance } = require('perf_hooks');


function initMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 21.418764, lng: -157.931359 },
      zoom: 10,
      mapTypeId: "terrain"
    });
    

    let infoWindow = new google.maps.InfoWindow();
    const locationButton = document.createElement("button");
    locationButton.textContent = "Pan to Current Location";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  
    locationButton.addEventListener("click", () => {
      // Try HTML5 geolocation.
      //var startTime = performance.now();
      console.time('doSomething')


      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            console.log(position);
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            //var endTime = performance.now();
            //console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
            console.timeEnd('doSomething');

  
            infoWindow.setPosition(pos);
            infoWindow.setContent("Location found.");
            infoWindow.open(map);
            map.setCenter(pos);
          },
          () => {
            handleLocationError(true, infoWindow, map.getCenter());
          }
        );
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
    });
  
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
