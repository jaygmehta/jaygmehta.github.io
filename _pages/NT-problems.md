---
layout: page
permalink: /nt/
title: Number Theory Problems
description: For Problem Solving (NET and NBHM)
nav: false
nav_order: 8
toc:
  sidebar: left
---
<head>
<style type="text/css">
.classname {
	box-shadow: inset 0px 1px 0px 0px #bee2f9;
	background-color: #63b8ee;
	border-top-left-radius: 3px;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;
	border-bottom-left-radius: 3px;
	text-indent: 0;
	border: 0.5px solid #3866a3;
	display:inline-block;
	color: #14396a;
	font-family: arial;
	/* font-size: 15px; */
  font-size: 13.5px;
	font-weight: bold;
	font-style: normal;
	height: 34px;
	/* line-height: 34px; */
  line-height: 24px;
	/* width: 133px; */
  width: 153px;
	text-decoration: none;
	text-shadow: 0px 1px 0px #7cacde;
	margin-top: 11px;
}
.classname:hover {
	background-color: #468ccf;
}
.classname:active {
	position: relative;
	top: 1px;
}
.css-input {
	margin-right: 25px;
     padding: .85em 1em;
     height: 40px;
     width: 150px;	
     border-width: 2px;
     border-color: #504f4f;
     background-color: #FFFFFF;
     color: #000000;
     border-style: solid;
     border-radius: 0px;
     box-shadow: -1px 2px 4px rgba(59,59,59,.86);
     text-shadow: -50px 0px 0px rgba(66,66,66,.0);
}
 .css-input:focus {
     outline:none;
}
.error-text{
  background: #F8D7DA;
  padding: 7px;
  border-radius: 3px;
  color: #8B3E46;
  border: 1px solid #F5C6CB;
  display: none;
  margin-bottom: 7px;
  font-weight: bold;
  width: 90%;
  text-align: center;
}

</style>


<form  onsubmit="return passcheck()">
	<div class="error-text">
	</div>
	<span style="font-size: 15px; font-weight: bold; font-family: 'Noto Sans', sans-serif; margin-right: 15px;">To download the Workshop (NWPSM-XIII) Session Transcript, click below:<br/> Enter Password: </span>
	<input type="Password" class="css-input" required id="pass1">
	<input type="submit" class="classname" value="Download Transcript!" >
</form>
<p>
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
<!-- <div style='transform: scale(0.65); position: relative; top: -190px;'> -->
<!-- <div style='transform: scale(0.75);'> -->

<h3>Dec 2023 (Part B)</h3>
  <p>
  <h5>Which one of the following is equal to
$1^{37}+2^{37}+3^{37}+\cdots + 88^{37}$ in $\mathbb Z/89\mathbb Z$?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2023op1' style='padding: .5px;'>
    <label for='option-dec2023op1' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2023op1' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(88\).</label>
  </div>
  <hr />

  <div id='block-dec2023op2' style='padding: .5px;'>
    <label for='option-dec2023op2' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2023op2' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(-88\).</label>
  </div>
  <hr />

  <div id='block-dec2023op3' style='padding: .5px;'>
    <label for='option-dec2023op3' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2023op3' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\).</label>
  </div>
  <hr />

  <div id='block-dec2023op4' style='padding: .5px;'>
    <label for='option-dec2023op4' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2023op4' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(0\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2023()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2023Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2023Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

<h3>Dec 2023 (Part C)</h3>
  <p>
  <h5>Let $n \in \mathbb Z$ be such that $n$ is
congruent to $1 \mod 7$ and $n$ is congruent to $4 \mod{15}$. Which of
the following statements are true.</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2023cop1' style='padding: .5px;'>
    <label for='option-dec2023cop1' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2023cop1' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $n$ is congruent to $1$ mod $3$</label>
  </div>
  <hr />

  <div id='block-dec2023cop2' style='padding: .5px;'>
    <label for='option-dec2023cop2' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2023cop2' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $n$ is congruent to $1$ mod $35$</label>
  </div>
  <hr />

  <div id='block-dec2023cop3' style='padding: .5px;'>
    <label for='option-dec2023cop3' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2023cop3' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $n$ is congruent to $1$ mod $21$</label>
  </div>
  <hr />

  <div id='block-dec2023cop4' style='padding: .5px;'>
    <label for='option-dec2023cop4' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2023cop4' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $n$ is congruent to $1$ mod $5$</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2023c()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2023cCorrect" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2023cIncorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

<h3>Sep 2022 (Part C) Q-84</h3>
  <p>
  <h5>Consider the function \(f(n) = n^5 - 2n^3 + n\), where \(n\) is a positive integer. Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-sep2022Q841' style='padding: .5px;'>
    <label for='option-sep2022Q841' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q841' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For every positive integer \(k\), there exists a positive integer \(n\) such that \(f(n)\) is divisible by \(2^k\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q842' style='padding: .5px;'>
    <label for='option-sep2022Q842' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q842' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(f(n)\) is even for every integer \(n \ge 20\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q843' style='padding: .5px;'>
    <label for='option-sep2022Q843' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q843' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For every integer \(n \ge 20\), either \(f(n)\) is odd or \(f(n)\) is divisible by \(4\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q844' style='padding: .5px;'>
    <label for='option-sep2022Q844' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q844' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For every odd integer \(n \ge 21\), \(f(n)\) is divisible by \(64\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswersep2022Q84()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rsep2022Q84Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rsep2022Q84Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

<h3>Sep 2022 (Part C) Q-83</h3>
  <p>
  <h5>Let \(a\) and \(b\) be positive integers with \(a > b\) and \(a+b=24\). Suppose that the following congruences have a common integer solution.
$$2x \equiv 3a \pmod 5, \ x \equiv 4b \pmod 5.$$
Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-sep2022Q831' style='padding: .5px;'>
    <label for='option-sep2022Q831' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q831' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(10 \le a-b \le 20\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q832' style='padding: .5px;'>
    <label for='option-sep2022Q832' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q832' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(3b > a > 2b\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q833' style='padding: .5px;'>
    <label for='option-sep2022Q833' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q833' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(a > 3b\).</label>
  </div>
  <hr />

  <div id='block-sep2022Q834' style='padding: .5px;'>
    <label for='option-sep2022Q834' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-sep2022Q834' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(a-b\) is divisible by \(5\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswersep2022Q83()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rsep2022Q83Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rsep2022Q83Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

  <h3>Feb 2022 (Part C) Q-85</h3>
  <p>
  <h5>Let \(p\) be a prime and \(N_p\) be the number of pairs of positive integers \((x,y)\) such that such that \(\frac{1}{x} + \frac{1}{y} = \frac{1}{p^4}\). Which among the following are possible values of \(N_p\)?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-feb2022Q851' style='padding: .5px;'>
    <label for='option-feb2022Q851' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q851' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(0\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q852' style='padding: .5px;'>
    <label for='option-feb2022Q852' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q852' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(4\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q853' style='padding: .5px;'>
    <label for='option-feb2022Q853' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q853' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(5\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q854' style='padding: .5px;'>
    <label for='option-feb2022Q854' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q854' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(9\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerfeb2022Q85()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rfeb2022Q85Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rfeb2022Q85Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>

  <h3>Feb 2022 (Part C) Q-84</h3>
  <p>
  <h5>For a positive integer \(n\), let \(\Omega(n)\) denote the number of prime factors of \(n\) counted with multiplicity. For instance, \(\Omega(3) = 1\), \(\Omega(6) = \Omega(9) = 2\). Let \(p > 3\) be a prime number and let \(N = p(p+2)(p+4)\). Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-feb2022Q841' style='padding: 0.5px;'>
    <label for='option-feb2022Q841' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q841' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\Omega(N) \ge 3\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q842' style='padding: 0.5px;'>
    <label for='option-feb2022Q842' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q842' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists primes \(p > 3\) such that \(\Omega(N) = 3\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q843' style='padding: 0.5px;'>
    <label for='option-feb2022Q843' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q843' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(p\) can never be the smallest prime divisor of \(N\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q844' style='padding: 0.5px;'>
    <label for='option-feb2022Q844' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q844' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(p\) can be the smallest prime divisor of \(N\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerfeb2022Q84()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rfeb2022Q84Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rfeb2022Q84Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Feb 2022 (Part C) Q-83</h3>
  <p>
  <h5>A positive integer \(n\) coprime to \(17\) is called a primitive root modulo \(17\) if \(n^k - 1\) is not divisible by \(17\) for all \(k\) with \(1 \le k \le 16\). Let \(a,b\) be distinct positive integers between \(1\) and \(16\). Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-feb2022Q831' style='padding: 0.5px;'>
    <label for='option-feb2022Q831' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q831' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\) is a primitive root modulo \(17\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q832' style='padding: 0.5px;'>
    <label for='option-feb2022Q832' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q832' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      If \(a\) is a primitive root modulo \(17\) then \(a^2\) is not necessarily a primitive root modulo \(17\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q833' style='padding: 0.5px;'>
    <label for='option-feb2022Q833' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q833' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      If \(a, b\) are primitive roots modulo \(17\), then \(ab\) is a primitive root modulo \(17\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q834' style='padding: 0.5px;'>
    <label for='option-feb2022Q834' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-feb2022Q834' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      Product of primitive roots modulo \(17\) between \(1\) to \(16\) is congruent to \(1\) modulo \(17\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerfeb2022Q83()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rfeb2022Q83Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rfeb2022Q83Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Feb 2022 (Part B) Q-37</h3>
  <p>
  <h5>Let \(S = \{n : 1\le n \le 999;\ 3 \mid n \text{ or } 37 \mid n\}\). How many integers are there in the set \(S^c = \{n : 1 \le n \le 999;\ n\not\in S\}\)?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-feb2022Q371' style='padding: 0.5px;'>
    <label for='option-feb2022Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-feb2022Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(639\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q372' style='padding: 0.5px;'>
    <label for='option-feb2022Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-feb2022Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(648\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q373' style='padding: 0.5px;'>
    <label for='option-feb2022Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-feb2022Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(666\)</label>
  </div>
  <hr />

  <div id='block-feb2022Q374' style='padding: 0.5px;'>
    <label for='option-feb2022Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-feb2022Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(909\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerfeb2022Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rfeb2022Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rfeb2022Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>30Nov20 (Part C) Q-85</h3>
  <p>
  <h5>For positive integers \(m\) and \(n\), let \(\gcd(m,n)\) denote their greatest common divisor. Let \(m > n\) be such that \(\gcd(m,n) =1\). Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-30nov2020Q851' style='padding: 0.5px;'>
    <label for='option-30nov2020Q851' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q851' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\gcd(m-n,m+n) = 1\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q852' style='padding: 0.5px;'>
    <label for='option-30nov2020Q852' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q852' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\gcd(m-n,m+n)\) can have a prime divisor</label>
  </div>
  <hr />

  <div id='block-30nov2020Q853' style='padding: 0.5px;'>
    <label for='option-30nov2020Q853' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q853' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists integers \(x,y\) such that \(nx-my = 3\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q854' style='padding: 0.5px;'>
    <label for='option-30nov2020Q854' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q854' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\gcd(m-n,m+n)\) can be an odd prime</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer30nov2020Q85()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r30nov2020Q85Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r30nov2020Q85Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>30Nov20 (Part C) Q-84</h3>
  <p>
  <h5>For a positive integer \(n\), let \(\varphi(n)\) be the Euler's \(\varphi\)-function. Which of the following statements are true for \(n > 3\)?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-30nov2020Q841' style='padding: 0.5px;'>
    <label for='option-30nov2020Q841' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q841' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\varphi(n)\) can never divided \(n\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q842' style='padding: 0.5px;'>
    <label for='option-30nov2020Q842' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q842' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\varphi(n) \mid n \Rightarrow\) there exists integers \(x,y\) such that \(nx+6y = 1\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q843' style='padding: 0.5px;'>
    <label for='option-30nov2020Q843' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q843' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\varphi(n) \mid n \Rightarrow\) \(n\) can have at most two distinct prime divisors</label>
  </div>
  <hr />

  <div id='block-30nov2020Q844' style='padding: 0.5px;'>
    <label for='option-30nov2020Q844' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q844' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\varphi(n) \mid \varphi(nk)\) for every positive integer \(k\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer30nov2020Q84()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r30nov2020Q84Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r30nov2020Q84Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>30Nov20 (Part C) Q-83</h3>
  <p>
  <h5>Let \(\mathbb N = \{1,2,\ldots\}\) denote the set of positive integers. For \(n \in \mathbb N\), let 
