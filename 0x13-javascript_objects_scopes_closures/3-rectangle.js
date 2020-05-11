#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) &&
    w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let height = 0; height < this.height; height++) {
      console.log('#'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
