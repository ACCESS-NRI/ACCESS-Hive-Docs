# ACCESS-ESM

![ACCESS ESM model](/assets/model-config-logos/configurations-without-titles/access-esm.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The **ACCESS E**arth **S**ystem **M**odel (ACCESS-ESM) is a fully-coupled global climate model that includes [atmosphere](/models/model_components/atmosphere), [land](/models/model_components/land), [ocean](/models/model_components/ocean), [sea ice](/models/model_components/sea-ice), [ocean biogeochemistry](/models/model_components/bgc_ocean) and [land biogeochemistry](/models/model_components/bgc_land) components, linked together by a [coupler](/models/model_components/coupler).<br>
This means it can simulate both the physical climate and global biogeochemical cycles, in particular the carbon cycle.

## ACESS-ESM1.6

ACCESS-ESM1.6 is a fully-coupled climate model with land and ocean carbon cycle components. ACCESS-ESM1.6 was developed primarily to enable Australia to participate in the [CMIP7 Assessment FastTrack](https://wcrp-cmip.org/cmip-phases/cmip7/#cmip7_assessment_fast_track_cmip7_aft) with an ESM version.

ACCESS-ESM1.6 was developed by ACCESS-NRI and CSIRO.

There are currently four supported configurations:

- ***Concentration-driven pre-industrial control, piControl***:<br>
      The _piControl_ configuration simulates the climate prior to the industrial revolution using prescribed CO~2~ concentrations and atmospheric forcings estimated for the year 1850.
- ***Emission-driven pre-industrial control, esm-piControl***:<br>
      The _esm-piControl_ configuration of ESM1.6 simulates the climate prior to the industrial revolution using a fully interactive carbon cycle where 3D CO~2~ tracers evolve freely in the atmosphere and are exchanged with the land and ocean biogeochemistry submodels.
- ***Concentration-driven historical***:<br>
      The historical configuration simulates the climate from 1850-2022 using prescribed atmospheric CO~2~ concentrations and forcings.
- ***Emission-driven historical***:<br>
      The esm-historical configuration simulates the climate from 1850-2022 using a fully interactive carbon cycle and historical CO~2~ anthropogenic emissions data.

Details on the forcings and parameters used in the supported configurations can be found in the [configuration documentation](https://access-esm1p6-configs.access-hive.org.au/configs_experiments/configurations/).

### Model components
- **Atmosphere**: [UM7.3](/models/model_components/atmosphere#unified-model-um), GA7.1 science configuration.<br>
  N96 spatial resolution (1.875° x 1.25°), 38 vertical levels.

- **Land**: [CABLE3](/models/model_components/land#cable).

- **Land Biogeochemistry**: [CASA-CNP](/models/model_components/bgc_land#casa-cnp).

- **Ocean**: [MOM5](/models/model_components/ocean#mom5).<br>
  Tripolar grid, 1° spatial resolution, 50 vertical levels.

- **Ocean Biogeochemistry**: [WOMBATlite](https://wombat-docs.readthedocs.io/latest/Model_description/WOMBATlite_model_description/).

- **Sea ice**: [CICE5](/models/model_components/sea-ice#cice5).<br>
  Same grid as Ocean.

- **Coupler**: [OASIS3-MCT](/models/model_components/coupler#oasis3-mct).

[Run ACCESS-ESM1.6](/models/run_a_model/run_access-esm1p6){: class="text-card"}

## ACCESS-ESM1.5

[ACCESS-ESM1.5](https://www.publish.csiro.au/es/ES19035) [@Ziehn2020] is a fully-coupled climate model with land and ocean carbon cycle components. ACCESS-ESM1.5 was developed primarily to enable Australia to participate in the [CMIP6](https://wcrp-cmip.org/cmip6/) with an ESM version.

ACCESS-NRI has released [ACCESS-ESM1.5 configurations](https://github.com/ACCESS-NRI/access-esm1.5-configs) as an adaptation of those originally developed by [CSIRO](https://www.csiro.au/en/research/environmental-impacts/climate-change/climate-science-centre) and [CLEX CMS](https://github.com/coecms/access-esm).

There are currently two supported configurations:

- ***Pre-industrial concentration driven***:<br>
      A global coupled model configuration running in CO~2~ concentration driven mode under pre-industrial forcings, as described in [Ziehn et al. (2020)](https://doi.org/10.1071/ES19035).
      Pre-industrial forcing data including atmospheric CO~2~ concentrations are primarily sourced from UKMO versions of CMIP6 inputs, with additional atmospheric forcings sourced from CMIP5 and land cover data adapted from [Lawrence et al. (2012)](https://doi.org/10.1175/JCLI-D-11-00256.1).
- ***Historical concentration driven***:<br>
      A global coupled model configuration running in CO~2~ concentration driven mode under time varying historical (1850-2014) forcings, as described in [Ziehn et al. (2020)](https://doi.org/10.1071/ES19035).
      Historical forcing data including atmospheric CO~2~ concentrations are primarily sourced from UKMO versions of CMIP6 inputs, with land use change data adapted from the Land-Use Harmonisation 2 (LUH2) dataset developed for CMIP6 [(Hurtt et al. 2017)](https://doi.org/10.22033/ESGF/input4MIPs.1127).

### Model components
- **Atmosphere**: [UM7.3](/models/model_components/atmosphere#unified-model-um), GA7.1 science configuration.<br>
  N96 spatial resolution (1.875° x 1.25°), 38 vertical levels.

- **Land**: [CABLE2.4](/models/model_components/land#cable).

- **Land Biogeochemistry**: [CASA-CNP](/models/model_components/bgc_land#casa-cnp).

- **Ocean**: [MOM5](/models/model_components/ocean#mom5).<br>
  Tripolar grid, 1° spatial resolution, 50 vertical levels.

- **Ocean Biogeochemistry**: [WOMBAT](/models/model_components/bgc_ocean#wombat).

- **Sea ice**: [CICE4.1](/models/model_components/sea-ice#cice4).<br>
  Same grid as Ocean.

- **Coupler**: [OASIS3-MCT](/models/model_components/coupler#oasis3-mct).

ACCESS-ESM1.5 has an equilibrium climate sensitivity of 3.87°C for doubled CO~2~ concentration.

[Run ACCESS-ESM1.5](/models/run_a_model/run_access-esm1p5){: class="text-card"}
