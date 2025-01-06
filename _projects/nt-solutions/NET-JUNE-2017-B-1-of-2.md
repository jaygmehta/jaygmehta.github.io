# **NET JUNE 2017 (B): 1 of 2** 

Let $S$ be the set of all integers from $100$ to
$999$ which are neither divisible by $3$ nor by $5$. The number of
elements in $S$ is

(a) $480$.<br>
(b) $420$.<br>
(c) $360$.<br>
(d) $240$.<br>

**Solution**

Here $|S|=900$. Let $M$ and $N$ be the set of all integers from $100$ to
$999$ which are divisible by $3$ and $5$ respectively. Then
$M=\{102, 105,\ldots\}$, $N=\{100, 105,\ldots\}$ and
$|M| = \frac{900}{3}=300$, $|N| = \frac{900}{5}=180$.<br>

If we compute $|S| - |M| - |N|$, then we have removed the number of
integers from $100$ to $999$ which are divisible by $3$ and divisible by
$5$ separately. But in this process, we would have removed the integers
divisible $3$ as well as by $5$ (i.e. by $15$). So we add the number of
integers from $100$ to $999$ which are divisible by $15$, i.e.
$|M \cap N|$. Now,
$$M \cap N =\{105, 120, \ldots\} \Rightarrow |M\cap N| =\frac{900}{15}=60.$$
So, finally our answer is
$|S| - |M| - |N| + |M\cap N| = 900-300-180+60=480$.


