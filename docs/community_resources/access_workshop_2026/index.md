# Technical Setup for 2026 Land and Coupled Modelling Workshop

🗓️ **Date:** 31 Aug. - 2 Sept. 2026

📍 **Location:** Angliss Institute, 555 La Trobe St, Melbourne VIC 3000

📝 [**Full workshop program**](https://www.access-nri.org.au/access-community-workshop-on-land-and-coupled-modelling/workshop-program-for-land-and-coupled-modelling-2026/)

!!! warning
    Some of the setup steps below can take multiple days. Please complete the setup as soon as possible.

??? note "How to get MOSRS accounts"

    ??? info "For ANU, UNSW, Monash, UniMelb, and UTAS"
        ACCESS-ESM1.6, ACCESS-AM3, and ACCESS-CM3 all utilise the UK Met Office (UKMO) atmosphere model (UM), so you are required to have a MOSRS account to run any of these models due to their licensing restrictions. Please complete the licensing process by following the steps on the [UKMO EULA signing page](https://reporting.access-nri-store.cloud.edu.au/partner_orgs/agreements/individual/ukmo/). 
        <br><br>
        For verification purposes, you will need to have an [ACCESS-Hive Forum](https://forum.access-hive.org.au/) account as you will be added to a forum group of verified MOSRS users. This group will be used as a dedicated channel for communication and MOSRS membership visibility. If you don’t already have a MOSRS account, please tick the box to request that ACCESS-NRI apply for one on your behalf. You must have AAF Authentication on your ACCESS-Hive Forum account for verification purposes (refer to this [guide to add or update AAF authentication](https://forum.access-hive.org.au/t/adding-aaf-authentication/4166)). By completing this UKMO Licensing process, you will also be invited to the [NCI project df42](https://my.nci.org.au/mancini/project/df42), which you will need to accept. This project will be used to control access to UKMO licensed materials that ACCESS-NRI administer. More details on this process can be found in [this Hive Forum post](https://forum.access-hive.org.au/t/accessing-ukmo-licensed-models/6168). 
        <br><br>

    ??? info "For CSIRO and Bureau of Meteorology"
        ACCESS-ESM1.6, ACCESS-AM3, and ACCESS-CM3 all utilise the UK Met Office (UKMO) atmosphere model (UM), so you are required to have a MOSRS account to run any of these models due to their licensing restrictions. Please work with your institution to obtain a MOSRS account (see relevant points of contact on [this webpage](https://opus.nci.org.au/spaces/DAE/pages/249495608/Prerequisites)). Note that this can take several days, so please request a MOSRS account promptly if you wish to take part in the hands-on training for either ACCESS-AM3 or ACCESS-ESM1.6. 
    
    If you do not obtain a MOSRS account by the time of the workshop, you are welcome to attend the training and follow along with a neighbor during the hands-on portions. 

### Session Descriptions

There are four training sessions across the first two days of the workshop. At each time slot, two sessions run in parallel, so you can attend up to two training sessions in total. You are not bound by the selection you made on the registration form. 

??? info "How to run ACCESS-AM3"
    In this hands-on session, you’ll learn the basics of running and configuring ACCESS-AM3 on Gadi. We’ll cover how to run the model, make basic changes to existing configurations, and find and work with model output, with a brief overview of how ACCESS-AM3 fits within the broader ACCESS-NRI infrastructure.  

??? info "How to run ESM1.6"

    In this session, you'll get hands on experience of running and configuring ACCESS-ESM1.6, the recently released earth system model developed for Australia's contribution to the CMIP7 Assessment Fast Track. During this session, we'll cover: 
    
    - What ACCESS-ESM1.6 is, and how it differs to the older model ACCESS-ESM1.5 
    - How to clone and run ACCESS-ESM1.6 configurations using payu on Gadi 
    - Key payu commands and concepts for managing climate model simulations 
    - How to customise ESM1.6 configurations 
    - Where to find more information and get help 

??? info "Using Benchcab"

    Interested in contributing to CABLE? The benchcab tool is used to test all contributions to the CABLE source code, and is a requirement for accepting a CABLE pull request. 
    
    In this training, you will learn about how benchcab works, how to run and compare multiple CABLE versions, and various tips and tricks along the way to help you get started. 

??? info "Finding and accessing ACCESS data for model evaluation"

    This training introduces the ACCESS-NRI Interactive Data Catalogue, a tool for finding and accessing climate data available to the ACCESS community on NCI. 
    
    We’ll first introduce the ACCESS-NRI Intake Catalogue, which underpins the Interactive Catalogue, and briefly explain how it works using a Python-based Jupyter notebook. 
    
    Then we'll dive into finding and discovering data with the Interactive Catalogue - a web-based interface to the Intake Catalogue that provides an easier, more user-friendly way to discover data for evaluating climate models.

---

### Technical Setup

The below table lists the required setup for each session. Please read through the instructions below for the session(s) you plan to attend **before attending the session**.

??? tip "Prerequisites for all training sessions"

    These prerequisites will help you get the most out of the hands-on sessions, but don't worry if you're not familiar with all of them, you're still very welcome to attend and learn along the way! 

    - 💻 Some experience working on NCI will be helpful.

    - :fontawesome-brands-github: Some familiarity with Git and GitHub workflows will be helpful. 
    
    - :fontawesome-solid-terminal: Some familiarity with the Unix command line will be helpful. 
    
    - 🌎 Understanding of basic climate model concepts.

    - 📚 Some familiarity working with Jupyter notebooks may be helpful. 

    - :fontawesome-brands-python: Some familiarity with Python may be helpful. 

| 📝 **Session Name** | ⚙️ **Setup Requirements** |
| ------------------- | -------------------------- |
| **How to run AM3** <br> 📆 31 Aug. 15:30-17:00 | 💻 [NCI](https://my.nci.org.au/mancini/signup) account <br> 🔑 MOSRS account <br> :fontawesome-brands-github: [GitHub](https://github.com/join) account <br> 🔗 Request access to [AM3 configurations repo](https://forum.access-hive.org.au/t/request-access-to-am3-configurations/5580) <br> 📂 Join projects: [access](https://my.nci.org.au/mancini/project/access/join), [vk83](https://my.nci.org.au/mancini/project/vk83/join), [xp65](https://my.nci.org.au/mancini/project/xp65/join), [hr22](https://my.nci.org.au/mancini/project/hr22/join), [nf33](https://my.nci.org.au/mancini/project/nf33/join) |
| **How to run ESM1.6** <br> 📆 31 Aug. 15:30-17:00 | 💻 [NCI](https://my.nci.org.au/mancini/signup) account <br> 🔑 MOSRS account <br> :fontawesome-brands-github: [GitHub](https://github.com/join) account <br> 📂 Join projects: [vk83](https://my.nci.org.au/mancini/project/vk83/join), [nf33](https://my.nci.org.au/mancini/project/nf33/join), [jq44](https://my.nci.org.au/mancini/project/jq44/join) |
| **Using Benchcab** <br> 📆 1 Sept. 15:30-17:00 | 💻 [NCI](https://my.nci.org.au/mancini/signup) account <br> 🔗 [modelevaluation.org](https://modelevaluation.org) account <br> 📂 Join projects: [wd9](https://my.nci.org.au/mancini/project/wd9/join), [ks32](https://my.nci.org.au/mancini/project/ks32/join), [xp65](https://my.nci.org.au/mancini/project/jq44/join), [nf33](https://my.nci.org.au/mancini/project/nf33/join)|
| **Finding and accessing ACCESS data for model evaluation** <br> 📆 1 Sept. 15:30-17:00 | 💻 [NCI](https://my.nci.org.au/mancini/signup) account <br> 📂 Join projects: [xp65](https://my.nci.org.au/mancini/project/xp65/join), [nf33](https://my.nci.org.au/mancini/project/nf33/join), [oi10](https://my.nci.org.au/mancini/project/oi10/join), [fs38](https://my.nci.org.au/mancini/project/fs38/join) <br> ➕ Optional projects: [av17](https://my.nci.org.au/mancini/project/av17/join "ACCESS-AM3 datasets"), [jq44](https://my.nci.org.au/mancini/project/jq44/join "ACCESS-ESM1.6 datasets"), [zv30](https://my.nci.org.au/mancini/project/zv30/join "ACCESS-CM3 datasets"), [p73](https://my.nci.org.au/mancini/project/p73/join "ACCESS-ESM1.5 and ACCESS-CM2 datasets") |
