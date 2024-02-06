---
layout: page
title: Computer Programming and Software
description: Semester IV (PS04EMTH32) <br>
            old course <br>
            same as Sem III (PS03EMTH32)
img: assets/img/pythonprog.jpg
importance: 4
category: Semester IV
# date: 2023-04-25 10:14:00-0400
# description: an example of a blog post with table of contents on a sidebar
# categories: sample-posts toc sidebar
# giscus_comments: false #true
# related_posts: false
toc:
  beginning: true
# toc:
#   sidebar: left
---
## Syllabus
<!-- The below command span will be used if we change first line layout to page instead of post -->
<!-- <span style="font-size:1.3em;"> **Syllabus** </span> --> 

|:---------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unit-I**          | The Basics: Literal constants, numbers, strings, variables, identifier naming, data types, objects, logical and physical lines, indentation. Operators, operator precedence, expressions. Control flow: the if statement, the while statement, the for loop, the break statement, the continue statement. |
| **Unit-II**         |  Functions: Defining a function, local variables, default argument values, keyword arguments, the return statement, DocStrings. Modules: using the sys module, the from import statement, creating modules, the dir() function.                                                               |
| **Unit-III & IV**        | List of computer practicals.                                                                                                                     |

<br>

### Reference Books

1. Swaroop C. H., A byte of Python.
2. James Payne, Beginning Python: Using Python 2.6 and Python 3, Wiley India, 2010.
3.  Amit Saha, Doing Math with Python, No Starch Press (2015).
4.  SCILAB - A Free software to MATLAB by Er. Hema Ramachandran and Dr. Achuthsankar S. Nair., S. Chand and Company Ltd. (2008).

<br>

### Practicals

1. To find the minimum/maximum of a given list of numbers.
2. To check whether a given number is odd or even. To check whether a given year is a leap year or not.
3. To find the real roots of a quadratic equation.
4. To compute $$n!$$, $$a^n$$, sum and average of a list of numbers. To prepare the result of a student.
5. Primality lists: To check whether a given number is prime or not, to list all the prime numbers within a given range, to factorize a number.
6. Manipulation of numbers: to check whether a given number is perfect or not, to check whether a given number is palindrome or not, to compute the sum of digits of a given number, to compute the sum of squares of the digits, to print a given number in reverse order of its digits.
7. To compute GCD and LCM of two numbers, to evaluate the functions $$\sigma(n)$$, $$\tau(n)$$, $$\phi(n)$$, $$\mu(n)$$ for a given positive integer $$n$$.
8. To generate Fibonacci sequence and Lucas sequences; to compute the sum of the series
and hence evaluate $$e^x$$, $$\sin(x)$$, $$\cos(x)$$, $$\tan(x)$$, $$\sinh(x)$$, $$\cosh(x)$$ (terminate the program after n terms of the series or terminate the program at the desired level of accuracy).
9. Basics of Scilab 1: Sum of matrices, determinant of a matrix, product of matrices, inverse of a matrix, row reduced echelon form.
10. Basics of Scilab 2: Plotting Cartesian, polar and parametric curves, commands for plotting functions.

------------------

## Programs' code
Codes of some programs (need not be in the best and efficient form) from the above syllabus of python programming are given below. You may try it out by clicking on the Output button and on Run to execture the code.

#### 1. To find the maximum of a given list of numbers.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code1">Code</button>
<div id="code1" class="collapse">

{% highlight python linenos %}

lst = []
n=int(input('How many numbers are there? '))

for i in range(n):
    num = float(input('Enter {}th number: '.format(i+1)))
    lst.append(num)
# k=range(n)
# print(k)
maxi=lst[0]
# print(maxi)
for i in range(1,n):
    if (maxi < lst[i]):
        maxi=lst[i]
print('Maximum computed manually is: ', maxi)
print('Maximum number from the list is: ', max(lst))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output1">Output</button>
<div id="output1" class="collapse">
<iframe src="https://trinket.io/embed/python3/67694a55e5?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

-------

#### 2(a). To check whether a given number is odd or even
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code2a">Code</button>
<div id="code2a" class="collapse">

{% highlight python linenos %}

# Program to check whether a number is odd or even
n=int(input('Enter your number: '))
if n%2 == 0:
    print('Your entered number', n, 'is even')
else:
    print('Your entered number', n, 'is odd')

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output2a">Output</button>
<div id="output2a" class="collapse">
<iframe src="https://trinket.io/embed/python3/043125ffcd?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 2(b). To check whether a given year is a leap year or not.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code2b">Code</button>
<div id="code2b" class="collapse">

