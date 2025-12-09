# Cryosphere Community Datapool

The Cryosphere Community Datapool (CCP) is a joint project between ACCESS-NRI and the [Cryospheric Sciences Working Group (CSWG)](https://forum.access-hive.org.au/c/cryosphere/34). The CCP has been designed as an open-access and freely available cryospheric data resource for the community, and houses a variety of datasets commonly used to parameterise ice sheet models. Datasets are currently grouped into (*but not limited to*) the following categories:

1. [**Elevation and geometry**](#elevation-and-geometry-data) - These datasets contain digital elevation models and key geometry attributes, including bed topography/bathymetry, ice surface elevation, ice thickness, and ice/ocean masks.

2. [**Ice velocity**](#ice-velocity-data) - These datasets contain ice velocity parameters, including surface ice velocities and associated error estimates.

3. [**Geospatial**](#geospatial-data) - These datasets contain geospatial information commonly used to discretise ice sheet models, including ice sheet basin boundaries and grounding line locations.

4. [**ISMIP6 simulation**](#ismip6-simulation-data) - These data include results from ISMIP6 model simulations of Antarctica and Greenland.

5. [**ISMIP6 forcing**](#ismip6-forcing-data) - These datasets include forcing parameters, such as surface mass balance, surface temperature, surface wind speeds and geothermal heat flux.


## Data hosting and access
All data in the CCP are securely hosted on the [National Computational Infrastructure (NCI) Gadi supercomputer](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview) within the `av17` and `cm45` projects, and are available to all users with an NCI account. If you do not have an NCI account, you can sign up [here](https://my.nci.org.au/mancini/signup) for free. If you do have a NCI Gadi account but are not a member of `av17` and `cm45`, you must apply to join the project from within your [NCI account](https://my.nci.org.au/mancini/login).

## Available data
The data listed in the following summary tables are currently hosted in the CCP. All data are accessible directly via the NCI Gadi filesystem for users with NCI accounts and `av17` and `cm45` project memberships. [ISMIP6 datasets](#ismip6-datasets) can be found at `/g/data/cm45/access-nri/ismip6/`, while all other datsets and can be found at `/g/data/av17/access-nri/cryosphere-data-pool/`.

### Elevation and geometry data 
[[back to top]](#cryosphere-community-datapool)


| Dataset name              | Key variables | NCI Gadi `av17` path | Source location |
| :------------------------ | :------------ | :-------- |:------: |
| <b>BedMachine Antarctica v1</b>  | Bed topography, Bed uncertainty, Bathymetry, Ice surface elevation, Ice thickness, Ice mask, Geoid  | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0756/versions/1) |
| <b>BedMachine Antarctica v2</b> | Bed topography, Bed uncertainty, Bathymetry, Ice surface elevation, Ice thickness, Ice mask, Geoid | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v2/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0756/versions/2) |
| <b>BedMachine Antarctica v3</b> | Bed topography, Bed uncertainty, Bathymetry, Ice surface elevation, Ice thickness, Ice mask, Geoid | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v3/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0756/versions/3) |
| <b>BedMap v1 (gridded) </b> | Bed topography, Bathymetry, Ice surface elevation, Ice thickness   | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v1/gridded_data/</code></pre> | [Source Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01717 ) |
| <b>BedMap v2 (gridded) </b> | Bed topography, Bed uncertainty, Bathymetry, Ice surface elevation, Ice thickness, Ice mask, Geoid, Ice thickness uncertainty   | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v2/gridded_data/</code></pre> | [ Source Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01617 ) |
| <b>BedMap v3 (gridded) </b> | Bed topography, Bed uncertainty, Bathymetry, Ice surface elevation, Ice thickness, Ice mask, Ice thickness uncertainty  | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/gridded_data/</code></pre> | [Source Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01615 ) |
| <b>BedMap v1 (point data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v1/point_data/</code></pre> | [Source Link](https://doi.org/jg6q) |
| <b>BedMap v2   (point data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v2/point_data/</code></pre> | [Source Link](https://doi.org/jg6r) |
| <b>BedMap v3   (point data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/point_data/</code></pre> | [Source Link](https://doi.org/jg6n)|
| <b>BedMap v1 (geospatial data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v1/geospatial_data/</code></pre> | [Source Link](https://doi.org/jg6s) |
| <b>BedMap v2 (geospatial data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v2/geospatial_data/</code></pre> | [Source Link](https://doi.org/jg6t) |
| <b>BedMap v3 (geospatial data)</b> | Bed topography, Ice surface elevation, Ice thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/geospatial_data/</code></pre> | [Source Link](https://doi.org/jg8b) |
| <b>MEaSURES ITS_LIVE Antarctic Grounded Ice Sheet Elevation Change, Version 1</b> | Ice surface elevation, Ice surface elevation change | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_its_live_antarctic_grounded_ice_sheet_elevation_change/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0782/versions/1) |
| <b>MEaSUREs ITS_LIVE Antarctic Annual 240 m Ice Sheet Extent Masks, 1997-2021, Version 1</b> | Ice mask | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_its_live_antarctic_annual_240m_ice_sheet_extent_masks_1997_2001/v1</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0794/versions/1) |
| <b>MEaSUREs ITS_LIVE Antarctic Quarterly 1920 m Ice Shelf Height Change and Basal Melt Rates, 1992-2017, Version 1</b> | Ice surface elevation change, Basal melt rate, Ice shelf thickness | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_its_live_antarctic_quarterly_1920m_ice_shelf_height_change_and_basal_melt_rates_1992_2017/v1</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0792/versions/1) |


### Ice velocity data
[[back to top]](#cryosphere-community-datapool)

| Dataset name              | Key variables | NCI Gadi `av17` path | Source location |
| :------------------------ | :------------ | :-------- |:------: |
| <b>MEaSUREs Phase-Based Antarctica Ice Velocity Map, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_phase_based_antarctica_ice_velocity_map/v1/</code></pre> |[Source Link](https://nsidc.org/data/nsidc-0754/versions/1) |
| <b>MEaSUREs Annual Antarctic Ice Velocity Maps, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_annual_antarctic_ice_velocity_maps/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0720/versions/1) |
| <b>MEaSUREs InSAR-Based Ice Velocity of the Amundsen Sea Embayment, Antarctica, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_insar_based_ice_velocity_of_the_amundsen_sea_embayment/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0545/versions/1) |
| <b>MEaSUREs InSAR-Based Ice Velocity Maps of Central Antarctica: 1997 and 2009, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_insar_based_ice_velocity_maps_of_central_antarctica/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0525/versions/1) |
| <b>MEaSUREs InSAR-Based Antarctica Ice Velocity Map, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_insar_based_antarctica_ice_velocity_map/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0484/versions/1) |
| <b>MEaSUREs InSAR-Based Antarctica Ice Velocity Map, Version 2</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_insar_based_antarctica_ice_velocity_map/v2/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0484/versions/2) |
| <b>MEaSURES ITS_LIVE Regional Glacier and Ice Sheet Surface Velocities, Version 1</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component, Change in surface ice velocity X component over time, Change in surface ice velocity Y component over time, Ice mask | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_its_live_regional_glacier_and_ice_sheet_surface_velocities/v1/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0776/versions/1) |
| <b>MEaSURES ITS_LIVE Regional Glacier and Ice Sheet Surface Velocities, Version 2</b>  | Surface ice velocity X component, Surface ice velocity Y component, Surface ice velocity uncertainty X component, Surface ice velocity uncertainty Y component, Change in surface ice velocity X component over time, Change in surface ice velocity Y component over time, Ice mask | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/ice_velocity/measures_its_live_regional_glacier_and_ice_sheet_surface_velocities/v2/</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0776/versions/2) |


### Geospatial data
[[back to top]](#cryosphere-community-datapool)

| Dataset name              | Key variables | NCI Gadi `av17` path | Source location |
| :------------------------ | :------------ | :-------- |:------: |
| <b>MEaSUREs Antarctic Boundaries for IPY 2007-2009 from Satellite Radar, Version 1</b>  | Coastline, grounding line, ice shelf, IMBIE basins, drainage basins, boundaries | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/geospatial/measures_antarctic_boundaries_for_ipy_2007_2009_from_satellite_radar/v1</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0709/versions/1) |
| <b>MEaSUREs Antarctic Boundaries for IPY 2007-2009 from Satellite Radar, Version 2</b>  | Coastline, grounding line, ice shelf, IMBIE basins, drainage basins, boundaries | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/geospatial/measures_antarctic_boundaries_for_ipy_2007_2009_from_satellite_radar/v2</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0709/versions/2) |
| <b>MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry, Version 1</b>  | Grounding line | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/geospatial/measures_antarctic_grounding_line_from_differential_satellite_radar_interferometry/v1</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0498/versions/1) |
| <b>MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry, Version 2</b>  | Grounding line | <pre><code>/g/data/av17/access-nri/cryosphere-data-pool/geospatial/measures_antarctic_grounding_line_from_differential_satellite_radar_interferometry/v2</code></pre> | [Source Link](https://nsidc.org/data/nsidc-0498/versions/2) |


### ISMIP6 datasets
The data listed in the following summary tables are currently hosted as part of the CCP on the [NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f8457_7185_0011_6384). All ISMIP6 data are accessible directly via the NCI Gadi filesystem for users with NCI accounts and `cm45` project membership, and can be found at `/g/data/cm45/access-nri/ismip6/`.

#### ISMIP6 simulation data
[[back to top]](#cryosphere-community-datapool)

| Dataset name              | Description | NCI Gadi `cm45` path | Source location |
| :------------------------ | :------------ | :--------: |:------: |
| <b>ISMIP6 21st Century Antarctic Projections</b> <i>[Replica]</i>  | These simulations focus on 21st century evolution of the Antarctic ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-AIS/</code></pre> | [Source Link](https://doi.org/10.5281/zenodo.11176028) |
| <b>ISMIP6 21st Century Greenland Projections</b> <i>[Replica]</i>  | These simulations focus on 21st century evolution of the Greenland ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-GrIS/</code></pre> | [Source Link](https://doi.org/10.5281/zenodo.11176023) |
| <b>ISMIP6 23rd Century Projections</b> <i>[Replica]</i>  | These datasets provide the ISMIP6 Projections 2300 Antarctica projection data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Projections-2300/</code></pre> | [Source Link](https://doi.org/10.5281/zenodo.13135599) |
| <b>ISMIP6 ABUMIP Simulations</b> <i>[Replica]</i>  | These datasets contain the ice sheet model simulation from the ABUMIP (Antarctic BUttressing Model Intercomparison Project) effort. ABUMIP aims at comparing model responses to complete loss of buttressing by investigating the end-member of ice-shelf buttressing, i.e., the total loss of ice shelves. This enables gauging the sensitivity of different ice sheet models with respect to grounding-line retreat, as a function of basal sliding, isostasy, and other model parameters. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-ABUMIP/</code></pre> | [Source Link](https://theghub.org/resources/4744) |
| <b>ISMIP6 initMIP-Antarctica simulations</b> <i>[Replica]</i>  | This dataset contains the initMIP-Antarctica model simulations from the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). As described in Nowicki et al. (2016) and Seroussi et al. (2019), the initMIP-Antarctica experiments focus on ice sheet initialization for the Antarctic ice sheet and associated uncertainty in sea-level projections. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Initmip-AIS/</code></pre> | [Source Link](https://theghub.org/resources/4745) |
| <b>ISMIP6 initMIP-Greenland simulations</b> <i>[Replica]</i>  | This dataset contains the initMIP-Greenland model simulations from the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). As described in Nowicki et al. (2016) and Goelzer et al. (2019), the initMIP-Greenland experiments focus on ice sheet initialization for the Greenland ice sheet and associated uncertainty in sea-level projections. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Initmip-GrIS/</code></pre> | [Source Link](https://theghub.org/resources/4746) |

#### ISMIP6 forcing data
[[back to top]](#cryosphere-community-datapool)

| Dataset name              | Description | NCI Gadi `cm45` path | Source location |
| :------------------------ | :------------ | :--------: |:------: |
| <b>ISMIP6 21st Century Forcing Datasets</b> <i>[Replica]</i>  | These datasets contain the 21st century atmospheric and oceanic forcing datasets used for Greenland and Antarctic standalone ice sheet model simulations as part of the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing/</code></pre> | [Source Link](https://doi.org/10.5281/zenodo.11176009) |
| <b>ISMIP6 23rd Century Forcing Datasets</b> <i>[Replica]</i>  | These datasets contain the ISMIP6 23rd century forcing data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | <pre><code>/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing-2300/</code></pre> | [Source Link](https://doi.org/10.5281/zenodo.13135571) |


## How to contribute
The Cryosphere Community Datapool is always growing and evolving to meet the changing needs of the Australian cryosphere community, so if you have suggestions for additional datasets not listed above, please [create an Issue](https://github.com/ACCESS-NRI/access-cryosphere-data-pool/issues) in the [CCP Github repository](https://github.com/ACCESS-NRI/access-cryosphere-data-pool). For broader discussions around cryospheric data, please start a thread in the [Cryosphere Data Category](https://forum.access-hive.org.au/c/cryosphere/data) on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/). 


