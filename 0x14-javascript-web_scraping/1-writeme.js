#!/usr/bin/node
// writes a string to a file
const fs = require('fs');
const path = process.argv.slice(2)[0];
const data = process.argv.slice(2)[1];

fs.writeFile(path, data, (err) => {
  if (err) { console.log(err); }
});
