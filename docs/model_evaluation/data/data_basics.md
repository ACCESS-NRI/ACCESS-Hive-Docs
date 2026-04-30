# Basics of ACCESS Data

### Structured data from gridded climate models

ACCESS climate models simulate the Earth system on three-dimensional grids, representing longitude, latitude, and height or depth. These simulations evolve over time, so model output is often four-dimensional (for example: longitude × latitude × depth × time).

Because of this, ACCESS model output is highly structured. Each dataset contains many variables (such as temperature, wind, or precipitation), each defined on specific grids and time intervals. Preserving this structure is essential for correctly interpreting and analysing the data.


### The NetCDF format

ACCESS model data is typically stored in **[netCDF (Network Common Data Form)](https://www.unidata.ucar.edu/software/netcdf)** files. The NetCDF format is well suited to climate and geoscience data because it stores:

- the data values
- metadata that describe what the data represent

Metadata includes information such as variable names, units, grid definitions, coordinate systems, and time conventions. This context is critical: without it, the raw numbers in a dataset are difficult to interpret or use correctly.



#### What’s inside a netCDF file?

A netCDF file is more than a container of numbers. It explicitly defines:

- **dimensions** (e.g. longitude, latitude, time, levels)  
- **variables** (data arrays associated with those dimensions)  
- **attributes** (metadata describing variables and the dataset as a whole)

Tools such as `ncdump` allow users to inspect this format directly, showing how variables are defined and how metadata is stored alongside the data. This self-describing nature is a key strength of netCDF.



### CF conventions and CMOR standards

Most ACCESS netCDF files follow the **[Climate and Forecast (CF) metadata conventions]((https://cfconventions.org)**. CF conventions provide standardised ways to describe:
<!-- https://cfconventions.org server error April2026-->

- coordinates and grids  
- physical quantities and units  
- time and calendar definitions  

These conventions make datasets easier for humans to understand and machines to interpret. Many analysis and visualisation tools (such as [Xarray](https://xarray.dev)) rely on CF conventions to automatically recognise coordinates, apply units correctly, and handle data consistently across different models and datasets.

The term _CMORised_ data may also be used to describe climate data standards. This refers to the use of Climate Model Output Rewriter (CMOR) which is a program writen by PCMDI (Program for Climate Model Diagnosis and Intercomparison) to apply CMIP (Coupled Model Intercomparison Project) standards to model outputs which can be submitted to [CMIP](https://wcrp-cmip.org/). CMOR standards are stricter than CF conventions, allowing consistent multi-model analysis both within and across CMIP generations.

ACCESS-NRI supports CMORisation of ACCESS models with ACCESS-MOPPy.
<!-- card for moppy -->

These standards can be applied alongside the [ACCESS output data specifications](/model_evaluation/data/sharing#access-output-data-specifications).


### Large datasets: chunks

ACCESS model output can be very large, often spanning many files and many terabytes of data. To support efficient access and analysis, data is often stored in chunks — smaller blocks of data organised within the same file.

Chunking allows analysis tools to read only the portions of data needed for a given task, rather than loading entire datasets into memory. While largely invisible to end users, chunking is an important concept when working with large-scale model output. For more information see [NetCDF chunking](https://acdguide.github.io/BigData/data/data-netcdf.html#what-is-data-chunking) and [Xarray with Dask user guide](https://docs.xarray.dev/en/latest/user-guide/dask.html)
