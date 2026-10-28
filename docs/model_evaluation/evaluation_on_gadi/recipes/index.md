# Evaluation recipes

There is a range of resources supported by ACCESS-NRI and created by the community to evaluate model data and compare it to observations. 
Researchers can build on existing code to suit their interests and load data formatted for comparison to model experiments.

**Prerequisites**

For running these evaluation recipes on _Gadi_ it is expected you would be familar with [ARE](https://are.nci.org.au/) 
and the _conda/analysis3_ Python environment. 
For guidance on usage:

- refer to instructions on [Getting Started with ARE](/getting_started/are), in particular starting a _JuypyterLab_ session. 
- refer to [conda/analysis3](/getting_started/environments), and in particular using within ARE JupyterLab instance.

## ACCESS Evaluation Recipes

ACCESS-NRI have assisted in writing a collection of jupyter notebooks utilising the ESMValTool framework 
and initially focused on the [CLIVAR ENSO metrics package](https://doi.org/10.1175/BAMS-D-19-0337.A). 

You can find a notebook for each metric in the [repository](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes).
Get started by cloning the repository on _Gadi_ and using the _conda/analysis3_ Python environment.

This collection has expanded to include Indian Ocean Dipole (IOD) recipes, tutorials, and exercises, as well as ocean recipes ported into the [ESMValCore/ESMValTool framework on _Gadi_](/model_evaluation/evaluation_on_gadi/esmvaltool_workflow). These leverage ESMValCore's built-in data discovery, loading, and preprocessing capabilities, and can be found in the repository subfolders.

### Relationship to ESMValTool and notebook-based recipes

These notebook-based workflows provide an accessible starting point for analysing climate data on _Gadi_ and developing the diagnostic. 
They can be adapted by cloning the repository and editing as needed, and are open to collaborations with researchers.
Because the framework is built on ESMValCore, converting a notebook to an ESMValTool YAML configuration is straightforward, enabling diagnostics to be run across multiple models in bulk.


## Community Evaluation Recipes

### ACCESS-CM3, ACCESS-AM3 and ACCESS-OM3

The community and ACCESS-NRI are evaluating the next generation of ACCESS models together, in shared repositories that anyone can contribute to.
See [Community Evaluation of ACCESS-CM3, AM3 and OM3](/model_evaluation/evaluation_on_gadi/community_evaluation) to get involved.

### COSIMA cookbook

The [COSIMA cookbook](https://cosima-recipes.readthedocs.io/en/latest/) has tutorials and recipes to help the community get started on writing their own recipes.
See [this COSIMA cookbook page](/model_evaluation/evaluation_on_gadi/cosima) to get started.
