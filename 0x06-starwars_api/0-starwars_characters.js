#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:

// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request

const req = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${movieId}/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    
    // Ensure characters data is available
    if (filmData && filmData.characters && filmData.characters.length > 0) {
      // Iterate through character URLs and fetch character names
      filmData.characters.forEach(characterUrl => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error fetching character:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Status Code:', charResponse.statusCode);
          } else {
            const characterData = JSON.parse(charBody);
            console.log('Character Name:', characterData.name);
          }
        });
      });
    } else {
      console.error('No character data found for this movie.');
    }
  }
});
