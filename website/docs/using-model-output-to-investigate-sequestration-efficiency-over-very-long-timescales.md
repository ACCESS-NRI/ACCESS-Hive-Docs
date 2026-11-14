---
title: Using model output to investigate sequestration efficiency over very long timescales
date: '2025-10-03'
description: This paper introduces a computationally efficient approach to calculating carbon sequestration efficiency using climate model archive data.
categories:
- News
tags:
- ACCESS-ESM1.5
banner: wp-content/uploads/2022/03/Unsplash-Smoke-Marek-piwnicki-1440x500.jpg
---

# Using model output to investigate sequestration efficiency over very long timescales

*October 3, 2025*

Over very long timescales, running climate model simulations can be prohibitively expensive and time-consuming, even with the fastest supercomputers. So how can climate models be used to investigate processes that occur over thousands of years?

A recent paper titled *The Sequestration Efficiency of the Deep Ocean* [published in Geophysical Research Letters](https://doi.org/10.1029/2025GL116799) (Pasquier et al., 2025) introduces a computationally efficient approach to calculating carbon sequestration efficiency using climate model archive data.

The premise of the research is simple: if carbon is stored at the seabed, then the ocean will delay the return of this carbon back into the atmosphere. A key question is therefore how long it takes for water at the seabed to return to the surface.

![](wp-content/uploads/2025/10/Pasquier-et-al-2025-Figure-1-1024x833.jpg)

Figure 1 from Pasquier *et al.* (2025). The diagram show the sequestration efficiency, ε, which is the fraction of water that has now reemerged at a specific location, r, after a certain time, τ. However, the methods described in this paper are more important than the results.

The research team, primarily based out of UNSW Sydney and CSIRO, used data from the archives of the [Earth System Model ACCESS-ESM1.5](models/earth-system-model-esm.md), submitted to [phase 6 of the Coupled Model Intercomparison Project (CMIP6)](https://wcrp-cmip.org/cmip-phases/cmip6/). Their approach calculated monthly ocean transport matrices to represent ocean circulation that varies seasonally but repeats yearly.

This idealised approach using model output means that the model does not have to be run directly over timescales on the order of a thousand years, which could take years running on powerful supercomputers.

The lead author, Benoît Pasquier, described the paper as the convergence of a lot of different tools. Beyond the use of the transport matrices themselves, there are two methodological approaches worth highlighting:

1. Instead of injecting ‘dye’ into the ocean and calculating return times to the surface, the water is tracked backwards in time from the surface back to the ocean interior, using an adjoint boundary propagator. This saves significant computational cost.
2. When running ACCESS-ESM1.5 (only required because ACCESS-ESM1.5 was not properly equilibrated in the CMIP6 archives), Anderson Acceleration was used to efficiently spin up the model.

*Thank you to Benoît Pasquier for bringing this paper to our attention, and for taking the time to explain and discuss this paper.*

#### Reference

Pasquier, B., Matear, R. J., Chamberlain, M. A., Ziehn, T., Hutchinson, D. K., Primeau, F. W., et al. (2025). The sequestration efficiency of the deep ocean. *Geophysical Research Letters*, 52, e2025GL116799. <https://doi.org/10.1029/2025GL116799>

**Categories:** [News](category/news.md)

**Tags:** [ACCESS-ESM1.5](tag/access-esm1-5.md)
