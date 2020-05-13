#!/usr/bin/node
// Script that reads and prints the content of a file.
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
