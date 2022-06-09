import {homepage_side_bar} from './components/side_bar/side_bar.js';
import {homepage_top_bar} from './components/top_bar/top_bar.js';
import {theme_toggler} from './components/theme_toggler.js';
import {mode_toggler} from './components/modes/modes.js';
import * as map_info from './components/map/map_info.js';
import * as api_queries from "./components/map/api_queries.js";

homepage_side_bar();
homepage_top_bar();
theme_toggler();
mode_toggler();

/* INSTANTIATE */
const number_of_modes = 15;
let current_coords;
let current_road;
let current_localities;
let current_neighborhood;
let active_modes = new Set();

function update_active_modes(){
    active_modes.clear();
    for (let i = 1; i <= number_of_modes; i++) {
        let mode = "mode" + i;
        if (document.getElementById(mode).classList.contains('active_item')){
            active_modes.add(mode);
        }
    }
    console.log(active_modes);
}

const track_location = (onSuccess, onError = () => { }) => {
    if (navigator.geolocation) {
        return navigator.geolocation.watchPosition((pos) => onSuccess(pos), onError);
    }
    return onError(new Error('Geolocation is not supported by your browser.'));
};

function run_updates(pos){

    console.log("running updates");
    map_info.update_coordinates(pos);
    current_coords = pos;

    let new_localities = api_queries.get_localities(pos);
    if (new_localities != current_localities){
        map_info.update_locality_info_given_localities(new_localities);
        current_localities = new_localities;
    }

    let new_neighborhood = api_queries.get_neighborhood(pos);
    if (new_neighborhood != current_neighborhood){
        map_info.update_neighborhood_info_given_neighborhood(new_neighborhood);
        current_neighborhood = new_neighborhood;
    }

    let new_road = api_queries.get_road(pos);
    if (new_road != current_road){
        map_info.update_road_info_given_road(new_road);
        current_road = new_road;
    }

}

function round_number(num, dec) {
    return Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
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

    if ((!current_coords) || (pos != current_coords)) {
        run_updates(pos);
    }
  }

document.getElementById('start').addEventListener('click', async () => {
    update_active_modes();
    track_location(
        on_track_location_success,
        (error) => {
          handleLocationError(error.message, infoWindow, map.getCenter());
        });
  });