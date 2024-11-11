---
layout: page
permalink: /preprints/
title: preprints
description: preprints (papers under preparation)
# years: [2023, 2022, 2020, 2017, 2016, 2015, 2014, 2012]
yearp: [2025-26]
# yearbc: [2023, 2025]
nav: false #true
nav_order: 1
---
<!-- ## Preprints -->
<div class="publications">

{%- for x in page.yearp %}
  <h2 class="year">{{x}}</h2>
  {% bibliography -f preprints -q @*[year={{x}}]* %}
{% endfor %}

</div>

-------------------------------------------------------------------------------------------------------------------
