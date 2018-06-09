var start = $('#timer_text').text();

setInterval(function() {
  if (start == 0) {
    start = 300;
  } else {
    start--;
  }
  $('#timer_text').text(start);
}, 1000);

