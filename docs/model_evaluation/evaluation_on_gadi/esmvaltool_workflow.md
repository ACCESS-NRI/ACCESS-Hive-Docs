# ESMValTool on Gadi

## What is ESMValTool?

The Earth System Model Evaluation Tool (ESMValTool) is a tool developed for evaluation of Earth System Models in CMIP. It allows for routine comparison of single or multiple models, either against predecessor versions or against observations. ESMValTool is a community-developed climate model diagnostics and evaluation software package, driven both by computational performance and scientific accuracy and reproducibility. It is open to both users and developers, encouraging open exchange of diagnostic source code and evaluation results from the CMIP ensemble of models. 

For more information, refer to the official [ESMValTool documentation](https://docs.esmvaltool.org/en/latest).

!!! note 
    ACCESS-NRI is supporting a Gadi-specific configuration of ESMValTool via the [_conda/analysis3_](/getting_started/environments) environment. 
    It includes the [ESMValTool](https://github.com/ESMValGroup/ESMValTool) and [ESMValCore](https://github.com/ESMValGroup/ESMValCore) Python packages, with the [ESMValTool collection of recipes and diagnostics](https://docs.esmvaltool.org/en/latest/recipes/index.html). It is configured to use the existing NCI-supported CMIP data collections and [Replicated observational datasets](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f0550_0998_4567_4139). 

ACCESS-NRI is a member of the [ESMValTool Consortium](https://esmvaltool.org/2024-12-11-Consortium_agreement/) and is contributing to the development of the tool for the Australian climate community.

## Using ESMValTool on Gadi

### Prerequisites

- Have an [NCI Account](/getting_started/set_up_nci_account)
- Join the [xp65](https://my.nci.org.au/mancini/project/xp65/join) project for the [_conda/analysis3_](/getting_started/environments) environment.

Depending on your needs, you may want to also join the following supported data collections:

- CMIP6: [fs38](https://my.nci.org.au/mancini/project/fs38/join), [oi10](https://my.nci.org.au/mancini/project/oi10/join)
- CMIP5: [rr3](https://my.nci.org.au/mancini/project/rr3/join), [al33](https://my.nci.org.au/mancini/project/al33/join)
- Observation data collection: [ct11](https://my.nci.org.au/mancini/project/ct11/join)
- ERA5 and ERA5-Land: [rt52](https://my.nci.org.au/mancini/project/rt52/join), [zz93](https://my.nci.org.au/mancini/project/zz93/join)
- obs4MIPs: [qv56](https://my.nci.org.au/mancini/project/qv56/join)

###  Using ESMValTool in a PBS job

_ESMValTool_ YAML recipes should be run within a [PBS job](https://opus.nci.org.au/display/Help/4.+PBS).

_ESMValTool_ is provided on _Gadi_ within the `conda/analysis3` environment.
See [use the environment in a PBS job](/getting_started/environments#use-the-environment-within-a-pbs-job).

To be able to use the `esmvaltool` command, load the `conda/analysis3` environment by adding:
```
module use /g/data/xp65/public/modules
module load conda/analysis3
```

Within the _PBS_ job script you can use the `run` command to run a recipe:
```
esmvaltool run examples/recipe_python.yml
```
See the [ESMValTool running documentation page](http://docs.esmvaltool.org/projects/ESMValCore/en/latest/quickstart/run.html) for more information.


### Using ESMValCore API in a Jupyter notebook

While _ESMValTool_ is used as a term to include both _ESMValTool_ and _ESMValCore_ packages together, though they are separate packages. _ESMValCore_ is the software package which provides the core functionality for _ESMValTool_, such as finding CMIP data and applying commonly-used preprocessing functions, and can be used without _ESMValTool_. 

The example below shows how to use _ESMValCore_ API within a Jupyter notebook.

#### Start an ARE session
Start an [ARE Jupyterlab](/getting_started/are/#jupyterlab) session with the [additional settings required by the conda/analysis3 environment](/getting_started/environments#use-the-environment-within-are).

#### Find and load datasets 
The example below finds all available ensemble members for the dataset defined. 
The `'*'` wildcard is used to find all available entries for the `ensemble` facet.

``` python
from esmvalcore.dataset import Dataset
dataset_search = Dataset(
    short_name='tos',
    mip='Omon',
    project='CMIP6',
    exp='historical',
    dataset='ACCESS-ESM1-5',
    ensemble='*',
    grid='gn',
)
ensemble_datasets = list(dataset_search.from_files())

print([ds['ensemble'] for ds in ensemble_datasets])
```

To load the first ensemble from the desired datasets you can use the `.load()` method:

```python
dataset = ensemble_datasets[0]
cube = dataset.load()
```

#### ESMValCore preprocessors
You can take advantage of built-in preprocessors. 

The example below shows how to find the monthly anomalies and the annual mean of a dataset:
```python
from esmvalcore.preprocessor import annual_statistics, anomalies

# Set the reference period for anomalies 
reference_period = {
    "start_year": 1950, "start_month": 1, "start_day": 1,
    "end_year": 1979, "end_month": 12, "end_day": 31,
}

cube = anomalies(cube, reference=reference_period, period='month')
cube = annual_statistics(cube, operator='mean')
```

See the [API reference](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/api/esmvalcore.preprocessor.html#) for further information on using preprocessors.

### Custom ESMValTool configuration

From version 2.12, ESMValTool looks for its configuration files in the `~/.config/esmvaltool` directory.

To copy an example _ESMValTool_ configuration file to this default directory you can use the `esmvaltool config copy` command.
You can list available example configuration files with `esmvaltool config list`. <br>
For example, to copy the custom configuration `defaults/config-user.yml` to _ESMValTool_'s default directory you can run:

```
esmvaltool config copy defaults/config-user.yml
```

You can edit configuration files in _ESMValTool's_ default folder to suit your needs, 
this would be added to the configuration in _conda/analysis3_.
This environment is pre-configured to access CMIP and observation datasets available on _Gadi_.

For more information on configuration see the [ESMValTool configure documentation](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/quickstart/configure.html#).


To load your own custom configuration from your _ESMValTool_ configuration folder in an _ARE_ Jupyter notebook you can use (You will need to include the full path for your HOME directory in an _ARE_ notebook):
``` python
from esmvalcore.config import CFG

CFG.load_from_dirs(['~/.config/esmvaltool']) 
# ~ is your HOME directory (e.g. /home/111/userid)
```

!!! tip
    This will overwrite the _conda/analysis3_ configuration so you will need to have [data sources](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/quickstart/configure.html#data-sources) configured to find data. This function takes a list so you can combine multiple configuration directories.<br>

### Tutorials

For tutorial series and material from previous workshops see [ESMValTool Tutorials](/tutorials/esmvaltool).
There is also a [tutorial](https://tutorial.esmvaltool.org/) with the ESMValTool organisation which you might find useful though is not taylored for use on _Gadi_.

## ESMValTool example recipes

<!-- Explain what the Tiers mean: Tier3 not to be distributed / license issue, Tier2: some restrictions, but can be redistributed while citing papers etc., Tier1: open for everyone -->
Some _ESMValTool_ example recipes are provided below:


<div class="card-container">
    <a href="https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar5ch9.html" target="_blank" class="vertical-card aspect-ratio1to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/esmvaltool/fig-9-3.png" alt="Computing Access"></img>
        </div>
        <div class="card-text-container bold">Example 1</div>
    </a>
    <a href="https://docs.esmvaltool.org/en/latest/recipes/recipe_perfmetrics.html" target="_blank" class="vertical-card aspect-ratio1to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/esmvaltool/fig4_ipccar5_ch9.png" alt="MED Conda Environment"></img>
        </div>
        <div class="card-text-container bold">Example 2</div>
    </a>
    <a href="https://docs.esmvaltool.org/en/latest/recipes/recipe_emergent_constraints.html" target="_blank" class="vertical-card aspect-ratio1to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/esmvaltool/ltmi1_1.png" alt="Model Variables"></img>
        </div>
        <div class="card-text-container bold">Example 3</div>
    </a>
</div>

## Support

For further assistance on using ESMValTool on _Gadi_, refer to [User support](/about/user_support/) on [ACCESS-Hive Forum](https://forum.access-hive.org.au).

General _ESMValTool_ support (i.e. non-specific to _Gadi_) can be found on the [ESMValTool Discussions](https://github.com/ESMValGroup/ESMValTool/discussions) page, where users can also post technical questions on the _ESMValTool_ installation, application and development. There are community meetings to keep up to date on developments or ask questions to other users. These are announced on the [ESMValTool Community repository](https://github.com/ESMValGroup/Community/discussions). You can also join the [ESMValTool mailing list](https://docs.esmvaltool.org/en/latest/introduction.html#mailing-list).

### Recipes and diagnostics

Contacts for specific diagnostic sets are listed as authors in the source code and in the corresponding [recipe and diagnostic documentation](https://docs.esmvaltool.org/en/latest/recipes/index.html#recipes).


### License

The _ESMValTool_ is released under the Apache License, version 2.0.<br>
Citation of the _ESMValTool_ paper (“Software Documentation Paper”) is requested upon use, along with the software DOI for _ESMValTool_ (**doi:10.5281/zenodo.3401363**) and _ESMValCore_ (**doi:10.5281/zenodo.3387139**) together with the version:

> Righi, M., Andela, B., Eyring, V., Lauer, A., Predoi, V., Schlund, M., Vegas-Regidor, J., Bock, L., Brötz, B., de Mora, L., Diblen, F., Dreyer, L., Drost, N., Earnshaw, P., Hassler, B., Koldunov, N., Little, B., Loosveldt Tomas, S., and Zimmermann, K.: Earth System Model Evaluation Tool (ESMValTool) v2.0 – technical overview, Geosci. Model Dev., 13, 1179–1199, https://doi.org/10.5194/gmd-13-1179-2020, 2020.

Besides the above citation, users are asked to register any journal articles or other scientific documents that use the software on the [ESMValTool website](https://www.esmvaltool.org/). Citing the Software Documentation Paper and registering your papers will serve to document the scientific impact of the Software, which is important for securing future funding. You should consider this an obligation if you have taken advantage of the _ESMValTool_, which represents the end product of considerable effort by the development team.
