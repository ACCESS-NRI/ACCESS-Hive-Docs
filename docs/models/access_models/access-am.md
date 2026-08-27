[run-access-am]: /models/run-a-model/run-access-am3

# ACCESS-AM

![ACCESS AM model](/assets/model-config-logos/configurations-without-tiles/access-am.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Atmosphere Model (ACCESS-AM) is a global land-atmosphere model that includes [atmosphere](/models/model_components/atmosphere#unified-model-um), [aerosols and atmospheric chemistry](/models/model_components/aerosols_atmospheric_chemistry) and [land](/models/model_components/land#cable).

{% set model = "ACCESS-AM3" %}
## {{ model }}

{{ model }} is a suite of coupled atmosphere-land configurations developed by ACCESS-NRI, CSIRO and the ARC Centre of Excellence for Weather in the 21st Century.

ACCESS-NRI has released [{{ model }} configurations][run-access-am].

- n96e-3.0: a low-resolution configuration using the GAL9 configuration.
- n512e-aeroclim-1.0: a higher resolution configuration using the GAL9 configuration with changes to use climatological aerosols.

### Model Components {: #model-components-{{model}} }

- **Atmosphere**: [UM13.8](/models/model_components/atmosphere#unified-model-um).

- **Aerosols and Atmospheric Chemistry**: [GLOMAP](/models/model_components/aerosols_atmospheric_chemistry#glomap) and [UKCA](/models/model_components/aerosols_atmospheric_chemistry#UKCA).

- **Land**: {{mode}} is using [CABLE](/models/model_components/land#cable) for most of the land interactions, complemented by [JULES](/models/model_components/land#jules) for processes not available in CABLE.

[Run ACCESS-AM](/models/run-a-model/run-access-am){: class="text-card"}