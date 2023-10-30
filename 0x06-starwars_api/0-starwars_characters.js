#!/usr/bin/node
const req = require('request');

function getRequest (url) {
  return new Promise((resolve, reject) => {
    req.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function fetchMovieAndCharacters (movieId) {
  try {
    const movieData = await getRequest(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characterPromises = movieData.characters.map(characterUrl =>
      getRequest(characterUrl).then(characterData => characterData.name)
    );

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(characterName => {
      console.log(`${characterName}`);
    });
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}

const movieId = process.argv[2];
fetchMovieAndCharacters(movieId);
