#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');
const url = process.argv.slice(2)[0];
const path = process.argv.slice(2)[1];

request(url, (error, response) => {
  if (!error) {
    const data = response.body;
    fs.writeFile(path, data, (err) => {
      if (err) { console.log(err); }
    });
  }
});
