import {homepage_side_bar} from './components/side_bar/side_bar.js';
import {homepage_top_bar} from './components/top_bar/top_bar.js';
import {theme_toggler} from './components/theme_toggler.js';
import {mode_toggler} from './components/modes/modes.js';
import * as map_info from './components/map/map_info.js';

homepage_side_bar();
homepage_top_bar();
theme_toggler();
mode_toggler();

/*
document.getElementById('start').addEventListener('click', () => {
    var modes = document.getElementsByClassName('mode');
    for (let i = 0; i < modes.length; i++) {
        mode = modes[i];
        if (mode.classList.contains('active')) {
            mode.classList.remove('show');
        }
    }
});
*/

let current_position;

const track_location = (onSuccess, onError = () => { }) => {
    if (navigator.geolocation) {
        return navigator.geolocation.watchPosition((pos) => onSuccess(pos), onError);
    }
    return onError(new Error('Geolocation is not supported by your browser.'));
};

function run_updates(pos){
    map_info.add_coordinates(pos);
    map_info.add_locality_info(pos);
    map_info.add_neighborhood_info(pos);
    map_info.add_road_info(pos);
}

function on_track_location_success(position){
    const pos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    };
    console.log(pos);
    pos.lat = round_number(pos.lat, 4);
    pos.lng = round_number(pos.lng, 4);
    console.log(pos);

    if (!current_position) {
        current_position = pos;
    }
    else{
        console.log("here");
        if (pos != current_position){
            run_updates(pos);
        }
    }
  }

document.getElementById('start').addEventListener('click', async () => {
    track_location(
        on_track_location_success,
        (error) => {
          handleLocationError(error.message, infoWindow, map.getCenter());
        });
  });