/* MAP INFO */
import * as api_queries from "./api_queries.js";

/* GETS */
export const get_road_info = () => {
    let text = document.getElementById("road_name").textContent();
    return text;
};

export const get_locality_info = () => {
    let text = document.getElementById("locality_name").textContent();
    return text;
};

export const get_neighborhood_info = () => {
    let text = document.getElementById("neighborhood_name").textContent();
    return text;
};


/* UPDATES */
export const update_coordinates = (pos) => {
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    document.getElementById("coordinates").innerHTML = "Coordinates: " + latitude + ", " + longitude;
}
  
export const update_road_info_given_pos = (pos) =>{
    let road = api_queries.get_road(pos);
    document.getElementById("road_name").innerHTML = "Road: " + road;
}

export const update_road_info_given_road = (road) =>{
    document.getElementById("road_name").innerHTML = "Road: " + road;
}
  
export const update_locality_info_given_pos = (pos) =>{
    let localities = api_queries.get_localities(pos);
    document.getElementById("locality_name").innerHTML = "Localities: " + localities;
}

export const update_locality_info_given_localities = (localities) =>{
    document.getElementById("locality_name").innerHTML = "Localities: " + localities;
}
  
export const update_neighborhood_info_given_pos = (pos) =>{
    let neighborhood = api_queries.get_neighborhood(pos);
    if (neighborhood != null) {
        document.getElementById("neighborhood_name").innerHTML = "Neighborhood: " + neighborhood;
    }
    else{
        document.getElementById("neighborhood_name").innerHTML = "Neighborhood: NONE";
    }
 }

 export const update_neighborhood_info_given_neighborhood = (neighborhood) =>{
    document.getElementById("neighborhood_name").innerHTML = "Neighborhood: " + neighborhood;
 }
