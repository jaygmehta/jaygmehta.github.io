---
layout: page
permalink: /journal/
title: journal publications
description: Papers published in journals #The following are my publications and preprints
years: [2025, 2023, 2022, 2020, 2017, 2016, 2015, 2014, 2012]
# yearp: []
# yearbc: [2023, 2025]
nav: false #true
nav_order: 1
---
For my MathSciNet (MR Reviews) profile: [click here](https://mathscinet.ams.org/mathscinet/author?authorId=1016163)

<!-- ------------------------------------------------------------------------------------------------------------------- -->
<!-- ## Journal Publications -->
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% comment %}
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
  {% endcomment %}
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

-------------------------------------------------------------------------------------------------------------------
