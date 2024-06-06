#!/usr/bin/node

const id = process.argv[2];
const path = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(path, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
