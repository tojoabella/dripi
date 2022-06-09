/* API QUERIES */
  
export const get_road = (pos) => {
    /* get road */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_road?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    console.log(response);
    return response;
};
  
export const get_localities = (pos) => {
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
  
export const get_neighborhood = (pos) => {
    /* get neighborhood */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_neighborhood?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    console.log(response);
    return response;
};
  