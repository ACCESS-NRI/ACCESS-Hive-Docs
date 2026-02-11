# What is the ACCESS-NRI Intake Catalogue?

The ACCESS-NRI Intake Catalogue is essentially Python interface to the table of
climate data products that form the ACCESS Data Catalogue on _Gadi_.
For detailed information, Python tutorials and more, please see the
ACCESS-NRI Intake Catalogue [documentation](https://access-nri-intake-catalog.readthedocs.io/en/latest/index.html).

Each entry in the table corresponds to a different product, where the columns contain attributes associated with that product (e.g., available models, frequencies and data variables). Users can search on the attributes to find the products that might be useful to them. For example, a user may want to know which data products contain variables X, Y and Z at monthly frequency.

The ACCESS-NRI Intake Catalogue enables users to find products that satisfy their
needs and to subsequently load the data with Python without having to know the
location or structure of the underlying files.

## Example: using the ACCESS-NRI Intake Catalogue to find, load and plot data with Python

A user might be interested in plotting a scalar ocean variable called _temp\_global\_ave_ for an [ACCESS-ESM1.5](/models/access-esm) run called _HI\_CN\_05_ (data product). This is an historical run using the same configuration as CMIP6 ACCESS-ESM1.5 historical _r1i1p1f1_, except that the phosphorus limitation within [CASA-CNP](/models/model_components/bgc_land#casa-cnp) is disabled.

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
```

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/intake_example.png" alt="Plot af timeseries of global average temperatures" width="50%"/>
</div>
