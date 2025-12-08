# Data Variables

<!-- For this content, I have used a lot of text from this website: https://pro.arcgis.com/en/pro-app/latest/help/data/multidimensional/fundamentals-of-netcdf-data-storage.htm -->

For climate modelling, we need to store multidimensional scientific data (variables) such as temperature, humidity, pressure, wind speed and direction.

Variables can be stored in multidimensional [data formats](/model_evaluation/data/data_format) such as <i>NetCDF</i> as separate dimensions where each dimension can have a name and length.


## Common variables

Variables used in climate modelling can differ in terms of naming conventions, units, etc. While this may be for historical reasons, the use of common variables is key not only for ease and compatibilty when working with the data, but also to unite the climate modelling community. Hence, projects will follow or relate to [CF conventions](https://cfconventions.org). These projects have current widely used lists.

<!-- We have created a prototype of markdown files with variable tables that can be queried via jquery -->
<!-- Because they were not ready for quick searches (jquery with extended html tables is slow), we did not include them in the Legacy Relase (July/August 2023). -->
<!-- The code and markdown files are hosted on a github repository, however: https://github.com/svenbuder/access_model_variables -->

### CMIP6 variables
You can search the extensive list of Coupled Model Intercomparison Project phase 6 <a href="https://clipc-services.ceda.ac.uk/dreq/index/var.html" target="_blank">(CMIP6) variables</a> by either the MIP variable name or associated CF standard name.

### ERA5 variables
ERA5 is the fifth generation European Centre for Medium-Range Weather Forecasts (ECMWF) atmospheric reanalysis of the global climate, which spans a period from January 1940 to present. ERA5 provides hourly estimates of a significant number of atmospheric, land and oceanic climate variables.
<br>
<br>
A full list of ERA5 parameters is available on the <a href="https://codes.ecmwf.int/grib/param-db/" target="_blank">ECMWF database</a>. It covers both the <a href="https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-Parameterlistings" target="_blank">ERA5 parameter listings</a> as well as the <a href="https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation#ERA5Land:datadocumentation-parameterlistingParameterlistings" target="_blank">ERA5-LAND parameter listings</a>.

