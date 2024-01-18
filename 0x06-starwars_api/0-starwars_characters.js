#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data from the Star Wars API:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data from the Star Wars API. Status Code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
  } else {
    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data from the Star Wars API:', charError);
          process.exit(1);
        }

        if (charResponse.statusCode !== 200) {
          console.error('Failed to fetch character data from the Star Wars API. Status Code:', charResponse.statusCode);
          process.exit(1);
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  }
});
