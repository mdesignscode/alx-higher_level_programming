#!/usr/bin/node
const $ = window.$;
// updates the text color of the <header> element to
// red (#FF0000) when the user clicks on the tag

$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
