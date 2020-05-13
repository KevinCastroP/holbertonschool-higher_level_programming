#!/usr/bin/node
// Script that reads and prints the content of a file.

const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

function writeFile (nameFile, data) {
  fs.writeFile(nameFile, data, 'utf8', (err) => {
    if (err) {
      return console.error(err);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    writeFile(fileName, body);
  }
});