$$A_n = \{(x,y,z) \in \mathbb N^3 : x^n + y^n = z^n \text{ and } z< n\}.$$
Let \(F_n\) be the cardinality of the set \(A_n\). Which of the following statements are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-30nov2020Q831' style='padding: 0.5px;'>
    <label for='option-30nov2020Q831' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q831' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(F(n)\) is finite for \(n \ge 3\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q832' style='padding: 0.5px;'>
    <label for='option-30nov2020Q832' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q832' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(F(2) = \infty\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q833' style='padding: 0.5px;'>
    <label for='option-30nov2020Q833' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q833' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(F(n) = 0\) for all \(n\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q834' style='padding: 0.5px;'>
    <label for='option-30nov2020Q834' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-30nov2020Q834' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(F(n)\) is non zero for some \(n > 2\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer30nov2020Q83()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r30nov2020Q83Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r30nov2020Q83Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>30Nov20 (Part B) Q-37</h3>
  <p>
  <h5>The last two digits of \(3^{2019}\) are?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-30nov2020Q371' style='padding: 0.5px;'>
    <label for='option-30nov2020Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-30nov2020Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(27\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q372' style='padding: 0.5px;'>
    <label for='option-30nov2020Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-30nov2020Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(37\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q373' style='padding: 0.5px;'>
    <label for='option-30nov2020Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-30nov2020Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(57\)</label>
  </div>
  <hr />

  <div id='block-30nov2020Q374' style='padding: 0.5px;'>
    <label for='option-30nov2020Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-30nov2020Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(67\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer30nov2020Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r30nov2020Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r30nov2020Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>26Nov20 (Part C) Q-88</h3>
  <p>
  <h5>Let $p$ be an odd prime such that $p \equiv 2 \pmod 3$. Let $\mathbb F_p$ be the field with $p$ elements. Consider the subset $E$ of $\mathbb F_p \times \mathbb F_p$ given by $E =\{(x,y) \in \mathbb F_p \times \mathbb F_p : y^2 = x^3 + 1\}$. Which of the following are true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-26nov2020Q881' style='padding: 0.5px;'>
    <label for='option-26nov2020Q881' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-26nov2020Q881' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $E$ has at least two elements</label>
  </div>
  <hr />

  <div id='block-26nov2020Q882' style='padding: 0.5px;'>
    <label for='option-26nov2020Q882' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-26nov2020Q882' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $E$ has at most $2p$ elements</label>
  </div>
  <hr />

  <div id='block-26nov2020Q883' style='padding: 0.5px;'>
    <label for='option-26nov2020Q883' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-26nov2020Q883' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $E$ can have $p^2$ elements</label>
  </div>
  <hr />

  <div id='block-26nov2020Q884' style='padding: 0.5px;'>
    <label for='option-26nov2020Q884' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-26nov2020Q884' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      $E$ has at least $2p$ elements</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer26nov2020Q88()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r26nov2020Q88Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r26nov2020Q88Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>26Nov20 (Part A) Q-18</h3>
  <p>
  <h5>The sum of first \(n\) even integers is</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-26nov2020Q181' style='padding: 0.5px;'>
    <label for='option-26nov2020Q181' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q181' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      divisible by \(n\) and not \(n+1\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q182' style='padding: 0.5px;'>
    <label for='option-26nov2020Q182' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q182' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      divisible by \(n+1\) and not \(n\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q183' style='padding: 0.5px;'>
    <label for='option-26nov2020Q183' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q183' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      divisible by both \(n\) and \(n+1\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q184' style='padding: 0.5px;'>
    <label for='option-26nov2020Q184' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q184' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      neither divisible by \(n\) nor by \(n+1\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer26nov2020Q18()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r26nov2020Q18Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r26nov2020Q18Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>26Nov20 (Part B) Q-37</h3>
  <p>
  <h5>Which of the following is true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-26nov2020Q371' style='padding: 0.5px;'>
    <label for='option-26nov2020Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      Every even integer \(n \ge 16\) divides \((n-1)!+3\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q372' style='padding: 0.5px;'>
    <label for='option-26nov2020Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      Every odd integer \(n \ge 16\) divides \((n-1)!\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q373' style='padding: 0.5px;'>
    <label for='option-26nov2020Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      Every even integer \(n \ge 16\) divides \((n-1)!\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q374' style='padding: 0.5px;'>
    <label for='option-26nov2020Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For every even integer \(n \ge 16\), \(n^2\) divides \(n!+1\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer26nov2020Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r26nov2020Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r26nov2020Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>26Nov20 (Part B) Q-39</h3>
  <p>
  <h5>Let \(\varphi(n)\) be the cardinality of the set \(\{a \mid 1 \le a \le n, \ (a,n) = 1\}\), where \((a,n)\) denotes the gcd of \(a\) and \(n\). Which of the following is NOT true?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-26nov2020Q391' style='padding: 0.5px;'>
    <label for='option-26nov2020Q391' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q391' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists infinitely many \(n\) such that \(\varphi(n) > \varphi(n+1)\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q392' style='padding: 0.5px;'>
    <label for='option-26nov2020Q392' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q392' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists infinitely many \(n\) such that \(\varphi(n) < \varphi(n+1)\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q393' style='padding: 0.5px;'>
    <label for='option-26nov2020Q393' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q393' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists \(N \in \mathbb N\) such that \(N > 2\) and for all \(n > N\), \(\varphi(N) < \varphi(n)\)</label>
  </div>
  <hr />

  <div id='block-26nov2020Q394' style='padding: 0.5px;'>
    <label for='option-26nov2020Q394' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-26nov2020Q394' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      The set \(\left\{\frac{\varphi(n)}{n} : n \in \mathbb N\right\}\) has finitely many limit points</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer26nov2020Q39()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="r26nov2020Q39Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="r26nov2020Q39Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2019 (Part A) Q-07</h3>
  <p>
  <h5>The difference between  the squares of two consecutive integers is \(408235\). The sum of the numbers is</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2019Q071' style='padding: 0.5px;'>
    <label for='option-dec2019Q071' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2019Q071' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(16324\)</label>
  </div>
  <hr />

  <div id='block-dec2019Q072' style='padding: 0.5px;'>
    <label for='option-dec2019Q072' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2019Q072' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(27061\)</label>
  </div>
  <hr />

  <div id='block-dec2019Q073' style='padding: 0.5px;'>
    <label for='option-dec2019Q073' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2019Q073' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(180235\)</label>
  </div>
  <hr />

  <div id='block-dec2019Q074' style='padding: 0.5px;'>
    <label for='option-dec2019Q074' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2019Q074' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(408235\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2019Q07()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2019Q07Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2019Q07Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>
<p>
  <h3>Jun 2019 (Part B) Q-37</h3>
  <p>
  <h5>For any integer $n \ge 1$, let <br>
$d(n) = $ number of positive divisors of $n$ <br>
$\nu(n) = $ number of distinct prime divisors of $n$<br>
$\omega(n) = $ number of prime divisors of $n$ counted with multiplicity.<br>

