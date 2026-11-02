---
title: ACCESS land modelling team releases the CABLE evaluation tool, benchcab 2.0.0
date: '2023-06-28'
description: The ACCESS-NRI team is pleased to announce the launch of benchcab version 2.0.0. benchcab is a software to run, compare and evaluate the ACCESS land...
categories:
- News
tags:
- ACCESS
- ACCESS-NRI
- benchcab
- CABLE
- evaluation
- model-evaluation
banner: wp-content/uploads/2022/03/Unsplash-Josh-Withers-Forest-Leura-NSW-1440x500.jpg
---

# ACCESS land modelling team releases the CABLE evaluation tool, benchcab 2.0.0

*June 28, 2023*

The ACCESS-NRI team is pleased to announce the launch of benchcab version 2.0.0. benchcab is a software to run, compare and evaluate the ACCESS land model, Community Atmosphere Biosphere Land Exchange (CABLE). CABLE is a land-surface model that simulates energy, water and carbon flows between the land surface and the atmosphere and has been developed by researchers from across the national climate science community. 

This release comes after a long effort started in 2019 by Martin De Kauwe and Gab Abramowitz and current development by the land modelling team at ACCESS-NRI .  

Access the full documentation for benchcab [here](https://benchcab.readthedocs.io/en/stable/).

![](wp-content/uploads/2023/06/benccab-300x169.png)

One of the outputs of the benchcab evaluation tool. It shows statistical ranking of two versions of CABLE for various configurations and physical quantities calculated over a range of statistics and FLUXNET observation sites.

“During the development of CABLE, we need to continuously evaluate its scientific and technical performance when new features are introduced. Several levels of testing are also required to provide rapid feedback during the development phase and more thorough evaluation before approval of new work in a release of CABLE, “ says Dr Claire Carouge, Team leader of the ACCESS-NRI Land Surface team. 

“benchcab has been designed to cover all these use cases, so we are really excited with this release”, says Dr Carouge.  

A CABLE user can simply specify the CABLE versions they want to use and the level of testing they need and benchcab will get the CABLE source codes, compile these and then set up and run all the simulations required for this testing. 

The analysis of the test results uses [modelevaluation.org](https://modelevaluation.org/). This website was built by Gab Abramowitz and his team to provide a web-based platform for analysing model outputs. Using this platform allows users to access analysis scripts and statistical methods that have been developed and honed over the years to help better understand the strengths and weaknesses of land models. 

In this version, benchcab is a Python package distributed via Anaconda. It is currently working exclusively at NCI where it has been centrally installed. This means users simply need to request access to the hh5 project at NCI and load an environment module to access this software. With the current version of benchcab, it is possible to: 

- Run tests at FLUXNET observation sites using a standard set of configurations and analyses.
- Test for bitwise comparison of model outputs between code versions
- Scientifically analyse the effect of a new feature
- Run tests on a customised set of configurations

You can see [a full description of features](https://forum.access-hive.org.au/t/benchcab-python-based-software-for-the-evaluation-of-cable/873) on the ACCESS-Hive forum. To get started with benchcab, please refer to [the documentation](https://benchcab.readthedocs.io/en/stable/). 

Further improvements, such as running gridded simulations, a fully automated process to run and analyse the data and analysis scripts specific to our purpose, are in progress. ACCESS-NRI is aiming to release these improvements later in the year.

**Categories:** [News](category/news.md)

**Tags:** [ACCESS](tag/access.md), [ACCESS-NRI](tag/access-nri.md), [benchcab](tag/benchcab.md), [CABLE](tag/cable.md), [evaluation](tag/evaluation.md), [model-evaluation](tag/model-evaluation.md)
