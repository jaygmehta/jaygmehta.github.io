---
layout: page
title: NET-JUNE-2015-C-3-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $\sigma : \{1,2,3,4,5\} \to \{1,2,3,4,5\}$ be a permutation (one-one and onto function) such that $\sigma^{-1}(j) \le \sigma(j)$, $\forall\ j$, $1 \le j \le 5$. Then which of the following are true?

(a) $\sigma \circ \sigma (j) = j$ for all $j$, \ $1 \le j \le 5$.<br>
(b) $\sigma^{-1}(j) = \sigma (j) = j$ for all $j$, \ $1 \le j \le 5$.<br>
(c) The set $\{k: \sigma (k) \neq k\}$ has even number of elements.<br>
(d) The set $\{k: \sigma (k) = k\}$ has odd number of elements.<br>

**Solution**

$\sigma^{-1}(j) \le \sigma(j)$, $\forall\ j$, $1 \le j \le 5$ implies that $\sigma^2(j) \ge j$ for all $j=1,2,3,4,5$. 

(a) $\sigma^2(5) \ge 5 \Rightarrow \sigma^2(5) = 5$. But then $\sigma^2(4) = 4$ as sigma is one-one and so it cannot be $5$. Similarly, $\sigma^2(j) = j$ for all $j=1,2,3,4,5$.<br>
(b) Applying $\sigma^{-1}$ we get $\sigma^{-1}(j) = \sigma(j)$ for all $j=1,2,3,4,5$.<br>
(c) Since $\sigma^2 = e$, $\sigma$ is either $e$ or of the form $2+1+1+1$ or $2+2+1$. In each case $\sigma$ permutes $0, 2$ and $4$ elements respectively. Hence, the set $\{k: \sigma (k) \neq k\}$ has even number of elements.<br>
(d) Since total $5$ elements are there in $\{1,2,3,45\}$, from above it follows that the set $\{k: \sigma (k) = k\}$ has odd number of elements.