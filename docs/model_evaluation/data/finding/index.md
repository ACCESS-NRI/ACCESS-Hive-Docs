# Finding ACCESS data

There are two data catalogues that can be used to find ACCESS model data.
The ideal catalogue to use depends on what data you’re trying to find.

## Which catalogue should you use?
- I’m looking for a published, citable ACCESS-related dataset
  <br>→ Use the **[NCI Data Catalogue](#nci-data-catalogue)**
- I want to discover what ACCESS data exists (e.g. by variable, frequency, or resolution), or find data that may not yet be published
  <br>→ Use the **[ACCESS-NRI Data Catalogue](#access-nri-data-catalogue)**

Both catalogues are publically available but access to the data files themselves
will usually require an NCI account and membership to certain NCI projects, with
a few exceptions noted below.


## NCI Data Catalogue
The **[NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/home)** is a web-based catalogue that anyone can access through a browser. It is the authoritative source for published and curated ACCESS datasets hosted at the National Computational Infrastructure (NCI).

The catalogue allows you to search and browse for data at the dataset level and includes:

- dataset titles and descriptions
- model, experiment, and project information
- publication status and citation details
- links to documentation and data locations at NCI
- links to download files from supported datasets over the web via THREDDS

**Best for:** finding published ACCESS datasets <br>
**Without an NCI account:** browse the catalogue, view all dataset metadata, download some data <br>
**With an NCI account:** access all data files themselves <br>
**More information:**
See the **[NCI Data Catalogue User Guide](https://opus.nci.org.au/spaces/Help/pages/114884997/1.+Finding+data)** for guidance on data access, project membership, and storage systems

*Note: The NCI Data Catalogue focuses on dataset-level metadata, rather than searching within the contents of the data (such as individual variable names).*


## ACCESS-NRI Data Catalogue
The ACCESS-NRI Data Catalogue supports discovery of ACCESS model and other related datasets across a wide range of model configurations and experiments, including datasets that may not yet be formally published.
Note that many datasets are present in both the ACCESS-NRI catalogue and the NCI catalogue.

Unlike the NCI Data Catalogue, the ACCESS-NRI Catalogue allows searching based on metadata describing the contents of the data, including:

- variable names
- temporal frequency of output
- realms
- model components, configurations, and experiments

The ACCESS-NRI Catalogue is accessible in two ways:

- via a Python API, the [ACCESS-NRI Intake Catalogue](access_nri_intake), and
- via a web-based version, the [ACCESS-NRI Interactive Catalogue](interactive_catalogue) (currently in alpha testing).

**Best for:** exploring what ACCESS data exists and discovering datasets based on their metadata attributes, loading and using data<br>
**Without an NCI account:** catalogue can be [viewed](https://access-nri.github.io/interactive-data-catalogue/) but data will not be accessible <br>
**With an NCI account:** required to access the catalogue and datasets on Gadi <br>
**More information:**
See the pages for the **[Intake](access_nri_intake)** and **[Interactive](interactive_catalogue)** interfaces to the catalogue.