[For example, if $p$ is a prime, then $d(p) = 2, \nu(p) = \nu(p^2) = 1, \omega(p^2)=2$]. </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2019Q371' style='padding: 0.5px;'>
    <label for='option-june2019Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2019Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      If $n \ge 1000$ and $\omega(n) \ge 2$, then $d(n) > \log n$</label>
  </div>
  <hr />

  <div id='block-june2019Q372' style='padding: 0.5px;'>
    <label for='option-june2019Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2019Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      there exists $n$ such that $d(n) > 3 \sqrt{n}$</label>
  </div>
  <hr />

  <div id='block-june2019Q373' style='padding: 0.5px;'>
    <label for='option-june2019Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2019Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For every $n$, $2^{\nu(n)} \le d(n) \le 2^{\omega(n)}$</label>
  </div>
  <hr />

  <div id='block-june2019Q374' style='padding: 0.5px;'>
    <label for='option-june2019Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2019Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      if $\omega(n) = \omega(m)$, then $d(n) = d(m)$</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2019Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2019Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2019Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2019 (Part C) Q-83</h3>
  <p>
  <h5>Let \(a \in \mathbb Z\) be such that \(a=b^2 +c^2\), where \(b,c \in \mathbb Z \smallsetminus \{0\}\). Then \(a\) cannot be written as </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2019Q831' style='padding: 0.5px;'>
    <label for='option-june2019Q831' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2019Q831' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(pd^2\), where \(d \in \mathbb Z\) and \(p\) is a prime with \(p \equiv 1 \pmod 4\)</label>
  </div>
  <hr />

  <div id='block-june2019Q832' style='padding: 0.5px;'>
    <label for='option-june2019Q832' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2019Q832' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(pd^2\), where \(d \in \mathbb Z\) and \(p\) is a prime with \(p \equiv 3 \pmod 4\)</label>
  </div>
  <hr />

  <div id='block-june2019Q833' style='padding: 0.5px;'>
    <label for='option-june2019Q833' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2019Q833' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(pqd^2\), where \(d \in \mathbb Z\) and \(p,q\) are primes with \(p \equiv 1 \pmod 4\), \(q \equiv 3 \pmod 4\)</label>
  </div>
  <hr />

  <div id='block-june2019Q834' style='padding: 0.5px;'>
    <label for='option-june2019Q834' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2019Q834' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(pqd^2\), where \(d \in \mathbb Z\) and \(p,q\) are primes with \(p, q \equiv 3 \pmod 4\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2019Q83()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2019Q83Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2019Q83Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2018 (Part B) Q-39</h3>
  <p>
  <h5>Given integers \(a\) and \(b\), let \(N_{a,b}\) denote the number of positive integers \(k < 100\) such that \(k \equiv a \pmod 9\) and \(k \equiv b \pmod{11}\). Then which of the following statements is correct?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2018Q391' style='padding: 0.5px;'>
    <label for='option-dec2018Q391' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2018Q391' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(N_{a,b} =1\) for all integers \(a\) and \(b\).</label>
  </div>
  <hr />

  <div id='block-dec2018Q392' style='padding: 0.5px;'>
    <label for='option-dec2018Q392' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2018Q392' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists integers \(a\) and \(b\) satisfying \(N_{a,b} > 1\).</label>
  </div>
  <hr />

  <div id='block-dec2018Q393' style='padding: 0.5px;'>
    <label for='option-dec2018Q393' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2018Q393' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists integers \(a\) and \(b\) satisfying \(N_{a,b} =0\).</label>
  </div>
  <hr />

  <div id='block-dec2018Q394' style='padding: 0.5px;'>
    <label for='option-dec2018Q394' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2018Q394' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists integers \(a\) and \(b\) satisfying \(N_{a,b} =\) and there exists integers \(c\) and \(d\) satisfying \(N_{c,d} > 1\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2018Q39()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2018Q39Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2018Q39Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2017 (Part B) Q-37</h3>
  <p>
  <h5>Let \(f: (\mathbb Z/4\mathbb Z) \times (\mathbb Z/6\mathbb Z)\) be the function \(f(n) = (n \mod 4, n\mod 6)\).</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2017Q371' style='padding: 0.5px;'>
    <label for='option-dec2017Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2017Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \((0 \mod 4, 3 \mod 6)\) is in the image of \(f\)</label>
  </div>
  <hr />

  <div id='block-dec2017Q372' style='padding: 0.5px;'>
    <label for='option-dec2017Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2017Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \((a \mod 4, b \mod 6)\) is in the image of \(f\) for all even integers \(a\) and \(b\)</label>
  </div>
  <hr />

  <div id='block-dec2017Q373' style='padding: 0.5px;'>
    <label for='option-dec2017Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2017Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      image of \(f\) has exactly \(6\) elements</label>
  </div>
  <hr />

  <div id='block-dec2017Q374' style='padding: 0.5px;'>
    <label for='option-dec2017Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2017Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      kernel of \(f= 24\mathbb Z\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2017Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2017Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2017Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2017 (Part A) Q-03</h3>
  <p>
  <h5>What is the remainder when \(3^{256}\) is divided by \(5\)?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2017Q031' style='padding: 0.5px;'>
    <label for='option-june2017Q031' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q031' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(1\)</label>
  </div>
  <hr />

  <div id='block-june2017Q032' style='padding: 0.5px;'>
    <label for='option-june2017Q032' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q032' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\)</label>
  </div>
  <hr />

  <div id='block-june2017Q033' style='padding: 0.5px;'>
    <label for='option-june2017Q033' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q033' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(3\)</label>
  </div>
  <hr />

  <div id='block-june2017Q034' style='padding: 0.5px;'>
    <label for='option-june2017Q034' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q034' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(4\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2017Q03()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2017Q03Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2017Q03Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2017 (Part B) Q-37</h3>
  <p>
  <h5>Let \(S\) be the set of all integers from \(100\) to \(999\) which are neither divisible by \(3\) nor by \(5\). The number of elements in \(S\) is </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2017Q371' style='padding: 0.5px;'>
    <label for='option-june2017Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(480\)</label>
  </div>
  <hr />

  <div id='block-june2017Q372' style='padding: 0.5px;'>
    <label for='option-june2017Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(420\)</label>
  </div>
  <hr />

  <div id='block-june2017Q373' style='padding: 0.5px;'>
    <label for='option-june2017Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(360\)</label>
  </div>
  <hr />

  <div id='block-june2017Q374' style='padding: 0.5px;'>
    <label for='option-june2017Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(240\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2017Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2017Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2017Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2017 (Part B) Q-38</h3>
  <p>
  <h5>The remainder obtained when \(16^{2016}\) is divided by \(9\) equals </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2017Q381' style='padding: 0.5px;'>
    <label for='option-june2017Q381' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q381' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(1\)</label>
  </div>
  <hr />

  <div id='block-june2017Q382' style='padding: 0.5px;'>
    <label for='option-june2017Q382' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q382' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\)</label>
  </div>
  <hr />

  <div id='block-june2017Q383' style='padding: 0.5px;'>
    <label for='option-june2017Q383' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q383' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(3\)</label>
  </div>
  <hr />

  <div id='block-june2017Q384' style='padding: 0.5px;'>
    <label for='option-june2017Q384' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2017Q384' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(7\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2017Q38()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2017Q38Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2017Q38Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2016 (Part B) Q-37</h3>
  <p>
  <h5>Given a natural number \(n >1\) such that \((n-1)! \equiv -1 \pmod n\), we can conclude that </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2016Q371' style='padding: 0.5px;'>
    <label for='option-dec2016Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2016Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=p^k\) where \(p\) is prime, \(k>1\).</label>
  </div>
  <hr />

  <div id='block-dec2016Q372' style='padding: 0.5px;'>
    <label for='option-dec2016Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2016Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=pq\) where \(p\) and \(q\) are distinct primes.</label>
  </div>
  <hr />

  <div id='block-dec2016Q373' style='padding: 0.5px;'>
    <label for='option-dec2016Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2016Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=pqr\) where \(p,q,r\) are distinct primes.</label>
  </div>
  <hr />

  <div id='block-dec2016Q374' style='padding: 0.5px;'>
    <label for='option-dec2016Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2016Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=p\) where \(p\) is a prime.</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2016Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2016Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2016Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2016 (Part B) Q-37</h3>
  <p>
  <h5>Which of the following statements is FALSE? There exists an integer \(x\) such that </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-jun2016Q371' style='padding: 0.5px;'>
    <label for='option-jun2016Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2016Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(x \equiv 23 \pmod {1000}\) and \(x \equiv 45 \pmod {6789}\).</label>
  </div>
  <hr />

  <div id='block-jun2016Q372' style='padding: 0.5px;'>
    <label for='option-jun2016Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2016Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(x \equiv 23 \pmod {1000}\) and \(x \equiv 54 \pmod {6789}\).</label>
  </div>
  <hr />

  <div id='block-jun2016Q373' style='padding: 0.5px;'>
    <label for='option-jun2016Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2016Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(x \equiv 32 \pmod {1000}\) and \(x \equiv 54 \pmod {9876}\).</label>
  </div>
  <hr />

  <div id='block-jun2016Q374' style='padding: 0.5px;'>
    <label for='option-jun2016Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2016Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(x \equiv 32 \pmod {1000}\) and \(x \equiv 44 \pmod {9876}\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjun2016Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjun2016Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjun2016Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2015 (Part C) Q-80</h3>
  <p>
  <h5>Which of the following intervals contains an integer satisfying the following three congruences: <br/>
        \(x\equiv 2 \pmod 5\), \(x \equiv 3 \pmod 7\) and \(x \equiv 4 \pmod {11}\). </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2015Q801' style='padding: 0.5px;'>
    <label for='option-dec2015Q801' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2015Q801' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \([401,600]\)</label>
  </div>
  <hr />

  <div id='block-dec2015Q802' style='padding: 0.5px;'>
    <label for='option-dec2015Q802' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2015Q802' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \([601,800]\)</label>
  </div>
  <hr />

  <div id='block-dec2015Q803' style='padding: 0.5px;'>
    <label for='option-dec2015Q803' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2015Q803' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \([801,1000]\)</label>
  </div>
  <hr />

  <div id='block-dec2015Q804' style='padding: 0.5px;'>
    <label for='option-dec2015Q804' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2015Q804' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \([1001,1200]\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2015Q80()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2015Q80Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2015Q80Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2015 (Part C) Q-84</h3>
  <p>
  <h5>Which of the following primes satisfy the congruence <br/> \(a^{24} \equiv 6a +2 \mod {13}\)?</h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-jun2015Q841' style='padding: 0.5px;'>
    <label for='option-jun2015Q841' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2015Q841' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(41\)</label>
  </div>
  <hr />

  <div id='block-jun2015Q842' style='padding: 0.5px;'>
    <label for='option-jun2015Q842' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2015Q842' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(47\)</label>
  </div>
  <hr />

  <div id='block-jun2015Q843' style='padding: 0.5px;'>
    <label for='option-jun2015Q843' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2015Q843' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(67\)</label>
  </div>
  <hr />

  <div id='block-jun2015Q844' style='padding: 0.5px;'>
    <label for='option-jun2015Q844' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2015Q844' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(83\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjun2015Q84()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjun2015Q84Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjun2015Q84Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2014 (Part B) Q-33</h3>
  <p>
  <h5>If \(n\) is a positive integer such that sum of all positive integers \(a\) satisfying \(1 \le a \le n\) and GCD\((a,n)=1\) is equal to \(240 n\), then the number of summands, namely, \(\phi(n)\), is </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-jun2014Q331' style='padding: 0.5px;'>
    <label for='option-jun2014Q331' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2014Q331' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(120\)</label>
  </div>
  <hr />

  <div id='block-jun2014Q332' style='padding: 0.5px;'>
    <label for='option-jun2014Q332' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2014Q332' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(124\)</label>
  </div>
  <hr />

  <div id='block-jun2014Q333' style='padding: 0.5px;'>
    <label for='option-jun2014Q333' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2014Q333' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(240\)</label>
  </div>
  <hr />

  <div id='block-jun2014Q334' style='padding: 0.5px;'>
    <label for='option-jun2014Q334' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-jun2014Q334' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(480\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjun2014Q33()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjun2014Q33Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjun2014Q33Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2014 (Part C) Q-90</h3>
  <p>
  <h5>For positive integers \(m\) and \(n\), let \(F_n = 2^{2^n}+1\) and \(G_m= 2^{2^m}-1\). Which of the following are true? </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-jun2014Q901' style='padding: 0.5px;'>
    <label for='option-jun2014Q901' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2014Q901' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(F_n\) divides \(G_m\) whenever \(m>n\).</label>
  </div>
  <hr />

  <div id='block-jun2014Q902' style='padding: 0.5px;'>
    <label for='option-jun2014Q902' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2014Q902' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\gcd(F_n,G_m) = 1\) whenever \(m \neq n\).</label>
  </div>
  <hr />

  <div id='block-jun2014Q903' style='padding: 0.5px;'>
    <label for='option-jun2014Q903' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2014Q903' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\gcd(F_n,F_m) = 1\) whenever \(m \neq n\).</label>
  </div>
  <hr />

  <div id='block-jun2014Q904' style='padding: 0.5px;'>
    <label for='option-jun2014Q904' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-jun2014Q904' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(G_m\) divides \(F_n\) whenever \(m < n\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjun2014Q90()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjun2014Q90Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjun2014Q90Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2013 (Part B) Q-39</h3>
  <p>
  <h5>For any integers \(a, b\), let \(N_{a,b}\) denote the number of positive integers \(x < 1000\) such that \(x \equiv a \pmod {27}\) and \(x \equiv b \pmod{37}\). Then, </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2013Q391' style='padding: 0.5px;'>
    <label for='option-dec2013Q391' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2013Q391' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists \(a,b\) such that \(N_{a,b} =0\).</label>
  </div>
  <hr />

  <div id='block-dec2013Q392' style='padding: 0.5px;'>
    <label for='option-dec2013Q392' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2013Q392' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For all \(a,b\), \(N_{a,b} = 1\).</label>
  </div>
  <hr />

  <div id='block-dec2013Q393' style='padding: 0.5px;'>
    <label for='option-dec2013Q393' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2013Q393' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      For all \(a,b\), \(N_{a,b} > 1\).</label>
  </div>
  <hr />

  <div id='block-dec2013Q394' style='padding: 0.5px;'>
    <label for='option-dec2013Q394' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2013Q394' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      There exists \(a, b\) such that \(N_{a,b} =1\) and there exists \(a,b\) such that \(N_{a,b}=2 \).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2013Q39()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2013Q39Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2013Q39Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2013 (Part A) Q-08</h3>
  <p>
  <h5>What is the last digit of \(7^{73}\)? </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2013Q081' style='padding: 0.5px;'>
    <label for='option-june2013Q081' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2013Q081' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(7\)</label>
  </div>
  <hr />

  <div id='block-june2013Q082' style='padding: 0.5px;'>
    <label for='option-june2013Q082' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2013Q082' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(9\)</label>
  </div>
  <hr />

  <div id='block-june2013Q083' style='padding: 0.5px;'>
    <label for='option-june2013Q083' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2013Q083' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(3\)</label>
  </div>
  <hr />

  <div id='block-june2013Q084' style='padding: 0.5px;'>
    <label for='option-june2013Q084' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2013Q084' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(1\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2013Q08()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2013Q08Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2013Q08Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2013 (Part C) Q-95</h3>
  <p>
  <h5>Consider the congruence \(x^n \equiv 2 \pmod {13}\). This congruence has a solution for \(x\) if </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2013Q951' style='padding: 0.5px;'>
    <label for='option-june2013Q951' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2013Q951' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=5\)</label>
  </div>
  <hr />

  <div id='block-june2013Q952' style='padding: 0.5px;'>
    <label for='option-june2013Q952' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2013Q952' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=6\)</label>
  </div>
  <hr />

  <div id='block-june2013Q953' style='padding: 0.5px;'>
    <label for='option-june2013Q953' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2013Q953' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=7\)</label>
  </div>
  <hr />

  <div id='block-june2013Q954' style='padding: 0.5px;'>
    <label for='option-june2013Q954' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-june2013Q954' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n=8\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2013Q95()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2013Q95Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2013Q95Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2012 (Part B) Q-37</h3>
  <p>
  <h5>The last two digits of \(7^{81}\) are </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2012Q371' style='padding: 0.5px;'>
    <label for='option-dec2012Q371' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2012Q371' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(07\)</label>
  </div>
  <hr />

  <div id='block-dec2012Q372' style='padding: 0.5px;'>
    <label for='option-dec2012Q372' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2012Q372' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(17\)</label>
  </div>
  <hr />

  <div id='block-dec2012Q373' style='padding: 0.5px;'>
    <label for='option-dec2012Q373' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2012Q373' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(37\)</label>
  </div>
  <hr />

  <div id='block-dec2012Q374' style='padding: 0.5px;'>
    <label for='option-dec2012Q374' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-dec2012Q374' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(47\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2012Q37()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2012Q37Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2012Q37Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Dec 2012 (Part C) Q-84</h3>
  <p>
  <h5>For positive integers \(m\), let \(\phi(m)\) denote the number of integer \(k\) such that \(1 \le k \le n\) and GCD\((k,m)=1\). Then which of the following statements are necessarily true? </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-dec2012Q841' style='padding: 0.5px;'>
    <label for='option-dec2012Q841' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2012Q841' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(\phi(n)\) divides \(n\) for every positive integer \(n\).</label>
  </div>
  <hr />

  <div id='block-dec2012Q842' style='padding: 0.5px;'>
    <label for='option-dec2012Q842' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2012Q842' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n\) divides \(\phi\big(a^n-1\big)\) for all positive integers \(a\) and \(n\).</label>
  </div>
  <hr />

  <div id='block-dec2012Q843' style='padding: 0.5px;'>
    <label for='option-dec2012Q843' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2012Q843' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(n\) divides \(\phi\big(a^n-1\big)\) for all positive integers \(a\) and \(n\) such that GCD\((a,n)=1\).</label>
  </div>
  <hr />

  <div id='block-dec2012Q844' style='padding: 0.5px;'>
    <label for='option-dec2012Q844' style=' padding: .5px; font-size: 1rem;'>
      <input type='checkbox' name='option' id='option-dec2012Q844' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(a\) divides \(\phi\big(a^n-1\big)\) for all positive integers \(a\) and \(n\) such that GCD\((a,n)=1\).</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerdec2012Q84()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rdec2012Q84Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rdec2012Q84Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2012 (Part B) Q-28</h3>
  <p>
  <h5>The last digit of \((38)^{2011}\) is </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2012Q281' style='padding: 0.5px;'>
    <label for='option-june2012Q281' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q281' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(6\)</label>
  </div>
  <hr />

  <div id='block-june2012Q282' style='padding: 0.5px;'>
    <label for='option-june2012Q282' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q282' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\)</label>
  </div>
  <hr />

  <div id='block-june2012Q283' style='padding: 0.5px;'>
    <label for='option-june2012Q283' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q283' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(4\)</label>
  </div>
  <hr />

  <div id='block-june2012Q284' style='padding: 0.5px;'>
    <label for='option-june2012Q284' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q284' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(8\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2012Q28()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2012Q28Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2012Q28Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2012 (Part B) Q-22</h3>
  <p>
  <h5>The number of positive divisors of \(50000\) is </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2012Q221' style='padding: 0.5px;'>
    <label for='option-june2012Q221' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q221' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(20\)</label>
  </div>
  <hr />

  <div id='block-june2012Q222' style='padding: 0.5px;'>
    <label for='option-june2012Q222' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q222' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(30\)</label>
  </div>
  <hr />

  <div id='block-june2012Q223' style='padding: 0.5px;'>
    <label for='option-june2012Q223' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q223' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(40\)</label>
  </div>
  <hr />

  <div id='block-june2012Q224' style='padding: 0.5px;'>
    <label for='option-june2012Q224' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2012Q224' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(50\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2012Q22()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2012Q22Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2012Q22Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2011 (Part B) Q-27</h3>
  <p>
  <h5>The number of elements in the set <br/>
