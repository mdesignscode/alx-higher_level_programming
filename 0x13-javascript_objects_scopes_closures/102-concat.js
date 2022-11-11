#!/usr/bin/node
// concatenates 2 files
const fs = require('fs');
const file1 = process.argv.slice(2)[0];
const file2 = process.argv.slice(2)[1];
const file3 = process.argv.slice(2)[2];

const content1 = fs.readFileSync(file1, 'utf-8');
const content2 = fs.readFileSync(file2, 'utf-8');
fs.writeFileSync(file3, `${content1}${content2}`);
