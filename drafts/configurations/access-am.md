#  ACCESS-AM  


<img src="../../../assets/model-config-logos/configurations-without-titles/access-am.png" alt="ACCESS AM model" class="white-background round-edges with-padding"></img>

The ACCESS Atmosphere Model (ACCESS-AM) is a global model with atmosphere and land surface components. It is often used in Atmospheric Model Intercomparison Project (AMIP) experiments where it is driven by historically observed sea surface temperature and sea ice data.

ACCESS-NRI will release supported ACCESS-AM configurations.  The first release, ACCESS-AM2, will be derived from the [CSIRO ACCESS-CM2 configuration](./access-cm.md#access-cm2) and will include [atmosphere] and [land] components.

## ACCESS-AM2

This is the model configuration used for the AMIP experiments contributed to the World Climate Research Programme’s Coupled Model Intercomparison Project Phase 6 (CMIP6). Note that the CMIP model naming is the same for both the AM and CM configurations, so the CMIP6 experiments are ACCESS-CM2 AMIP rather than ACCESS-AM2.

The component models are the same as ACCESS-CM2:

- Atmosphere model (UM vn10.6, GA7.1 science configuration): N96 resolution (1.875° x 1.25°, 85 levels). Physical model only – no carbon cycle.

- Land surface model (CABLE2.5)

[**Citation** [@Bi2020]][ACCESS-CM2-cite]

### Other configurations

Some experiments already run with other atmospheric model configurations  are listed at:

 - [CLEX CMS wiki][UMexperiments]

[atmosphere]: ../model_components/atmosphere.md
[land]: ../model_components/land.md
[UM-hive]: ../model_components/atmosphere.md#the-unified-model
[JULES-hive]: ../model_components/land.md#jules
[CABLE-hive]: ../model_components/land.md#cable
[UMstart]: https://climate-cms.wikis.unsw.edu.au/Unified_Model
[UMexperiments]: https://climate-cms.wikis.unsw.edu.au/UM_Experiments
[ACCESS-CM2-cite]: https://www.publish.csiro.au/es/ES19040
