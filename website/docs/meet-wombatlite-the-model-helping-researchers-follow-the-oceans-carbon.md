---
title: 'Meet WOMBATlite: the model helping researchers follow the ocean’s carbon'
date: '2026-07-29'
description: 'In short: ACCESS-NRI and CSIRO have released two new configurations of the ACCESS ocean models, ACCESS-OM2 and ACCESS-OM3 featuring WOMBATlite, a new ocean carbon cycle...'
categories:
- News
tags:
- ACCESS Ocean model
- ACCESS-NRI
- Biogeochemical model
- Climate
- WOMBATlite
banner: wp-content/uploads/2026/07/Pixabay-Bluebudgie-seaweed-2360116_1920-1440x500.jpg
---

# Meet WOMBATlite: the model helping researchers follow the ocean’s carbon

*July 29, 2026*

**In short: ACCESS-NRI and CSIRO have released two new configurations of the ACCESS ocean models, ACCESS-OM2 and ACCESS-OM3 featuring WOMBATlite, a new ocean carbon cycle model built to help researchers understand how carbon moves through the ocean, one of the planet’s most important carbon sponges.**

The ocean absorbs roughly a quarter of humanity’s carbon dioxide emissions each year. Understanding how that happens, and how it might change, is essential for predicting our climate’s future. To do that, scientists need models that simulate not just the physical processes of the ocean, such as currents and temperature, but the full web of biological and chemical processes that move carbon through the water column.

That is the job of WOMBAT, the World Ocean Model of Biogeochemistry and Trophic Dynamics. WOMBAT simulates nutrients, plankton, oxygen and carbon, and is coupled into the ocean circulation model MOM as part of Australia’s ACCESS climate model. ACCESS-NRI and CSIRO researchers have now released WOMBATlite, a streamlined new version rebuilt from the ground up.

![](wp-content/uploads/2026/07/Schematic_WOMBATlite_PearseBuchannan-300x169.png)

Schematic of the Carbon cycle, modelled by WOMBATlite. Credit: Pearse Buchannan, CSIRO.

*“We need a carbon cycle model, because climate change is a carbon cycle problem. WOMBATlite is designed to integrate the physical, chemical, and biological processes by which carbon enters and exits the ocean. This is essential as a tool for prediction purposes, but also for basic research purposes,”* [says Dr Pearse Buchanan, Research Scientist at CSIRO](in-conversation-with-pearse-buchanan.md) and co-developer of the model.

This new WOMBAT version has been updated with the latest science, but has also been completely rewritten for use in the next generation of climate models. The previous version, WOMBAT Legacy, was written directly into the older MOM5 ocean model and could not be used with MOM6, the ocean model that now underpins the ACCESS Earth System Model.

*“We basically rewrote the model entirely from scratch. Previously, we had separate copies of WOMBAT in different ACCESS models, and they diverged over time. Now it is one library that can be used across all our models, which means changes made in one place are reflected everywhere,*” says [Dr Dougie Squire, Principal Research Software Engineer in the Ocean Model team at ACCESS-NRI](in-conversation-with-dougie-squire.md).

The new model includes a substantial update of the ecosystem component to better represent phytoplankton growth and their acclimation to light. The iron and calcium carbonate cycles have also been rebuilt to reflect the latest understanding of how they affect the biological and chemical processes in the ocean.

**A hierarchy of models**

Global biogeochemical models are computationally expensive, and versions that include many variables can be too costly to run at high resolution or across the large ensembles that climate research demands. WOMBATlite is designed to find a balance between these constraints, keeping it efficient enough for high-resolution simulations and large ensembles, while still capturing the processes that matter most.

![](wp-content/uploads/2026/07/wombatlite_om3-6-figures-300x287.png)

Key WOMBATlite output variables on the ocean ecosystem and carbon cycle in ACCESS-OM3. Credit: Pearse Buchannan (CSIRO) and Dougie Squire (ACCESS-NRI)

WOMBAT is now available in two versions: lite and mid, with an even more complex version also planned. Each model is suited to different research questions. WOMBATlite trades process detail for efficiency, while WOMBAT-mid offers a richer set of ecological interactions.

