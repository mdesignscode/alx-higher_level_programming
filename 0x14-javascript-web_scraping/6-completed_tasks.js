#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv.slice(2)[0];

request(url, (error, response) => {
  if (!error) {
    const listOfCompleted = JSON.parse(response.body).filter((a) => { return a.completed});
    const completed = {};
    for (const user of listOfCompleted) {
      const userCompleted = listOfCompleted.filter((u) => { return u.userId ===  user.userId})
      completed[user.userId] = userCompleted.length
    }
    console.log(completed);
  }
});
