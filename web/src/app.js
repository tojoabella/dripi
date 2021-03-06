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
const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
let track_location_id;
let current_coords;
let current_road = "";
let current_localities = "";
let current_neighborhood = "";
let active_modes = new Set();

//on page load
document.getElementById('alert_history_text').innerHTML = `Alert History (${timezone})`;

function update_active_modes(){
    active_modes.clear();
    for (let i = 1; i <= number_of_modes; i++) {
        let mode = "mode" + i;
        if (document.getElementById(mode).classList.contains('active_item')){
            active_modes.add(mode);
        }
    }
}

const track_location = (onSuccess, onError = () => { }) => {
    if (navigator.geolocation) {
        return navigator.geolocation.watchPosition((pos) => onSuccess(pos), onError);
    }
    return onError(new Error('Geolocation is not supported by your browser.'));
};

function run_updates(pos){
    let time = new Date();
    let current_time = time_converter(time.getHours(), time.getMinutes());
    let alert;

    map_info.update_coordinates(pos);
    current_coords = pos;
    // below is for testing purposes
    alert = `${current_time} --- change in coords --- ${pos.lat}`
    document.getElementById('alert_history').innerHTML = `${alert} <br> ${document.getElementById('alert_history').innerHTML}`;
    
    //current_time + "    " + pos.lat + "<br>" + document.getElementById('alert_history').innerHTML;

    let new_localities = api_queries.get_localities(pos);
    if (new_localities != current_localities){
        map_info.update_locality_info_given_localities(new_localities);
        current_localities = new_localities;
    }

    let new_neighborhood = api_queries.get_neighborhood(pos);
    if (new_neighborhood != current_neighborhood){
        if (new_neighborhood == null) {
            map_info.update_neighborhood_info_given_neighborhood("NONE");
        }
        else{
            map_info.update_neighborhood_info_given_neighborhood(new_neighborhood);
        }
        current_neighborhood = new_neighborhood;
    }

    let new_road = api_queries.get_road(pos);
    if (new_road != current_road){
        map_info.update_road_info_given_road(new_road);
        current_road = new_road;

        if ("mode1" in active_modes){
            alert = `${current_time} --- road change --- ${new_road}`;
            document.getElementById('alert_history').innerHTML = `${alert} <br> ${document.getElementById('alert_history').innerHTML}`;
        }
    }

}

function time_converter(hour, minute){
    if (minute < 10){
        minute = "0" + minute;
    }
    if (hour > 12){
        hour = hour - 12;
        return `${hour}:${minute}pm`;
    }
    if (hour == 0){
        return `12:${minute}am`;
    }
    return `${hour}:${minute}am`;
}

function round_number(num, dec) {
    return Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
  }

function on_track_location_success(position){
    const pos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    };
    pos.lat = round_number(pos.lat, 4);
    pos.lng = round_number(pos.lng, 4);

    if ((!current_coords) || ((pos.lat != current_coords.lat) && (pos.lng != current_coords.lng) )) {
        if (current_coords) {console.log("previous position: " + current_coords.lat + ", " + current_coords.lng); console.log("new position: " + pos.lat + ", " + pos.lng);}
        run_updates(pos);
    }
  }

document.getElementById('start').addEventListener('click', async () => {
    update_active_modes();
    track_location_id = track_location(
        on_track_location_success,
        (error) => {
          handleLocationError(error.message, infoWindow, map.getCenter());
        });

    
    let stop_button = document.getElementById('stop')
    if (stop_button.classList.contains('active_item')){
        stop_button.classList.remove('active_item');
        stop_button.classList.add('inactive_item');
    }

    document.getElementById('start').classList.add('active_item');
    document.getElementById('start').classList.remove('inactive_item');
});

document.getElementById('stop').addEventListener('click', () => {
    if (track_location_id) {
        navigator.geolocation.clearWatch(track_location_id);
        track_location_id = null;
    }

    let start_button = document.getElementById('start')
    if (start_button.classList.contains('active_item')){
        start_button.classList.remove('active_item');
        start_button.classList.add('inactive_item');
    }

    document.getElementById('stop').classList.add('active_item');
    document.getElementById('stop').classList.remove('inactive_item');
});

document.getElementById('clear').addEventListener('click', () => {
    map_info.clear_map_info();
    current_coords = null;
    current_road = "";
    current_localities = "";
    current_neighborhood = "";
    active_modes.clear();


    let start_button = document.getElementById('start')
    if (start_button.classList.contains('active_item')){
        start_button.classList.remove('active_item');
        start_button.classList.add('inactive_item');
    }
    let stop_button = document.getElementById('stop');
    if (stop_button.classList.contains('active_item')){
        stop_button.classList.remove('active_item');
        stop_button.classList.add('inactive_item');
    }
});