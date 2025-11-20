# ACCESS-Vis

## What is ACCESS-Vis?

[ACCESS-Vis](https://github.com/ACCESS-NRI/ACCESS-Vis) is a Python-based package for advanced visualisation workflows, including 
open-source 3D visualisations. It supports the creation of interactive 3D climate data visualisations for ACCESS-NRI releases, 
helping researchers more easily explore and analyse outputs from ACCESS models and CMIP datasets.

The [ACCESS Visualisation Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes) repository 
hosts a collection of visualisation workflows developed for the ACCESS community. 
These recipes help users easily visualise and analyse climate model data using ACCESS-Vis. The resources were developed by [Owen Kaluza](https://www.access-nri.org.au/person/owen-kaluza/) at ACCESS-NRI.


![Heights of Land and Depth of Oceans](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/earth_rotating.gif?raw=true)


## Use ACCESS-Vis on Gadi

*ACCESS-Vis* is available on Gadi, the steps below will help you set up a JupyterLab session on [ARE](https://are.nci.org.au), which can be used to run the example notebooks from the recipes repository.

#### Pre-requisites
  - You need to be a member of <a href="https://my.nci.org.au/mancini/project/xp65/join" target="_blank">xp65</a> to use the Gadi installation.
  - Clone the [ACCESS-Visualisation-Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes) repository to your local directory.


#### 1. Open JupterLab on ARE
  - Go to the [Australian Research Environment](https://are-auth.nci.org.au/) website and log in with your NCI
    username and password.
  - Select *JupyterLab* under *Featured Apps*.

#### 2. Configure JupyterLab session
  - **Queue**: Select `gpuvolta`.
  - **Compute Size**: Select `1xGPU (1 gpu, 12 cpus, 95G mem)`.
  - **Storage**: Add the storage paths, and the specific storage you need for data.
    `gdata/xp65, /scratch/$PROJECT, ...` 
    
    By default, *ACCESS-Vis* caches its data on Gadi in `/scratch/$PROJECT/$USER/.accessvis`

  - **Module directories**: Add `/g/data/xp65/public/modules`
  - **Modules**: Add the environment: `conda/analysis3`

#### 3. Launch your JupyterLab session
  - After configuring the session, click *Launch* and wait for the JupyterLab instance to be ready.
  - Once started, click *Open JupyterLab* 
  - Navigate to the your clone of the recipes repository to begin working with the recipes.


## Installation

ACCESS-Vis is available on PyPI, and can be installed via *pip*:

```bash
pip install accessvis
```

## Visualisation Examples

#### Plot Ozone Concentration
[This example](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/Examples/annual_maximum_ozone.ipynb) shows how to visualise the maximum ozone concentration for each year (both historical and predicted). 

![Max Ozone Hole](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/max_ozone_level.gif?raw=true)

#### Change the Earth and Sun Based on Time

[This example](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/02-Sun-And-Seasons.ipynb) shows how to visualise the change in sun position, ice cover and greenery based on the time of day/year.

![Sun and Seasons](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/seasons.gif?raw=true)


## Acknowledgements

The python package and visualisation recipes were initially developed by Owen Kaluza at ACCESS-NRI.

[![DOI](https://zenodo.org/badge/875944360.svg)](https://doi.org/10.5281/zenodo.14167706)
[![DOI](https://zenodo.org/badge/767301983.svg)](https://doi.org/10.5281/zenodo.14167608)
