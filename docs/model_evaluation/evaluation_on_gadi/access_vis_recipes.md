# ACCESS Visualisation

The [ACCESS-Vis](https://github.com/ACCESS-NRI/ACCESS-Vis) package allows for complex visualisation tasks, including
open-source 3D visualisations. It is used to create interactive visualisations of climate data and 3D visualisations 
for ACCESS-NRI releases. The tools in this package are designed to make it easier for researchers to visualise and 
analyse climate data outputs from the ACCESS models and CMIP datasets.

The [ACCESS Visualisation Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes) repository 
hosts visualisation recipes developed for the ACCESS community.
These recipes enable users to easily visualise climate model data and perform analysis using
Python-based tools. These resources were developed by Owen Kaluza at ACCESS-NRI.


![Heights of Land and Depth of Oceans](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/earth_rotating.gif?raw=true)


## Getting started on Gadi (ARE)

ACCESS-Vis is available to use on Gadi, the steps below will help you set up a JupyterLab session on the [ARE](https://are.nci.org.au), which can be used to run the example notebooks from the recipes repository.

#### Pre-requisites
  - You need to be a member of <a href="https://my.nci.org.au/mancini/project/xp65/join" target="_blank">xp65</a> to use the Gadi installation.
  - Clone the [ACCESS-Visualisation-Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes) repository to your local directory.


#### 1. Open JupterLab on ARE
  - Go to the [Australian Research Environment](https://are-auth.nci.org.au/) website and log in with your NCI
    username and password.
  - Select **JupyterLab** under *Featured Apps*.

#### 2. Configure JupyterLab session
  - **Queue**: Select `gpuvolta`.
  - **Compute Size**: Select `1xGPU (1 gpu, 12 cpus, 95G mem)`.
  - **Storage**: Add the storage paths, and the specific storage you need for data.
    `gdata/xp65, /scratch/$PROJECT, ...` 
    Also, the location for data caching. By default, *ACCESS-Vis* caches its data on Gadi in `/scratch/$PROJECT/$USER/.accessvis`
  - **Module directories**: Add `/g/data/xp65/public/modules`
  - **Modules**: Add the environment: `conda/access-vis`
  *ACCESS-Vis* has been added to the `conda/analysis3` environemnt from `-25.04` so can also be used.

#### 3. Launch your JupyterLab session
  - After configuring the session, click `Launch` and wait for the JupyterLab instance to be ready.
  - Once started, click `Open JupyterLab` 
  - Navigate to the your clone of the recipes repository to begin working with the recipes.


## Alternative use (not on Gadi)

If you're not running on Gadi, you can still use the resources by installing the `accessvis` package locally. To do this,
run the following command to install the package via `pip`:

```bash
pip install accessvis
```

Once the package is installed, you can proceed to use a cloned visualisation recipes repository and interact with climate model data on
your local machine or other computational environments.

## Visualisation Examples

#### Plot Ozone Concentration

[Plot the maximum ozone concentration](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/Examples/annual_maximum_ozone.ipynb) 
for each year (both historical and predicted). 
![Max Ozone Hole](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/max_ozone_level.gif?raw=true)

#### Change the Earth and Sun Based on Time

Change ice cover and greenery based on the time of year or move the sun based on the time of day/year in 
[this notebook](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/02-Sun-And-Seasons.ipynb).
![Sun and Seasons](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/seasons.gif?raw=true)


## Acknowledgements

The python package and visualisation recipes were initially developed by Owen Kaluza at ACCESS-NRI.
To contribute open an issue in the repositories.

[![DOI](https://zenodo.org/badge/875944360.svg)](https://doi.org/10.5281/zenodo.14167706)
[![DOI](https://zenodo.org/badge/767301983.svg)](https://doi.org/10.5281/zenodo.14167608)
