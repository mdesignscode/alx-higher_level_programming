#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
const file = process.argv.slice(2)[0];

fs.readFile(file, 'utf-8', (err, data) => {
  data ? console.log(data) : console.log(err);
});
