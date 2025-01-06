# **NBHM MSc 2018:** 

What is the highest power of $3$ dividing $1000!$?

**Solution**

First we count the number of terms in $1000!$ which are divisible by
$5$. They are $3, 6, 9, 12, \ldots, 999$. So the total number of such
terms is 
$$\left\lfloor \frac{1000}{3}\right\rfloor = 333.$$

Now we count the number of terms in $1000!$ which are divisible by
$3^2$. They are $9, 18, 27, \ldots, 999$. These have to be counted twice
but we considered them only once above. Totally we have
$$\left\lfloor \frac{1000}{9}\right\rfloor = 111$$ 
such terms. Now one
more power of $3$ appears in the terms in $1000!$ which are divisible by
$3^3$. But we counted them only twice (once in divisibility by $3$ and
second time in divisibility by $9$). So total number of such terms are
$$\left\lfloor \frac{1000}{3^3}\right\rfloor = 37.$$ 
Similarly, we have
$$\left\lfloor \frac{1000}{3^4}\right\rfloor = 12, \ \left\lfloor \frac{1000}{3^5}\right\rfloor = 4, \ \left\lfloor \frac{1000}{3^6}\right\rfloor = 1,$$
and
$$\left\lfloor \frac{1000}{3^n}\right\rfloor = 0, \qquad \forall\ n \ge 7.$$
Hence, the highest power of $3$ appearing in $1000!$ is
$$333+111+37+12+4+1 =498.$$