*“We called it WOMBATlite because we were trying to stay as light as possible in terms of computational efficiency, while still resolving the processes that are essential for understanding how carbon flows through the ocean,*” says Dr Buchanan.

Having multiple versions of the model makes it possible to manage the tension between computational efficiency and including more variables. For some research questions, researchers need to capture more variables and processes, even if this means slowing down the process.

**A collaboration built for the model**

![](wp-content/uploads/2026/07/Figure-Chlorophyll--300x222.png){ .align-left }WOMBATlite is as much a story about how models get built as what they simulate. The release rests on a close, ongoing partnership between Dr Buchanan’s biogeochemical expertise at CSIRO and Dr Squire’s software engineering at ACCESS-NRI.

*“I think our collaboration has been massively successful. It really comes down to complementary skill sets. There’s a lot of infrastructure ACCESS-NRI puts in place that people don’t notice until it stops working. Having that support means Pearse can focus on what he knows best, pushing the science further, knowing we’ll catch any issues together through review,”* says Dr Squire.

“Because I know I’m supported, I can spread my wings and explore new things, like implementing how seawater viscosity affects the sinking rate of particles, just because I think it matters. That improves my confidence in what I put into the model, scientifically,” says Dr Buchanan.

That same collaboration shaped the [model’s documentation](https://wombat-docs.readthedocs.io/2026.05.001/Model_description/WOMBATlite_model_description/). Dr Buchanan wrote it with students in mind, having struggled himself to learn WOMBAT Legacy without any descriptions.

*“Now, everything is clearly described and linked to the literature it is based on or inspired by. Dougie also encouraged me to include the variable names as they appear in the code, so people can search for an equation and find exactly how it’s implemented,”* says Dr Buchanan.

**What’s next**

WOMBATlite and WOMBAT-mid are opening a new landscape of research questions that scientists couldn’t previously answer or test, and are enabling links with other research areas such as omics, ocean genetics and ecosystem modelling.

In the future, WOMBATlite will be included in the new version of the ACCESS Ocean model, ACCESS-OM3 and the Earth System model ACCESS-ESM1.6 and ACCESS-ESM3, and also contribute to CMIP7 (the Coupled Model Intercomparison Project, Phase 7) and to the Ocean Alkalinity Enhancement MIP (OAE-MIP), supporting international efforts to quantify how alkalinity additions affect ocean carbon uptake, as well as future global carbon budget assessments.

**Acknowledgements**

*Thanks to Matthew Chamberlain and Richard Matear at CSIRO, authors of the original WOMBAT Legacy model on which this work is based.*

*ACCESS-NRI modelling relies on computational and data resources operated by Australia’s [National Computational Infrastructure (NCI)](https://nci.org.au/), located at the Australian National University. ACCESS-NRI and NCI are enabled by the Australian Government, Department of Education, through the National Collaborative Research Infrastructure Strategy (NCRIS).*

---

*![](wp-content/uploads/2025/08/ACCESS-icon-BCG-OCEAN-300x300.png){ .align-left }*

**Would you like to use this model?**
**How to use**
The released configurations can be run using the payu experiment manager. For instructions, see the [ACCESS-Hive Docs – Run ACCESS-OM2 documentation](https://docs.access-hive.org.au/models/run_a_model/run_access-om2/).

**Details of the releases, including a full list of changes, are here:**

- ACCESS-OM2: <https://forum.access-hive.org.au/t/access-om2-release-information/1602/6>
- ACCESS-OM3: <https://forum.access-hive.org.au/t/access-om3-release-information/4494/>

To access the model documentation go to: [WOMBATlite documentation](https://wombat-docs.readthedocs.io/2026.05.001/Model_description/WOMBATlite_model_description/)
Recent publication:<https://bg.copernicus.org/articles/22/5349/2025/>

**Categories:** [News](category/news.md)

**Tags:** [ACCESS Ocean model](tag/access-ocean-model.md), [ACCESS-NRI](tag/access-nri.md), [Biogeochemical model](tag/biogeochemical-model.md), [Climate](tag/climate.md), [WOMBATlite](tag/wombatlite.md)
