#!/usr/bin/node
// prints the title of a Star Wars movie where the
// episode number matches a given integer

const request = require('request');
const id = process.argv.slice(2)[0];
const link = 'https://swapi-api.hbtn.io/api/films/' + id;

request(link, (e, r) => {
  console.log(JSON.parse(r.body).title);
});
