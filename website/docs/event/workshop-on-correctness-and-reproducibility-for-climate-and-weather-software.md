---
title: Workshop on Correctness and Reproducibility for Climate and Weather Software
description: In this workshop, we aim to provide a venue to discuss challenges, opportunities, and recent advances in ensuring software correctness and reproducibility for climate and...
tags:
- Climate
- Models
- tools
type: event
banner: wp-content/uploads/2022/03/ACCESS_Andy-Hogg_400mwholedomain-1440x500.jpg
---

# Workshop on Correctness and Reproducibility for Climate and Weather Software

*November 9, 2023*

In this workshop, we aim to provide a venue to discuss challenges, opportunities, and recent advances in ensuring software correctness and reproducibility for climate and weather modelers, HPC community members, and industry partners.

When: 9-10 November

Where: NCAR’s Mesa Laboratory (in person) and Online

More information and to register:<https://ncar.github.io/correctness-workshop/>

Link to the Hive-Forum topic: <https://forum.access-hive.org.au/t/workshop-on-correctness-and-reproducibility-for-climate-and-weather-software/1368>

Model simulations are essential tools for understanding weather and climate. As we adapt to our changing climate, simulation codes inform both our understanding and policy decisions. These complex software artifacts are often the result of multiple decades of development. And they are in a state of near-constant development as scientific capabilities advance and high-performance computing (HPC) technologies evolve.

Given the societal importance of these codes, maintaining confidence and preserving code quality and reliability is critical. Yet scientific computing applications are often developed without the use of extensive software verification tools and techniques. Instead, development practices are typically dominated by short-term concerns about performance, resources, and project timelines. Technical challenges in running and evaluating climate and weather models further complicate code verification efforts. Given the scale of these models, a thorough correctness evaluation may be prohibitively expensive. It is also customary to require regression tests to yield bitwise identical results. This requirement is often unmet due to the chaotic nature of climate and weather models and the large variety of hardware/software environments they are run on. When bitwise identical results cannot be sought, field experts are to evaluate model results in a time-consuming and subjective manner.

In short, climate and weather modeling communities are in need of practical and feasible means of ensuring correctness and reproducibility. For example, we are interested in means to easily assess whether changes to a model code result in output that is systematically different or introduce artifacts that could influence scientific conclusions. Such changes may include hardware or software stack infrastructure differences, replacing parts of the model with ML-routines, or applying data compression to the output data. In this workshop, we aim to provide a venue to discuss challenges, opportunities, and recent advances in ensuring software correctness and reproducibility for climate and weather modelers, HPC community members, and industry partners.

Topics of interest include but not limited to:

- Tools and approaches for software testing, debugging, quality assurance, and continuous integration.
- Statistical and ensemble-based approaches for evaluating model consistency and software correctness.
- Software design approaches and development practices for streamlining correctness and reproducibility efforts.
- Formal methods, abstraction, and logical proof techniques for rigorous verification.
- Verifying and validating large-scale applications running on HPC clusters, cloud computing systems, heterogeneous systems, GPUs, etc.
- Other software correctness and reproducibility approaches for facilitating verification and validation.

**Tags:** [Climate](../tag/climate.md), [Models](../tag/models.md), [tools](../tag/tools.md)
