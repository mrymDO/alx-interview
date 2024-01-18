#!/usr/bin/node

if (process.argv.length > 2) {
  const id = process.argv[2];
  const request = require('request');

  const getCharacterName = async (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, resp, body) => {
        if (err) reject(err);
        resolve(JSON.parse(body).name);
      });
    });
  };

  const API_URL = 'https://swapi-api.hbtn.io/api/films/' + id;

  (async () => {
    try {
      const body = await new Promise((resolve, reject) => {
        request(API_URL, (err, resp, body) => {
          if (err) reject(err);
          resolve(body);
        });
      });

      const charactersURL = JSON.parse(body).characters;
      const charactersName = await Promise.all(charactersURL.map(getCharacterName));

      console.log(charactersName.join('\n'));
    } catch (err) {
      console.log(err);
    }
  })();
}
