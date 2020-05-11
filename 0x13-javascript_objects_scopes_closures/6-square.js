#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let height = 0; height < this.height; height++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