\(\{m \mid 1 \le m \le 1000, m \text{ and } 1000 \text{ are relatively prime}\} \text { is}\) </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2011Q271' style='padding: 0.5px;'>
    <label for='option-june2011Q271' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q271' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(100\)</label>
  </div>
  <hr />

  <div id='block-june2011Q272' style='padding: 0.5px;'>
    <label for='option-june2011Q272' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q272' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(250\)</label>
  </div>
  <hr />

  <div id='block-june2011Q273' style='padding: 0.5px;'>
    <label for='option-june2011Q273' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q273' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(300\)</label>
  </div>
  <hr />

  <div id='block-june2011Q274' style='padding: 0.5px;'>
    <label for='option-june2011Q274' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q274' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(400\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2011Q27()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2011Q27Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2011Q27Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>

<p>
  <h3>Jun 2011 (Part B) Q-28</h3>
  <p>
  <h5>The unit digit of \(2^{100}\) is </h5>
  <!-- <p>Choose 1 answer</p> -->
  <hr />

  <div id='block-june2011Q281' style='padding: 0.5px;'>
    <label for='option-june2011Q281' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q281' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(2\)</label>
  </div>
  <hr />

  <div id='block-june2011Q282' style='padding: 0.5px;'>
    <label for='option-june2011Q282' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q282' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(4\)</label>
  </div>
  <hr />

  <div id='block-june2011Q283' style='padding: 0.5px;'>
    <label for='option-june2011Q283' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q283' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(6\)</label>
  </div>
  <hr />

  <div id='block-june2011Q284' style='padding: 0.5px;'>
    <label for='option-june2011Q284' style=' padding: .5px; font-size: 1rem;'>
      <input type='radio' name='option' id='option-june2011Q284' style='transform: scale(1.5); margin-right: 10px; vertical-align: middle; margin-top: -1px;' />
      \(8\)</label>
  </div>
  <hr />
  <button type='button' onclick='displayAnswerjune2011Q28()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
  <div id="rjune2011Q28Correct" class="riHide ri-alert-success">
    Correct
  </div>
  <div id="rjune2011Q28Incorrect" class="riHide ri-alert-danger">
    In-correct
  </div>


