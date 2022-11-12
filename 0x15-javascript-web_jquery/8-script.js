#!/usr/bin/node
const $ = window.$;
//  fetches and lists the title for all movies by using this URL:
// https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    for (const item of data.results) {
      $('#list_movies').append(`<li>${item.title}</li>`);
    }
  });
});
