#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

exports.esrever = function (list) {
  const arrayOne = list;
  const array2 = [];

  for (let i = arrayOne.length - 1; i >= 0; i--) {
    array2.push(arrayOne[i]);
  }
  return array2;
};
