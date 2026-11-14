---
title: 'Modernising climate modelling software: the ACCESS OM2 model starts using a new software pipeline'
date: '2024-05-16'
description: 'In short: ACCESS-NRI, Australia’s Climate Simulator, has completed its first fully supported model release: the ACCESS-OM2 Ocean and Sea-Ice Model. This release uses a...'
categories:
- News
tags:
- ACCESS-NRI
- Climate
- Earth system
- Ocean model
- simulator
- software pipeline
---

# Modernising climate modelling software: the ACCESS OM2 model starts using a new software pipeline

*May 16, 2024*

**![](wp-content/uploads/2024/05/ACCESS-NRI-Software-Pipeline-300x300.png){ .align-left }**

**In short:** ACCESS-NRI, Australia’s Climate Simulator, has completed its first fully supported model release: the ACCESS-OM2 Ocean and Sea-Ice Model. This release uses a new software pipeline and best practices to ensure that models produce reliable results and can be easily found and used by researchers. 

**What’s next?**ACCESS-NRI will apply this new software integration and deployment pipeline to all the models released in the future, including the new version of the ocean and sea-ice model ACCESS-OM3. 

 **ACCESS-NRI, Australia’s Climate Simulator**, recently completed the release of ACCESS-OM2, the ACCESS Ocean-Sea Ice computer model, to the Australian research community using a![](wp-content/uploads/2024/05/Visuals-Hive-Style-1-300x300.png){ .align-right } new software integration and deployment pipeline. This is ACCESS-NRI’s first fully supported version of ACCESS-OM2 and the same pipeline will be applied to all Earth System models and software tools released by ACCESS-NRI in the future.  

Computer models are the climate scientist’s equivalent of laboratory experiments, allowing researchers to explore the intricate dynamics of our planet’s climate system. These models, just like instruments in a laboratory, need continuous maintenance and support to ensure they are reliable, reproducible and replicable. 

“Our role as a software infrastructure, is to ensure scientists can be confident that any variation in their climate model outputs is due to factors under their control, rather than changes in software or tools used to build their model.” says Dr Aidan Heerdegen, team leader of the ACCESS-NRI Model Release team. 

This new pipeline brings three main new features: 

- **Software engineering best practices**, such as continuous integration testing and continuous deployment, to the scientific code used to model our Earth’s systems.
- [**Spack****,**](https://spack.io/) a build-from-source package manager that has revolutionised the way climate models are managed on high-performance computers. Spack works by creating a wrapper around every software package, like a Lego piece, to make it easier to join software together allowing us to build reproducible and reliable climate models across many platforms.
- **The pipeline is configured and run from GitHub**, adhering to the FAIR principles (e.g., Findability, Accessibility, Interoperability, and Reusability).

“This modern pipeline with in-built quality assurance checking makes it possible for us to scale. The manual nature of previous approaches is error prone, requiring significantly more effort to prevent the introduction of errors,” says Dr Heerdegen. 

![](wp-content/uploads/2024/05/ACCESS-NRI-Software-Pipeline1-1-300x300.png){ .align-left }**ACCESS-OM2**, being fully open-source and well documented, was a perfect test-case for ACCESS-NRI’s new software pipeline to ensure the model produces robust results and is reproducible.  This model stands as a cornerstone in climate research, unravelling the complexities of the oceans and their role in shaping our planet’s climate. ACCESS-OM2 was [developed by the Consortium for Sea-Ice Modelling in Australia (COSIMA)](https://cosima.org.au) and first described in [Kiss et al. (2020)](https://gmd.copernicus.org/articles/13/401/2020/). 

“Since its release in 2019, this multi-resolution model suite has been widely adopted in Australia, underpinning more than 70 publications by approximately 180 researchers from many Universities in Australia as well as national research organisations, such as CSIRO, the Bureau of Meteorology and the Australian Antarctic Division (AAD) and international institutions like the National Oceanic and Atmospheric Administration (NOAA)”, says Australian National University’s Dr Andrew Kiss, who has been working with ACCESS-OM2 since its release.  

“A fantastic aspect of ACCESS-OM2 is that many researchers have used it and improved it over the years and record their experiments in the COSIMA Cookbook, a collection of software recipes that allows users to benefit from other people’s experiments and get the output they need without knowing the complex details of the model. This has grown into a cooperative cultural approach of co-creation, where everything is open and transparent and the tools and data are easily accessible,” says Dr Kiss. 

Thanks to the support from ACCESS-NRI, researchers can now focus on the development of its successor, ACCESS-OM3, which will update Australia’s ocean and sea ice modelling systems to keep abreast of the leading edge of international model development. ACCESS-OM3’s features include new components such as a wave model, updated biogeochemistry and representation of ice-wave and ice-ocean interactions together with much higher-resolution regional configurations that will be used for Australia’s next Coupled Model Intercomparison Project (CMIP7) submission.  

“The support from ACCESS-NRI means that we can dramatically increase the scope of things we can attempt to do and the rate at which we can achieve them,” says Dr Andrew Kiss. 

ACCESS-NRI will apply this software pipeline to all the models released in the future. Future enhancements of the release pipeline will also focus on improving further data reproducibility with end-to-end provenance of all model input and output data.  

Image credits: Blue globe: Adele Morrison, COSIMA and ANU. Surface current speed in the 0.1° global model ACCESS-OM2-01, highlighting the East Australian Current and Antarctic Circumpolar Current.

---

**![](wp-content/uploads/2024/05/ACCESS-NRI-Software-Pipeline2-300x300.png){ .align-left }Interested in running ACCESS-OM2?** You can find our ACCESS-OM2 User Guide [here](https://docs.access-hive.org.au/models/run_a_model/run_access-om2/).    

Release information can be found on our ACCESS Hive Forum [**here**](https://forum.access-hive.org.au/t/access-om2-release-information/1602)**.** 

**Need support?** See the [ACCESS Help and Support topic](https://forum.access-hive.org.au/t/access-help-and-support/908) for details on how to get help from our team!  

ACCESS-NRI modelling relies on computational and data resources from high-performance supercomputers operated by Australia’s [**National Computational Infrastructure (NCI)**](https://www.nci.org.au/) located at [The Australian National University](https://www.anu.edu.au/). 

ACCESS-NRI and NCI are enabled by the Australian Government, Department of Education, through the National Collaborative Research Infrastructure Strategy (NCRIS).

**Categories:** [News](category/news.md)

**Tags:** [ACCESS-NRI](tag/access-nri.md), [Climate](tag/climate.md), [Earth system](tag/earth-system.md), [Ocean model](tag/ocean-model.md), [simulator](tag/simulator.md), [software pipeline](tag/software-pipeline.md)
