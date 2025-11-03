# Accessing Model Data on Gadi

To assist with finding and accessing model data on Gadi, ACCESS-NRI has created a catalog called the ACCESS-NRI Intake catalog.
This aims to provide a way for Python users to discover and load data across a broad range of climate data products available on <i>Gadi</i>. 

For detailed information, tutorials and more, please go to <a href="https://access-nri-intake-catalog.readthedocs.io/en/latest/index.html" target="_blank">ACCESS-NRI intake catalog documentation</a>.
<!-- <div class="card-container">
    <a href="https://access-nri-intake-catalog.readthedocs.io/en/latest/index.html" class="vertical-card aspect-ratio2to1" target="_blank">
        <div class="card-image-container">
            <img src="../../assets/model_evaluation/accessnri_intake.png" alt="ACCESS-NRI intake catalog documentation" class="img-contain white-background with-padding"></img>
        </div>
        <div class="card-text-container bold ">Documentation</div>
    </a>
</div> -->

## What is the ACCESS-NRI Intake catalog?

The ACCESS-NRI Intake catalog is essentially a table of climate data products available on <i>Gadi</i>. 

Each entry in the table corresponds to a different product, where the columns contain attributes associated with that product (e.g., available models, frequencies and data variables). Users can search on the attributes to find the products that might be useful to them. For example, a user may want to know which data products contain variables X, Y and Z at monthly frequency. 

The ACCESS-NRI Intake catalog enables users to find products that satisfy their query and to subsequently load their data without having to know the location and structure of the underlying files.

## Example: use ACCESS-NRI Intake to find, load and plot data

A simple use case of the ACCESS-NRI Intake catalog is a user wants to plot a timeseries of a variable from a specific data product. 
<br>
For example, the user is interested in plotting a scalar ocean variable called <i>temp_global_ave</i> for an [ACCESS-ESM1.5](/models/access_models/access-esm) run called <i>HI_CN_05</i> (data product). This is an historical run using the same configuration as CMIP6 ACCESS-ESM1.5 historical <i>r1i1p1f1</i>, except that the phosphorus limitation within <a href="\models/model_components/bgc_land#casa-cnp">CASA-CNP</a> is disabled.

First, load the catalog as follows:

```python
import intake
catalog = intake.cat.access_nri
```

To see all available catalogs, run:
```
catalog
```

Now you can load and plot available datasets for the <i>temp_global_ave</i> variable of the <i>HI_CN_05</i> data product as follows:

```python
import matplotlib.pyplot as plt

# This returns an xarray Dataset
dataset = catalog["HI_CN_05"].search(variable="temp_global_ave").to_dask()

# Plot the data
dataset["temp_global_ave"].plot()
plt.title("")
plt.grid()
```

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/intake_example.png" alt="Plot af timeseries of global average temperatures" width="50%"/>
</div>
