{% set om3_configs_docs = "https://access-om3-configs.access-hive.org.au" %}
[cosima]: https://cosima.org.au/

# ACCESS-OM

![ACCESS OM model](/assets/model-config-logos/configurations-without-titles/access-om.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Ocean Model (ACCESS-OM) is a global coupled ocean model that includes [ocean](/models/model_components/ocean), [ocean biogeochemistry](/models/model_components/bgc_ocean), and [sea ice](/models/model_components/sea-ice) components, linked together by a [coupler](/models/model_components/coupler).<br>
The atmospheric fields that drive the model are provided by a data source, usually derived from reanalysis.

{% set model = "ACCESS-OM3" %}
## {{ model }}

[![Config docs](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{om3_configs_docs}}){: class="text-card"}

{{ model }} is a suite of coupled ocean-sea ice models developed by ACCESS-NRI and the [Consortium for Ocean-Sea Ice Modelling in Australia (COSIMA)][cosima].

ACCESS-NRI has released [{{ model }} configurations](https://github.com/ACCESS-NRI/access-om3-configs).

There is a global configuration for **one spatial resolution**:

- 0.25° or 25km horizontal resolution, 75 vertical levels.

For the above resolution there is **one option of JRA55-do atmospheric forcing**:

- Repeat Year Forcing (RYF): repeated 1 May 1990 - 30 April 1991 forcing

Each configuration also has an optional biogeochemical (BGC) configuration that uses the [Biogeochemistry Ocean component](/models/model_components/bgc_ocean), if required.
!!! warning
    BGC experiments are slower and generally consume more resources (compute time and disk space).

### Model Components {: #model-components-{{model}} }

- **Ocean**: [MOM6](/models/model_components/ocean#mom6).<br>
  Tripolar grid.

- **Sea ice**: [CICE6](/models/model_components/sea-ice#cice6).<br>
    Same grid as ocean.

- **Ocean Biogeochemistry**: [WOMBAT](/models/model_components/bgc_ocean#wombat)  (optional).

- **Coupler**: [NUOPC](/models/model_components/coupler#nuopc).

[Run {{ model }}](/models/run_a_model/run_access-om3){: class="text-card"}

{% set model = "ACCESS-OM2" %}
## {{ model }}

[{{ model }}](https://gmd.copernicus.org/articles/13/401/2020/) [@Kiss2020] [@ACCESS-OM2-report] [@Solodoch2022] [@Hayashida2023] [@Menviel2023] is a suite of coupled ocean-sea ice models originally developed by the [Consortium for Ocean-Sea Ice Modelling in Australia (COSIMA)][cosima].<br>

ACCESS-NRI has released [{{ model }} configurations](https://github.com/ACCESS-NRI/access-om2-configs) as an adaptation of those originally developed by COSIMA.

There are global configurations for **three spatial resolutions**:

- 1° horizontal resolution, 50 vertical levels.
- 0.25° horizontal resolution, 50 vertical levels.
- 0.1° horizontal resolution, 75 vertical levels.

For each resolution there are **two options of JRA55-do atmospheric forcing**:

- Repeat Year Forcing (RYF): repeated 1 May 1990 - 30 April 1991 forcing
- Inter-Annual Forcing (IAF): 1958-2018 forcing

Each configuration also has an optional biogeochemical (BGC) configuration that uses the [Biogeochemistry Ocean component](/models/model_components/bgc_ocean), if required.
!!! warning
    BGC experiments are slower and generally consume more resources (compute time and disk space).

### Model Components {: #model-components-{{model}} }
<div class="tabLabels" label="ACCESS-OM2-versions">
    <button id="{{ model }}-1deg">{{ model }}-1</button>
    <button id="{{ model }}-025deg">{{ model }}-025</button>
    <button id='{{ model }}-01deg'>{{ model }}-01</button>
</div>

- **Ocean**: [MOM5](/models/model_components/ocean#mom5).<br>
  Tripolar grid, <span tabcontentfor="{{ model }}-1deg">1</span><span tabcontentfor="{{ model }}-025deg">0.25</span><span tabcontentfor="{{ model }}-01deg">0.1</span>° spatial resolution, <span tabcontentfor="{{ model }}-1deg">50</span><span tabcontentfor="{{ model }}-025deg">50</span><span tabcontentfor="{{ model }}-01deg">75</span> vertical levels.

- **Ocean Biogeochemistry**: [WOMBAT](/models/model_components/bgc_ocean#wombat) (optional).

- **Sea ice**: [CICE5.1.2](/models/model_components/sea-ice#cice5).<br>
    Same grid as ocean.

- **Coupler**: [OASIS3-MCTv2](/models/model_components/coupler#oasis3-mct).

More details on the models can be found in [this ACCESS-Hive Forum post](https://forum.access-hive.org.au/t/access-om2-control-experiments/258), together with details on the extensive control experiment data already available without needing to run a new experiment.

Full conditions of use for {{ model }} models and outputs can be viewed in the  [{{ model }}-configs README](https://github.com/ACCESS-NRI/access-om2-configs?tab=readme-ov-file#conditions-of-use).

[Run {{ model }}](/models/run_a_model/run_access-om2){: class="text-card"}
