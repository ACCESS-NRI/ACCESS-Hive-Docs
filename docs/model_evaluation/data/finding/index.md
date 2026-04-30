# Finding ACCESS data

There are two data catalogues that can be used to find ACCESS model data. Which catalogue to use depends on the type of data you are looking for.

<div class="card-container">
    <a href="#nci-data-catalogue" class="vertical-card aspect-ratio2to1">
        <div class="card-image-container">
            <img src="/assets/nci_logo.svg" alt="NCI" class="img-cover"></img>
        </div>
        <div class="card-text-container bold ">NCI Data Catalogue</div>
    </a>
    <a href="#access-nri-data-catalogue" class="vertical-card aspect-ratio2to1">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/accessnri_intake.png" alt="ACCESS-NRI intake" class="img-cover"></img>
        </div>
        <div class="card-text-container bold ">ACCESS-NRI Data Catalogue</div>
    </a>
</div>

## Which data catalogue should I use?

This depends on the type of data you are looking for.

- If you are looking for a published, citable ACCESS-related dataset:
  <br>→ Use the **[NCI Data Catalogue](#nci-data-catalogue)**
- If you want to discover what ACCESS data exists (e.g. by variable, frequency, or resolution), or find data that may not yet be published:
  <br>→ Use the **[ACCESS-NRI Data Catalogue](#access-nri-data-catalogue)**

Both catalogues are publicly available. However, access to the underlying data files 
usually requires an NCI account and membership to specific NCI projects, with
a few exceptions noted below.


## NCI Data Catalogue
The **[NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/home)** is a publicly accessible web-based catalogue. It is the authoritative source for published and curated ACCESS datasets hosted at the National Computational Infrastructure (NCI).

The catalogue allows you to search and browse for datasets and includes:

- dataset titles and descriptions
- model, experiment, and project information
- publication status and citation details
- links to documentation and data locations at NCI
- links to download files from supported datasets over the web via THREDDS

**Best for:** finding published ACCESS datasets <br>
**Without an NCI account:** browse the catalogue, view all dataset metadata, download some data <br>
**With an NCI account:** access all underlying data files <br>
**More information:**
Refer to the **[NCI Data Catalogue User Guide](https://opus.nci.org.au/spaces/Help/pages/114884997/1.+Finding+data)** for guidance on data access, project membership, and storage systems

!!! info
    The NCI Data Catalogue is designed to search dataset-level metadata, rather than the internal contents of datasets (e.g., individual variable names).


## ACCESS-NRI Data Catalogue
The ACCESS-NRI Data Catalogue supports discovery of ACCESS model and other related datasets across a wide range of model configurations and experiments, including datasets that are not yet formally published.
Note that some datasets are present in both the ACCESS-NRI and NCI catalogues.

Unlike the NCI Data Catalogue, the ACCESS-NRI Catalogue allows searching based on metadata describing the contents of the data, including:

- variable names
- temporal frequency of output
- realms
- model components, configurations, and experiments

**Best for:** exploring what ACCESS data exists and discovering datasets based on their metadata attributes, loading and using data<br>
**Without an NCI account:** [view the catalogue](https://access-nri.github.io/interactive-data-catalogue/) (data will not be accessible) <br>
**With an NCI account:** access the catalogue and datasets on _Gadi_ <br>

The ACCESS-NRI Catalogue is accessible in the following ways:

<div class="card-container">
    <a href="access_nri_intake" class="horizontal-card">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/accessnri_intake.png" alt="ACCESS-NRI intake" class="img-contain white-background with-padding">
        </div>
        <div class="card-text-container">
            <span class="bold" >ACCESS-NRI Intake Catalogue</span>
            <span>
                via the ACCESS-NRI Intake Catalogue Python API
            </span>
        </div>
    </a>
    <a href="interactive_catalogue" class="horizontal-card">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/Mar-Business_2.jpg" alt="Look by Freepik - Flaticon" class="img-cover">
        </div>
        <div class="card-text-container">
            <span class="bold" >ACCESS-NRI Interactive Catalogue</span>
            <span>
                via the ACCESS-NRI Interactive Catalogue web-based discovery version (currently in alpha testing)
            </span>
        </div>
    </a>
  </div>

<custom-references>
[Image by jcomp on Freepik](https://www.freepik.com/free-vector/work-office-computer-man-woman-business-character-marketing-online-employee-technology-business-man-cartoon-co-working-flat-design-freelance_13744794.htm#fromView=keyword&page=1&position=1&uuid=69ad7f5f-035d-43cd-a8f5-1bab7cf4c85d)
</custom-references>