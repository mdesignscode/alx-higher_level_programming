#!/usr/bin/node
// prints the first argument passed to it

const myArg = process.argv.slice(2, 3)[0];

if (!myArg) {
  console.log('No argument');
} else {
  console.log(myArg);
}
