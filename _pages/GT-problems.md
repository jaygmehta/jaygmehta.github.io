---
layout: page
permalink: /gt/
title: Group Theory Problems
description: For Problem Solving (NET)
nav: false
nav_order: 8
# toc:
#   sidebar: left
---
<!-- <h1>Type: Column Question</h1>
<h2>all MCQs in the set are listed, one may attempt one or more whichever one chooses</h2> -->
<div id="h5p-container-12" style="border: 2px dashed red; 
padding: 20px; text-align: center; 
max-width: 800px; margin: 0 auto;"></div>
<script>
  (function() {
    let h5pContainer = document.getElementById("h5p-container-12"); // div tag ID
    let h5pJsonPath = '/H5P/column-34-group'; // YOUR H5P FILE (THIS IS A FOLDER PATH)
    if (!document.getElementById('h5p-bundle-js')) {
      let script = document.createElement('script');
      script.id = 'h5p-bundle-js';
      script.src = '/libs/h5p/main.bundle.js';
      h5pContainer.parentNode.insertBefore(script, h5pContainer.nextSibling);
    }
    window.addEventListener("load", function() {
      const options = {
        h5pJsonPath: h5pJsonPath,
        frameJs: '/libs/h5p/frame.bundle.js',
        frameCss: '/libs/h5p/styles/h5p.css',
      }
      new H5PStandalone.H5P(h5pContainer, options);
    });
  }) ();
</script>