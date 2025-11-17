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
| <b>ISMIP6 21st Century Antarctic Projections [Replica]</b>  | These simulations focus on 21st century evolution of the Antarctic ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-AIS/) | [Link](https://doi.org/10.5281/zenodo.11176028) |
| <b>ISMIP6 21st Century Greenland Projections [Replica]</b>  | These simulations focus on 21st century evolution of the Greenland ice sheet under selected CMIP scenarios (RCP2.6, RCP8.5, SSP126 and SSP585) and CMIP models. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projection-GrIS/) | [Link](https://doi.org/10.5281/zenodo.11176023) |
| <b>ISMIP6 23rd Century Projections [Replica]</b>  | These datasets provide the ISMIP6 Projections 2300 Antarctica projection data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Projections-2300/) | [Link](https://doi.org/10.5281/zenodo.13135599) |

#### ISMIP6 forcing data

| Dataset name              | Description | `cm45` location | Source location |
| :------------------------ | :------------ | :--------: |:------: |
| <b>ISMIP6 21st Century Forcing Datasets [Replica]</b>  | These datasets contain the 21st century atmospheric and oceanic forcing datasets used for Greenland and Antarctic standalone ice sheet model simulations as part of the Ice Sheet Model Intercomparison Project for CMIP6 (ISMIP6). | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing/) | [Link](https://doi.org/10.5281/zenodo.11176009) |
| <b>ISMIP6 23rd Century Forcing Datasets [Replica]</b>  | These datasets contain the ISMIP6 23rd century forcing data that focus on simulations of the Antarctic Ice Sheet (AIS) extended to year 2300. These simulations are based on CMIP5 and CMIP6 climate model outputs, and are a follow-on to the simulations to 2100. | [Path](/g/data/cm45/access-nri/ismip6/ISMIP6-Forcing-2300/) | [Link](https://doi.org/10.5281/zenodo.13135571) |


## How to contribute
There are many ways of reading files, though a common way is via the Python package *xarray*.
<br>
For more information, refer to a <a href="https://docs.xarray.dev/en/stable/getting-started-guide/quick-overview.html" target="_blank">quick overview of xarray</a> and <a href="https://tutorial.xarray.dev/intro.html" target="_blank">xarray tutorials</a>.

*xarray* is a python package avaliable through the conda environment on NCI.
<br>
Hence, you can either use it directly (as shown below) or through the dataset capabilities of the [ACCESS-NRI Model Intake Catalog Tool](/model_evaluation/data/model_catalogs).

```
import xarray as xr
dataset = xr.open_dataset("example.nc")
dataset
```

<div style="text-align: center;">
     <img src="../../../assets/model_evaluation/netcdf_example.jpg" alt="Example of an actual NetCDF file with data (precipitation/rainfall over the dimensions latitude, longitude, and time) and metadata." title="Picture from https://pro.arcgis.com/en/pro-app/latest/help/data/multidimensional/fundamentals-of-netcdf-data-storage.htm" width="60%"/>
 </div>

## Other Data formats

NetCDF has been described in detail here as it is the most common format for climate data and then for comparison and optimizing evaluation workflows all data would be in the same format. [Observational data](/model_evaluation/data/observations) can come from different institutions and measured with various instruments. These institutions can manage their data for users other than climate researchers, therefore the data can come in other formats including plain text formats. This data can be [_CMORised_](#data-standards), for evaluation frameworks. Reach out on the [Hive Forum](https://forum.access-hive.org.au) for assistance and suggestions of any datasets that may be missing or could be useful.


<h6>References</h6>
<ul class="references">
    <li>
        <a href = "https://pro.arcgis.com/en/pro-app/latest/help/data/multidimensional/fundamentals-of-netcdf-data-storage.htm" target="_blank">https://pro.arcgis.com/en/pro-app/latest/help/data/multidimensional/fundamentals-of-netcdf-data-storage.htm</a>
    </li>
