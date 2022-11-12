#!/usr/bin/node
const $ = window.$;
// toggles the class of the <header> element when
// the user clicks on the tag DIV#toggle_header

$('#toggle_header').click(function () {
  const value = $('header').attr('class');
  if (value === 'green') {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
