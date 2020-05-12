#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
