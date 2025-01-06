# **NET SEP 2022 (C): 1 of 2** 

Let $a$ and $b$ be positive integers with $a > b$
and $a+b=24$. Suppose that the following congruences have a common
integer solution. 
$$2x \equiv 3a \pmod 5, \ x \equiv 4b \pmod 5.$$ 
Which
of the following statements are true?

(a) $10 \le a-b \le 20$.<br>
(b) $3b > a > 2b$.<br>
(c) $a > 3b$.<br>
(d) $a-b$ is divisible by $5$.<br>

**Solution**

Multiplying the congruence $2x \equiv 3a \pmod 5$ by $3$ (inverse of $2$
modulo $5$) on both the sides we get, $x \equiv 4a \pmod 5$. So from the
second congruence, we have $4a \equiv 4b \pmod 5$, i.e.,
$5 \mid 4(a-b)$. Since $5 \nmid 4$, we can say that $5 \mid a-b$ and
hence option (d) correct.<br>

Now, $a-b = 5y$. Since $a+b = 24$, either both are odd or both $a$ and
$b$ are even. Then $a-b$ is even and so $a-b = 5y$, where
$y = 0,2,4,6,\ldots$. Since $a>b$, $y=0$ is not possible. Also, $a$ and
$b$ being positive integers such that $a+b = 24$, $y \ge 6$ is not
possible. Hence, $y = 2$ or $y = 4$ and so $10 \le a-b \le 20$. This
shows option (a) is correct.<br>

Finally, if $y = 2$, then $a - b = 10$ and $a+b = 24$ implies $2a = 34$
and so $a = 17$ and $b = 7$. Thus, $a > 3b$ is not possible, i.e.,
option (c) is false. Similarly, if $y = 4$, then $a -b = 20$ and
$a+b = 24$ implies $a = 22$ and $b = 2$. Hence, $3b > a$ is not
possible, i.e., option (b) is false.


