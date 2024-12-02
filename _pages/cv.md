---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Mechanical Engineering, The University of Hong Kong, 2027 (expected)
* B.S. in Mechanical Engineering, Beijing Institute of Technology, 2023

Skills
======
* Programming & Modeling
  * Python
  * C
  * C++
  * Matlab
  * COMSOL
  * Bash
* Ab-initio Calculation
  * ABINIT
  * QuantumESPRESSO
  * Material Studio
  * YAMBO
  * VESTA
  * ATOMSK
* Experimental
  * XPS,UPS,REELS,AES (Thermo Scientific Escalab QXi)
  * AFM-IR, Nano-FTIR, s-SNOM (Neaspec IR-neaSCOPE+s)
  * Nano-Raman (Horiba LabRAM Odyssey Nano)
  * UV-VIS-NIR (Agilent Cary 5000)
  * Steady State PL (Edinburgh FLS1000)
  * PL spectroscopy
  * Home-built optical system
* Others
  * SolidWorks
  * AutoCAD

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
