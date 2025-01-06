# **NET DEC 2023 (C):** 

Let $n \in \mathbb Z$ be such that $n$ is
congruent to $1 \mod 7$ and $n$ is congruent to $4 \mod{15}$. Which of
the following statements are true.

(a) $n$ is congruent to $1$ mod $3$<br>
(b) $n$ is congruent to $1$ mod $35$<br>
(c) $n$ is congruent to $1$ mod $21$<br>
(d) $n$ is congruent to $1$ mod $5$<br>

**Solution**

We solve this by CRT. Since $n \equiv 1 \pmod 7$, $n$ is of the form
$n=7k+1$. Substituting this value in the second congruence, we have
$7k+1 \equiv 4 \mod{15}$. So $7k \equiv 3 \pmod{15}$. Multiplying both
sides by $2$, we get $14k \equiv -k \equiv 6 \pmod{15}$ and so
$k \equiv -6 \equiv 9 \pmod{15}$. Substituting this value of $k$ in $n$,
we get
$$n = 7k+1 \equiv 7 \cdot 9 + 1 \equiv 64 \pmod{15\cdot 7} \equiv 64 \pmod{105}.$$
Therefore, $n = 64 + 105m$, $m \in \mathbb Z$. Hence,
$n \equiv 1 \pmod{3}$, $n \equiv 29 \pmod{35}$, $n \equiv 1 \pmod{21}$,
and $n \equiv 4 \pmod{5}$.


