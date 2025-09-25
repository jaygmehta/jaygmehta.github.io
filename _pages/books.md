---
layout: page
permalink: /books/
title: books
description: Published Books
# years: [2023, 2022, 2020, 2017, 2016, 2015, 2014, 2012]
# yearp: []
yearb: [2025]
nav: false #true
nav_order: 1
---

<!-- ## Books -->
<div class="publications">

{%- for x in page.yearb %}
  <h2 class="year">{{x}}</h2>
  {% bibliography -f books -q @*[year={{x}}]* %}
{% endfor %}

</div>

------------------------------------------------------------------------------------------------------------------
