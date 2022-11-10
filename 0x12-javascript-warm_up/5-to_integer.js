#!/usr/bin/node
//  prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const myNumber = Number(process.argv.slice(2, 3)[0]);

if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNumber}`);
}
