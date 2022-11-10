#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const myList = process.argv.slice(2).map(function (n) { return Number(n); });

if (!myList.length || myList.length === 1) {
  console.log('0');
} else {
  const index = myList.indexOf(Math.max(...myList));
  myList.splice(index, 1);
  console.log(Math.max(...myList));
}
