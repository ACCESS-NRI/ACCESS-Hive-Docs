# ACCESS-CM

![ACCESS CM model](/assets/model-config-logos/configurations-without-titles/access-cm.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Coupled Model (ACCESS-CM) is a fully-coupled global climate model that includes [atmosphere](/models/model_components/atmosphere), [aerosols and atmospheric chemistry](/models/model_components/aerosols_atmospheric_chemistry), [land](/models/model_components/land), [ocean](/models/model_components/ocean) and [sea ice](/models/model_components/sea-ice) components, linked together by a [coupler](/models/model_components/coupler).<br>
It produces physical climate simulations.

{% set model = "ACCESS-CM2" %}

## {{ ACCESS-CM2 }}

!!! danger
    ACCESS-NRI does not maintain an official {{model}} release, but we continue to support the community in using this model where possible.

[ACCESS-CM2](https://www.publish.csiro.au/es/ES19040) [@Bi2020] was initially developed by [CSIRO](https://www.csiro.au/) and is one of Australia’s contributions to the World Climate Research Programme’s [Coupled Model Intercomparison Project Phase 6 (CMIP6)](https://wcrp-cmip.org/cmip6/).

### Model components
- **Atmosphere**: [UM10.6](/models/model_components/atmosphere#unified-model-um), GA7.1 science configuration.<br>
  N96 spatial resolution (1.875° x 1.25°), 85 vertical levels. Physical model only – no carbon cycle.
  
- **Aerosols and Atmospheric Chemistry**: [GLOMAP](/models/model_components/aerosols_atmospheric_chemistry#glomap) for the aerosols and [UKCA](/models/model_components/aerosols_atmospheric_chemistry#ukca) for the atmospheric chemistry.

- **Land**: [CABLE2.5](/models/model_components/land#cable).

- **Ocean**: [MOM5](/models/model_components/ocean#mom5).<br>
  Tripolar grid, 1° spatial resolution, 50 vertical levels.

- **Sea ice**: [CICE5.1.2](/models/model_components/sea-ice#cice5).<br>
  Same grid as Ocean.

- **Coupler**: [OASIS3-MCT](/models/model_components/coupler#oasis3-mct).

Compared to previous model versions, ACCESS-CM2 shows better global hydrological balance, more realistic ocean water properties (in terms of spatial distribution) and meridional overturning circulation in the Southern Ocean. It does, however, produce a poorer simulation of the Antarctic sea ice and a larger energy imbalance at the top of atmosphere. ACCESS-CM2 has a relatively high equilibrium climate sensivity of 4.7°C for doubled CO~2~ concentration.

[Run ACCESS-CM](/models/run_a_model/run_access-cm2){: class="text-card"}