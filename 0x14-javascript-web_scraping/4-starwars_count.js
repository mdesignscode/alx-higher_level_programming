#!/usr/bin/node
// prints the number of movies where the
// character “Wedge Antilles” is present
const request = require('request');
const url = process.argv.slice(2)[0];

request(url, (error, response) => {
  if (!error) {
    const results = JSON.parse(response.body).results;
    let present = 0;
    for (const key of results) {
      const characters = key.characters;
      for (const character of characters) {
        // if id is 18
        if (character.split('/')[5] === '18') {
          present += 1;
        }
      }
    }
    console.log(present);
  }
});
