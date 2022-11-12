#!/usr/bin/node
const $ = window.$;
// fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    $('#character').text(data.name);
  });
});
