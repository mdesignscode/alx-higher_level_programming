#!/usr/bin/node
// computes and prints a factorial

const n = Number(process.argv.slice(2, 3)[0]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  }

  return factorial(n - 1) * n;
}

console.log(factorial(n));
