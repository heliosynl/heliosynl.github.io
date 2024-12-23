---
title: 'Yambo for Linear Optics responses'
date: 2024-12-23
excerpt: 'Yambo linear optics responses calculation'
permalink: /posts/2024/blog1223/
type: blog
tags:
  - Ab Initio
  - Yambo
  - Linear Optics
  - blog
---
Optical responses of materials can be computed based on linear response theory, in which considering the electron density response of system to the external electric field. This is linked to the electric displacement field and the polarization field in Maxwell equations:

$$\vec D(\omega)=\varepsilon_0 \varepsilon_r(\omega) \vec E(\omega)=\varepsilon_0 (1+\chi) \vec E$$

in which $$\varepsilon_r=1+\chi$$ is the **relative** dielectric constant, and $$\chi$$ is the electric susceptibility, defining the polarization field $$\vec P=\chi \vec E$$

For simply, use $$\varepsilon(\omega)=1+\chi(\omega)$$ as relative dielectric function, considering its spectral dispersion.

In short, the (**reversed**) dielectric function is the **response function** of the external field. Or, the electrical susceptibility is response function. The generalized form of the definition of response function $$\chi(t)$$ is

$$F(t)=\int_0^{\infty} \chi(\tau) g(t-\tau) d\tau $$

In electric field expression, it is

$$V_{scattering}(\vec r,t)=V_{ext}(\vec r,t)+V_{ind}(\vec r,t)$$
$$V_{scattering}(\vec r,\omega)=\int d\vec r' \chi_{nn}(\vec r, \vec r', \omega)V_{ext}(\vec r,\omega)$$


For Yambo calculation, a prelinminary SCF (or NSCF) calculation of the electron density distribution is needed. Below takes QE PWscf as example
# 0. scf (or nscf)
go to output file, go `prefix.save` folder, type `p2y` (pwscf to yambo for memorizing). Generating folder `SAVE`.

create directory `yambo` at anywhere, and copy `SAVE` to that directory.

# 1. Yambo initialization
just type `yambo` in the shell, the code with detect the present 