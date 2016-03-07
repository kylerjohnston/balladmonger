if(typeof jQuery === 'undefined') {
  document.write(unescape("%3Cscript src='/static/js/jquery-2.2.1.min.js' type='text/javascript'%3E%3C/script%3E"));
};

function newBallad() {
  var rand = Math.floor((Math.random() * 100) + 1);
  $.getJSON("/json/ballad?" + rand, function(data) {
    var lines = [];
    $.each(data['lines'], function(index, value) {
      lines.push(value + "<br />");
    });
    $("p.ballad-text").html(lines);
    $("img#woodcut").attr("src", data['img']);
  });
};

newBallad();

$("button#new-ballad").on("click", function() {
  newBallad();
});

$(function() {
  var d = new Date();
  $('span#current-date').text(d.getFullYear());
});