<!-- <a id='showanswer1'></a> -->
<script>
  //    The function evaluates the answer and displays result
  function displayAnswerdec2023() {
    rdec2023_addClass(document.getElementById('rdec2023Correct'), 'riHide', );
  rdec2023_addClass(document.getElementById('rdec2023Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2023op1').checked
    && !document.getElementById('option-dec2023op2').checked
    && !document.getElementById('option-dec2023op3').checked
    && document.getElementById('option-dec2023op4').checked
    ) {
      rdec2023_removeClass(document.getElementById('rdec2023Correct'), 'riHide', )
    }
    else {
    rdec2023_removeClass(document.getElementById('rdec2023Incorrect'), 'riHide', );
  }
  }
   function rdec2023_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2023_addClass(ele, cls) {
  if (!rdec2023_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2023_removeClass(ele, cls) {
  if (rdec2023_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2023c() {
    rdec2023c_addClass(document.getElementById('rdec2023cCorrect'), 'riHide', );
  rdec2023c_addClass(document.getElementById('rdec2023cIncorrect'), 'riHide', );
    if (document.getElementById('option-dec2023cop1').checked
    && !document.getElementById('option-dec2023cop2').checked
    && document.getElementById('option-dec2023cop3').checked
    && !document.getElementById('option-dec2023cop4').checked
    ) {
      rdec2023c_removeClass(document.getElementById('rdec2023cCorrect'), 'riHide', )
    }
    else {
    rdec2023c_removeClass(document.getElementById('rdec2023cIncorrect'), 'riHide', );
  }
  }
   function rdec2023c_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2023c_addClass(ele, cls) {
  if (!rdec2023c_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2023c_removeClass(ele, cls) {
  if (rdec2023c_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
  function displayAnswersep2022Q84() {
    rsep2022Q84_addClass(document.getElementById('rsep2022Q84Correct'), 'riHide', );
  rsep2022Q84_addClass(document.getElementById('rsep2022Q84Incorrect'), 'riHide', );
    if (document.getElementById('option-sep2022Q841').checked
    && document.getElementById('option-sep2022Q842').checked
    && !document.getElementById('option-sep2022Q843').checked
    && document.getElementById('option-sep2022Q844').checked
    ) {
      rsep2022Q84_removeClass(document.getElementById('rsep2022Q84Correct'), 'riHide', )
    }
    else {
    rsep2022Q84_removeClass(document.getElementById('rsep2022Q84Incorrect'), 'riHide', );
  }
  }
   function rsep2022Q84_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rsep2022Q84_addClass(ele, cls) {
  if (!rsep2022Q84_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rsep2022Q84_removeClass(ele, cls) {
  if (rsep2022Q84_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
  function displayAnswersep2022Q83() {
    rsep2022Q83_addClass(document.getElementById('rsep2022Q83Correct'), 'riHide', );
  rsep2022Q83_addClass(document.getElementById('rsep2022Q83Incorrect'), 'riHide', );
    if (document.getElementById('option-sep2022Q831').checked
    && !document.getElementById('option-sep2022Q832').checked
    && !document.getElementById('option-sep2022Q833').checked
    && document.getElementById('option-sep2022Q834').checked
    ) {
      rsep2022Q83_removeClass(document.getElementById('rsep2022Q83Correct'), 'riHide', )
    }
    else {
    rsep2022Q83_removeClass(document.getElementById('rsep2022Q83Incorrect'), 'riHide', );
  }
  }
   function rsep2022Q83_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rsep2022Q83_addClass(ele, cls) {
  if (!rsep2022Q83_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rsep2022Q83_removeClass(ele, cls) {
  if (rsep2022Q83_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
  function displayAnswerfeb2022Q85() {
    rfeb2022Q85_addClass(document.getElementById('rfeb2022Q85Correct'), 'riHide', );
  rfeb2022Q85_addClass(document.getElementById('rfeb2022Q85Incorrect'), 'riHide', );
    if (!document.getElementById('option-feb2022Q851').checked
    && !document.getElementById('option-feb2022Q852').checked
    && !document.getElementById('option-feb2022Q853').checked
    && document.getElementById('option-feb2022Q854').checked
    ) {
      rfeb2022Q85_removeClass(document.getElementById('rfeb2022Q85Correct'), 'riHide', )
    }
    else {
    rfeb2022Q85_removeClass(document.getElementById('rfeb2022Q85Incorrect'), 'riHide', );
  }
  }
   function rfeb2022Q85_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rfeb2022Q85_addClass(ele, cls) {
  if (!rfeb2022Q85_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rfeb2022Q85_removeClass(ele, cls) {
  if (rfeb2022Q85_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerfeb2022Q84() {
  rfeb2022Q84_addClass(document.getElementById('rfeb2022Q84Correct'), 'riHide', );
  rfeb2022Q84_addClass(document.getElementById('rfeb2022Q84Incorrect'), 'riHide', );
    if (document.getElementById('option-feb2022Q841').checked
    && !document.getElementById('option-feb2022Q842').checked
    && document.getElementById('option-feb2022Q843').checked
    && !document.getElementById('option-feb2022Q844').checked
    ) {
      rfeb2022Q84_removeClass(document.getElementById('rfeb2022Q84Correct'), 'riHide', )
    }
    else {
    rfeb2022Q84_removeClass(document.getElementById('rfeb2022Q84Incorrect'), 'riHide', );
  }
  }
   function rfeb2022Q84_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rfeb2022Q84_addClass(ele, cls) {
  if (!rfeb2022Q84_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rfeb2022Q84_removeClass(ele, cls) {
  if (rfeb2022Q84_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerfeb2022Q83() {
  rfeb2022Q83_addClass(document.getElementById('rfeb2022Q83Correct'), 'riHide', );
  rfeb2022Q83_addClass(document.getElementById('rfeb2022Q83Incorrect'), 'riHide', );
    if (!document.getElementById('option-feb2022Q831').checked
    && document.getElementById('option-feb2022Q832').checked
    && !document.getElementById('option-feb2022Q833').checked
    && document.getElementById('option-feb2022Q834').checked
    ) {
      rfeb2022Q83_removeClass(document.getElementById('rfeb2022Q83Correct'), 'riHide', )
    }
    else {
    rfeb2022Q83_removeClass(document.getElementById('rfeb2022Q83Incorrect'), 'riHide', );
  }
  }
   function rfeb2022Q83_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rfeb2022Q83_addClass(ele, cls) {
  if (!rfeb2022Q83_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rfeb2022Q83_removeClass(ele, cls) {
  if (rfeb2022Q83_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerfeb2022Q37() {
  rfeb2022Q37_addClass(document.getElementById('rfeb2022Q37Correct'), 'riHide', );
  rfeb2022Q37_addClass(document.getElementById('rfeb2022Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-feb2022Q371').checked
    && document.getElementById('option-feb2022Q372').checked
    && !document.getElementById('option-feb2022Q373').checked
    && !document.getElementById('option-feb2022Q374').checked
    ) {
      rfeb2022Q37_removeClass(document.getElementById('rfeb2022Q37Correct'), 'riHide', )
    }
    else {
    rfeb2022Q37_removeClass(document.getElementById('rfeb2022Q37Incorrect'), 'riHide', );
  }
  }
   function rfeb2022Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rfeb2022Q37_addClass(ele, cls) {
  if (!rfeb2022Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rfeb2022Q37_removeClass(ele, cls) {
  if (rfeb2022Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer30nov2020Q85() {
  r30nov2020Q85_addClass(document.getElementById('r30nov2020Q85Correct'), 'riHide', );
  r30nov2020Q85_addClass(document.getElementById('r30nov2020Q85Incorrect'), 'riHide', );
    if (!document.getElementById('option-30nov2020Q851').checked
    && document.getElementById('option-30nov2020Q852').checked
    && document.getElementById('option-30nov2020Q853').checked
    && !document.getElementById('option-30nov2020Q854').checked
    ) {
      r30nov2020Q85_removeClass(document.getElementById('r30nov2020Q85Correct'), 'riHide', )
    }
    else {
    r30nov2020Q85_removeClass(document.getElementById('r30nov2020Q85Incorrect'), 'riHide', );
  }
  }
   function r30nov2020Q85_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r30nov2020Q85_addClass(ele, cls) {
  if (!r30nov2020Q85_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r30nov2020Q85_removeClass(ele, cls) {
  if (r30nov2020Q85_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer30nov2020Q84() {
  r30nov2020Q84_addClass(document.getElementById('r30nov2020Q84Correct'), 'riHide', );
  r30nov2020Q84_addClass(document.getElementById('r30nov2020Q84Incorrect'), 'riHide', );
    if (!document.getElementById('option-30nov2020Q841').checked
    && !document.getElementById('option-30nov2020Q842').checked
    && document.getElementById('option-30nov2020Q843').checked
    && document.getElementById('option-30nov2020Q844').checked
    ) {
      r30nov2020Q84_removeClass(document.getElementById('r30nov2020Q84Correct'), 'riHide', )
    }
    else {
    r30nov2020Q84_removeClass(document.getElementById('r30nov2020Q84Incorrect'), 'riHide', );
  }
  }
   function r30nov2020Q84_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r30nov2020Q84_addClass(ele, cls) {
  if (!r30nov2020Q84_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r30nov2020Q84_removeClass(ele, cls) {
  if (r30nov2020Q84_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer30nov2020Q83() {
  r30nov2020Q83_addClass(document.getElementById('r30nov2020Q83Correct'), 'riHide', );
  r30nov2020Q83_addClass(document.getElementById('r30nov2020Q83Incorrect'), 'riHide', );
    if (document.getElementById('option-30nov2020Q831').checked
    && !document.getElementById('option-30nov2020Q832').checked
    && document.getElementById('option-30nov2020Q833').checked
    && !document.getElementById('option-30nov2020Q834').checked
    ) {
      r30nov2020Q83_removeClass(document.getElementById('r30nov2020Q83Correct'), 'riHide', )
    }
    else {
    r30nov2020Q83_removeClass(document.getElementById('r30nov2020Q83Incorrect'), 'riHide', );
  }
  }
   function r30nov2020Q83_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r30nov2020Q83_addClass(ele, cls) {
  if (!r30nov2020Q83_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r30nov2020Q83_removeClass(ele, cls) {
  if (r30nov2020Q83_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer30nov2020Q37() {
  r30nov2020Q37_addClass(document.getElementById('r30nov2020Q37Correct'), 'riHide', );
  r30nov2020Q37_addClass(document.getElementById('r30nov2020Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-30nov2020Q371').checked
    && !document.getElementById('option-30nov2020Q372').checked
    && !document.getElementById('option-30nov2020Q373').checked
    && document.getElementById('option-30nov2020Q374').checked
    ) {
      r30nov2020Q37_removeClass(document.getElementById('r30nov2020Q37Correct'), 'riHide', )
    }
    else {
    r30nov2020Q37_removeClass(document.getElementById('r30nov2020Q37Incorrect'), 'riHide', );
  }
  }
   function r30nov2020Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r30nov2020Q37_addClass(ele, cls) {
  if (!r30nov2020Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r30nov2020Q37_removeClass(ele, cls) {
  if (r30nov2020Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer26nov2020Q88() {
  r26nov2020Q88_addClass(document.getElementById('r26nov2020Q88Correct'), 'riHide', );
  r26nov2020Q88_addClass(document.getElementById('r26nov2020Q88Incorrect'), 'riHide', );
    if (document.getElementById('option-26nov2020Q881').checked
    && document.getElementById('option-26nov2020Q882').checked
    && !document.getElementById('option-26nov2020Q883').checked
    && !document.getElementById('option-26nov2020Q884').checked
    ) {
      r26nov2020Q88_removeClass(document.getElementById('r26nov2020Q88Correct'), 'riHide', )
    }
    else {
    r26nov2020Q88_removeClass(document.getElementById('r26nov2020Q88Incorrect'), 'riHide', );
  }
  }
   function r26nov2020Q88_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r26nov2020Q88_addClass(ele, cls) {
  if (!r26nov2020Q88_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r26nov2020Q88_removeClass(ele, cls) {
  if (r26nov2020Q88_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer26nov2020Q18() {
  r26nov2020Q18_addClass(document.getElementById('r26nov2020Q18Correct'), 'riHide', );
  r26nov2020Q18_addClass(document.getElementById('r26nov2020Q18Incorrect'), 'riHide', );
    if (!document.getElementById('option-26nov2020Q181').checked
    && !document.getElementById('option-26nov2020Q182').checked
    && document.getElementById('option-26nov2020Q183').checked
    && !document.getElementById('option-26nov2020Q184').checked
    ) {
      r26nov2020Q18_removeClass(document.getElementById('r26nov2020Q18Correct'), 'riHide', )
    }
    else {
    r26nov2020Q18_removeClass(document.getElementById('r26nov2020Q18Incorrect'), 'riHide', );
  }
  }
   function r26nov2020Q18_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r26nov2020Q18_addClass(ele, cls) {
  if (!r26nov2020Q18_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r26nov2020Q18_removeClass(ele, cls) {
  if (r26nov2020Q18_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer26nov2020Q37() {
  r26nov2020Q37_addClass(document.getElementById('r26nov2020Q37Correct'), 'riHide', );
  r26nov2020Q37_addClass(document.getElementById('r26nov2020Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-26nov2020Q371').checked
    && !document.getElementById('option-26nov2020Q372').checked
    && document.getElementById('option-26nov2020Q373').checked
    && !document.getElementById('option-26nov2020Q374').checked
    ) {
      r26nov2020Q37_removeClass(document.getElementById('r26nov2020Q37Correct'), 'riHide', )
    }
    else {
    r26nov2020Q37_removeClass(document.getElementById('r26nov2020Q37Incorrect'), 'riHide', );
  }
  }
   function r26nov2020Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r26nov2020Q37_addClass(ele, cls) {
  if (!r26nov2020Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r26nov2020Q37_removeClass(ele, cls) {
  if (r26nov2020Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswer26nov2020Q39() {
  r26nov2020Q39_addClass(document.getElementById('r26nov2020Q39Correct'), 'riHide', );
  r26nov2020Q39_addClass(document.getElementById('r26nov2020Q39Incorrect'), 'riHide', );
    if (!document.getElementById('option-26nov2020Q391').checked
    && !document.getElementById('option-26nov2020Q392').checked
    && !document.getElementById('option-26nov2020Q393').checked
    && document.getElementById('option-26nov2020Q394').checked
    ) {
      r26nov2020Q39_removeClass(document.getElementById('r26nov2020Q39Correct'), 'riHide', )
    }
    else {
    r26nov2020Q39_removeClass(document.getElementById('r26nov2020Q39Incorrect'), 'riHide', );
  }
  }
   function r26nov2020Q39_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function r26nov2020Q39_addClass(ele, cls) {
  if (!r26nov2020Q39_hasClass(ele, cls)) ele.className += " " + cls;
}
    function r26nov2020Q39_removeClass(ele, cls) {
  if (r26nov2020Q39_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2019Q07() {
  rdec2019Q07_addClass(document.getElementById('rdec2019Q07Correct'), 'riHide', );
  rdec2019Q07_addClass(document.getElementById('rdec2019Q07Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2019Q071').checked
    && !document.getElementById('option-dec2019Q072').checked
    && !document.getElementById('option-dec2019Q073').checked
    && document.getElementById('option-dec2019Q074').checked
    ) {
      rdec2019Q07_removeClass(document.getElementById('rdec2019Q07Correct'), 'riHide', )
    }
    else {
    rdec2019Q07_removeClass(document.getElementById('rdec2019Q07Incorrect'), 'riHide', );
  }
  }
   function rdec2019Q07_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2019Q07_addClass(ele, cls) {
  if (!rdec2019Q07_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2019Q07_removeClass(ele, cls) {
  if (rdec2019Q07_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2019Q37() {
  rjune2019Q37_addClass(document.getElementById('rjune2019Q37Correct'), 'riHide', );
  rjune2019Q37_addClass(document.getElementById('rjune2019Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2019Q371').checked
    && !document.getElementById('option-june2019Q372').checked
    && document.getElementById('option-june2019Q373').checked
    && !document.getElementById('option-june2019Q374').checked
    ) {
      rjune2019Q37_removeClass(document.getElementById('rjune2019Q37Correct'), 'riHide', )
    }
    else {
    rjune2019Q37_removeClass(document.getElementById('rjune2019Q37Incorrect'), 'riHide', );
  }
  }
   function rjune2019Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2019Q37_addClass(ele, cls) {
  if (!rjune2019Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2019Q37_removeClass(ele, cls) {
  if (rjune2019Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2019Q83() {
  rjune2019Q83_addClass(document.getElementById('rjune2019Q83Correct'), 'riHide', );
  rjune2019Q83_addClass(document.getElementById('rjune2019Q83Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2019Q831').checked
    && document.getElementById('option-june2019Q832').checked
    && document.getElementById('option-june2019Q833').checked
    && document.getElementById('option-june2019Q834').checked
    ) {
      rjune2019Q83_removeClass(document.getElementById('rjune2019Q83Correct'), 'riHide', )
    }
    else {
    rjune2019Q83_removeClass(document.getElementById('rjune2019Q83Incorrect'), 'riHide', );
  }
  }
   function rjune2019Q83_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2019Q83_addClass(ele, cls) {
  if (!rjune2019Q83_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2019Q83_removeClass(ele, cls) {
  if (rjune2019Q83_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2018Q39() {
  rdec2018Q39_addClass(document.getElementById('rdec2018Q39Correct'), 'riHide', );
  rdec2018Q39_addClass(document.getElementById('rdec2018Q39Incorrect'), 'riHide', );
    if (document.getElementById('option-dec2018Q391').checked
    && !document.getElementById('option-dec2018Q392').checked
    && !document.getElementById('option-dec2018Q393').checked
    && !document.getElementById('option-dec2018Q394').checked
    ) {
      rdec2018Q39_removeClass(document.getElementById('rdec2018Q39Correct'), 'riHide', )
    }
    else {
    rdec2018Q39_removeClass(document.getElementById('rdec2018Q39Incorrect'), 'riHide', );
  }
  }
   function rdec2018Q39_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2018Q39_addClass(ele, cls) {
  if (!rdec2018Q39_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2018Q39_removeClass(ele, cls) {
  if (rdec2018Q39_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2017Q37() {
  rdec2017Q37_addClass(document.getElementById('rdec2017Q37Correct'), 'riHide', );
  rdec2017Q37_addClass(document.getElementById('rdec2017Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2017Q371').checked
    && document.getElementById('option-dec2017Q372').checked
    && !document.getElementById('option-dec2017Q373').checked
    && !document.getElementById('option-dec2017Q374').checked
    ) {
      rdec2017Q37_removeClass(document.getElementById('rdec2017Q37Correct'), 'riHide', )
    }
    else {
    rdec2017Q37_removeClass(document.getElementById('rdec2017Q37Incorrect'), 'riHide', );
  }
  }
   function rdec2017Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2017Q37_addClass(ele, cls) {
  if (!rdec2017Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2017Q37_removeClass(ele, cls) {
  if (rdec2017Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2017Q03() {
  rjune2017Q03_addClass(document.getElementById('rjune2017Q03Correct'), 'riHide', );
  rjune2017Q03_addClass(document.getElementById('rjune2017Q03Incorrect'), 'riHide', );
    if (document.getElementById('option-june2017Q031').checked
    && !document.getElementById('option-june2017Q032').checked
    && !document.getElementById('option-june2017Q033').checked
    && !document.getElementById('option-june2017Q034').checked
    ) {
      rjune2017Q03_removeClass(document.getElementById('rjune2017Q03Correct'), 'riHide', )
    }
    else {
    rjune2017Q03_removeClass(document.getElementById('rjune2017Q03Incorrect'), 'riHide', );
  }
  }
   function rjune2017Q03_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2017Q03_addClass(ele, cls) {
  if (!rjune2017Q03_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2017Q03_removeClass(ele, cls) {
  if (rjune2017Q03_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2017Q37() {
  rjune2017Q37_addClass(document.getElementById('rjune2017Q37Correct'), 'riHide', );
  rjune2017Q37_addClass(document.getElementById('rjune2017Q37Incorrect'), 'riHide', );
    if (document.getElementById('option-june2017Q371').checked
    && !document.getElementById('option-june2017Q372').checked
    && !document.getElementById('option-june2017Q373').checked
    && !document.getElementById('option-june2017Q374').checked
    ) {
      rjune2017Q37_removeClass(document.getElementById('rjune2017Q37Correct'), 'riHide', )
    }
    else {
    rjune2017Q37_removeClass(document.getElementById('rjune2017Q37Incorrect'), 'riHide', );
  }
  }
   function rjune2017Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2017Q37_addClass(ele, cls) {
  if (!rjune2017Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2017Q37_removeClass(ele, cls) {
  if (rjune2017Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2017Q38() {
  rjune2017Q38_addClass(document.getElementById('rjune2017Q38Correct'), 'riHide', );
  rjune2017Q38_addClass(document.getElementById('rjune2017Q38Incorrect'), 'riHide', );
    if (document.getElementById('option-june2017Q381').checked
    && !document.getElementById('option-june2017Q382').checked
    && !document.getElementById('option-june2017Q383').checked
    && !document.getElementById('option-june2017Q384').checked
    ) {
      rjune2017Q38_removeClass(document.getElementById('rjune2017Q38Correct'), 'riHide', )
    }
    else {
    rjune2017Q38_removeClass(document.getElementById('rjune2017Q38Incorrect'), 'riHide', );
  }
  }
   function rjune2017Q38_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2017Q38_addClass(ele, cls) {
  if (!rjune2017Q38_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2017Q38_removeClass(ele, cls) {
  if (rjune2017Q38_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2016Q37() {
  rdec2016Q37_addClass(document.getElementById('rdec2016Q37Correct'), 'riHide', );
  rdec2016Q37_addClass(document.getElementById('rdec2016Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2016Q371').checked
    && !document.getElementById('option-dec2016Q372').checked
    && !document.getElementById('option-dec2016Q373').checked
    && document.getElementById('option-dec2016Q374').checked
    ) {
      rdec2016Q37_removeClass(document.getElementById('rdec2016Q37Correct'), 'riHide', )
    }
    else {
    rdec2016Q37_removeClass(document.getElementById('rdec2016Q37Incorrect'), 'riHide', );
  }
  }
   function rdec2016Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2016Q37_addClass(ele, cls) {
  if (!rdec2016Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2016Q37_removeClass(ele, cls) {
  if (rdec2016Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjun2016Q37() {
  rjun2016Q37_addClass(document.getElementById('rjun2016Q37Correct'), 'riHide', );
  rjun2016Q37_addClass(document.getElementById('rjun2016Q37Incorrect'), 'riHide', );
    if (!document.getElementById('option-jun2016Q371').checked
    && !document.getElementById('option-jun2016Q372').checked
    && document.getElementById('option-jun2016Q373').checked
    && !document.getElementById('option-jun2016Q374').checked
    ) {
      rjun2016Q37_removeClass(document.getElementById('rjun2016Q37Correct'), 'riHide', )
    }
    else {
    rjun2016Q37_removeClass(document.getElementById('rjun2016Q37Incorrect'), 'riHide', );
  }
  }
   function rjun2016Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjun2016Q37_addClass(ele, cls) {
  if (!rjun2016Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjun2016Q37_removeClass(ele, cls) {
  if (rjun2016Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2015Q80() {
  rdec2015Q80_addClass(document.getElementById('rdec2015Q80Correct'), 'riHide', );
  rdec2015Q80_addClass(document.getElementById('rdec2015Q80Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2015Q801').checked
    && document.getElementById('option-dec2015Q802').checked
    && !document.getElementById('option-dec2015Q803').checked
    && document.getElementById('option-dec2015Q804').checked
    ) {
      rdec2015Q80_removeClass(document.getElementById('rdec2015Q80Correct'), 'riHide', )
    }
    else {
    rdec2015Q80_removeClass(document.getElementById('rdec2015Q80Incorrect'), 'riHide', );
  }
  }
   function rdec2015Q80_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2015Q80_addClass(ele, cls) {
  if (!rdec2015Q80_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2015Q80_removeClass(ele, cls) {
  if (rdec2015Q80_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjun2015Q84() {
  rjun2015Q84_addClass(document.getElementById('rjun2015Q84Correct'), 'riHide', );
  rjun2015Q84_addClass(document.getElementById('rjun2015Q84Incorrect'), 'riHide', );
    if (document.getElementById('option-jun2015Q841').checked
    && !document.getElementById('option-jun2015Q842').checked
    && document.getElementById('option-jun2015Q843').checked
    && !document.getElementById('option-jun2015Q844').checked
    ) {
      rjun2015Q84_removeClass(document.getElementById('rjun2015Q84Correct'), 'riHide', )
    }
    else {
    rjun2015Q84_removeClass(document.getElementById('rjun2015Q84Incorrect'), 'riHide', );
  }
  }
   function rjun2015Q84_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjun2015Q84_addClass(ele, cls) {
  if (!rjun2015Q84_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjun2015Q84_removeClass(ele, cls) {
  if (rjun2015Q84_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjun2014Q33() {
  rjun2014Q33_addClass(document.getElementById('rjun2014Q33Correct'), 'riHide', );
  rjun2014Q33_addClass(document.getElementById('rjun2014Q33Incorrect'), 'riHide', );
    if (!document.getElementById('option-jun2014Q331').checked
    && !document.getElementById('option-jun2014Q332').checked
    && !document.getElementById('option-jun2014Q333').checked
    && document.getElementById('option-jun2014Q334').checked
    ) {
      rjun2014Q33_removeClass(document.getElementById('rjun2014Q33Correct'), 'riHide', )
    }
    else {
    rjun2014Q33_removeClass(document.getElementById('rjun2014Q33Incorrect'), 'riHide', );
  }
  }
   function rjun2014Q33_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjun2014Q33_addClass(ele, cls) {
  if (!rjun2014Q33_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjun2014Q33_removeClass(ele, cls) {
  if (rjun2014Q33_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjun2014Q90() {
  rjun2014Q90_addClass(document.getElementById('rjun2014Q90Correct'), 'riHide', );
  rjun2014Q90_addClass(document.getElementById('rjun2014Q90Incorrect'), 'riHide', );
    if (document.getElementById('option-jun2014Q901').checked
    && !document.getElementById('option-jun2014Q902').checked
    && document.getElementById('option-jun2014Q903').checked
    && !document.getElementById('option-jun2014Q904').checked
    ) {
      rjun2014Q90_removeClass(document.getElementById('rjun2014Q90Correct'), 'riHide', )
    }
    else {
    rjun2014Q90_removeClass(document.getElementById('rjun2014Q90Incorrect'), 'riHide', );
  }
  }
   function rjun2014Q90_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjun2014Q90_addClass(ele, cls) {
  if (!rjun2014Q90_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjun2014Q90_removeClass(ele, cls) {
  if (rjun2014Q90_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2013Q39() {
  rdec2013Q39_addClass(document.getElementById('rdec2013Q39Correct'), 'riHide', );
  rdec2013Q39_addClass(document.getElementById('rdec2013Q39Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2013Q391').checked
    && document.getElementById('option-dec2013Q392').checked
    && !document.getElementById('option-dec2013Q393').checked
    && !document.getElementById('option-dec2013Q394').checked
    ) {
      rdec2013Q39_removeClass(document.getElementById('rdec2013Q39Correct'), 'riHide', )
    }
    else {
    rdec2013Q39_removeClass(document.getElementById('rdec2013Q39Incorrect'), 'riHide', );
  }
  }
   function rdec2013Q39_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2013Q39_addClass(ele, cls) {
  if (!rdec2013Q39_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2013Q39_removeClass(ele, cls) {
  if (rdec2013Q39_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2013Q39() {
  rdec2013Q39_addClass(document.getElementById('rdec2013Q39Correct'), 'riHide', );
  rdec2013Q39_addClass(document.getElementById('rdec2013Q39Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2013Q391').checked
    && document.getElementById('option-dec2013Q392').checked
    && !document.getElementById('option-dec2013Q393').checked
    && !document.getElementById('option-dec2013Q394').checked
    ) {
      rdec2013Q39_removeClass(document.getElementById('rdec2013Q39Correct'), 'riHide', )
    }
    else {
    rdec2013Q39_removeClass(document.getElementById('rdec2013Q39Incorrect'), 'riHide', );
  }
  }
   function rdec2013Q39_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2013Q39_addClass(ele, cls) {
  if (!rdec2013Q39_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2013Q39_removeClass(ele, cls) {
  if (rdec2013Q39_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2013Q08() {
  rjune2013Q08_addClass(document.getElementById('rjune2013Q08Correct'), 'riHide', );
  rjune2013Q08_addClass(document.getElementById('rjune2013Q08Incorrect'), 'riHide', );
    if (document.getElementById('option-june2013Q081').checked
    && !document.getElementById('option-june2013Q082').checked
    && !document.getElementById('option-june2013Q083').checked
    && !document.getElementById('option-june2013Q084').checked
    ) {
      rjune2013Q08_removeClass(document.getElementById('rjune2013Q08Correct'), 'riHide', )
    }
    else {
    rjune2013Q08_removeClass(document.getElementById('rjune2013Q08Incorrect'), 'riHide', );
  }
  }
   function rjune2013Q08_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2013Q08_addClass(ele, cls) {
  if (!rjune2013Q08_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2013Q08_removeClass(ele, cls) {
  if (rjune2013Q08_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2013Q95() {
  rjune2013Q95_addClass(document.getElementById('rjune2013Q95Correct'), 'riHide', );
  rjune2013Q95_addClass(document.getElementById('rjune2013Q95Incorrect'), 'riHide', );
    if (document.getElementById('option-june2013Q951').checked
    && !document.getElementById('option-june2013Q952').checked
    && document.getElementById('option-june2013Q953').checked
    && !document.getElementById('option-june2013Q954').checked
    ) {
      rjune2013Q95_removeClass(document.getElementById('rjune2013Q95Correct'), 'riHide', )
    }
    else {
    rjune2013Q95_removeClass(document.getElementById('rjune2013Q95Incorrect'), 'riHide', );
  }
  }
   function rjune2013Q95_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2013Q95_addClass(ele, cls) {
  if (!rjune2013Q95_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2013Q95_removeClass(ele, cls) {
  if (rjune2013Q95_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2012Q37() {
  rdec2012Q37_addClass(document.getElementById('rdec2012Q37Correct'), 'riHide', );
  rdec2012Q37_addClass(document.getElementById('rdec2012Q37Incorrect'), 'riHide', );
    if (document.getElementById('option-dec2012Q371').checked
    && !document.getElementById('option-dec2012Q372').checked
    && !document.getElementById('option-dec2012Q373').checked
    && !document.getElementById('option-dec2012Q374').checked
    ) {
      rdec2012Q37_removeClass(document.getElementById('rdec2012Q37Correct'), 'riHide', )
    }
    else {
    rdec2012Q37_removeClass(document.getElementById('rdec2012Q37Incorrect'), 'riHide', );
  }
  }
   function rdec2012Q37_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2012Q37_addClass(ele, cls) {
  if (!rdec2012Q37_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2012Q37_removeClass(ele, cls) {
  if (rdec2012Q37_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerdec2012Q84() {
  rdec2012Q84_addClass(document.getElementById('rdec2012Q84Correct'), 'riHide', );
  rdec2012Q84_addClass(document.getElementById('rdec2012Q84Incorrect'), 'riHide', );
    if (!document.getElementById('option-dec2012Q841').checked
    && document.getElementById('option-dec2012Q842').checked
    && document.getElementById('option-dec2012Q843').checked
    && !document.getElementById('option-dec2012Q844').checked
    ) {
      rdec2012Q84_removeClass(document.getElementById('rdec2012Q84Correct'), 'riHide', )
    }
    else {
    rdec2012Q84_removeClass(document.getElementById('rdec2012Q84Incorrect'), 'riHide', );
  }
  }
   function rdec2012Q84_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rdec2012Q84_addClass(ele, cls) {
  if (!rdec2012Q84_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rdec2012Q84_removeClass(ele, cls) {
  if (rdec2012Q84_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2012Q28() {
  rjune2012Q28_addClass(document.getElementById('rjune2012Q28Correct'), 'riHide', );
  rjune2012Q28_addClass(document.getElementById('rjune2012Q28Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2012Q281').checked
    && document.getElementById('option-june2012Q282').checked
    && !document.getElementById('option-june2012Q283').checked
    && !document.getElementById('option-june2012Q284').checked
    ) {
      rjune2012Q28_removeClass(document.getElementById('rjune2012Q28Correct'), 'riHide', )
    }
    else {
    rjune2012Q28_removeClass(document.getElementById('rjune2012Q28Incorrect'), 'riHide', );
  }
  }
   function rjune2012Q28_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2012Q28_addClass(ele, cls) {
  if (!rjune2012Q28_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2012Q28_removeClass(ele, cls) {
  if (rjune2012Q28_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2012Q22() {
  rjune2012Q22_addClass(document.getElementById('rjune2012Q22Correct'), 'riHide', );
  rjune2012Q22_addClass(document.getElementById('rjune2012Q22Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2012Q221').checked
    && document.getElementById('option-june2012Q222').checked
    && !document.getElementById('option-june2012Q223').checked
    && !document.getElementById('option-june2012Q224').checked
    ) {
      rjune2012Q22_removeClass(document.getElementById('rjune2012Q22Correct'), 'riHide', )
    }
    else {
    rjune2012Q22_removeClass(document.getElementById('rjune2012Q22Incorrect'), 'riHide', );
  }
  }
   function rjune2012Q22_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2012Q22_addClass(ele, cls) {
  if (!rjune2012Q22_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2012Q22_removeClass(ele, cls) {
  if (rjune2012Q22_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2011Q27() {
  rjune2011Q27_addClass(document.getElementById('rjune2011Q27Correct'), 'riHide', );
  rjune2011Q27_addClass(document.getElementById('rjune2011Q27Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2011Q271').checked
    && !document.getElementById('option-june2011Q272').checked
    && !document.getElementById('option-june2011Q273').checked
    && document.getElementById('option-june2011Q274').checked
    ) {
      rjune2011Q27_removeClass(document.getElementById('rjune2011Q27Correct'), 'riHide', )
    }
    else {
    rjune2011Q27_removeClass(document.getElementById('rjune2011Q27Incorrect'), 'riHide', );
  }
  }
   function rjune2011Q27_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2011Q27_addClass(ele, cls) {
  if (!rjune2011Q27_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2011Q27_removeClass(ele, cls) {
  if (rjune2011Q27_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
function displayAnswerjune2011Q28() {
  rjune2011Q28_addClass(document.getElementById('rjune2011Q28Correct'), 'riHide', );
  rjune2011Q28_addClass(document.getElementById('rjune2011Q28Incorrect'), 'riHide', );
    if (!document.getElementById('option-june2011Q281').checked
    && !document.getElementById('option-june2011Q282').checked
    && document.getElementById('option-june2011Q283').checked
    && !document.getElementById('option-june2011Q284').checked
    ) {
      rjune2011Q28_removeClass(document.getElementById('rjune2011Q28Correct'), 'riHide', )
    }
    else {
    rjune2011Q28_removeClass(document.getElementById('rjune2011Q28Incorrect'), 'riHide', );
  }
  }
   function rjune2011Q28_hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}
function rjune2011Q28_addClass(ele, cls) {
  if (!rjune2011Q28_hasClass(ele, cls)) ele.className += " " + cls;
}
    function rjune2011Q28_removeClass(ele, cls) {
  if (rjune2011Q28_hasClass(ele, cls)) {
    var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}
</script>

<script>
	// by https://www.gxfreee.com/
	
	const errorText = document.querySelector(".error-text");
	var Password ="NT200125";
	function passcheck(){
		if (document.getElementById('pass1').value != Password) {
			errorText.style.display = "block";
      errorText.textContent = "Incorrect Password";
			// errorText.textContent = "ERROR! Password Not Match.";
			return false;
		}
		if (document.getElementById('pass1').value == Password) {
			// window.open("https://www.google.com", "_blank");
      window.open("https://www.dropbox.com/scl/fi/mt40qeo61qlctmn3r250p/SPU_Workshop_20_Jan_2025_Transcript.pdf?rlkey=seylru6qqvldv2t2yl6ps2inq&st=gg7uctpy&dl=1");
		}

	}
	// by https://www.gxfreee.com/
</script>
<html/>