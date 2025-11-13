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

<form action="/search" method="get">
  <input type="search" size="60" id="search-input" name="q" placeholder="Search datapool...">
  <button type="submit">Search</button>
</form>

## Data hosting and access
All data in the CCP are securely hosted on the National Computational Infrastructure (NCI) Gadi system storage within the `av17` project and are available to all users with an NCI account. If you do not have an NCI account, you can sign up [here](https://my.nci.org.au/mancini/signup) for free. If you do have a NCI Gadi account but are not a member of `av17`, you must apply to join the project from within your [NCI account](https://my.nci.org.au/mancini/login).

## Available data
The data listed in the following summary table are currently hosted in the CCP. All data are accessible directly via the NCI Gadi filesystem for users with NCI accounts and `av17` project membership, and can be found at `/g/data/av17/access-nri/cryosphere-data-pool/`.

#### Elevation models & geometry data

| Dataset name              | Key variables | `av17` location | Source location | API |
| :------------------------ | :------------ | :--------: |:------: | :---: |
| <b>BedMachine Antarctica v1</b>  | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask  | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v1) | [Link](https://nsidc.org/data/nsidc-0756/versions/1) |  |
| <b>BedMachine Antarctica v2</b> | Bed topography, bed uncertainty, bathymetry, ice surface elevation, ice thickness, ice mask  | [Path](/g/data/av17/access-nri/cryosphere-data-pool/elevation_geometry/measures_bedmachine_antarctica/v2) | [Link](https://nsidc.org/data/nsidc-0756/versions/1) |  |


## Contribute
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
