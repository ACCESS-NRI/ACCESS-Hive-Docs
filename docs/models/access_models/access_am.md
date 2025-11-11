[run-access-am]: /models/run-a-model/run-access-am3

# ACCESS-AM

![ACCESS AM model](/assets/model-config-logos/configurations-without-tiles/access-am.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Atmosphere Model (ACCESS-AM) is a global coupled atmospheric model that includes [atmosphere](), [aerosols and atmospheric chemistry](), [land]() and [land biogeochemistry]().

{% set model = "ACCESS-AM3" %}
## {{ model }}

{{ model }} is a suite of coupled atmosphere-land configurations developed by ACCESS-NRI, [CSIRO]() and the [ARC Centre of Excellence for Weather in the 21st Century].

ACCESS-NRI has released [{{ model }} configurations][run-access-am].

**Fill in configurations for release.**

### Model Components {: #model-components-{{model}} }

- **Atmosphere**: [UM13.5](/models/model_components/atmosphere#unified-model-um).

- **Aerosols and Atmospheric Chemistry**: [GLOMAP](/models/model_components/aerosols_atmospheric_chemistry#glomap) and [UKCA](/models/model_components/aerosols_atmospheric_chemistry#UKCA).

- **Land**: [CABLE](/models/model_components/land#cable).

- **Land Biogeochemistry**: [CASA-CNP](/models/model_components/l`and_bgc#casa_cnp).

[Run ACCESS-AM](/models/run-a-model/run-access-am){: class="text-card"}
