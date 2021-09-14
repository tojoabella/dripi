/* how to account for intersections? multiple points?*/
export default function road_identity(coord) {
    const API_KEY = 'AIzaSyCBR3urEI8Mfxrcji7c42ZcsDGUoCXwK8A';
  
    let request = 'https://roads.googleapis.com/v1/nearestRoads?points=';
    request = request + coord.latitude + '%2C' + coord.longitude;
    request = request + '&key=' + API_KEY;
    
    let axios = require('axios');
    let config = {
      method: 'get',
      url: request,
      headers: { }
    };
    axios(config)
    .then(function (response) {
      response = JSON.stringify(response.data)
      console.log(response);
      return response;
    })
    .catch(function (error) {
      console.log(error);
      return error;
    });
  }