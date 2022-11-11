#!/usr/bin/node
// defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let x = '';
      for (let col = 0; col < this.width; col++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    this.height = [this.width, this.width = this.height][0];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
