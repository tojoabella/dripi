import road_identity from './lib/road_identity.js';
export default function road_lengths() {
  let API_KEY = 'AIzaSyCBR3urEI8Mfxrcji7c42ZcsDGUoCXwK8A';
  let coordinate = {
    latitude:21.288795, 
    longitude: -157.830716
  }
  road = road_identity(coordinate)
  /*
  let request = 'https://roads.googleapis.com/v1/snapToRoads?path='
  
  var axios = require('axios');

  var config = {
    method: 'get',
    url: 'https://roads.googleapis.com/v1/snapToRoads?path=-35.27801%2C149.12958%7C-35.28032%2C149.12907%7C-35.28099%2C149.12929%7C-35.28144%2C149.12984%7C-35.28194%2C149.13003%7C-35.28282%2C149.12956%7C-35.28302%2C149.12881%7C-35.28473%2C149.12836&interpolate=true&key=YOUR_API_KEY',
    headers: { }
  };

  axios(config)
  .then(function (response) {
    console.log(JSON.stringify(response.data));
  })
  .catch(function (error) {
    console.log(error);
  });
  */
 return road;
  };