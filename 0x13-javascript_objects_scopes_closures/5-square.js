#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// defines a square and inherits from Rectangle

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
