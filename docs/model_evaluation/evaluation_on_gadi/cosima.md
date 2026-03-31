# COSIMA Cookbook on Gadi


<a href="https://cosima.org.au/" target="_blank">COSIMA</a> stands for the Consortium for Ocean-Sea Ice Modelling in Australia, which brings together Australian-based researchers involved in global ocean and sea ice modelling. The <i>COSIMA Cookbook</i> is a collection of "recipes", i.e., computational notebooks in the form of tutorials and documented examples that are curated for analysing output from ocean-sea ice models.

???+ warning "Support Level: Supported on <i>Gadi</i>, but not owned by ACCESS-NRI"
    <!-- Who develped the tool? -->
    The <i>COSIMA Cookbook</i> is developed and maintained by COSIMA. While ACCESS-NRI does not contribute to the scientific scope of the code, it actively supports the use of the recipes within the <i>COSIMA Cookbook</i> on <i>Gadi</i>. 
    ACCESS-NRI provides an environment that can run the latest version of <i>COSIMA Recipes</i> via the `xp65` `conda/analysis3` conda environment for Model Evaluation on Gadi, provided 3rd party packages maintain compatibility.

The <i>COSIMA Cookbook</i> framework focuses on the <a href="/models/access_models/access-om">ACCESS-OM2 and ACCESS-OM3</a> suite of models being developed and run by members of <a href="https://cosima.org.au/" target="_blank">COSIMA</a> and ACCESS-NRI. This framework demonstrates how to analyze output from MOM5/MOM6 and CICE5/CICE6.

## Getting Started

The easiest way to use the _COSIMA Cookbook_ is through the [Australian Research Environment (ARE)](https://are.nci.org.au)" on _Gadi_.<br>
To be able to access _Gadi_ you need to have an NCI account. For more information, check how to [Set Up your NCI Account](/getting_started/set_up_nci_account).

To use the <i>COSIMA Cookbook</i> in the `conda/analysis3` environment of *xp65*, you need to <a href="https://my.nci.org.au/mancini/project/xp65" target="_blank">join NCI project *xp65*</a>.

1. Login  via *ssh* to <i>Gadi</i> and clone the <a href="https://github.com/COSIMA/cosima-recipes" target="_blank"><i>cosima-recipes</i></a> repository to your local directory.  

2. Find the recipes that you want to run and make sure you have access to the specific projects and their storage (e.g., project *ik11* to get access to */g/data/ik11*).

3. Start an <a href="https://are.nci.org.au" target="_blank">ARE JupyterLab</a> session on NCI:  
  <b>Storage</b>: `gdata/xp65` (add the specific storage you need for the recipe you want to run)
  <br>
  <b>Module directories</b>: `/g/data/xp65/public/modules`  
  <b>Modules</b>: `conda/analysis3`
  <br>
  If you are new to ARE, refer to instructions on [Getting Started with ARE](/getting_started/are).
1. Within the ARE environment, navigate to one of the COSIMA recipes and run the analysis.

## COSIMA Cookbook information

For more information on the <i>COSIMA Cookbook</i>, refer to the <a href="https://cosima-recipes.readthedocs.io/en/latest/" target="_blank">documentation</a>, as well as the following lists of recipes:

- <a href="https://cosima-recipes.readthedocs.io/en/latest/cooking-lessons-101/index.html" target="_blank">Tutorials</a>
- <a href="https://cosima-recipes.readthedocs.io/en/latest/appetisers.html" target="_blank">Appetiser recipes</a>
- <a href="https://github.com/COSIMA/cosima-recipes/tree/cosima_cookbook/ACCESS-OM2-GMD-Paper-Figs" target="_blank">Notebooks</a> to reproduce figures of the <a href="https://gmd.copernicus.org/articles/13/401/2020/" target="_blank">ACCESS-OM2 announcement paper</a>


### Help evaluate and improve applications of OM3
There is a community based group (ACCESS-OM3 model evaluation team) that are helping with OM3 evaluation and development. Contributions from people of all career stages and backgrounds are highly encouraged.

All community members can get write access to the [OM3 evaluation repository](https://github.com/ACCESS-Community-Hub/access-om3-paper-1). To get write access, you need to create an issue and request access, please use [this issue template](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/new?template=add-user-request-to--access-om3-paper-1--repository-.md). Evaluation figures are being coordinated in [issue #23](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23) of the repository. Instructions to get started are in the README of the repository.