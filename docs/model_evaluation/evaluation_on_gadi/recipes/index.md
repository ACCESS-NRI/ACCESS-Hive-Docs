# Evaluation recipes

There is a range of resources supported by ACCESS-NRI and created by the community to evaluate model data and compare to observations. 
Researchers can build on existing code to suit their interests and load data formatted for comparison to model experiments.

**Pre-requisites**

For running these evaluation recipes on _Gadi_ it is expected you would be familar with [ARE](https://are.nci.org.au/) 
and the _conda/analysis3_ Python environment. 
For guidance on usage:

- refer to instructions on [Getting Started with ARE](/getting_started/are), in particular starting a _JuypyterLab_ session. 
- refer to [conda/analysis3](/getting_started/environments), and in particular using within ARE JupyterLab instance.

## ACCESS Evaluation Recipes

ACCESS-NRI have assisted in writing a collection of jupyter notebooks utilising the ESMValTool framework 
and initially focused on the [CLIVAR ENSO metrics package](https://doi.org/10.1175/BAMS-D-19-0337.A). 
You can find a notebook for each metric in the repository.

<div class="card-container">
    <a href="https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes" class="vertical-card aspect-ratio2to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/sst_bias.png" alt="SST bias" class="img-cover"></img>
        </div>
        <div class="card-text-container bold">ACCESS-ENSO-recipes</div>
    </a>
</div>

This collection has been expanded to include IOD(Indian Ocean Dipole) recipes, some tutorials and exercises and a number of ocean recipes
that have been ported into this [ESMValCore/ESMValTool framework](/model_evaluation/evaluation_on_gadi/esmvaltool_workflow) which leverages 
data finding and loading and the common preprocessors built into ESMValCore. These can be found in the subfolders of the repository.

### Relationship to ESMValTool and notebook-based recipes

These notebook-based workflows allow easier entry to get started analysing climate data on _Gadi_ and developing the diagnostic. 
They are adaptable by cloning the repository and editing to how it suits. These can be updated and added to from collaborative work with researchers.
As the framework is based on using the ESMValCore package, this makes the conversion to an ESMValTool _.yml_ simplier, 
which will allow for running the diagnostic on multiple models in bulk.


## Community Evaluation Recipes

### ACCESS-OM3 applications

There is a community based group (ACCESS-OM3 model evaluation team) that are helping with OM3 evaluation and development. Contributions from people of all career stages and backgrounds are highly encouraged.

All community members can get write access to the [OM3 evaluation repository](https://github.com/ACCESS-Community-Hub/access-om3-paper-1). To get write access, you need to create an issue and request access, please use [this issue template](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/new?template=add-user-request-to--access-om3-paper-1--repository-.md). Evaluation figures are being coordinated in [issue #23](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23) of the repository. Instructions to get started are in the README of the repository.

### ACCESS-CM3 applications

A collaborative project for evaluation of ACCESS-CM3 can be found in the [access-cm3-paper-1](https://github.com/acCESS-Community-Hub/access-cm3-paper-1/) repository. 

All community members can get write access to this repository. To get write access, you need to create an issue requesting access using [this template](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/new?template=add-user-request-to--access-cm3-1-repository-.md). Instructions to get started are in the README of the repository.

???+ tip "Join the conversation!"
    With either ACCESS-OM3 and ACCESS-CM3, you can also join the conversation on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/), 
    in either the [COSIMA](https://forum.access-hive.org.au/c/cosima/working-group/42) or 
    [ESM](https://forum.access-hive.org.au/c/esm/esm-working-group/43) working groups.

### COSIMA cookbook

The [COSIMA cookbook](https://cosima-recipes.readthedocs.io/en/latest/) has tutorials and recipes to help the community get started on writing their own recipes.

<div class="card-container">
    <a href="/model_evaluation/evaluation_on_gadi/cosima" class="vertical-card aspect-ratio2to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/logo_cosima.png" alt="Pangeo/COSIMA" class="img-cover"></img>
        </div>
        <div class="card-text-container bold">COSIMA cookbook</div>
    </a>
</div>