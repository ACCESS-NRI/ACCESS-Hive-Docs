# ESMValTool-workflow on Gadi

## What is ESMValTool?

The Earth System Model Evaluation Tool (ESMValTool) is a tool developed for evaluation of Earth System Models in CMIP (Climate Model Intercomparison Projects). It allows for routine comparison of single or multiple models, either against predecessor versions or against observations. ESMValTool is a community-developed climate model diagnostics and evaluation software package, driven both by computational performance and scientific accuracy and reproducibility. It is open to both users and developers, encouraging open exchange of diagnostic source code and evaluation results from the CMIP ensemble of models. 

For more information, refer to the official <a href="https://docs.esmvaltool.org/en/latest" target="_blank">ESMValTool documentation</a>.

<!--<div class="card-container">
    <a href="https://docs.esmvaltool.org/en/latest/" target="_blank" class="vertical-card aspect-ratio2to1">
        <div class="card-image-container">
            <img src="../../../assets/model_evaluation/logo_esmvaltool.png" alt="ESMValTool" class="img-cover"></img>
        </div>
        <div class="card-text-container bold">ESMValTool</div>
    </a>
</div> -->

<div class="note">ACCESS-NRI is supporting a Gadi-specific configuration of ESMValTool under the name <i>ESMValTool-workflow</i>. </div> 

*ESMValTool-workflow* is the ACCESS-NRI software and data infrastructure that enables the ESMValTool evaluation framework on NCI Gadi. It includes the <a href="https://github.com/ESMValGroup/ESMValTool" target="_blank">ESMValTool</a>/<a href="https://github.com/ESMValGroup/ESMValCore" target="_blank">ESMValCore</a> Python packages, the <a href="https://docs.esmvaltool.org/en/latest/recipes/index.html" target="_blank">ESMValTool collection of recipes and diagnostics</a> and some <a href="https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f0550_0998_4567_4139" target="_blank">observational datasets</a>. *ESMValTool-workflow* is configured to use the existing NCI supported CMIP data collections. 

## Using ESMValTool on Gadi

### Pre-requisites

<i>ESMValTool</i> is provided through the <a href="https://my.nci.org.au/mancini/project/xp65/join" target="_blank">xp65</a> project on Gadi.To enable the  <i>ESMValTool-workflow</i>, you need to be a member of the <i>xp65</i> NCI project.

Depending on your needs, you may want to also join the following supported data collections:

- CMIP6: <a href="https://my.nci.org.au/mancini/project/fs38/join" target="_blank">fs38</a>, <a href="https://my.nci.org.au/mancini/project/oi10/join" target="_blank">oi10</a>
- CMIP5: <a href="https://my.nci.org.au/mancini/project/rr3/join" target="_blank">rr3</a>, <a href="https://my.nci.org.au/mancini/project/al33/join" target="_blank">al33</a>
- Observation data collection: <a href="https://my.nci.org.au/mancini/project/ct11/join" target="_blank">ct11</a>
- ERA5 and ERA5-Land: <a href="https://my.nci.org.au/mancini/project/rt52/join" target="_blank">rt52</a>, <a href="https://my.nci.org.au/mancini/project/zz93/join" target="_blank">zz93</a>
<!-- 

- obs4MIPs: `qv56`
-->
### Loading the ESMValTool-workflow modules
 <!-- #### Load the `access-med` conda environment -->

To load the the *esmvaltool* module, execute the following commands:
```
    module use /g/data/xp65/public/modules
    module load esmvaltool
```

This *esmvaltool* module is pre-configured to access CMIP and observation datasets available on Gadi.
By default, ESMValTool looks for the *config_user.yml* file in the home directory, inside the *.esmvaltool* folder.
To start, you can get a copy in your home directory, *.esmvaltool* folder by running the below or use the `--path=dest` flag to save elsewhere.

```
esmvaltool config get_config_user
```

To list which ESMValTool recipes are available on <i>Gadi</i>, run:
```
esmvaltool recipes list
```

To find out details of a specific *recipe_name.yml*, execute:
```
esmvaltool recipes show recipe_name.yml
```

To retrieve a recipe (and modify it), execute:
```
esmvaltool recipes get recipe_name.yml
```

To execute *recipe_name.yml* and automatically download the required climate data to the default directory, run:

```
esmvaltool run examples/recipe_python.yml --search_esgf=when_missing
```
The `--search_esgf=when_missing` option tells <i>ESMValTool</i> to search for and download the necessary climate data files from Earth System Grid Federation (ESGF), if they cannot be found locally.

## ESMValTool recipe examples

<!-- Explain what the Tiers mean: Tier3 not to be distributed / license issue, Tier2: some restrictions, but can be redistributed while citing papers etc., Tier1: open for everyone -->

A list of <i>ESMValTool</i> recipes available on <i>Gadi</i> can be found on the <a href="https://github.com/ACCESS-NRI/ESMValTool-workflow.git" target="_blank">ACCESS-NRI MED ESMValTool Workflow</a> GitHub repository. Some example recipes are provided below:


<!-- Compare to list from https://github.com/ACCESS-NRI/ESMValTool-workflow/issues/103 -->

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

To get help running your ESMValTool recipe on <i>Gadi</i>, you can submit an issue on the <a href="https://github.com/ACCESS-NRI/ESMValTool-workflow.git" target="_blank">ESMValTool-Workflow</a> GitHub repository or ask for help on the <a href="https://forum.access-hive.org.au" target="_blank">ACCESS-Hive Forum</a>.

General ESMValTool support (i.e. non-specific to <i>Gadi</i>) can be found on the <a href="https://github.com/ESMValGroup/ESMValTool/discussions" target="_blank">ESMValTool Discussions</a> page, where users can also post technical questions on the ESMValTool installation, application and development.

### Recipes and diagnostics

Contacts for specific diagnostic sets are the authors listed in the source code and corresponding <a href="https://docs.esmvaltool.org/en/latest/recipes/index.html#recipes" target="_blank">recipe and diagnostic documentation</a>.

The current status of <i>ESMValTool</i> recipes for the *xp65* conda environment on <i>Gadi</i> is available <a href="https://github.com/ACCESS-NRI/ESMValTool-workflow.git" target="_blank">here</a>

### License

The <i>ESMValTool</i> is released under the Apache License, version 2.0. Citation of the <i>ESMValTool</i> paper (“Software Documentation Paper”) is requested upon use, along with the software DOI for <i>ESMValTool</i> (doi:10.5281/zenodo.3401363) and <i>ESMValCore</i> (doi:10.5281/zenodo.3387139) together with the version:

> Righi, M., Andela, B., Eyring, V., Lauer, A., Predoi, V., Schlund, M., Vegas-Regidor, J., Bock, L., Brötz, B., de Mora, L., Diblen, F., Dreyer, L., Drost, N., Earnshaw, P., Hassler, B., Koldunov, N., Little, B., Loosveldt Tomas, S., and Zimmermann, K.: Earth System Model Evaluation Tool (ESMValTool) v2.0 – technical overview, Geosci. Model Dev., 13, 1179–1199, https://doi.org/10.5194/gmd-13-1179-2020, 2020.

Besides the above citation, users are asked to register any journal articles (or other scientific documents) that use the software at the ESMValTool webpage (https://www.esmvaltool.org/). Citing the Software Documentation Paper and registering your paper(s) will serve to document the scientific impact of the Software, which is important for securing future funding. You should consider this an obligation if you have taken advantage of the <i>ESMValTool</i>, which represents the end product of considerable effort by the development team.

</table>