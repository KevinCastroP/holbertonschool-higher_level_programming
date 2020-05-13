#!/usr/bin/node
// Script that reads and prints the content of a file.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const dictCompletTodoUser = {};
    for (const todo of jsonBody) {
      if (todo.completed) {
        if (dictCompletTodoUser[todo.userId]) {
          dictCompletTodoUser[todo.userId] += 1;
        } else {
          dictCompletTodoUser[todo.userId] = 1;
        }
      }
    }
    console.log(dictCompletTodoUser);
  }
});
