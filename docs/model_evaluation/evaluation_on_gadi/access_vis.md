# ACCESS-Vis

## What is ACCESS-Vis?

[ACCESS-Vis](https://github.com/ACCESS-NRI/ACCESS-Vis) is a Python-based package for advanced visualisation workflows, including 
open-source 3D visualisations. It supports the creation of interactive 3D climate data visualisations for ACCESS-NRI releases, 
helping researchers more easily explore and analyse outputs from ACCESS models and CMIP datasets.

The [ACCESS Visualisation Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes) repository 
hosts a collection of visualisation workflows developed for the ACCESS community. 
These recipes help users easily visualise and analyse climate model data using ACCESS-Vis. The resources were developed by [Owen Kaluza](https://www.access-nri.org.au/person/owen-kaluza/) at ACCESS-NRI.

<video width="500" autoplay loop muted playsinline>
  <source src="/assets/model_evaluation/vis/earth_rotating.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>



## Use ACCESS-Vis on Gadi

*ACCESS-Vis* is already installed on _Gadi_ within the `xp65` `conda/analysis3` environment.<br>
To use ACCESS-Vis, follow the instruction on [how to use the `conda/analysis3` environment within ARE](/getting_started/environments/#are-jupyterlab), making sure to also specify the following fields in the ARE dashboard:

- **Queue**: `gpuvolta`
- **Compute Size**: `1xGPU (1 gpu, 12 cpus, 95G mem)`

Also make sure to add your project scratch path `/scratch/$PROJECT` to **Storage**, as ACCESS-Vis caches its data on _Gadi_ by default in `/scratch/$PROJECT/$USER/.accessvis`.

## Installation

ACCESS-Vis is available on PyPI, and can be installed via `pip` on your local computer:

```bash
pip install accessvis
```

## Visualisation Examples

#### Plot Ozone Concentration
[This example](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/Examples/annual_maximum_ozone.ipynb) shows how to visualise the maximum ozone concentration for each year (both historical and predicted). 

<video width="500" autoplay loop muted playsinline>
  <source src="/assets/model_evaluation/vis/max_ozone_level.mp4" type="video/mp4">
</video>

#### Change the Earth and Sun Based on Time

[This example](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/02-Sun-And-Seasons.ipynb) shows how to visualise the change in sun position, ice cover and greenery based on the time of day/year.

<video width="500" autoplay loop muted playsinline>
  <source src="/assets/model_evaluation/vis/seasons.mp4" type="video/mp4">
</video>


<custom-references>
- [https://doi.org/10.5281/zenodo.14167706](https://doi.org/10.5281/zenodo.14167706)
- [https://doi.org/10.5281/zenodo.14167608](https://doi.org/10.5281/zenodo.14167608)
</custom-references>
