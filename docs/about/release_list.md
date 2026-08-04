
[Hive Forum]: https://forum.access-hive.org.au
# ACCESS-NRI Release List

<div class="card-container">
    <a href="/about/releases" class="horizontal-card">
        <div class="card-image-container">
            <img class="img-contain white-background" src="/assets/rocket_release.svg" alt="ACCESS-NRI release stages">
        </div>
        <div class="card-text-container">
            <span class="bold" >ACCESS-NRI Release Stages</span>
            <span>
                Information about ACCESS-NRI release stages and their meaning.
            </span>
        </div>
    </a>
</div>


## Release type
The types used to categorise the release products are broad and not all releases fall neatly into these types. Some ACCESS-NRI releases involving training, informational videos on [_YouTube_](https://www.youtube.com/@AustraliasClimateSimulator) and visualisations on [_Vimeo_](https://vimeo.com/accessnri) are not included in the tables below.

:octicons-ai-model-16: [**Model**](#models): Refers to climate model components and [configurations](/about/releases/#fn:1). <br>
:material-tools: [**Tool**](#tools): Refers to supporting tools used for pre- and post- processing, evaluation and diagnostics. <br>
:material-database: [**Data**](#data): Collections listed are curated collections which can include data required for model runs, observations for evaluation and some model outputs.

Links in the tables below point to release notes that are usually posted on the [Hive Forum]. 
In these release notes, make sure you scroll down to the latest post for most recent updates.


### Models
| |  |
| :--- | :---------- |
|[ACCESS-ESM1.5](https://forum.access-hive.org.au/t/access-esm1-5-release-information/2352) | A coupled global Earth system model |
|[ACCESS-OM2](https://forum.access-hive.org.au/t/access-om2-release-information/1602) | Global coupled Ocean-Sea Ice Model developed by COSIMA |
|[ACCESS-rAM3](https://forum.access-hive.org.au/t/access-ram3-release-information/4308) | An implementation of the UKMO regional nesting suite that supports creating regional atmosphere/land configurations in an Australian context |
|[CABLE](https://forum.access-hive.org.au/t/cable-is-now-under-git-and-github/1643) | Land surface model in ACCESS models. Code available on GitHub |

### Tools
| |  |
| :--- | :---------- |
|[ESMValTool Workflow](https://forum.access-hive.org.au/t/esmvaltool-workflow-releases/1599) | NCI configuration of ESMValTool developed for evaluations of Earth System Models in CMIP |
|[iLAMB workflow](https://forum.access-hive.org.au/t/ilamb-workflow-v1-0-launches-today-here-is-what-you-need-to-know/1600) | NCI configurations of ILAMB|
|[Benchcab](https://forum.access-hive.org.au/t/benchcab-python-based-software-for-the-evaluation-of-cable/873/11) | Python-based software for the scientific evaluation of CABLE on NCI |
|[Model Live Diagnostics](https://forum.access-hive.org.au/t/official-model-live-diagnotics-v1-0-released-today-read-on-to-find-out-more/1647) | Framework to check, monitor, visualise and evaluate model behaviour and progress for models currently running on _Gadi_ |
|[ACCESS Intake Catalog](https://forum.access-hive.org.au/t/access-nri-intake-catalog-a-way-to-find-load-and-share-data-on-gadi/1659) | Find, load and share ACCESS & ACCESS-related model data on _Gadi_ |
|[Payu](https://forum.access-hive.org.au/t/payu-a-workflow-manager-for-some-access-models/1098) | Tool used to run a number of ACCESS models on NCI hardware |
|[um2nc](https://forum.access-hive.org.au/t/um2nc-a-utility-for-converting-unified-model-files-to-netcdf/3968) | Utility for converting UM data files to netCDF |
|[ACCESS-Vis and Visualisation recipes](https://forum.access-hive.org.au/t/access-visualisation-recipes-1-0-0-is-now-available/3970) | Collection of notebooks to enhance the visualisation of ACCESS climate model data using the `accessvis` python package |
|[Model tools](https://forum.access-hive.org.au/t/model-tools/4696) | Multiple tools deployed on _Gadi_ to support model tasks, such as FRE-NCtools, mppnccombine-fast, esmf, etc. |
|[ACCESS Model Scaling](https://forum.access-hive.org.au/t/access-nri-model-scaling-repository-a-collection-of-parallel-scalability-studies/5426) | A collection of Jupyter Notebooks that generate and display scaling data for ACCESS-NRI models |
|[ACCESS-MOPPy](https://forum.access-hive.org.au/t/access-moppy-1-0-beta-release-announcement/5979) | CMORisation tool to post-process ACCESS model output into CMIP-compliant datasets |

### Data
|  |  |
| :--- | :---------- |
|[Replicated datasets for evaluation](https://forum.access-hive.org.au/t/official-release-of-the-access-nri-replicated-datasets-for-climate-model-evaluation-nci-data-collection/1661) | Observational datasets in a format that the evaluation frameworks supported by ACCESS-NRI can use |
|[AUS2200](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f6014_0604_9188_1923) | A high-resolution regional atmospheric model configuration that covers the entire Australian continent and surrounding oceans at 2.2km grid spacing, using the UM atmospheric model|
|[Ancillary Data](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f9243_2030_4580_5589) | This collection provides access to replica, ancillary and other useful data for ACCESS-NRI and the broader community |
