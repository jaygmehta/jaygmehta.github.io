---
layout: page
title: Advanced Group Theory
description: Semester III (PS03EMTH54) <br>
             same as Sem IV (PS04EMTH57)
img: assets/img/groupdjk34.jpg
importance: 1
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
| **Unit-I**          | Definition of a group, some examples of groups, some preliminary lemmas, subgroups, Lagrange’s theorem, Euler’s theorem, Fermat’s theorem, counting principle, the condition for $$HK$$ to be a subgroup, order of $$HK$$, normal subgroups, and quotient groups, characterizations of normal subgroups, homomorphism, isomorphism, first isomorphism theorem, simple group, Cauchy’s theorem for abelian groups, relation of two homomorphic groups. |
| **Unit-II**         | Automorphism, inner automorphism, Cayley’s theorem and its applications, permutation groups, permutation as a product of disjoint cycles and transpositions, even and odd permutations, alternating group, another counting principle, conjugate classes, class equation and its applications, Cauchy’s theorem (general case), number of conjugate classes in permutation group.                                                                 |
| **Unit-III**        | Sylow’s theorem, first proof, definition of $$p$$-Sylow subgroup, second proof of Sylow’s theorem, double cosets and its order, existence of $$p$$-Sylow subgroup in subgroups, second part of Sylow’s theorem, number of $$p$$-Sylow subgroups in a group, third part of Sylow’s theorem, examples based on Sylow’s theorems.                                                                                                                          |
| **Unit-IV**  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Direct products, external direct product and internal direct product, properties of internal direct product, finite abelian groups as direct product of cyclic groups, invariants of an abelian group of order  power of prime $$p$$, the subgroup $$G(s)$$ of an abelian group $$G$$, for an integer $$s$$ for a prime $$p$$, uniqueness of invariants, number of non-isomorphic abelian groups of a given order.                                          |

<br>

### Reference Books

1. Herstein, I. N., Topics in Algebra, (Second Edition), Wiley Eastern Ltd., New Delhi, 1975.
2. Fraleigh J. B., A First Course in Abstract Algebra (Third Edition), Narosa, 1983.
3. Gallian, J. A., Contemporary Abstract Algebra (Fourth Edition), Narosa, 2008.

------------------

## Video Lectures
These videos are discussion of the course on Group Theory of MSc Sem-III of my university. The videos are provided for the students as a part of the additional viewing material during the online course taken on google meet. Any interested mathematician can watch these videos and share his/her valuable feedback or suggestions.

------------------

