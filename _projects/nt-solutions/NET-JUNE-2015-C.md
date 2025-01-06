# **NET JUNE 2015 (C):** 

Which of the following primes satisfy the
congruence\
$a^{24} \equiv 6a +2 \mod {13}$?

(a) $41$.<br>
(b) $47$.<br>
(c) $67$.<br>
(d) $83$.<br>

**Solution**

By Euler's theorem, if $a$ is relatively prime to $n$, then
$a^{\phi(n)}\equiv 1 \pmod n$. Here $n=13$ and all choices of $a$ given
are prime. Therefore $(a,13)=1$ and $\phi(13)=12$. Then
$$\begin{align*}
& a^{12} &\equiv &\ 1 \pmod {13}\\
\Rightarrow & {(a^{12})}^{2} &\equiv &\ 1^{2} \pmod {13}\\
\Rightarrow & {(a^{24})} &\equiv &\ 1 \pmod {13}.
\end{align*}$$ 
Then the given congruence
$a^{24} \equiv 6a +2 \mod {13}$ becomes $6a +2\equiv 1 \mod {13}$ or
$6a \equiv -1 \pmod {13}$. For simplicity, multiply both sides of the
congruence by $11$. Then we get
$$66a \equiv -11 \pmod{13} \quad \text{ or } \quad a \equiv 2 \pmod{13}.$$
Substituting the given choices, we observe that $a=41$ and $a=67$
satisfy the congruence $a \equiv 2 \pmod{13}$.


