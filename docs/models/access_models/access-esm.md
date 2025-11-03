# ACCESS-ESM

![ACCESS ESM model](/assets/model-config-logos/configurations-without-titles/access-esm.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Earth System Model (ACCESS-ESM) is a fully-coupled global climate model that includes [atmosphere](/models/model_components/atmosphere), [land](/models/model_components/land), [ocean](/models/model_components/ocean), [sea ice](/models/model_components/sea-ice), [ocean biogeochemistry](/models/model_components/bgc_ocean) and [land biogeochemistry](/models/model_components/bgc_land) components, linked together by a [coupler](/models/model_components/coupler).<br>
This means it can simulate both the physical climate and global biogeochemical cycles, in particular the carbon cycle.

## ACCESS-ESM1.5

[ACCESS-ESM1.5](https://www.publish.csiro.au/es/ES19035) [@Ziehn2020] is a fully-coupled climate model with land and ocean carbon cycle components. ACCESS-ESM1.5 was developed primarily to enable Australia to participate in the [Coupled Model Intercomparison Project Phase 6 (CMIP6)](https://wcrp-cmip.org/cmip6/) with an Earth System Model (ESM) version.

ACCESS-NRI has released [ACCESS-ESM1.5 configurations](https://github.com/ACCESS-NRI/access-esm1.5-configs) as an adaptation of those originally developed by [CSIRO](https://www.csiro.au/en/research/environmental-impacts/climate-change/climate-science-centre) and [CLEX CMS](https://github.com/coecms/access-esm).

There are currently two supported configurations:

- ***Pre-industrial concentration driven***:<br>
      A global coupled model configuration running in CO~2~ concentration driven mode under pre-industrial forcings, as described in [Ziehn et al. (2020)](https://doi.org/10.1071/ES19035).
      Pre-industrial forcing data including atmospheric CO~2~ concentrations are primarily sourced from UKMO versions of CMIP6 inputs, with additional atmospheric forcings sourced from CMIP5 and land cover data adapted from [Lawrence et al. (2012)](https://doi.org/10.1175/JCLI-D-11-00256.1).
- ***Historical concentration driven***:<br>
      A global coupled model configuration running in co2 concentration driven mode under time varying historical (1850-2014) forcings, as described in [Ziehn et al. (2020)](https://doi.org/10.1071/ES19035).
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

[Run ACCESS-ESM](/models/run_a_model/run_access-esm){: class="text-card"}