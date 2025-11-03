#  Land Surface component

![Land Surface component image](/assets/component-logos/component-maps/land-component-map.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

## CABLE

[Community Atmosphere Biosphere Land Exchange (CABLE)](https://cable.readthedocs.io/en/latest/) is a land surface model used to calculate the fluxes of momentum, energy, water and carbon between the land surface, vegetation canopy and the atmospheric boundary layer. It also includes descriptions of thermal and hydrological processes in the soil and snow, and models the main biogeochemical cycles of the land ecosystem when used in conjunction with the [CASA-CNP](/models/model_components/bgc_land#casa-cnp) module.  

CABLE is an open source model developed by a community of Australian climate science researchers.<br>
Refer to [CABLE documentation](https://cable.readthedocs.io/en/latest/user_guide) to know how to work with the CABLE model.

### Models that use CABLE

- [ACCESS-CM2](/models/access_models/access-cm#access-cm2) (directly coupled into the [UM](/models/model_components/atmosphere#unified-model-um))
- [ACCESS-ESM1.5](/models/access_models/access-esm#access-esm15) (directly coupled into the [UM](/models/model_components/atmosphere#unified-model-um))

CABLE can also be run as a standalone model.

### Benchcab: evaluation tool for CABLE

[_Benchcab_](https://benchcab.readthedocs.io/en/stable) is a testing framework tool for CABLE. It allows to test CABLE's scientific performance across a range of model configurations and model versions.<br>
The tool currently works with the following configurations for CABLE:

- **Flux site simulations (offline)**<br>
  running CABLE forced with observed eddy covariance data at a single site
- **Global/regional simulations (offline)**<br>
  running CABLE forced with meteorological fields, globally or over a region

The output of these simulations can then be uploaded to [modelevaluation.org](https://modelevaluation.org/) for a statistical analysis of the scientific performance of the supplied configurations.

To learn more about _benchcab_, its functionalities and limitations, refer to [_benchcab_'s documentation](https://benchcab.readthedocs.io/en/stable/).

## JULES

The [Joint UK Land Environment System (JULES)](https://jules.jchmr.org/) is a community land surface model that can be used both as a standalone model and as the land surface component in the UM model. By modelling different land surface processes (surface energy balance, hydrological cycle, carbon cycle, dynamic vegetation, etc.) and their interaction with each other, JULES provides a framework to assess the impact of modifying a particular process on the ecosystem as a whole, for example the impact of climate change on hydrology.

### Models that use JULES
- [ACCESS-rAM3](/models/access_models/access-ram#access-ram3)

Other ACCESS models used for weather simulations, not supported by ACCESS-NRI, use JULES. Examples are ACCESS-S and ACCESS-C developed by the [Bureau of Meteorology (BoM)](http://www.bom.gov.au/).
