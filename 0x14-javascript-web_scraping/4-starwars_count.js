#!/usr/bin/node
// Script that reads and prints the content of a file.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    let item = 0;
    for (const film of jsonBody.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          item += 1;
        }
      }
    }
    console.log(item);
  }
});
