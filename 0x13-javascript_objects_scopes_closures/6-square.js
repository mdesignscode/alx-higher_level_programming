#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// defines a square and inherits from Rectangle

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let row = 0; row < this.size; row++) {
      const l = c || 'X';
      let x = '';
      for (let col = 0; col < this.size; col++) {
        x += l;
      }
      console.log(x);
    }
  }
}
module.exports = Square;
