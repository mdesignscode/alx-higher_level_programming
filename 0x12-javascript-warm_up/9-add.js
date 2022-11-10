#!/usr/bin/node
// prints the addition of 2 integers

const a = Number(process.argv.slice(2, 3)[0]);
const b = Number(process.argv.slice(3, 4)[0]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
