# ACCESS-AM

![ACCESS AM model](/assets/model-config-logos/configurations-without-tiles/access-am.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Atmosphere Model (ACCESS-AM) is a global coupled atmospheric model that includes [atmosphere](/models/model_components/atmosphere), [aerosols and atmospheric chemistry](/models/model_components/aerosols_atmospheric_chemsitry), [land](/models/model_components/land) and [land biogeochemistry](/models/model_components/bgc_land).

{% set model = "ACCESS-AM3" %}
## {{ model }}

{{ model }} is a set of coupled atmosphere-land configurations developed by ACCESS-NRI, the [Commonwealth Science and Industrial Research Organisation](https://www.csiro.au/en/research/natural-environment?start=0&count=12) (CSIRO) and the [ARC Centre of Excellence for Weather in the 21st Century](https://21centuryweather.org.au/).

ACCESS-NRI has released [{{ model }} configurations](/models/run_a_model/run_access-am3).

**Fill in configurations for release.**

### Model Components {: #model-components-{{model}} }

- **Atmosphere**: [UM13.5](/models/model_components/atmosphere#unified-model-um).

- **Aerosols and Atmospheric Chemistry**: [GLOMAP](/models/model_components/aerosols_atmospheric_chemistry#glomap) and [UKCA](/models/model_components/aerosols_atmospheric_chemistry#UKCA).

- **Land**: [CABLE](/models/model_components/land#cable).

- **Land Biogeochemistry**: [CASA-CNP](/models/model_components/bgc_land#casa_cnp).

[Run ACCESS-AM](/models/run_a_model/run_access-am3){: class="text-card"}
