# Community Processing Data Processing Tools

<custom-not-supported/>

If we are missing an important tool please let us know.<br> Check [How To Contribute](/about/contribute) to get in touch.

<table>
<tr>
<td width="25%">
    <div align='center' width="100%">
    <h3>Dataset</h3>
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
    <h3>Description</h3>
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://cmor.llnl.gov/" target="_blank">CMOR3<br>(Climate Model Output Rewriter Version 3)</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        CMOR is used to produce CF-compliant netCDF files. The structure of the files created by CMOR and the metadata they contain fulfill the requirements of many of the climate community’s standard model experiments (which are referred to here as “MIPs” and include, for example, AMIP, PMIP, APE, and IPCC scenario runs).
        <br>
        <a href="https://cmor.llnl.gov/" target="_blank">Documentation</a> |
        <a href="https://github.com/PCMDI/cmor" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://github.com/ACCESS-Community-hub/APP4" target="_blank">APP4 (The ACCESS Post Processor)</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        The APP4 is a CMORisation tool designed to convert ACCESS model output to ESGF-compliant formats, primarily for publication to CMIP6. The code was originally built for CMIP5, and was further developed for CMIP6-era activities. It uses CMOR3 and files created with the CMIP6 data request to generate CF-compliant files according to the CMIP6 data standards.
        <br>
        <a href="https://github.com/ACCESS-Community-hub/APP4" target="_blank">Documentation</a> |
        <a href="https://github.com/ACCESS-Community-hub/APP4" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://github.com/ACCESS-NRI/ACCESS-MOPPy" target="_blank">ACCESS-MOPPy<br>(Model Output Post-Processor in Python)</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        ACCESS-MOPPy is a CMORisation tool that post-processes ACCESS model output into CMIP-compliant datasets. It offers a Python API, Dask-enabled parallel processing, PBS batch processing on HPC with a web dashboard for monitoring, and support for CMIP6 and CMIP7 FastTrack. Currently an alpha release.
        <br>
        <a href="https://access-moppy.readthedocs.io/en/latest/" target="_blank">Documentation</a> |
        <a href="https://github.com/ACCESS-NRI/ACCESS-MOPPy" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://github.com/ACCESS-Community-hub/ACCESS-Archiver" target="_blank">ACCESS-Archiver</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        The ACCESS Archiver is designed to archive model output from ACCESS simulations. It's focus is to copy ACCESS model output from its initial location to a secondary location (typically from `/scratch` to `/g/data`), while converting UM files to netCDF, compressing MOM/CICE files, and culling restart files to 10-yearly. Saves 50-80% of storage space due to conversion and compression.
        <br>
        <a href="https://github.com/ACCESS-Community-hub/ACCESS-Archiver" target="_blank">Documentation</a> |
        <a href="https://github.com/ACCESS-Community-hub/ACCESS-Archiver" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://fsspec.github.io/kerchunk/" target="_blank">Kerchunk</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        Kerchunk is a library that provides a unified way to represent a variety of chunked, compressed data formats (e.g. NetCDF/HDF5, GRIB2, TIFF, …), allowing efficient access to the data from traditional file systems or cloud object storage. It also provides a flexible way to create virtual datasets from multiple files.
        Read this <a href="https://medium.com/pangeo/accessing-netcdf-and-grib-file-collections-as-cloud-native-virtual-datasets-using-kerchunk-625a2d0a9191" target="_blank">blogpost</a> on how to access NetCDF and GRIB file colletions with Kerchunk.
        <br>
        <a href="https://fsspec.github.io/kerchunk/" target="_blank">Documentation</a> |
        <a href="https://github.com/fsspec/kerchunk" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://cmip6-preprocessing.readthedocs.io/en/latest/?badge=latest" target="_blank">xMIP</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        This package facilitates the cleaning, organisation and interactive analysis of Model Intercomparison Projects (MIPs) within the Pangeo software stack.
        <br>
        <a href="https://cmip6-preprocessing.readthedocs.io/en/latest/?badge=latest" target="_blank">Documentation</a> |
        <a href="https://github.com/jbusecke/xMIP" target="_blank">Source Code</a> |
        <a href="https://github.com/coecms/xmip_nci" target="_blank">Tutorial</a>
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://espri-mod.github.io/synda/" target="_blank">esgpull and synda</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        esgpull and synda are command line tools to search and download files from the Earth System Grid Federation (ESGF) archive. esgpull is a tool that simplifies usage of the ESGF Search API for data discovery, and manages procedures related to downloading and storing files from ESGF.
        <br>
        <a href="https://github.com/ESGF/esgf-download" target="_blank">Documentation</a> |
        <a href="https://github.com/ESGF/esgf-download" target="_blank">Source Code (esgpull)</a> |
        <a href="https://espri-mod.github.io/synda/" target="_blank">Source Code (synda)</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://github.com/aukkola/FluxnetLSM" target="_blank">FluxnetLSM</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        R package for post-processing FLUXNET datasets for use in land surface modelling. Performs quality control and data conversion of FLUXNET data and collated site metadata. Supports FLUXNET2015, La Thuile, OzFlux and ICOS data releases.
        <br>
        <a href="https://gmd.copernicus.org/articles/10/3379/2017/" target="_blank">Documentation</a> |
        <a href="https://github.com/aukkola/FluxnetLSM" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://unidata.github.io/MetPy/latest/examples/formats/index.html" target="_blank">MetPy</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        MetPy is a collection of tools in Python for reading, visualizing, and performing calculations with weather data. Format types are GINI Water Vapor Imagery, NEXRAD Level 3 File, and NEXRAD Level 2 File.
        <br>
        <a href="https://unidata.github.io/MetPy/latest/examples/formats/index.html" target="_blank">Documentation</a> |
        <a href="https://github.com/Unidata/MetPy" target="_blank">Source Code</a> 
    </div>
</td>
</tr>

<tr>
<td width="25%">
    <div align='center' width="100%">
    <a href="https://xskillscore.readthedocs.io/en/stable/" target="_blank">xskillscore</a> 
    </div>
</td>
<td width="75%">
    <div align='center' width="100%" >
        xskillscore is a Python library for computing a wide variety of skill metrics. Its typical application is to verify deterministic and probabilistic forecasts relative to observations.
        <br>
        <a href="https://xskillscore.readthedocs.io/en/stable/" target="_blank">Documentation</a> |
        <a href="https://github.com/xarray-contrib/xskillscore" target="_blank">Source Code</a> 
    </div>
</td>
</tr>
</table>