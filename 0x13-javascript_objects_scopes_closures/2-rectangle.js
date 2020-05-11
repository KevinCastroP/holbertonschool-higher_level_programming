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
}

module.exports = Rectangle;