{% highlight python linenos %}

# Program to check if the input year is a leap year or not

year = int(input("Enter a year number of your choice: "))

#if year%400 == 0 or (year %4==0 and year%100!=0):
#    print('The year {} is a leap year.'.format(year))
#else:
#    print('The year {} is not a leap year.'.format(year))

if (year % 4 == 0):
    if (year % 100 == 0):
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))



{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output2b">Output</button>
<div id="output2b" class="collapse">
<iframe src="https://trinket.io/embed/python3/16db0d2ca0?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  
------

#### 3. To find the real roots of a quadratic equation.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code3">Code</button>
<div id="code3" class="collapse">

{% highlight python linenos %}

# Program to find roots of quadratic equation

print('Consider the equation of the form ax^2+bx+c=0')

a=float(input('Enter the non-zero coefficient a of x^2: '))
b=float(input('Enter the coefficient b of x: '))
c=float(input('Enter the constant term c: '))

delta = b**2 - 4 * a * c
d=delta**(0.5)

if (delta<0):
    print('The given quadratic equation {}x^2 + {}x + c =0 has no real roots'.format(a,b,c))
else:
    r1 = (-b+d)/(2*a)
    r2 = (-b-d)/(2*a)
    print('The real roots of given quadratic equation {}x^2 + {}x + {} =0 are {} and {}'.format(a,b,c,r1,r2))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output3">Output</button>
<div id="output3" class="collapse">
<iframe src="https://trinket.io/embed/python3/5a2c39d825?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  
------

#### 4. To compute $$n!$$ (factorial of a given non-negative integer $$n$$).
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code4">Code</button>
<div id="code4" class="collapse">

{% highlight python linenos %}

# Python program to compute n factorial
n = int(input('Enter a non-negative integer: '))
if n<0:
    print('Please enter a non-negative integer.')
elif n==0:
    print('0! = 1')
else:
    i=n
    nfact=1
    for i in range(n,0,-1):
        nfact = nfact * i
    print('{}! = {}'.format(n,nfact))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output4">Output</button>
<div id="output4" class="collapse">
<iframe src="https://trinket.io/embed/python3/b780273ac5?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  
-------

#### 5(a). To check whether a given number is prime or not.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code5a">Code</button>
<div id="code5a" class="collapse">

{% highlight python linenos %}

# Python program to check whether a number is prime or not
n=int(input('Enter an integer n>2: '))
for i in range(2,int((n**0.5)+1)):
    if n%i==0:
        print("The entered number {} is not prime.".format(n))
        print(i)
        break
else:
    print("The entered number {} is a prime number.".format(n))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output5a">Output</button>
<div id="output5a" class="collapse">
<iframe src="https://trinket.io/embed/python3/e4b7cf318b?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 5(b). To list all prime numbers within a given range.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code5b">Code</button>
<div id="code5b" class="collapse">

{% highlight python linenos %}

# Python program to list all the prime numbers in a given range
a = int(input('Give the starting point a (> 0) of the range: '))
b = int(input('Give the ending point b (> a) of the range: '))
if b > a > 0:
    if a == 1:
        a1 = 2
    else:
        a1 = a
    print('The prime numbers between {} and {} are the following:'.format(a,b))
    for n in range(a1, b+1):
        test = 0
        for i in range(2, int((n**0.5)+1)):
            if n % i == 0:
                test = 1
                break
#        else:
        if test == 0:
            print(n, end=', ')
else:
    print("Please enter a valid range.")

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output5b">Output</button>
<div id="output5b" class="collapse">
<iframe src="https://trinket.io/embed/python3/0a2837f270?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 5(c). To factorize a given number.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code5c">Code</button>
<div id="code5c" class="collapse">

{% highlight python linenos %}

# Program to factorize a given number
n = int(input("Enter the number (n > 1) which you want to factorize: "))
lst = [1]
#lst.append(1)
for i in range(2, n+1):
    if n % i == 0:
        lst.append(i)
if len(lst) == 2:
    print("The number {} is prime and it only factors are 1 and {}.".format(n,n))
else:
    print('The factors of {} are the following:'.format(n))
    for p in lst:  # range(len(lst)):
        print(p, end=', ')
# Extending the program to check whether the number is perfect or not
print('')
if n == sum(lst)-n:
    print('The number',n,'is perfect')

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output5c">Output</button>
<div id="output5c" class="collapse">
<iframe src="https://trinket.io/embed/python3/20fc981595?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 5(d). To print the $$n^{\rm th}$$ prime.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code5d">Code</button>
<div id="code5d" class="collapse">

{% highlight python linenos %}

# Program to compute the nth prime number

n = int(input('Enter the value of n to compute the nth prime number: '))
c = 2
x = 5
while c < n:
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            break
    else:
        c = c + 1
    x = x + 2
print(n,"th prime number is ",x-2)

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output5d">Output</button>
<div id="output5d" class="collapse">
<iframe src="https://trinket.io/embed/python3/2d558dbf89?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

------

#### 6. Manipulation of numbers: to check whether a given number is perfect or not, to check whether a given number is palindrome or not, to compute the sum of digits of a given number, to compute the sum of squares of the digits, to print a given number in reverse order of its digits.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code6">Code</button>
<div id="code6" class="collapse">

{% highlight python linenos %}

# Program to do various manipulation of numbers
# We check number is perfect or not, palindrome or not, compute sum of digits, sum of squares of digits and reverse the number

n = int(input('Enter the number: '))

sumdiv = 0  # for storing sum of divisors

for i in range(1,int(n/2)+1):
    if n % i == 0:
        sumdiv = sumdiv + i

if sumdiv == n:
    print('The entered number {} is perfect'.format(n))
else:
    print('The entered number {} is Not perfect'.format(n))

num = n  # num will be used for manipulation without disturbing n
sum = 0  # will be used to store the sum of digits of n
sumsq = 0  # will be used to store the sum of squares of digits
rev = 0  # will be used to reverse the number

while num > 0:
    digit = num % 10
    sum = sum + digit
    sumsq = sumsq + (digit**2)
    rev = (rev * 10) + digit
    num = num // 10

if rev == n:
    print('The entered number {} is palindrome'.format(n))
else:
    print('The entered number {} is Not palindrome'.format(n))

print('The sum of digits of {} is {}'.format(n,sum))
print('The sum of the squares of digits of {} is {}'.format(n,sumsq))
print('The entered number {} in the reverse order of its digits is {}'.format(n,rev))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output6">Output</button>
<div id="output6" class="collapse">
<iframe src="https://trinket.io/embed/python3/29ff262e01?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

-------

#### 7(a). To compute GCD and LCM of two numbers.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code7a">Code</button>
<div id="code7a" class="collapse">

{% highlight python linenos %}

# Program to find gcd and lcm of two numbers
a = int(input('Enter first positive integer a: '))
b = int(input('Enter second positive integer b: '))

gc = 1

def gcd(x,y):
    global gc
    x1=x
    y1=y
    if x1 % y1 == 0:
        print('GCD of {} and {} computed by recurrence is {}'.format(a,b,y1))
        gc = y1
    else:
        gcd(y1,(x1%y1))


gcd(a, b)

for i in range (min(int(a/2),int(b/2))+1,0,-1):
    if a % i == 0 and b % i == 0:
        print('GCD of {} and {} computed by loop is {}'.format(a,b,i))
        break

print('LCM of {} and {} is {} (using y1)'.format(a,b,int(a*b/gc)))
print('LCM of {} and {} is {} (using i)'.format(a,b,int(a*b/i)))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output7a">Output</button>
<div id="output7a" class="collapse">
<iframe src="https://trinket.io/embed/python3/37911d82b9?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 7(b). To evaluate the function $$\phi(n)$$ for a given positive integer $$n$$.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code7b">Code</button>
<div id="code7b" class="collapse">

{% highlight python linenos %}

# Python Program to compute Euler's phi function for n >= 2

g=1
def gcd(x,y):
    global g
    if x % y == 0:
        g = y
#        return y
    else:
        gcd(y,x%y)

n = int(input('Enter a positive integer: '))
c = 0

for i in range(1,n):
    gcd(n,i)
    if g == 1:
        c = c + 1
print('Euler\'s function of {} is {}'.format(n,c))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output7b">Output</button>
<div id="output7b" class="collapse">
<iframe src="https://trinket.io/embed/python3/dede9fabce?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 7(c). To evaluate the Möbius function $$\mu(n)$$ for a given positive integer $$n$$.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code7c">Code</button>
<div id="code7c" class="collapse">

{% highlight python linenos %}

# Python Program to compute the mobius function mu(n)
n = int(input('Enter the value of n: '))
u=1
def is_prime(x):
    for i in range(2,int(x**(0.5))+1):
        if x%i==0:
            return 0
    else:
        return 1

if n <=0:
    print('Enter a valid positive integer n')
elif n==1:
    print('u(1)=1')
else:
    for k in range(2,n+1):
        if is_prime(k)==1 and n%k==0:
            if n%(k*k)==0:
                u=0
                break
            else:
                u = u*(-1)
    print('Mobius function u({})={}'.format(n,u))

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output7c">Output</button>
<div id="output7c" class="collapse">
<iframe src="https://trinket.io/embed/python3/5b291fb708?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  
-------

#### 8(a). To generate Fibonacci sequence.
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code8a">Code</button>
<div id="code8a" class="collapse">

{% highlight python linenos %}

# Python program to compute n terms of fibonacci sequence

def fibo(x):
    if x <= 0:
        print('Enter a positive integer.')
    elif x  == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

n = int(input('Enter the term n: '))

#print(fibo(n))  # To print the nth fibonacci number

#for i in range(1,n+1):  # To print first n fibonacci numbers
#    print(fibo(i))

i = 1
while fibo(i)<= n:  # To print fibonacci numbers upto n
    print(fibo(i))
    i = i + 1

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output8a">Output</button>
<div id="output8a" class="collapse">
<iframe src="https://trinket.io/embed/python3/b844ffd7ea?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  

#### 8(b). To compute the sum of the series and hence evaluate $$e^x$$, $$\sin(x)$$, $$\cos(x)$$, $$\tan(x)$$, $$\sinh(x)$$, $$\cosh(x)$$ (terminate the program after n terms of the series or terminate the program at the desired level of accuracy).
<button type="button" class="bibtex" data-toggle="collapse" data-target="#code8b">Code</button>
<div id="code8b" class="collapse">

{% highlight python linenos %}

# Python program to compute the sum of the series e^x, sin x, cos x, sinh x and cosh x upto n terms

import math

x = float(input('Enter the value of x: '))
n = int(input('Enter the number of terms of the series n: '))

#x = y*math.pi/180

def expo(x):
    sumex = 1
    termex = 1
    for m in range(1,n):
        termex = (termex * x)/m
        sumex = sumex + termex
    return sumex

sumcos = 1
termcos = 1
termsin = x
sumsin = termsin

#i=1
#while math.fabs(termcos) > 0.0001:
for i in range(1,n):
    termsin = (termsin * (x**2) * (-1))/((2*i)*(2*i+1))
    sumsin = sumsin + termsin
    termcos = (termcos * (x**2) * (-1))/((2*i-1)*(2*i))
    sumcos = sumcos + termcos
#    i = i + 1

print('')
print('The computed value of e^{} upto {} terms is {}.'.format(x,n,expo(x)))
print('The actual value of e^{} using math module is {}.'.format(x,math.exp(x)))
print('')

print('The computed value of sin({}) upto {} terms is {}.'.format(x,n,sumsin))
print('The actual value of sin({}) using math module is {}.'.format(x,math.sin(x)))
print('')

print('The computed value of cos({}) upto {} terms is {}.'.format(x,n,sumcos))
print('The actual value of cos({}) using math module is {}.'.format(x,math.cos(x)))
print('')

print('The computed value of sinh({}) upto {} terms is {}.'.format(x,n,(expo(x)-expo(-1*x))/2))
print('The actual value of sinh({}) using math module is {}.'.format(x,math.sinh(x)))
print('')

print('The computed value of cosh({}) upto {} terms is {}.'.format(x,n,(expo(x)+expo(-1*x))/2))
print('The actual value of cosh({}) using math module is {}.'.format(x,math.cosh(x)))
print('')

{% endhighlight %}
</div>  
<button type="button" class="bibtex" data-toggle="collapse" data-target="#output8b">Output</button>
<div id="output8b" class="collapse">
<iframe src="https://trinket.io/embed/python3/5e56d21d03?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>  
------------------

## Lecture Notes
<p>Download the PDF file of lecture notes <a href="/assets/pdf/PS03EMTH32.pdf" target="_blank"  class="float-none"><i class="fas fa-file-pdf" style="font-size:24px;color:red"></i></a></p>

<iframe width="100%" height="800" src="/assets/pdf/PS03EMTH32.pdf">

<!-- <object data="https://jaygmehta.com/assets/pdf/PS03EMTH32.pdf" type="application/pdf" width="100%" height="800">
    <embed src="https://jaygmehta.com/assets/pdf/PS03EMTH32.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://jaygmehta.com/assets/pdf/PS03EMTH32.pdf">Download PDF</a>.</p>
    </embed>
</object> -->
