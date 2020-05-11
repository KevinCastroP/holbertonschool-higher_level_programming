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
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const count = this.height;
    this.height = this.width;
    this.width = count;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
