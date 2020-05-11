#!/usr/bin/node
/*
Creating an empty class Rectangle
*/

exports.nbOccurences = function (list, searchElement) {
  list.sort();

  let item = 0;
  for (const element of list) {
    if (element === searchElement) {
      item += 1;
    }
  }
  return item;
};
