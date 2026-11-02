---
title: NESP/ACCESS-NRI community science workshop
date: '2022-11-14'
description: A NESP/ACCESS-NRI hybrid community science workshop was held in Canberra between the 20-21of October 2022 with the participation of 33 people (20 in person and...
categories:
- News
banner: wp-content/uploads/2022/03/Unsplash-BiogeoChem-Javardh-1440x500.jpg
---

# NESP/ACCESS-NRI community science workshop

*November 15, 2022*

A NESP/ACCESS-NRI hybrid community science workshop was held in Canberra between the 20-21of October 2022 with the participation of 33 people (20 in person and 13 online).

#### ![](wp-content/uploads/2022/03/ACCESS-ESM-Model-300x214.png){ .align-left }Objectives of workshop:

The aim of the workshop was to bring the Australian community together to have a discussion around our current modelling capability for CABLE, WOMBAT and ACCESS-ESM.
Further focus was on assessing what the priorities are for any future developments that will help us to better address questions around mitigation pathways and the role of the
terrestrial biosphere, in particular the Australian terrestrial biosphere, and oceans in achieving net zero emissions.

#### The workshop covered a number of topics:

• **Stocktake and review** – led by Ian Harman: Overview of CABLE and CABLE in ACCESS around current capabilities and features
• **Update from LSM summit** – led by Gab Abramowitz: Summary of recent land surface modelling summit in Oxford (UK) including future needs and challenges
• **Land management and nature based solutions** – led by Tammas Loughran:Overview of current work in this area (no land management representation in
ACCESS-ESM)
• **Ocean BGC and WOMBAT** – led by Matt Chamberlain: Overview and potential new developments for WOMBAT including new nutrients, extra phytoplankton classes
and coastal processes. Benefits of higher resolution ocean model for ACCESS-ESM1.5 to the BGC state were shown.
• **Fire modelling in CABLE and ACCESS** – led by Pep Canadell: Overview of SIMFIREBLAZE and POP-LUC coupled to offline CABLE
• **Dynamic vegetation** – led by Juergen Knauer: Overview of tree demography schemein POP
• **Land use and land cover change** – led by Tilo Ziehn: Overview of current land use change scheme in ACCESS-ESM1.5; Ying-Ping Wang provided some information on his new land use change scheme

#### Outcomes and recommendations:

It was generally recognised that:

(a) coupled configurations need stability while offline configurations can accommodate greater complexity,

(b) some applications may only require offline configurations while others need to include the feedbacks,

(c) there will always be a lag between uncoupled and coupled configurations/applications,

(d) intrinsic climate bias remains a challenge for tuning/evaluating land surface models.

Nevertheless, we should maximise use of offline developments in ACCESS wherever possible.
The capability to represent secondary vegetation (managed forests), dynamic vegetation (e.g. tree demography) and disturbances such as fire in the ACCESS Earth System Model has been identified as one of the highest priorities during the discussion of this workshop. The well-established modular framework POP (demography)-LUC (land use change) and SIMFIRE-BLAZE (fire) offer this capability. The development of these components was led by the Australian community and has been evaluated coupled to a version of CABLE (offline) through global TRENDY simulations.

The primary and most urgent recommendation, therefore, is for the CABLE community to move rapidly towards enabling the version of CABLE used in ACCESS-ESM1.5 with this
capability. The following steps were agreed to implement this recommendation:

1. Establish a working group to investigate the technical feasibility of coupling POP-LUC and SIMFIRE-BLAZE to CABLE in ACCESS-ESM1.5, specifically whether running those
components as a separate executable is the preferred option.
2. If implementation is possible, the working group is to also map out resource requirements and timeframe for coupling and evaluation in ACCESS-ESM1.5 so that
this new development can be made available for CMIP7.
3. Investigate feasibility and resourcing of merging POP-LUC/BLAZE capability into CABLE3 trunk for other offline users or separate out in offline case as well.
4. Assess what other features/capabilities are available from the Canberra CABLE branch(es) and what value they might add to ACCESS-ESM.
5. Lead researchers across the key Agencies should brief their respective managers who should develop a joint resourcing strategy, and timeline, for these steps.

Other recommendations include:
• Manual coupling of CABLE to the UM (JaC won’t be available for UM) for development of next generation ACCESS model is essential.
• Stop putting JAC-related tickets through MetOffice code review unless also applicable for NGMS.
• Benchmarking (e.g. ILAMB) and documentation need to be progressed (documentation workshop 7-8 Nov; ACCESS-NRI is also working on ILAMB availability).
• Implementation of crop model (including irrigation, harvest and fertilization) in ACCESS-ESM would provide capability around land management (Tammas and Juergen to follow-up on initial work by Juergen on crop capability).
• Higher resolution (1/4 degree) ocean model with WOMBAT for ACCESS-ESM1.5. The development of new capabilities (nutrients, size classes and/or processes) will depend in part on the interests of the new CSIRO hire and ongoing community interaction (e.g. COSIMA).
• A CABLE offline configuration that can (approximately) reproduce CABLE in ACCESS would be valuable for spin-up, tuning, sensitivity testing and any future developments.

**Categories:** [News](category/news.md)
