#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const arg1 = process.argv.slice(2, 3)[0];
const arg2 = process.argv.slice(3, 4)[0];

console.log(`${arg1} is ${arg2}`);
