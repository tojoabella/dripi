/* MAP INFO */
export const add_coordinates = (pos) => {
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    document.getElementById("coordinates").innerHTML = "Coordinates: " + latitude + ", " + longitude;
  }
  
export const add_road_info = (pos) =>{
    let road = mode_1(pos);
    document.getElementById("road_name").innerHTML = "Road: " + road;
}
  
export const add_locality_info = (pos) =>{
    let localities = mode_2(pos);
    document.getElementById("locality_name").innerHTML = "Localities: " + localities;
}
  
export const add_neighborhood_info = (pos) =>{
    let neighborhood = mode_3(pos);
    if (neighborhood != null) {
    document.getElementById("neighborhood_name").innerHTML = "Neighborhood: " + neighborhood;
    }
    else{
        document.getElementById("neighborhood_name").innerHTML = "Neighborhood: NONE";
    }
 }
  
/* MODES */
  
export const mode_1 = (pos) => {
    /* get road */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_road?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    console.log(response);
    return response;
};
  
export const mode_2 = (pos) => {
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
    return text;
};
  
export const mode_3 = (pos) => {
    /* get neighborhood */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_neighborhood?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    console.log(response);
    return response;
};
  
export function round_number(num, dec) {
    return Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
  }
  
export function on_track_location_success(position){
    const pos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    };
    add_coordinates(pos);
    pos[lat] = round_number(pos[lat], 4);
    pos[lng] = round_number(pos[lng], 4);
    return pos;
}