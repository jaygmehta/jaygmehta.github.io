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

<br>

### Reference Books

1. Hoffstein J., Pipher J., Silverman J. H., An Introduction to Mathematical Cryptography, Undergraduate Texts in Mathematics, Springer, New York, (2008).
2. Douglas R. Stinson, Cryptography: Theory and Practice, Second Edition, Chapman and Hall/CRC, (2005).
3. N. Koblitz, A Course in Number Theory and Cryptography, Springer (1994).
4. J. A. Buchmann, Introduction to Cryptography, Second Edition, Undergraduate Texts in Mathematics, Springer-Verlag, New York, (2004).

------------------

## [Past Papers MCQ](/projects/NTC-SPU-MCQ/index-en.html){:target="_blank"} <sub><sup><sub>(use landscape mode of phone)<sub/><sup/><sub/>
<!-- <br> -->

##### [PS03EMTH55-(11-11-2022)](/projects/NTC-SPU-MCQ/PS03EMTH55-(11-11-2022).html){:target="_blank"}
<!-- <br> -->

##### [PS03EMTH55-(27-04-2023)](/projects/NTC-SPU-MCQ/PS03EMTH55-(27-04-2023).html){:target="_blank"}
<!-- <br> -->

##### [PS04EMTH59-(01-05-2023)](/projects/NTC-SPU-MCQ/PS04EMTH59-(01-05-2023).html){:target="_blank"}
<!-- <br> -->

##### [PS03EMTH55-(01-11-2023)](/projects/NTC-SPU-MCQ/PS03EMTH55-(01-11-2023).html){:target="_blank"}
<!-- <br> -->

##### [PS04EMTH59-(04-11-2023)](/projects/NTC-SPU-MCQ/PS04EMTH59-(04-11-2023).html){:target="_blank"}
<!-- <br> -->

##### [PS03EMTH55-(12-04-2024)](/projects/NTC-SPU-MCQ/PS03EMTH55-(12-04-2024).html){:target="_blank"}
<!-- <br> -->

##### [PS04EMTH59-(09-04-2024)](/projects/NTC-SPU-MCQ/PS04EMTH59-(09-04-2024).html){:target="_blank"}
<!-- <br> -->

##### [PS03EMTH55-(06-12-2024)](/projects/NTC-SPU-MCQ/PS03EMTH55-(06-12-2024).html){:target="_blank"}
<!-- <br> -->

##### [PS04EMTH59-(27-11-2024)](/projects/NTC-SPU-MCQ/PS04EMTH59-(27-11-2024).html){:target="_blank"}
<!-- <br> -->

##### [PS03EMTH55-(16-04-2025)](/projects/NTC-SPU-MCQ/PS03EMTH55-(16-04-2025).html){:target="_blank"}
<!-- <br> -->

##### [PS04EMTH59-(16-04-2025)](/projects/NTC-SPU-MCQ/PS04EMTH59-(16-04-2025).html){:target="_blank"}
<!-- <br> -->

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

### Square roots modulo n=pq, where p,q = 4k+3
<strong>Program to find solution of $$x^2 \equiv c \pmod{n}$$ , where $$n=pq$$, and $$p, q \equiv 3 \pmod{4}$$ are distinct primes.</strong><br>
<iframe src="https://trinket.io/embed/python3/3fbb912f2596?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Miller-Rabin Primality Test
<strong>Enter the value of $$n$$ to test whether it is composite by finding a Miller-Rabin witness.</strong><br>
<iframe src="https://trinket.io/embed/python3/4fe1ec9fd7e5?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

------------------

### Pollard's $$p-1$$ Algorithm
<strong>Enter the value of $$N=pq$$ (the product of two primes) to factorize.</strong><br>
<iframe src="https://trinket.io/embed/python3/0a088fe3bf?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>

------------------

### Adding points on elliptic curve using equation of line
<strong>Enter the value of $$A, B$$ for $$E: Y^2 = X^3 + AX + B$$ coordinates $$x_1, y_1$$ and $$x_2,y_2$$ of points $$P$$ and $$Q$$ respectively to compute $$P\oplus Q$$.</strong><br>
<iframe src="https://trinket.io/embed/python3/c75d4adc9dd8?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

------------------

### Adding points on elliptic curve over finite field using addition formula
<strong>Enter the value of $$A, B$$ for $$E: Y^2 = X^3 + AX + B$$ coordinates $$x_1, y_1$$ and $$x_2,y_2$$ of points $$P$$ and $$Q$$ respectively to compute $$P+Q$$.</strong><br>
<iframe src="https://trinket.io/embed/python3/a32e119a3230?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

------------------

### $$\#E(\mathbb F_p)$$ and Trace of Frobenius $$t_p$$
<strong>Enter the value of $$p$$ for $$\mathbb F_p$$ and $$A, B$$ for $$E: Y^2 = X^3 + AX + B$$ to compute the number of points on $$E$$ and the trace of Frobenius $$t_p$$.</strong><br>
<iframe src="https://trinket.io/embed/python3/7f613f3d62cb?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

------------------

### Double and Add algorithm to compute $$nP$$ for $$P \in E(\mathbb F_p)$$
<strong>Enter the value of $$p$$ for $$\mathbb F_p$$, input values of $$A, B$$ for $$E: Y^2 = X^3 + AX + B$$, coordinates $$x_1, y_1$$ of a point $$P$$ and the value of $$n$$ to compute $$nP$$.</strong><br>
<iframe src="https://trinket.io/embed/python3/912163c11b52?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen="allowfullscreen"></iframe>

------------------

## Lecture Notes
<p>Download the PDF file of lecture notes <a href="/assets/pdf/PS03EMTH55.pdf" target="_blank"  class="float-none"><i class="fas fa-file-pdf" style="font-size:24px;color:red"></i></a></p>

<iframe width="100%" height="800" src="/assets/pdf/PS03EMTH55.pdf">

<!-- <object data="https://jaygmehta.com/assets/pdf/PS03EMTH55.pdf" type="application/pdf" width="100%" height="800">
    <embed src="https://jaygmehta.com/assets/pdf/PS03EMTH55.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://jaygmehta.com/assets/pdf/PS03EMTH55.pdf">Download PDF</a>.</p>
    </embed>
</object> -->
