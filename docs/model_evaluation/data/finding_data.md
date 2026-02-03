# Finding ACCESS data

There are two main data catalogues to find ACCESS model data, depending on what you’re trying to do.

## Which catalogue should you use?
- I’m looking for a published, citable ACCESS-related dataset
  → Use the NCI Data Catalogue
- I want to discover what ACCESS data exists (e.g. by variable, frequency, or resolution), or find data that may not yet be published
  → Use the ACCESS-NRI Data Catalogue

Both catalogues are open to browse. Access to the data files themselves will usually require an NCI account and NCI project membership, with a few exceptions noted below.


## NCI Data Catalogue
The **[NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/home)** is a web-based catalogue that anyone can access through a browser. It is the authoritative source for published and curated ACCESS datasets hosted at the National Computational Infrastructure (NCI).

The catalogue allows you to search and browse at the dataset level, including:
- dataset titles and descriptions
- model, experiment, and project information
- publication status and citation details
- links to documentation and data locations at NCI

**Best for:** finding known, published ACCESS datasets <br>
**Without an NCI account:** browse the catalogue and view all high-level dataset metadata <br>
**With an NCI account:** access the data files themselves <br>
**More information:**
See the **[NCI Data Catalogue User Guide](https://opus.nci.org.au/spaces/Help/pages/114884997/1.+Finding+data)** for guidance on data access, project membership, and storage systems

*Note: The NCI Data Catalogue focuses on dataset-level metadata, rather than searching within the contents of the data (such as individual variable names).*



## ACCESS-NRI Data Catalogue
The ACCESS-NRI Data catalogue supports discovery of ACCESS model and other related datasets across a wide range of model configurations and experiments, including datasets that may not yet be formally published.

Unlike the NCI Data Catalogue, the ACCESS-NRI catalogue enables searching based on metadata describing the contents of the data itself, including:
- variable names
- temporal frequency of output
- realms
- model components, configurations, and experiments

The ACCESS-NRI catalogue is accessible via a Python API ([The ACCESS-NRI Intake Catalog](/model_evaluation/data/access_nri_intake)), allowing users to query and filter metadata. An interactive, web-based version of the catalogue is currently in development ([The ACCESS-NRI Interactive Data Catalog](https://charles-turner-1.github.io/catalog-viewer-spa/#/)).

Note that the ACCESS-NRI catalogue includes the ACCESS-related datasets that are in the NCI Data Catalogue.

**Best for:** exploring what ACCESS data exists and discovering datasets based on their metadata attributes, loading an using data<br>
**Without an NCI account:** catalogue is currently not accessible <br>
**With an NCI account:** required to access the catalogue and datasets within the catalogue <br>
**More information:**
See the **[ACCESS-NRI Data catalogue documentation](https://access-nri-intake-catalog.readthedocs.io/en/latest/index.html)**
