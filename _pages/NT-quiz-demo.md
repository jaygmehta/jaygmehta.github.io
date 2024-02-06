---
layout: page
# permalink: /contact/
title: Number Theory Questions
description: For Problem Solving (NET and NBHM)
nav: false
nav_order: 8
toc:
  sidebar: left
---
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
<div style='transform: scale(0.65); position: relative; top: -150px;'>
  <h2>What fraction of a day is 6 hours?</h2>
  <h4>What fraction of a day is 6 hours?</h4>
  <p>Choose 1 answer</p>
  <hr />

  <div id='block-11' style='padding: 1.0px;'>
    <label for='option-11' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 1.0px;'>
    <label for='option-12' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-12'></span>
  </div>
  <hr />

  <div id='block-13' style='padding: 1.0px;'>
    <label for='option-13' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-13'></span>
  </div>
  <hr />

  <div id='block-14' style='padding: 1.0px;'>
    <label for='option-14' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-14'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="riCorrect" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="riIncorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

  <h2>What fraction of a day is 5 hours?</h2>
  <p>Choose 1 answer</p>
  <hr />

  <div id='block-21' style='padding: 1.0px;'>
    <label for='option-21' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-21'></span>
  </div>
  <hr />

  <div id='block-22' style='padding: 1.0px;'>
    <label for='option-22' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-22'></span>
  </div>
  <hr />

  <div id='block-23' style='padding: 1.0px;'>
    <label for='option-23' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='1/3' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-23'></span>
  </div>
  <hr />

  <div id='block-24' style='padding: 1.0px;'>
    <label for='option-24' style=' padding: .5px; font-size: 1.5rem;'>
      <input type='checkbox' name='option' value='1/6' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-24'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer2()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r2Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r2Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<!-- <a id='showanswer1'></a> -->
<script>
  //    The function evaluates the answer and displays result
  function displayAnswer1() {
    ri_addClass(document.getElementById('riCorrect'), 'riHide', );
  ri_addClass(document.getElementById('riIncorrect'), 'riHide', );
    if (document.getElementById('option-11').checked
    && !document.getElementById('option-12').checked
    && document.getElementById('option-13').checked
    && !document.getElementById('option-14').checked
    ) {
      ri_removeClass(document.getElementById('riCorrect'), 'riHide', )
    }
    else {
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
  function displayAnswer2() {
    ri_addClass(document.getElementById('r2Correct'), 'riHide', );
  ri_addClass(document.getElementById('r2Incorrect'), 'riHide', );
    if (document.getElementById('option-21').checked
    && !document.getElementById('option-22').checked
    && !document.getElementById('option-23').checked
    && document.getElementById('option-24').checked
    ) {
      r2_removeClass(document.getElementById('r2Correct'), 'riHide', )
    }
    else {
    r2_removeClass(document.getElementById('r2Incorrect'), 'riHide', );
  }
  }
   function r2_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r2_addClass(ele, cls) {
  if (!ri_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r2_removeClass(ele, cls) {
  if (r2_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
  // the functon displays the link to the correct answer
//   function showCorrectAnswer1() {
//     let showAnswer1 = document.createElement('p')
//     // showAnswer1.innerHTML = 'Show Corrent Answer'
//     showAnswer1.style.position = 'relative'
//     showAnswer1.style.top = '-180px'
//     showAnswer1.style.fontSize = '1.75rem'
//     document.getElementById('showanswer1').appendChild(showAnswer1)
//     showAnswer1.addEventListener('click', () => {
//       document.getElementById('block-11').style.border = '3px solid limegreen'
//       document.getElementById('result-11').style.color = 'limegreen'
//       document.getElementById('result-11').innerHTML = 'Correct!'
//       document.getElementById('showanswer1').removeChild(showAnswer1)
//     })
//   }
</script>
<html/>