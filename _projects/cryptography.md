---
layout: page
title: Number Theory and Cryptography
description: Semester III (PS03EMTH55) <br>
             same as Sem IV (PS04EMTH59)
img: assets/img/crypto.jpg
importance: 2
category: Semester III
# date: 2023-04-25 10:14:00-0400
# description: an example of a blog post with table of contents on a sidebar
# categories: sample-posts toc sidebar
giscus_comments: false #true
related_posts: false
toc:
  beginning: true
# toc:
#   sidebar: left
---
## Syllabus
<!-- The below command span will be used if we change first line layout to page instead of post -->
<!-- <span style="font-size:1.3em;"> **Syllabus** </span> --> 

|:---------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unit-I**          | Number Theory and Discrete Logarithm Problem: Simple substitution ciphers (except cryptanalysis), divisibility and GCD, modular arithmetic, prime numbers, unique factorization and finite fields, primitive roots in finite fields. The discrete logarithm problem. |
| **Unit-II**         | DLP based cryptosystems: The Diffie-Hellman key exchange, the ElGamal public key cryptosystem, difficulty of discrete log problem (DLP), a collision algorithm for the DLP, the Chinese remainder theorem, the Pohlig-Hellman algorithm.                                                                 |
| **Unit-III**        | The RSA Algorithm: Euler’s formula and roots modulo pq, the RSA public key cryptosystem, implementation and security issues, primality testing, Pollard’s p-1 factorization algorithm.                                                                                                                          |
| **Unit-IV**  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Elliptic curve cryptography: Elliptic curves, elliptic curve over finite fields, the elliptic curve discrete logarithm problem, elliptic curve cryptography.                                          |

------------------

## Python Programs in Cryptography
Below are some algorithms we studied in our course Number Theory and Cryptography. One can execute the code by clicking on **Run** and find the solution of the numerical problems.

------------------

### Extended Euclidean Algorithm (EEA)
<strong>Enter a and b to compute gcd(a,b) and au + bv = gcd(a,b)</strong><br>
<iframe src="https://trinket.io/embed/python3/237e52137e?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Box Method (an alternative to EEA for coprime integers)
<strong>Give a and b and program computes au+bv = 1 = gcd(a,b) using Box Method</strong><br>
<iframe src="https://trinket.io/embed/python3/c5aa096759?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Fast Powering Algorithm (FPA) or Square and Multiply Algorithm (SAM)
<strong>Enter g, A, m to compute g^A (mod m) using Fast Powering Algorithm</strong><br>
<iframe src="https://trinket.io/embed/python3/f3eee92dcb?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Shanks's (Babystep Giantstep) Algorithm
<strong>Program to find discrete log of h mod p to the base g using Shanks's Babystep Giantstep Algorithm</strong><br>
<iframe src="https://trinket.io/embed/python3/ab487250db?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Chinese Remainder Theorem (CRT)
<strong>Provide the number of congruences n , then enter values of ai and mi for each i = 1,2,...,n to obtain a&nbsp; solution by Chinese Remainder Theorem.</strong><br>
<iframe src="https://trinket.io/embed/python3/3a10443a42?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Pollard's $$p-1$$ Algorithm
<strong>Enter the value of $$N=pq$$ (the product of two primes) to factorize.</strong><br>
<iframe src="https://trinket.io/embed/python3/0a088fe3bf?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

## Lecture Notes
<p>Download the PDF file of lecture notes <a href="/assets/pdf/PS04EMTH59.pdf" target="_blank"  class="float-none"><i class="fas fa-file-pdf" style="font-size:24px;color:red"></i></a></p>

<iframe width="100%" height="800" src="https://jaygmehta.com/assets/pdf/PS04EMTH59.pdf">

<!-- <object data="https://jaygmehta.com/assets/pdf/PS04EMTH59.pdf" type="application/pdf" width="100%" height="800">
    <embed src="https://jaygmehta.com/assets/pdf/PS04EMTH59.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://jaygmehta.com/assets/pdf/PS04EMTH59.pdf">Download PDF</a>.</p>
    </embed>
</object> -->
