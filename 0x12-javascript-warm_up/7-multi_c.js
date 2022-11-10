#!/usr/bin/node
// prints x times “C is fun”

const times = Number(process.argv.slice(2)[0]);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < times; index++) {
    console.log('C is fun');
  }
}
