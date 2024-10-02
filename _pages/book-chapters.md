---
layout: page
permalink: /book-chapters/
title: book chapters
description: Contribution of chapters in books
# years: [2023, 2022, 2020, 2017, 2016, 2015, 2014, 2012]
# yearp: []
yearbc: [2023]
nav: false #true
nav_order: 1
---

<!-- ## Book Chapters -->
<div class="publications">

{%- for x in page.yearbc %}
  <h2 class="year">{{x}}</h2>
  {% bibliography -f bookchapters -q @*[year={{x}}]* %}
{% endfor %}

</div>

-------------------------------------------------------------------------------------------------------------------
