---
layout: page
# permalink: /contact/
title: quiz2
description: For practice
nav: false
nav_order: 8
toc:
  sidebar: left
---

## First
<html>
    <head>
    <style type="text/css">
        .riHide {
  display: none;
}
.ri-alert-success {
  position: relative;
  padding: .75rem 1.25rem;
  margin: 1rem;
  border: 1px solid transparent;
  border-radius: .25rem;
  color: #155724;
  background-color: #d4edda;
  border-color: #c3e6cb;
}
.ri-alert-danger {
   position: relative;
  padding: .75rem 1.25rem;
  margin: 1rem;
  border: 1px solid transparent;
  border-radius: .25rem;
  color: #ce4f4f;
  background-color: #edd4d4;
  border-color: #edd4d4;
}
</style>
</head>
    <body>
<div style="margin:10px;">
  <h2>
    Choose 3 of the best selling albums in Australia?
  </h2>
  <form>
    <input type="checkbox" id="riItem1"> Bat out of Hell - Meatloaf<br>
    <input type="checkbox" id="riItem2"> Whispering Jack John Farmham<br>
    <input type="checkbox" id="riItem3"> 5 to 4 - Empire Between<br>
    <input type="checkbox" id="riItem4"> Back in Black - AC/DC<br>
  </form>
  <button id="riCheckanswer">
    Check Answer
  </button>
  <div id="riCorrect" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="riIncorrect" class="riHide ri-alert-danger">
    In-correct
  </div>
</div>
        <script language="JavaScript"  type="text/javascript">
(function() {
  // your page initialization code here
  // the DOM will be available here
  var e = document.getElementById('riCheckanswer');
  e.addEventListener('click', function(event) {
    fnCheckAnswer()
  });
})();
function fnCheckAnswer() {
  ri_addClass(document.getElementById('riCorrect'), 'riHide', );
  ri_addClass(document.getElementById('riIncorrect'), 'riHide', );
  if (
    document.getElementById('riItem1').checked &&
    document.getElementById('riItem2').checked &&
    !document.getElementById('riItem3').checked &&
    document.getElementById('riItem4').checked
  ) {
    ri_removeClass(document.getElementById('riCorrect'), 'riHide', );
  } else {
    ri_removeClass(document.getElementById('riIncorrect'), 'riHide', );
  }
}
function ri_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function ri_addClass(ele, cls) {
  if (!ri_hasClass(ele, cls)) ele.className += " " + cls;
}
function ri_removeClass(ele, cls) {
  if (ri_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
        </script>   
    </body>
</html>

## Second
