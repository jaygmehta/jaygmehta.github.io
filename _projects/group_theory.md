---
layout: page
title: Advanced Group Theory
description: Semester III (PS03EMTH54) <br>
             Semester IV (PS04EMTH57)
img: assets/img/groupdjk34.jpg
importance: 1
category: work
---
|:---------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unit-I**          | Definition of a group, some examples of groups, some preliminary lemmas, subgroups, Lagrange’s theorem, Euler’s theorem, Fermat’s theorem, counting principle, the condition for $HK$ to be a subgroup, order of $HK$, normal subgroups, and quotient groups, characterizations of normal subgroups, homomorphism, isomorphism, first isomorphism theorem, simple group, Cauchy’s theorem for abelian groups, relation of two homomorphic groups. |
| **Unit-II**         | Automorphism, inner automorphism, Cayley’s theorem and its applications, permutation groups, permutation as a product of disjoint cycles and transpositions, even and odd permutations, alternating group, another counting principle, conjugate classes, class equation and its applications, Cauchy’s theorem (general case), number of conjugate classes in permutation group.                                                                 |
| **Unit-III**        | Sylow’s theorem, first proof, definition of $p$-Sylow subgroup, second proof of Sylow’s theorem, double cosets and its order, existence of $p$-Sylow subgroup in subgroups, second part of Sylow’s theorem, number of $p$-Sylow subgroups in a group, third part of Sylow’s theorem, examples based on Sylow’s theorems.                                                                                                                          |
| **Unit-IV**  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Direct products, external direct product and internal direct product, properties of internal direct product, finite abelian groups as direct product of cyclic groups, invariants of an abelian group of order  power of prime $p$, the subgroup $G(s)$ of an abelian group $G$, for an integer $s$ for a prime $p$, uniqueness of invariants, number of non-isomorphic abelian groups of a given order.                                          |

Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, *bled* for your project, and then... you reveal its glory in the next row of images.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}
```html
<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```
{% endraw %}
<iframe width="100%" height="800" src="https://jaygmehta.com/assets/pdf/PS03EMTH54.pdf">

<!-- <object data="https://jaygmehta.com/assets/pdf/cv_jay.pdf" type="application/pdf" width="100%" height="800">
    <embed src="https://jaygmehta.com/assets/pdf/cv_jay.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://jaygmehta.com/assets/pdf/cv_jay.pdf">Download PDF</a>.</p>
    </embed>
</object> -->