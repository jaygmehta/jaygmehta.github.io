---
layout: page
permalink: #/publications/
title: publications
description: The following are my publications and preprints
years: [2023, 2022, 2020, 2017, 2016, 2015, 2014, 2012]
yearp: [2023]
nav: false #true
nav_order: 1
---
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

## Preprints
<!-- {% comment %} -->
<div class="publications">

{%- for x in page.yearp %}
  <h2 class="year">{{x}}</h2>
  {% bibliography -f preprints -q @*[year={{x}}]* %}
{% endfor %}

</div>
<!-- {% endcomment %} -->
