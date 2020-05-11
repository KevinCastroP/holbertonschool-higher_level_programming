#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

exports.esrever = function (list) {
  var arrayOne = list;
  var array2 = [];

  for (var i = arrayOne.length - 1; i >= 0; i--) {
    array2.push(arrayOne[i]);
  }
  return array2;
};
