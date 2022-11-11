#!/usr/bin/node
// imports an array and computes a new array
const { list } = require('./100-data');

const newList = list.map((i, j) => { return i * j; });
console.log(list);
console.log(newList);
