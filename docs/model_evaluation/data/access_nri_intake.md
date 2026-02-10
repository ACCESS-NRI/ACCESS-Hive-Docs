# Accessing Model Data on Gadi

To assist with finding and accessing model data on Gadi, ACCESS-NRI maintains a catalog called the ACCESS-NRI Intake catalog.
This aims to provide a way for Python users to discover and load data across a broad range of climate data products available on <i>Gadi</i>. 

## What is the ACCESS-NRI Intake catalog?

The ACCESS-NRI Intake catalog is essentially a table of climate data products available on _Gadi_.

Each entry in the table corresponds to a different product, where the columns contain attributes associated with that product (e.g., available models, frequencies and data variables). Users can search on the attributes to find the products that might be useful to them. For example, a user may want to know which data products contain variables X, Y and Z at monthly frequency. 

The ACCESS-NRI Intake catalog enables users to find products that satisfy their query and to subsequently load their data without having to know the location and structure of the underlying files.

## Example: use ACCESS-NRI Intake to find, load and plot data

A simple use case of the ACCESS-NRI Intake catalog is a user wants to plot a timeseries of a variable from a specific data product.<br>
For example, the user is interested in plotting a scalar ocean variable called _temp\_global\_ave_ for an [ACCESS-ESM1.5](/models/access-esm) run called _HI\_CN\_05_ (data product). This is an historical run using the same configuration as CMIP6 ACCESS-ESM1.5 historical _r1i1p1f1_, except that the phosphorus limitation within [CASA-CNP](/models/model_components/bgc_land#casa-cnp) is disabled.

We can load and plot <i>temp_global_ave</i> for <i>HI_CN_05</i> as follows:

```python
import intake
import matplotlib.pyplot as plt

# Load the catalogue
catalog = intake.cat.access_nri

# This returns an Xarray Dataset
dataset = catalog["HI_CN_05"].search(variable="temp_global_ave").to_dask()

# Plot the data
dataset["temp_global_ave"].plot()
plt.title("")
plt.grid()

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/intake_example.png" alt="Plot af timeseries of global average temperatures" width="50%"/>
</div>
