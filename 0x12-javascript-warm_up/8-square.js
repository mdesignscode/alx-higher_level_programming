#!/usr/bin/node
// prints a square

const size = Number(process.argv.slice(2)[0]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let x = '';
    for (let col = 0; col < size; col++) {
      x += 'X';
    }
    console.log(x);
  }
}
