#!/usr/bin/node
// display the status code of a GET request?
const request = require('request');
const link = process.argv.slice(2)[0];

request(link, (e, r) => {
  console.log(`code: ${r.statusCode}`);
});
