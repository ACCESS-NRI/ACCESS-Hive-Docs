# ILAMB-workflow on Gadi

## What is ILAMB?

The [International Land Model Benchmarking (_ILAMB_)](https://www.ilamb.org/) benchmarking system is a python framework used to quantitatively compare a defined set of observable variables with a number of land models.


This documentation is tailored to using _ILAMB_ on _Gadi_ and, hence, it supplements rather than replaces the official documentation. Users are encouraged to read the  [ILAMB documentation](https://www.ilamb.org/doc/) and relevant [tutorials](https://www.ilamb.org/doc/tutorial.html).

!!! note
    ACCESS-NRI is supporting an NCI configuration of ILAMB under the name _ILAMB-workflow_ via the [_conda/analysis3_](/getting_started/environments) environment.

*ILAMB-workflow* is the ACCESS-NRI software and data infrastructure that enables the ILAMB evaluation framework on NCI Gadi. It includes the 

- *ILAMB* Python packages, 
- a series of *ILAMB* outputs for ACCESS model evaluation,
- the *ILAMB-Data* collection of observational datasets. 

ILAMB-workflow is configured to use the existing NCI supported CMIP data collections.

## Using ILAMB on Gadi

### Pre-requisites

To use *ILAMB* on *Gadi* ensure you fulfill the [Set Up your NCI Account](/getting_started/set_up_nci_account) section.
_ILAMB_ is provided through the [xp65](https://my.nci.org.au/mancini/project/xp65/join) NCI projects on _Gadi_, so you need to have an NCI account and be a member of this projects to use it. 


Depending on your needs, you may want to also join the following supported data collections:

- CMIP6: [fs38](https://my.nci.org.au/mancini/project/fs38/join), [oi10](https://my.nci.org.au/mancini/project/oi10/join)
- CMIP5: [rr3](https://my.nci.org.au/mancini/project/rr3/join), [al33](https://my.nci.org.au/mancini/project/al33/join)

### Loading the ILAMB-workflow modules

To load the the *ilamb* module, execute the following commands:
```
    module use /g/data/xp65/public/modules
    module load conda/analysis3
```

Visit [ACCESS-NRI documentation](https://ilamb-workflow.readthedocs.io/en/latest/?badge=latest) on how to run _ILAMB_ on _Gadi_.


To run _ILAMB_, you need to execute the command `ilamb-run` with a number of arguments/ files:
```
ilamb-run --config config.cfg --model_setup model_setup.txt --regions regions.txt
```

    * _config.cfg_ defines which observables and observational datasets to be compared.
    * _model_setup.txt_ defines the paths of models that to be compared.
    * _regions.txt_ defines the regions to be compared, e.g., _global_, _aust_ (Australia), etc.

While these files can be self-defined, ACCESS-NRI provides the necessary files and tools to set your model paths to run on _Gadi_. All you need to do is decide which observations and models you wish to compare. 

NCI hosts replicas of the _ILAMB_ observational data sets through the NCI project [ct11](https://my.nci.org.au/mancini/project/ct11/join) as well as a large amount of model outputs are available on _Gadi_, such as ACCESS model output.

For more information, refer to [Finding ACCESS Data](/model_evaluation/data/finding) on how to find data on NCI.

To learn more about how to adjust the _ILAMB_ setup, refer to the official [ILAMB documentation](https://www.ilamb.org/doc/) and relevant [tutorials](https://www.ilamb.org/doc/tutorial.html).

## Example: CMIP6 comparisons and ACCESS ESM1.5 benchmarking

ACCESS-NRI is maintaining a collection of benchmark comparisons for the ACCESS community, such as that with CMIP data, see in the [workflow documentation.](https://ilamb-workflow.readthedocs.io/en/latest/source/ILAMB.html#ilamb-cmip-confrontations-maintained-by-access-nri)


In the following example, the supported [ACCESS-ESM1.5](/models/access_models/access-esm#access-esm1.5) is compared with two other ESM models:

- [BCC ESM1 (Beijing Climate Center Earth System Model version 1)](https://gmd.copernicus.org/articles/13/977/2020/)
- [CanESM5 (Canadian Earth System Model version 5)](https://gmd.copernicus.org/articles/12/4823/2019/gmd-12-4823-2019.html)

Numerous benchmark comparisons have been defined in the configuration file. The comparison of variables have been organised under different sections, such as the _Hydrology Cycle_. 

For other variables, such as the _Gross Primary Productivity_ (*gpp*), one or more datasets are available. For example, the gross primary productivity measurements of [FLUXNET2015](https://fluxnet.org/data/fluxnet2015-dataset/). 

<br>
By clicking on a row in the table, you can expand it to see the underlying datasets used. The table's colourmap extends from best values in purple to worse data in orange.

<p align="center"><img align="center" width="50%" src="../../../assets/model_evaluation/ilamb_output_3.png" alt="Starting side of ILAMB output"></p>  

<br>

Clicking on one of these datasets, for example `CERESed4.1`, will take you to an interactive and quantitative comparison page for Albedo measurements of the [Clouds and the Earth’s Radiant Energy System (CERES)](https://ceres.larc.nasa.gov) project:

<p align="center"><img align="center" width="100%" src="../../../assets/model_evaluation/ilamb_loop.gif" alt="Comparison of different ILAMB outputs"></p>
