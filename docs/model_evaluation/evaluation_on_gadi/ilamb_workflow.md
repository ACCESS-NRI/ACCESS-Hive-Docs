# ILAMB-workflow on Gadi

## What is ILAMB?

The [International Land Model Benchmarking (_ILAMB_)](https://www.ilamb.org/) benchmarking system is a Python framework used to quantitatively compare a defined set of observable variables with a number of land models.


This documentation is tailored to using _ILAMB_ on _Gadi_ and, hence, it supplements _ILAMB_'s official documentation rather than replacing it. Users are encouraged to read the [ILAMB official documentation](https://www.ilamb.org/doc/) and relevant [tutorials](https://www.ilamb.org/doc/tutorial.html).

!!! note
    ACCESS-NRI is supporting an NCI configuration of _ILAMB_ under the name _ILAMB-workflow_ via the [_conda/analysis3_](/getting_started/environments) environment.

*ILAMB-workflow* is the ACCESS-NRI software and data infrastructure that enables the _ILAMB_ evaluation framework on NCI _Gadi_. It includes:

- *ILAMB* Python packages, 
- a series of *ILAMB* outputs for ACCESS model evaluation,
- the *ILAMB-Data* collection of observational datasets. 

ILAMB-workflow is configured to use the existing NCI-supported CMIP data collections.

## Using ILAMB on Gadi

### Pre-requisites

- Have an [NCI Account](/getting_started/set_up_nci_account)
- Join the [xp65](https://my.nci.org.au/mancini/project/xp65/join) project for the [_conda/analysis3_](/getting_started/environments) environment.

Depending on your needs, you may want to also join the following supported data collections:

- CMIP6: [fs38](https://my.nci.org.au/mancini/project/fs38/join), [oi10](https://my.nci.org.au/mancini/project/oi10/join)
- CMIP5: [rr3](https://my.nci.org.au/mancini/project/rr3/join), [al33](https://my.nci.org.au/mancini/project/al33/join)

### Enable ILAMB-workflow commands

_ILAMB_ is provided through the _conda/analysis3_ environment. To enable the _ILAMB-workflow_ commands, load the module by running:
```
    module use /g/data/xp65/public/modules
    module load conda/analysis3
```

### How to use ILAMB-workflow

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

Visit [ILAMB-workflow documentation](https://ilamb-workflow.readthedocs.io/en/latest/?badge=latest) for further information on how to use _ILAMB_ on _Gadi_.

To learn more about how to adjust the _ILAMB_ setup, refer to the official [ILAMB documentation](https://www.ilamb.org/doc/) and relevant [tutorials](https://www.ilamb.org/doc/tutorial.html).

#### Example: CMIP6 comparisons and ACCESS ESM1.5 benchmarking

ACCESS-NRI maintains a collection of benchmark comparisons for the ACCESS community, including comparisons with data from CMIP. See the [workflow documentation](https://ilamb-workflow.readthedocs.io/en/latest/source/ILAMB.html#ilamb-cmip-confrontations-maintained-by-access-nri) for details.


In the following example, [ACCESS-ESM1.5](/models/access_models/access-esm#access-esm1.5) is compared with two other ESM models:

- [BCC ESM1 (Beijing Climate Center Earth System Model version 1)](https://gmd.copernicus.org/articles/13/977/2020/)
- [CanESM5 (Canadian Earth System Model version 5)](https://gmd.copernicus.org/articles/12/4823/2019/gmd-12-4823-2019.html)

Numerous benchmark comparisons have been defined in the configuration file. The comparison of variables have been organised under different sections, such as the _Hydrology Cycle_. 

For other variables, such as the _Gross Primary Productivity_ (*gpp*), one or more datasets are available (e.g. the gross primary productivity measurements of [FLUXNET2015](https://fluxnet.org/data/fluxnet2015-dataset/)). 

<br>
By clicking on a row in the table, you can expand it to see the underlying datasets used. The table's colourmap extends from best values in purple to worse data in orange.

<p align="center"><img align="center" width="50%" src="../../../assets/model_evaluation/ilamb_output_3.png" alt="Starting side of ILAMB output"></p>  

<br>

Clicking on one of these datasets, for example `CERESed4.1`, will take you to an interactive and quantitative comparison page for Albedo measurements of the [Clouds and the Earth’s Radiant Energy System (CERES)](https://ceres.larc.nasa.gov) project:

<p align="center"><img align="center" width="100%" src="../../../assets/model_evaluation/ilamb_loop.gif" alt="Comparison of different ILAMB outputs"></p>
