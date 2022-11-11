#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

let c = 0;
exports.logMe = (item) => {
  console.log(`${c}: ${item}`);

  c += 1;
};
