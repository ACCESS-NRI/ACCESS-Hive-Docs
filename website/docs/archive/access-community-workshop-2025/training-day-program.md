---
title: Training Day program for ACCESS Community Workshop 2025
description: The ACCESS Training Day 2025 is held on Tuesday 9 September. It contains a mix of instructor-led sessions and unstructured sessions.
---

# Training Day program for ACCESS Community Workshop 2025

The ACCESS Training Day 2025 is held on Tuesday 9 September. It contains a mix of instructor-led sessions on a particular topic, and unstructured sessions where ACCESS-NRI staff will be on hand to answer questions and clarify concepts. The program is subject to amendments—please revisit this webpage for the most up-to-date version of the program.

[Download PDF version of Training Day program](../../wp-content/uploads/2025/08/ACCESS-Training-Day-2025-Program-and-Session-Details-4.pdf){ .buttononblue }

On this page:

- [Program overview](#Overview)
- [Session details](#Details)
  - [Advanced Git](#Advanced-Git)
  - [Git workflows and GitHub best practices](#Git-workflows)
  - [Unlocking the power of Xarray and Dask for large data analysis](#Xarray-Dask)
  - [Hands-on training in machine learning models with PyEarthTools](#PyEarthTools)
  - [Evaluating ENSO in ACCESS Models for CMIP7](#ENSO)
  - [Unstructured sessions: Getting started running ACCESS models](#Unstructured-basic)
  - [Unstructured sessions for advanced users: Alpha/beta release testing](#Unstructured-advanced)

## Program overview { #Overview }

An overview of the sessions is displayed in the table below. For a more detailed description of each session and its learning objectives, intended audience, and prerequisites, visit the [session details](#Details) section of this webpage.

| Time | Session | Topic | Location |
| --- | --- | --- | --- |
| *09:00–09:30* | *Arrival* | *Registration and tea/coffee* | *Foyer areas, The Lab* |
| 09:30–11:00 | Structured sessions | [Unlocking the power of Xarray and Dask for large data analysis](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Xarray-Dask) | M13/M14 |
| [Advanced Git](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Advanced-Git) | M03 |
| Unstructured sessions:   - [Getting started running ACCESS models](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Unstructured-basic)  - [For advanced users: Alpha/beta release testing](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Unstructured-advanced) | ACCESS-ESM1.5 and ACCESS-ESM1.6 | M01/M02 |
| ACCESS-OM2 | M06 |
| ACCESS-rAM3 | M07 |
| CABLE and ACCESS-AM3 | M10 |
| *11:00–11:15* | *Morning tea* | *Food served at The Lab* | *The Lab, Foyer areas* |
| 11:15–12:45 | Sessions started before morning tea (from 09:30–11:00) continue in the same rooms. | | |
| *12:45–13:45* | *Lunch* | *Food served at The Lab* | *The Lab, Foyer areas* |
| 13:45–15:15 | Structured sessions | [Hands-on training in machine learning models with PyEarthTools](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#PyEarthTools) | M13/M14 |
| [Git workflows and GitHub best practices](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Git-workflows) | M03 |
| [Evaluating ENSO in ACCESS models for CMIP7](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#ENSO) | M01/M02 |
| Unstructured sessions:   - [Getting started running ACCESS models](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Unstructured-basic)  - [For advanced users: Alpha/beta release testing](https://www.access-nri.org.au/access-community-workshop-2025/training-day-program/#Unstructured-advanced) | ACCESS-OM2 and ACCESS-OM3 | M06 |
| ACCESS-rAM3 | M07 |
| ACCESS-AM3 | M10 |
| ACCESS-CM3 | M08 |
| ACCESS-ESM1.5 | M16 |
| *15:15–15:30* | *Afternoon tea* | *Food served at The Lab* | *The Lab, Foyer areas* |
| 15:30–17:00 | Sessions started before afternoon tea (from 13:45–15:15) continue in the same rooms. | | |

## Session details { #Details }

The details on each session are described below. Note that it is possible that a session will not run depending on room allocations and registration numbers.

#### Advanced Git { #Advanced-Git }

*Instructor: **Micael Oliveira***

Learn how to use Git more effectively by becoming familiar with more advanced concepts and commands. If you have been using Git at a basic level but would like to understand what a commit is, what really happens during a merge, what the difference is between a merge and a rebase, or how to fix mistakes, then this tutorial is for you.

Learning objectives:

- Understand what a Git directed acyclic graph (DAG) is.
- Learn how more advanced Git commands work (merge, rebase, restore etc.), and how they change DAG.
- Learn how to undo and fix common mistakes when using Git.

Intended audience:

- All backgrounds, domains, and career stages.
- Those who want to improve their Git skills.

Pre-requisites:

- Working knowledge of **basic Git commands** (add, commit, pull, push).

#### Git workflows and GitHub best practices { #Git-workflows }

*Instructor: **Micael Oliveira***

This session builds on the *Advanced Git* session, taking the next step by focusing on Git workflows and GitHub best practices. Specifically, we will explain some common Git workflows used by developers to collaborate efficiently and share some best practices when using GitHub.

Learning objectives:

- Exposure to common Git workflows in software development.
- Understanding of how to best use Git and GitHub for scientific software development.

Intended audience:

- Those who want to use Git and GitHub for scientific software development.
- All domains and career stages.

Pre-requisites:

- Attendance at the session ***Advanced Git***.
- **OR all of the following:**
  - Working knowledge of **advanced Git commands** (merge, rebase, restore etc.).
  - Basic familiarity with **GitHub**.

#### Unlocking the power of Xarray and Dask for large data analysis { #Xarray-Dask }

*Instructors: **Jemma Jeffree**, **Paige Martin** and **Thomas Moore***

The python packages Xarray and Dask underpin the analysis of large datasets such as climate model output, reanalysis, or observations. As such, these packages are key tools for climate scientists. However, both packages remain an enigma to many of the scientists who use them.

This session will provide you with the skills to optimise your analysis code—ie, improve both speed and memory usage—with Xarray and Dask, focussing specifically on climate model output on Gadi. We will explain what happens “under the hood” of both libraries, and build on this understanding, with additional techniques, to boost code performance.

Learning objectives are to answer the questions:

- What does it mean to write good code, and why should you bother?
- How can Xarray and Dask help with this objective, and what do they actually do?
- Why does chunking matter, and how should you choose chunks?
- How do you troubleshoot performance issues in your Dask workflows?
- When does it not make sense to use Dask?

Intended audience:

- Any scientist who analyses large datasets in NetCDF or Zarr files with python (or who would like to).
- Tailored to scientists who use Xarray, but who find Dask troublesome.

Pre-requisites:

- Familiarity with scientific programming in **Python**.
- Basic familiarity with **Xarray** (i.e., you have previously used Xarray to open a dataset, and done some analysis (such as calculating a mean) on that data. If you’re not yet familiar with Xarray, [this tutorial](https://foundations.projectpythia.org/core/xarray/xarray-intro/) is a good place to start).
- Active NCI account.

#### Hands-on training in machine learning models with PyEarthTools { #PyEarthTools }

*Instructor: **Tennessee Leeuwenburg***

This session will take you through several applied, real-world machine learning projects to gain a hands-on understanding of the tools and processes for applied machine learning research. You will use PyEarthTools framework to train three models and gain an understanding of how to apply machine learning to your own projects.

Learning objectives:

- A brief introduction to core techniques of machine learning, and how to apply to your own projects.
- 1: Train your own global earth system model.
- 2: Train a climate bias correction model.
- 3: Train a model to perform observations quality control.
- Examples include deep neural networks based on PyTorch, and a gradient-boosted decision tree based on XGBoost.

Intended audience:

- Those who want to use machine learning for Earth system science.
- Those interested in model development of observational data handling.
- All backgrounds, domains and career stages.

Pre-requisites:

- The ability to run and execute a **Jupyter Notebook**.
- A basic knowledge of **Python** and of **meteorological data**.
- An NCI account is not required, but may be the preferred platform for most participants. If you do not use NCI, some local machine setup will be required in advance.

#### Evaluating ENSO in ACCESS Models for CMIP7 { #ENSO }

*Instructors: **Romain Beucher** and **Felicity Chun***
This session will focus on how to evaluate ENSO in ACCESS models ahead of CMIP7. We’ll give an overview of the evaluation framework being developed by ACCESS-NRI and show how it can help make ENSO evaluation more consistent and easier to run. We’ll walk through the [ACCESS-ENSO-Recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes), which provide practical examples and workflows that participants can adapt to their own work. We’ll also touch on simple ways to prepare raw model outputs so they can be used in these workflows. The session will include time for discussion and feedback to help shape future development.

Learning objectives:

- Learn how to run standard ENSO evaluations using current workflows.
- Understand what the ACCESS-ENSO-Recipes offer and how to use them.
- Get tips on preparing model output for analysis.
- Share feedback on evaluation needs for CMIP7.

Intended audience:

- Anyone involved in ACCESS model development or interested in evaluating ENSO for CMIP7.

Pre-requisites:

- Familiarity with **Gadi** and the ability to run a **JupyterLab** session on the **Australian Research Environment (ARE)**.
- Some experience with **Python** and the **conda/analysis3** environment.
- Active **NCI account**.

#### Unstructured sessions: Getting started running ACCESS models { #Unstructured-basic }

These self-guided sessions are for those who want to get started running [an ACCESS model](https://docs.access-hive.org.au/models/). ACCESS-NRI staff will be on hand to answer questions and clarify concepts. There is no formal instruction—participants will follow online documentation on how to run a model (the [Run a Model section of the ACCESS-Hive Docs](https://docs.access-hive.org.au/models/run_a_model/) for ACCESS-ESM1.5, ACCESS-OM2, and ACCESS-rAM3 or [CABLE documentation](https://cable.readthedocs.io/en/latest/)) and go at their own pace.

Learning objectives:

- Run an ACCESS climate model.
- Explore documentation and tools relevant to ACCESS models.
- Chat with ACCESS-NRI staff to clarify concepts and model approaches.

Intended audience:

- Anyone interested in running one of the listed models.

Pre-requisites:

- Basic understanding of climate modelling concepts and terminology.
- Basic familiarity with the command line.
- Active **NCI account**.
- **No previous experience** running a climate model is required.

#### Unstructured sessions for advanced users: Alpha/beta release testing { #Unstructured-advanced }

These self-guided sessions are for **experienced model users** who want to contribute to the testing of alpha and beta releases of ACCESS-ESM1.6, ACCESS-AM3, ACCESS-CM3, or ACCESS-OM3. ACCESS-NRI staff will be on hand to answer questions, support troubleshooting, and gather input. There is **no formal instruction**–participants will work independently or in small groups.

Learning objectives:

- Gain experience with pre-released versions of climate models.
- Contribute to the improvement of climate models and documentation.
- Gain experience documenting issues for model developers.

Intended audience:

- Advanced users with significant experience running ACCESS climate models.

Pre-requisites:

- Significant experience running ACCESS climate models on Gadi.
- Ability to debug model code and interpret error logs.
- Active **NCI account**.
