# Cryosphere Community Datapool

The Cryosphere Community Datapool (CCP) is a joint project between ACCESS-NRI and the [Cryospheric Sciences Working Group (CSWG)](https://forum.access-hive.org.au/c/cryosphere/34). The CCP has been designed as an open-access and freely available cryospheric data resource for the community primarily containing (*but not limited to*):

* <b>Observational data</b>
  * Ice velocities, inSAR
<br><br>
* <b>Derived data</b>
  * Elevation and Geometry data (e.g. BedMachine, BedMap, MEaSUREs)
<br><br>
* <b>Experiment data</b>
  * Ice-sheet modelling output (e.g. ISSM)


## Data hosting and access
All data in the CCP are securely hosted on the National Computational Infrastructure (NCI) Gadi system storage within the `av17` and `cm45` projects and are available to all users with an NCI account. If you do not have an NCI account, you can sign up [here](https://my.nci.org.au/mancini/signup) for free. If you do have a NCI Gadi account but are not a member of `av17` and `cm45`, you must apply to join the project from within your [NCI account](https://my.nci.org.au/mancini/login).

## Available data
The data listed in the following summary table are currently hosted in the CCP. All data are accessible directly via the NCI Gadi filesystem for users with NCI accounts and `av17` project membership, and can be found at `/g/data/av17/access-nri/cryosphere-data-pool/`.

#### Elevation models & geometry data

| Dataset name              | Key variables | `av17` location | Source location | API |
| :------------------------ | :------------ | :--------: |:------: | :--- |
| <b>BedMachine Antarctica v1</b>  | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask  | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v1) | [Link](https://nsidc.org/data/nsidc-0756/versions/1) |  |
| <b>BedMachine Antarctica v2</b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask  | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v2) | [Link](https://nsidc.org/data/nsidc-0756/versions/2) |  |
| <b>BedMachine Antarctica v3</b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask  | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v3) | [Link](https://nsidc.org/data/nsidc-0756/versions/3) | NASA Earthdata  |
| <b>BedMap v1 (gridded) </b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask   | [Path ?](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/gridded_data) | [Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01717 ) |  |
| <b>BedMap v2 (gridded) </b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask   | [Path ?](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/gridded_data) | [Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01717 ) |  |
| <b>BedMap v3 (gridded) </b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask   | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/bedmap/v3/gridded_data) | [Link](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01717 ) |  |
| <b>BedMap v1 (point data)</b> | Bed topography, ice surface elevation, ice thickness | [Path ?]() | [Link 1](https://doi.org/jg6q) [Link 2](https://doi.org/jg6s) [Link 3](https://doi.org/j2vz) |  |
| <b>BedMap v2   (point data)</b> | Bed topography, ice surface elevation, ice thickness | [Path ?]() | [Link 1](https://doi.org/jg6r) [Link 2](https://doi.org/jg8b ) |  |
| <b>BedMap v3   (point data)</b> | Bed topography, ice surface elevation, ice thickness | [Path ?]() | [Link 1](https://doi.org/jg6n) [Link 2](https://doi.org/jg6s)|  |
| <b>MEaSUREs ITS_LIVE Antarctic Grounded Ice Sheet Elevation Change, Version 1</b> | Ice surface elevation, ice surface elevation change | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0782/versions/1) | NASA Earthdata |
| <b>MEaSUREs ITS_LIVE Antarctic Annual 240 m Ice Sheet Extent Masks, 1997-2021, Version 1</b> | Ice mask  | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0794/versions/1) | NASA Earthdata |
| <b>MEaSUREs ITS_LIVE Antarctic Quarterly 1920 m Ice Shelf Height Change and Basal Melt Rates, 1992-2017, Version 1</b> | Ice surface elevation change, basal melt rate, ice shelf thickness | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0792/versions/1) | NASA Earthdata |

#### Ice velocity data

| Dataset name              | Key variables | `av17` location | Source location | API |
| :------------------------ | :------------ | :--------: |:------: | :--- |
| <b>MEaSUREs Phase-Based Antarctica Ice Velocity Map, Version 1</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0754/versions/1) | NASA Earthdata |
| <b>MEaSUREs Annual Antarctic Ice Velocity Maps, Version 1</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0720/versions/1) | NASA Earthdata |
| <b>MEaSUREs InSAR-Based Ice Velocity of the Amundsen Sea Embayment, Antarctica, Version 1</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0545/versions/1) | NASA Earthdata |
| <b>MEaSUREs InSAR-Based Ice Velocity Maps of Central Antarctica: 1997 and 2009, Version 1</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0525/versions/1) | NASA Earthdata |
| <b>MEaSUREs InSAR-Based Antarctica Ice Velocity Map, Version 1</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0484/versions/1) | NASA Earthdata |
| <b>MEaSUREs InSAR-Based Antarctica Ice Velocity Map, Version 2</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0484/versions/2) | NASA Earthdata |
| <b>MEaSURES ITS_LIVE Annual Velocity Maps</b>  | X/Y surface ice velocity components, X/Y surface ice velocity uncertainty | [Path ?]() | [Link](https://nsidc.org/apps/itslive/) | |

#### Geospatial data

| Dataset name              | Key variables | `av17` location | Source location | API |
| :------------------------ | :------------ | :--------: |:------: | :--- |
| <b>MEaSUREs Antarctic Boundaries for IPY 2007-2009 from Satellite Radar, Version 1</b>  | Coastline, grounding line, ice shelf, IMBIE basins, drainage basins, boundaries | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0709/versions/1) | NASA Earthdata |
| <b>MEaSUREs Antarctic Boundaries for IPY 2007-2009 from Satellite Radar, Version 2</b>  | Coastline, grounding line, ice shelf, IMBIE basins, drainage basins, boundaries | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0709/versions/2) | NASA Earthdata |
| <b>MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry, Version 1</b>  | Grounding line | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0498/versions/1) | NASA Earthdata |
| <b>MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry, Version 2</b>  | Grounding line | [Path ?]() | [Link](https://nsidc.org/data/nsidc-0498/versions/2) | NASA Earthdata |

## ISMIP6 datasets
The data listed in the following summary table are currently hosted as part of the CCP on the [NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f8457_7185_0011_6384). All ISMIP6 data are accessible directly via the NCI Gadi filesystem for users with NCI accounts and `cm45` project membership, and can be found at `/g/data/cm45/access-nri/ismip6/`.

#### ISMIP6 simulation data

| Dataset name              | Description | `cm45` location | Source location |
| :------------------------ | :------------ | :--------: |:------: |
| <b>ISMIP6 21st Century Antarctic Projections</b> <i>[Replica]</i>  | These simulations focus on 21st century evolution of the Antarctic ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-AIS/) | [Link](https://doi.org/10.5281/zenodo.11176028) |
| <b>ISMIP6 21st Century Greenland Projections</b> <i>[Replica]</i>  | These simulations focus on 21st century evolution of the Greenland ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-GrIS/) | [Link](https://doi.org/10.5281/zenodo.11176023) |
| <b>ISMIP6 23rd Century Projections</b> <i>[Replica]</i>  | These datasets provide the ISMIP6 Projections 2300 Antarctica projection data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projections-2300/) | [Link](https://doi.org/10.5281/zenodo.13135599) |
| <b>ISMIP6 ABUMIP Simulations</b> <i>[Replica]</i>  | These datasets contain the ice sheet model simulation from the ABUMIP (Antarctic BUttressing Model Intercomparison Project) effort. ABUMIP aims at comparing model responses to complete loss of buttressing by investigating the end-member of ice-shelf buttressing, i.e., the total loss of ice shelves. This enables gauging the sensitivity of different ice sheet models with respect to grounding-line retreat, as a function of basal sliding, isostasy, and other model parameters. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-ABUMIP/) | [Link](https://theghub.org/resources/4744) |
| <b>ISMIP6 initMIP-Antarctica simulations</b> <i>[Replica]</i>  | This dataset contains the initMIP-Antarctica model simulations from the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). As described in Nowicki et al. (2016) and Seroussi et al. (2019), the initMIP-Antarctica experiments focus on ice sheet initialization for the Antarctic ice sheet and associated uncertainty in sea-level projections. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Initmip-AIS/) | [Link](https://theghub.org/resources/4745) |
| <b>ISMIP6 initMIP-Greenland simulations</b> <i>[Replica]</i>  | This dataset contains the initMIP-Greenland model simulations from the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). As described in Nowicki et al. (2016) and Goelzer et al. (2019), the initMIP-Greenland experiments focus on ice sheet initialization for the Greenland ice sheet and associated uncertainty in sea-level projections. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Initmip-GrIS/) | [Link](https://theghub.org/resources/4746) |

#### ISMIP6 forcing data

| Dataset name              | Description | `cm45` location | Source location |
| :------------------------ | :------------ | :--------: |:------: |
| <b>ISMIP6 21st Century Forcing Datasets</b> <i>[Replica]</i>  | These datasets contain the 21st century atmospheric and oceanic forcing datasets used for Greenland and Antarctic standalone ice sheet model simulations as part of the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing/) | [Link](https://doi.org/10.5281/zenodo.11176009) |
| <b>ISMIP6 23rd Century Forcing Datasets</b> <i>[Replica]</i>  | These datasets contain the ISMIP6 23rd century forcing data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing-2300/) | [Link](https://doi.org/10.5281/zenodo.13135571) |


## How to contribute
The Cryosphere Community Datapool is always growing and evolving to meet the changing needs of the Australian cryosphere community, so if you have suggestions for additional datasets not listed above, please [join the ACCESS-Hive forum](https://forum.access-hive.org.au/) and post your dataset request in the CCD forum [request a dataset thread](https://forum.access-hive.org.au/t/cryosphere-data-pool-request-your-datasets/5230).


```
import xarray as xr
dataset = xr.open_dataset("example.nc")
dataset
```
