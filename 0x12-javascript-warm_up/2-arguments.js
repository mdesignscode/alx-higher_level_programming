#!/usr/bin/node
// prints a message depending of the number of arguments passed:

const args = process.argv.slice(2);

if (!args.length) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
