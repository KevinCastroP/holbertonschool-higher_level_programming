#!/usr/bin/node
// Script that reads and prints the content of a file.
const fs = require('fs');
const file = process.argv[2];
const stringg = process.argv[3];

fs.writeFile(file, stringg, 'utf8', function write (err) {
  if (err) {
    console.log(err);
  }
});