### Unit 1

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/bLz8caD9aoQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text1">Video Lecture 01</button>
        <div id="text1" class="collapse">
        We discuss some factors indicating significance of groups, the definition of group, motivation behind the definition, and some basic examples.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/VpRBk9XdSFU" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text2">Video Lecture 02</button>
        <div id="text2" class="collapse">
        We try to explore whether the set of all functions from a nonempty set \(S\) onto itself forms a group under composition of functions or not. We find that it doesn't satisfy the property "existence of inverse". Hence, we take bijective functions from \(S\) onto \(S\), which we denote by \(A(S)\). We show that \(A(S)\) is a group under composition. When we take \(S\) to be a finite set, we get the permutation group and we can write the functions as permutation of elements of the set \(S\).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/QLa65PMg2zY" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text3">Video Lecture 03</button>
        <div id="text3" class="collapse">
        We discuss some factors indicating significance of groups, the definition of group, motivation behind the definition, and some basic examples.
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/eo3SReV9NMw" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text4">Video Lecture 04</button>
        <div id="text4" class="collapse">
        We see definition of a subgroup with some examples and related results, and definition of a cyclic group. If \(G\) is a group and \(H\) is a subgroup of \(G\), then we define an equivalence relation on \(G\) by \(a \equiv b \mod H\) if \(ab^{-1} \in H\),  for \(a, b \in G\). We see that the equivalence class of any \(a \in G\) under this relation is nothing but \(Ha\), the right coset of \(H\) in \(G\). We conclude with an exercise to show that there is one-one correspondence between any two (left or) right cosets of \(H\) in \(G\) and between a left coset and a right coset of \(H\) in \(G\).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/8uc9Gmu4RBg" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text5">Video Lecture 05</button>
        <div id="text5" class="collapse">
        We see a sketch of the proof of Lagrange's theorem and some of its important consequences.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/72H--F45ht4" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text6">Video Lecture 06</button>
        <div id="text6" class="collapse">
        We discuss the result that if \(G\) is a group and \(H, K\) are subgroups of \(G\), then \(HK\) is a subgroup of \(G\) if and only if \(HK=KH\). Our next goal is to determine \(o(HK)\) in terms of the number of elements in \(H\) and \(K\). The motivation/intuition related to that is also discussed here in this video at the end.
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/KOXw1igjLPo" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text7">Video Lecture 07</button>
        <div id="text7" class="collapse">
        We discuss the result that if \(G\) is a group and \(H, K\) are finite subgroups of G, then \(o(HK) = \frac{o(H) o(K)}{o(H \cap K)}\). The motivation/intuition based on examples related to this result was discussed at the end of the last video. Furthermore, we prove that if \(G\) is a group of order \(pq\) (product of two primes) and \(p > q\), then \(G\) has at most one subgroup of order \(p\).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/0mHVIPGINA8" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text8">Video Lecture 08</button>
        <div id="text8" class="collapse">
        In this video, we discuss normal subgroups and quotient group.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/_ncDzJxwL-Y" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text9">Video Lecture 09</button>
        <div id="text9" class="collapse">
        In this lecture, we discuss group homomorphism and its properties.
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/aSOTjcav8g4" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text10">Video Lecture 10</button>
        <div id="text10" class="collapse">
        We discuss isomorphism of groups, First Isomorphism theorem (hint for the proof) and Cauchy's theorem for finite abelian groups.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <!-- {% include video.html path="https://youtube.com/embed/hcp_KtyOkPQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text23">Video Lecture 23</button>
        <div id="text23" class="collapse">
        We discuss Third Sylow theorem, simple groups, and applications of Sylow theorems.
        </div> -->
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <!-- {% include video.html path="https://youtube.com/embed/hcp_KtyOkPQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text23">Video Lecture 23</button>
        <div id="text23" class="collapse">
        We discuss Third Sylow theorem, simple groups, and applications of Sylow theorems.
        </div> -->
    </div>
</div>

------------------

### Unit 2

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/KJaZJtWkbYw" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text11">Video Lecture 11</button>
        <div id="text11" class="collapse">
        We discuss automorphism of groups and inner automorphisms.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/VO7jmjDnmFQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text12">Video Lecture 12</button>
        <div id="text12" class="collapse">
        We discuss number of automorphisms of a cyclic group and the proof of Cayley's theorem.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/lt-4G0pl26A" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text13">Video Lecture 13</button>
        <div id="text13" class="collapse">
        We discuss some applications of Cayley's theorem.
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/_-yqYOKD-kk" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text14">Video Lecture 14</button>
        <div id="text14" class="collapse">
        We discuss applications of permutation group. We see the definition of orbit and cycles and prove the result that every permutation can be written as the product of its cycles.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/eoCAGcgWT3Q" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text15">Video Lecture 15</button>
        <div id="text15" class="collapse">
        We discuss transpositions (i.e. \(2\)-cycles), odd and even permutations, every permutation can be written as the product of transpositions, and the alternating group \(A_n\) is a normal subgroup of \(S_n\).        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/a85yytJPqaA" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text16">Video Lecture 16</button>
        <div id="text16" class="collapse">
        We discuss the conjugates of elements of a group \(G\), conjugate class of an element of the group, the normalizer of an element of \(G\) and the class equation of \(G\).
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/pcfjgXTc7aQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text17">Video Lecture 17</button>
        <div id="text17" class="collapse">
        We discuss the two applications of the class equation of a group \(G\). As a first application we see that the center of a \(p\)-group is always non-trivial and hence every group of order a square of a prime is abelian. As another application, we prove general version of Cauchy's theorem. We already proved the Cauchy's theorem for finite abelian groups in Unit-1.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/3j-LNq47i1s" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text18">Video Lecture 18</button>
        <div id="text18" class="collapse">
        We discuss the partition of \(n\) and the following two results:
        1. Two permutations in \(S_n\) have the same cycle decomposition iff they are conjugates of each other and as a consequence.
        2. The number of conjugate classes in \(S_n\) is \(p(n)\), the number of partitions of \(n\).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <!-- {% include video.html path="https://youtube.com/embed/hcp_KtyOkPQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="btn btn-info" data-toggle="collapse" data-target="#text23">Video Lecture 23</button>
        <div id="text23" class="collapse">
        We discuss Third Sylow theorem, simple groups, and applications of Sylow theorems.
        </div> -->
    </div>
</div>

------------------

### Unit 3

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/YhgOOJJe8Zk" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text19">Video Lecture 19</button>
        <div id="text19" class="collapse">
        We discuss the definition of a \(p\)-Sylow subgroup of a group and the proof of Sylow's theorem (combinatorial argument).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/PyLBJe82BZA" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text20">Video Lecture 20</button>
        <div id="text20" class="collapse">
        We discuss another proof of Sylow's theorem (using induction and class equation).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/3upzarmiJy0" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text21">Video Lecture 21</button>
        <div id="text21" class="collapse">
        We discuss the notion of double coset \(AxB\) of two subgroups \(A\) and \(B\) in a group \(G\) and the order of \(AxB\) in terms of the order of \(A\) and the order of \(B\).
        </div>
    </div>
</div>
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/hU5Ynu9Bjik" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text22">Video Lecture 22</button>
        <div id="text22" class="collapse">
        We discuss the Second Sylow Theorem, a unique \(p\)-Sylow subgroup is normal, and the number of \(p\)-Sylow subgroups in G is \(o(G)/o(N(P))\), where \(P\) is any \(p\)-Sylow subgroup and \(N(P)\) denotes its normalizer in \(G\).
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="https://youtube.com/embed/hcp_KtyOkPQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="bibtex hidden" data-toggle="collapse" data-target="#text23">Video Lecture 23</button>
        <div id="text23" class="collapse">
        We discuss Third Sylow theorem, simple groups, and applications of Sylow theorems.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <!-- {% include video.html path="https://youtube.com/embed/hcp_KtyOkPQ" class="img-fluid rounded z-depth-1" %}
        <button type="button" class="btn btn-info" data-toggle="collapse" data-target="#text23">Video Lecture 23</button>
        <div id="text23" class="collapse">
        We discuss Third Sylow theorem, simple groups, and applications of Sylow theorems.
        </div> -->
    </div>
</div>

------------------

## Lecture Notes

<p>Download the PDF file of lecture notes <a href="/assets/pdf/PS03EMTH54.pdf" target="_blank"  class="float-none"><i class="fas fa-file-pdf" style="font-size:24px;color:red"></i></a></p>

<iframe width="100%" height="800" src="/assets/pdf/PS03EMTH54.pdf">

<!-- <object data="https://jaygmehta.com/assets/pdf/PS03EMTH54.pdf" type="application/pdf" width="100%" height="800">
    <embed src="https://jaygmehta.com/assets/pdf/PS03EMTH54.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://jaygmehta.com/assets/pdf/PS03EMTH54.pdf">Download PDF</a>.</p>
    </embed>
</object> -->