#!/usr/bin/node
const $ = window.$;
// fetches from https://fourtonfish.com/hellosalut/?lang=fr and
// displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, (data) => { $('#hello').text(data.hello); });
});
