{% set ram3_configs_docs = "https://access-ram3-configs.access-hive.org.au" %}
[run_access-ram]: /models/run_a_model/run_access-ram

# ACCESS-rAM 

![ACCESS RAM model](/assets/model-config-logos/configurations-without-titles/access-ram.png){: class="img-contain white-background round-edges with-padding intro-img" loading="lazy"}

The ACCESS Regional Atmosphere Model (ACCESS-rAM) is an implementation of the [UK Met Office (UKMO)](https://www.metoffice.gov.uk/) Regional Nesting Suite, comprising [atmosphere](/models/model_components/atmosphere) and [land](/models/model_components/land) components.<br>
Unlike the UKMO Regional Nesting Suite that relies on operational land-surface initial conditions, ACCESS-rAM derives its initial conditions from alternative sources, enhancing its capability for high-resolution regional atmosphere modelling on [Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview).

ACCESS-rAM requires both initial conditions and lateral boundary (_driving_) conditions. It also supports multiple [_nesting_](#nesting) configurations, automatically providing their necessary initial and lateral boundary conditions.

### Nesting
_Nesting_ is the process of embedding a smaller, finer resolution region (often referred to as _nest_ or _nested region_) within a larger, coarser-resolution domain to improve accuracy for localised weather events. This approach enables atmospheric variables such as temperature, pressure, and wind speed from the larger domain to be used as lateral boundary conditions for the nested region, allowing more accurate simulations within the nest.<br>

In ACCESS-rAM, the coarser-resolution domains are referred to as _nested regions_.
Each region can contain multiple concentric _nests_, with each nest increasing the resolution of the simulation, allowing for progressively finer detail in areas of interest.

Since the regional forecasting is performed separately for each nested region and for every individual nest within, the total computational cost increases with both the number of nested regions and the number of nests contained within each of them.

## ACCESS-rAM3

[![Config docs](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{ram3_configs_docs}}){: class="text-card"}

Similar to the UKMO Regional Nesting Suite, ACCESS-rAM3 is configured to derive its initial and lateral boundary conditions from the [ECMWF Reanalysis v5 (ERA5)](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5) dataset.<br>
However, for its land-surface initial conditions, ACCESS-rAM3 offers flexibility by allowing the use of alternative datasets.

Information about the amount of NCI resources (such as Service Units (SU) and storage) used by a typical ACCESS-rAM3 experiment run are available on the [ACCESS-Hive Forum release notes page](https://forum./t/access-ram3-release-information/4308).

### Land-surface initial conditions source
- [ERA5-Land](https://www.ecmwf.int/en/era5-land) (default)
- [ERA5](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5)
- [BARRA-R2](http://www.bom.gov.au/research/publications/researchreports/BRR-067.pdf)

### Nesting configuration
The structure, horizontal resolution and placement of [nests](#nesting) can be customised.<br>
For details on how to modify these configuration settings, refer to [Change the nested region's nest configuration](/models/run_a_model/run_access-ram/#change-the-nested-regions-nest-configuration).

The default nesting configuration for the `ERA5-Land` land-surface initial conditions are the following:

**2-level nest**

- Outer nest: 0.1° x 0.1° (≈10km) horizontal resolution
- Inner nest: 0.0198° x 0.0198° (≈2km) horizontal resolution

### Model components 

- **Atmosphere:** [UM13.5](/models/model_components/atmosphere/#unified-model-um)<br>
   Nests > 4km: GAL9 science configuration, 70 vertical levels.<br>
   Nests <= 4km: [RAL3.2 science configuration](https://doi.org/10.5194/gmd-2024-201), 90 vertical levels.<br>
   Spatial resolution depending on the [nesting configuration](#nesting-configuration).
- **Land:** [Jules7.5](/models/model_components/land/#jules)<br>
   Nests > 4km: GAL9 science configuration, 70 vertical levels.<br>
   Nests <= 4km: [RAL3.2 science configuration](https://doi.org/10.5194/gmd-2024-201), 90 vertical levels.<br>
   Spatial resolution depending on the [nesting configuration](#nesting-configuration).

[Run ACCESS-rAM][run_access-ram]{: class="text-card"}

<custom-references>
- [https://gmd.copernicus.org/articles/13/1999/2020/](https://gmd.copernicus.org/articles/13/1999/2020/)
- [https://doi.org/10.5194/gmd-2024-201](https://doi.org/10.5194/gmd-2024-201)
</custom-references>
