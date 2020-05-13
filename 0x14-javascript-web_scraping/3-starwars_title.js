#!/usr/bin/node
// Script that reads and prints the content of a file.
const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
