export function toggle_modes() {
    document.getElementById('mode1').addEventListener('click', () => {
        document.getElementById('side_bar').getElementsByTagName('li')[0].getElementsByTagName('a')[0].classList.toggle('active_item');
    });
};


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

export function mode_1(pos) {
    /* get road */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_road?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    return response;
    // document.getElementById("road_name").innerHTML = "Road: " + response;
};
  
export function mode_2(pos){
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
    // document.getElementById("locality_name").innerHTML = "Localities: " + text;
};
  
export function mode_3(pos){
    /* get neighborhood */
    let latitude = pos["lat"];
    let longitude = pos["lng"];
    let url = "http://127.0.0.1:5000//get_neighborhood?lat=" + latitude + "&lng=" + longitude;
    let response = httpGet(url);
    response = JSON.parse(response);
    console.log(response);
    return response;
    // document.getElementById("neighborhood_name").innerHTML = "Neighborhood: " + response;
};