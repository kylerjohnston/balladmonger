(function balladGeneration() {
  var httpRequest;

  function getJSON() {
    httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = parseRequest;
    httpRequest.open('GET', '/json/ballad?' + Math.floor((Math.random() * 100) +2));
    httpRequest.send(null);
  }

  function parseRequest() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      var balladText = document.getElementById('ballad-text');
      if (httpRequest.status === 200) {
        var response = JSON.parse(httpRequest.responseText);
        var lines = [];
        var woodcut = document.getElementById('woodcut');
        response['lines'].forEach(function(i) {
          lines.push(i + '<br>');
        });
        balladText.innerHTML = lines.join('');
        woodcut.src = response['img'];
      }
      else {
        balladText.innerHTML = '<p>There was a problem with the request. Please try again.</p>';
      }
    }
  }

  var button = document.getElementById('new-ballad');
  button.onclick = getJSON;

  getJSON();
})();

(function footerDate() {
  var d = new Date();
  var dateSpan = document.getElementById('current-date');
  dateSpan.textContent = d.getFullYear();
})();
