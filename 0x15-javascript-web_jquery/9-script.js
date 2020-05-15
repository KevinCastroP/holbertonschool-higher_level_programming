// Fetches from https://fourtonfish.com/hellosalut/?lang=fr and
// displays the value of hello from that fetch in the HTML’s tag DIV#hello

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
