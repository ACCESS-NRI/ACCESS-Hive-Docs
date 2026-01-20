{% set model = "ACCESS-ESM1.5" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-esm1.5-configs" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-esm1-5-release-information/2352" %}
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[payu]: https://github.com/payu-org/payu
[model components]: /models/access_models/access-esm/#model-components
[model configurations]: /models/access_models/access-esm/#access-esm15

<div class="text-card-group" markdown>

[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configurations]({{github_configs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

{{ model }} is a fully-coupled global climate model, combining  atmosphere, land, ocean, sea ice, ocean biogeochemistry and land biogeochemistry components. A description of the model and its components is available in the [{{ model }} overview][model configurations].

The instructions below outline how to run {{ model }} using ACCESS-NRI's software deployment pipeline, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_][gadi].

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are open source, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1")![CC icon](https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"}![BY icon](https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"} and available on [ACCESS-NRI GitHub]({{github_configs}}).

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated when new releases are made available.


## Prerequisites

- **Payu instructions**<br>
    Before running {{ model }}, please get familiar with [our instructions for the workflow manager, _payu_](payu.md). In particular, make sure you follow the prerequisites instructions for _payu_ and that you can access the _payu_ software.

- **_MOSRS_ account**<br>
    The [Met Office Science Repository Service (MOSRS)](https://code.metoffice.gov.uk) is a server run by the UK Met Office (UKMO) to support collaborative development with other partners organisations. MOSRS contains the source code and configurations for some model components in {{ model }} (e.g., the [UM](/models/model_components/atmosphere/#unified-model-um)).<br>
    To apply for a _MOSRS_ account, please contact your [local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
    {: #mosrs-account}

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [ki32](https://my.nci.org.au/mancini/project/ki32/join)
    - [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)

    !!! tip
        To request membership for the _ki32_mosrs_ subproject, you need to:
        
        - already be member of the _ki32_ project
        {: style="list-style-type: disc"}
        - have a [MOSRS account](#mosrs-account)
        {: style="list-style-type: disc"}

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

----------------------------------------------------------------------------------------

## Get {{ model }} configuration

All released {{ model }} configurations are available from the [{{ model }} configs]({{github_configs}}) GitHub repository.<br>
Released configurations are tested and supported by ACCESS-NRI, as an adaptation of those originally developed by [CSIRO](https://www.csiro.au/en/research/environmental-impacts/climate-change/climate-science-centre) and [CLEX CMS](https://github.com/coecms/access-esm).

For more information on {{ model }} configurations, check [{{model}}][model configurations] page.

More information about the available experiments and the naming scheme of the branches can also be found in the [{{ model }} configs]({{github_configs}}) GitHub repository.

Once you have chosen a configuration to start with, follow the [_payu_ instructions](payu.md#get-the-model-configuration) to source the configuration, modify it, run it and monitor the run. Additional information specific to {{ model }} is listed below. It is organised using the same headers as in the _payu_ instructions to simplify cross-referencing.

----------------------------------------------------------------------------------------

## Edit {{ model }} configuration {: #edit-{{ model.lower() }}-configuration }

### Change run length {: #runtime .no-toc }

!!! warning
    The _run length_ (controlled by `runtime`) should be left at 1 year for {{model}} experiments in order to avoid errors. Shorter simulations can be useful when setting up and debugging new experiments, however they require additional configuration changes. See the section [Run for less than one year](#shorter-runs) for details.
    
!!! tip
    The `walltime` must be set to be long enough that the PBS job can complete. The model usually runs a single year in 90 minutes or less, but the `walltime` for a single model run is set to `2:30:00` out of an abundance of caution to make sure the model has time to run when there are occasional slower runs for unpredictable reasons. When setting `runspersub > 1` the `walltime` doesn't need to be a simple multiple of `2:30:00` because it is highly unlikely that there will be multiple anomalously slow runs per submit.

#### Run for less than one year {: id="shorter-runs"}

When debugging changes to a model, it is common to reduce the run length to minimise resource consumption and return faster feedback on changes. In order to run the model for a single month, the `runtime` can be changed to

```yml
    runtime:
        years: 0
        months: 1
        days: 0
```

With the default configuration settings, the sea ice component of {{ model }} will produce restart files only at the end of each year. If valid restart files are required when running shorter simulations, the sea ice model configuration should be modified so that restart files are produced at monthly frequencies. To do this, change the `dumpfreq = 'y'` setting to `dumpfreq = 'm'` in the `cice_in.nml` configuration file located in the `ice` subdirectory of the _control_ directory.


### Syncing output data to long-term storage

!!! Warning
    The {{model}} configurations include a [postprocessing script](#postscripts) which converts atmospheric outputs to NetCDF format. This script runs in a separate PBS job and prevents the output and restart files of the most recent run from being automatically synced.<br>
    After a series of runs and the final post-processing is completed, manually execute `payu sync` in the _control_ directory to sync the final output and restart files.

### Other configuration options

#### Postscripts {: .no-toc }

```yaml
postscript: -v PAYU_CURRENT_OUTPUT_DIR,PROJECT -lstorage=${PBS_NCI_STORAGE} ./scripts/NetCDF-conversion/UM_conversion_job.sh
```

All {{ model }} configurations include the NetCDF conversion postscript mentioned above. This script converts the [UM](/models/model_components/atmosphere#unified-model-um)'s fields file format output to NetCDF in order to facilitate analysis and reduce storage requirements. By default, the conversion script will delete the fields files upon successful completion, leaving only the NetCDF output. This automatic deletion can be disabled by commenting out the `--delete-ff` command line flag from the conversion job submission script located in the _control_ directory under `scripts/NetCDF-conversion/UM_conversion_job.sh`.<br>

That means changing

```bash
esm1p5_convert_nc $PAYU_CURRENT_OUTPUT_DIR --delete-ff
```

to

```bash
esm1p5_convert_nc $PAYU_CURRENT_OUTPUT_DIR # --delete-ff
```

### Edit a single {{ model }} component configuration

Each of [{{ model }} components][model components] contains additional configuration options that are read in when the model component is running.<br> These options are typically useful to modify the physics used in the model, the input data, or the model variables saved in the output files.

These configuration options are specified in files located inside a subfolder of the _control_ directory, named according to the submodel's `name` specified in the `config.yaml` `submodels` section (e.g., configuration options for the _ocean_ component are in the `~/access-esm/preindustrial+concentrations/ocean` directory).<br>
To modify these options please refer to the User Guide of the respective model component.

### Create a custom {{ model }} build
All the executables needed to run {{ model }} are pre-built into independent configurations using _Spack_.<br>
To customise {{ model }}'s build (for example to run {{ model }} with changes in the source code of one of its component), refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code#{{model|lower}}).

### Controlling model output
Selecting the variables to save from a simulation can be a balance between enabling future analysis and minimising storage requirements. The choice and frequency of variables saved by each model can be configured from within each submodel's _control_ directory. 

Each submodel's _control_ directory contains _detailed_ and _standard_ presets for controlling the output, located in the `diagnostic_profiles` subdirectories (e.g. `~/access-esm/preindustrial+concentrations/ice/diagnostic_profiles` for the sea ice submodel). The _detailed_ profiles request a large number of variables at higher frequencies, while the _standard_ profiles restrict the output to variables more regularly used across the community. Details on the variables saved by each preset are available in [this Hive Forum topic](https://forum.access-hive.org.au/t/preset-output-profiles-for-esm1-5/3629).

Selecting a preset output profile to use in a simulation can be done by pointing the following symbolic links to the desired profile:

 * `STASHC` in the atmosphere _control_ directory.
 * `diag_table` in the ocean _control_ directory.
 * `ice_history.nml` in the ice _control_ directory.

For example, to select the _detailed_ output profile for the atmosphere:
<terminal-window>
    <terminal-line data="input">cd ~/access-esm/preindustrial+concentrations/atmosphere</terminal-line>
    <terminal-line data="input">ln -sf diagnostic_profiles/STASHC_detailed STASHC</terminal-line>
</terminal-window>


## Get Help

If you have questions or need help regarding {{ model }}, consider creating a topic in the [Earth System Model category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/esm/earth-system-model/72).<br>
For assistance on how to request help from ACCESS-NRI, follow the [guidelines on how to get help](/about/user_support/#still-need-help).

<custom-references>
- [https://github.com/access-nri/access-esm1.5](https://github.com/access-nri/access-esm1.5)
- [https://opus.nci.org.au/](https://opus.nci.org.au/)
- [https://github.com/coecms/esm-pre-industrial](https://github.com/coecms/esm-pre-industrial)
- [https://payu.readthedocs.io/en/latest/usage.html](https://payu.readthedocs.io/en/latest/usage.html)
</custom-references>
