# ACCESS Visualisation Recipes


There is a repository that hosts visualisation recipes developed for the ACCESS (Australian Community Climate and Earth-System
Simulator) community. The recipes make use of the [accessvis](https://github.com/ACCESS-NRI/ACCESS-Vis) package to create 
interactive visualisations of climate data, including outputs from ACCESS models and other CMIP6 datasets.
These recipes are enable users to easily visualise climate model data and perform analysis using
Python-based tools. Check out the repository: [ACCESS Visualisation Recipes](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes).
The recipes are part of the Model Evaluation and Diagnostics team's efforts at ACCESS-NRI and
were initially developed by Owen Kaluza at ACCESS-NRI.

![Heights of Land and Depth of Oceans](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/earth_rotating.gif?raw=true)


## Getting started on Gadi (Australian Research Environment)

ACCESS-Vis is available to use on Gadi, the steps below will help you set up a JupyterLab session on the [Australian Research Environment (ARE)](https://are.nci.org.au), which can be used to run the example notebooks.

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
  - **Project**: Use your research project, e.g., `xp65`.
  - **Storage**: Add the storage paths, and the specific storage you need for data.
    ```
    gdata/xp65...
    ```
  - **Module directories**: Add:
    ```
    /g/data/xp65/public/modules
    ```
  - **Modules**: Add the environment:
    ```
    conda/access-vis-0.3
    ```

#### 3. Launch your JupyterLab session
  - After configuring the session, click `Launch` and wait for the JupyterLab instance to be ready.
  - Once started, click `Open JupyterLab` 
  - Navigate to the your clone of the repository to begin working with the recipes.

---

## Alternative (Not on Gadi)

If you're not running on Gadi, you can still use the recipes by installing the `accessvis` package locally. To do this,
run the following command to install the package via `pip`:

```bash
pip install accessvis
```

Once the package is installed, you can proceed to use the visualisation recipes and interact with climate model data on
your local machine or other computational environments.

## Visualisation Examples

#### Plot Ozone Concentration

[Plot the maximum ozone concentration](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/Examples/annual_maximum_ozone.ipynb) 
for each year (both historical and predicted). 
![Max Ozone Hole]https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/max_ozone_level.gif?raw=true)

#### Change the Earth and Sun Based on Time

Change ice cover and greenery based on the time of year or move the sun based on the time of day/year in 
[this notebook](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/02-Sun-And-Seasons.ipynb).
![Sun and Seasons](https://github.com/ACCESS-NRI/ACCESS-Visualisation-Recipes/blob/main/assets/gallery/seasons.gif?raw=true)


## Acknowledgements

The visualisation recipes were initially developed by Owen Kaluza at ACCESS-NRI. 
These tools are designed to make it easier for researchers to
visualise and analyse climate data outputs from the ACCESS models and CMIP6 datasets.

For more information or to contribute, please check out the documentation or open an issue in this repository.
[![DOI](https://zenodo.org/badge/875944360.svg)](https://doi.org/10.5281/zenodo.14167706)
