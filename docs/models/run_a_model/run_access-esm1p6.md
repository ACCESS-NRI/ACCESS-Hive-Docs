{% set model = "ACCESS-ESM1.6" %}
{% set model_type = "access-esm" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-esm1.6-configs" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-esm1-6-release-information/6755" %}
{% set config_example = "release-piControl" %}
{% set WG_project = "`lg87` project (ESM Working Group)" %}
{% set WG_project_code = "lg87" %}
{% set configs_docs = "https://access-esm1p6-configs.access-hive.org.au/" %}
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[payu]: https://github.com/payu-org/payu
[model components]: /models/access_models/access-esm/#model-components
[model configurations]: /models/access_models/access-esm/#access-esm16

<div class="text-card-group" markdown>

[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configs docs]({{configs_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

{{ model }} is a fully-coupled global Earth system model, combining  atmosphere, land, ocean, sea ice, ocean biogeochemistry and land biogeochemistry components. A description of the model and its components is available in the [{{ model }} overview][model configurations].

The instructions below outline how to run {{ model }} using ACCESS-NRI's deployed software, specifically designed to run on [NCI](https://nci.org.au/about-us/who-we-are)'s supercomputer [_Gadi_][gadi].

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are open source, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1")![CC icon](https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"}![BY icon](https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"} and available on [ACCESS-NRI GitHub]({{github_configs}}).

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated when new releases are made available.

## Prerequisites

- **NCI Account**<br> 
    Before running {{ model }}, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **_MOSRS_ account**<br>
    [MOSRS](https://code.metoffice.gov.uk) is a server run by the UKMO to support collaborative development with other partners organisations. MOSRS contains the source code for some ACCESS model components and configurations, and a MOSRS account is a license requirement to run these ACCESS-NRI supported models.<br>

    To apply for a MOSRS account, agree to the [ACCESS-NRI Terms of Use](https://reporting.access-nri-store.cloud.edu.au/partner_orgs/agreements/individual/ukmo/) and select the option to request a MOSRS account. For more information on this process, read the [Accessing UKMO licensed models post](https://forum.access-hive.org.au/t/accessing-ukmo-licensed-models/6168) on the ACCESS-Hive Forum. 
    Note that ACCESS-NRI can only facilitate MOSRS account requests for users at ACCESS-NRI partner universities. If you are affiliated with another organisation, you will need to follow your institution's process for obtaining a MOSRS account.
 {: #mosrs-account}

    !!! warning
        The waiting time to obtain a MOSRS account can be up to 2 weeks.

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [ki32](https://my.nci.org.au/mancini/project/ki32/join)
    - [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
{%
    include-markdown "includes/payu.md"
    start="<!--start:payu-projects-->"
    end="<!--end:payu-projects-->"
%}
    !!! tip
        To request membership for the _ki32_mosrs_ subproject, you need to:
        
        - already be member of the _ki32_ project
        {: style="list-style-type: disc"}
        - have a [MOSRS account](#mosrs-account)
        {: style="list-style-type: disc"}

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Terminology

??? info "_Configuration_ and _experiment_ definitions"

    {%
        include-markdown "includes/terminology.md"
        start="<!--start:terminology-conf-vs-exp-->"
        end="<!--end:terminology-conf-vs-exp-->"
    %}

## Workflow manager, _payu_

{%
    include-markdown "includes/payu.md"
    start="<!--start:payu-about-->"
    end="<!--end:payu-about-->"
%}

??? info "_Payu_'s data organisation"

    {%
        include-markdown "includes/payu.md"
        start="<!--start:payu-organisation-->"
        end="<!--end:payu-organisation-->"
    %}
    For {{model}}, the standard output is saved in the file `access-esm1.6.out` and the standard error in `access-esm1.6.err`.

{%
    include-markdown "includes/payu.md"
    start="<!--start:access-payu-->"
    end="<!--end:access-payu-->"
%}

----------------------------------------------------------------------------------------

## Get {{ model }} configuration

Released configurations are developed, tested and supported by ACCESS-NRI and [CSIRO](https://www.csiro.au/en/research/environmental-impacts/climate-change/climate-science-centre).<br> 

All released {{ model }} configurations are available from the [{{ model }} configs]({{github_configs}}) GitHub repository: `{{github_configs}}`.<br>

Supported configurations:

| Configuration | Reference | Branch name |
|---------------|-----------|-------------|
| piControl     | [CMIP7 experiment setup](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/picontrol/) | release-piControl |
| esm-piControl | [CMIP7 experiment setup](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-picontrol/) | release-esm-piControl |
| historical    | [CMIP7 experiment setup](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/historical/) | release-historical |
| esm-historical | [CMIP7 experiment setup](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-hist/) | release-esm-historical |


{%
    include-markdown "includes/payu.md"
    start="<!--start:get-config-payu-->"
    end="<!--end:get-config-payu-->"
%}

??? example "Example: Cloning a configuration"
    {%
        include-markdown "includes/payu.md"
        start="<!--start:payu-clone-example-->"
        end="<!--end:payu-clone-example-->"
    %}

??? info "Testing the configuration"
    {%
        include-markdown "includes/payu.md"
        start="<!--start:payu-test-config-->"
        end="<!--end:payu-test-config-->"
    %}

!!! tip
    If you want to restart your experiment from a specific restart point, please refer to [Start the run from a specific restart file](#specific-restart).

----------------------------------------------------------------------------------------

## Run an experiment

{% include-markdown "includes/payu.md"
    start="<!--start:payu-run-experiment-->"
    end="<!--end:payu-run-experiment-->"
%}

!!! warning
    For production {{model}} experiments, the run length defined in the configuration should remain at 1 year to avoid errors. To run the model for longer, use multiple runs. _Payu_ provides several options for controlling the experiment length, as described in this section.

    The only exception is for testing: runs shorter than one year are possible, but require additional modifications described in [Run for less than one year](#shorter-runs).

??? tip "Identifying the run length for your experiment to ensure it is set to 1 year"

    In {{model}}, the run length is controlled by the `runtime` setting in the `config.yaml` file in the configuration. A 1-year run length is given by:

    ```yml
        runtime:
            years: 1
            months: 0
            days: 0
    ```

??? info "Minimise the number of PBS jobs used"

    {% include-markdown "includes/payu.md"
        start="<!--start:payu-optimise-PBS-->"
        end="<!--end:payu-optimise-PBS-->"
    %}

    !!! tip "Setting `walltime` in `config.yaml`"
        The `walltime` must be long enough for the PBS job to complete. {{model}} typically runs a single year in 60 minutes or less, but `walltime` is set to `2:30:00` to allow for occasional unexpectedly slow runs. When `runspersub > 1`, the `walltime` need not be a multiple of `2:30:00`, as multiple unexpectedly slow runs within a single submission are highly unlikely.

    ??? example "Examples: Time management for experiments"

        {% include-markdown "includes/payu.md"
            start="<!--start:payu-runspersub-examples-->"
            end="<!--end:payu-runspersub-examples-->"
        %}

??? info "Simulate more years for an existing experiment"

    {% include-markdown "includes/payu.md"
        start="<!--start:payu-continue-experiment-->"
        end="<!--end:payu-continue-experiment-->"
    %}

??? info "Re-run an experiment"

    {% include-markdown "includes/payu.md"
        start="<!--start:payu-re-run-experiment-->"
        end="<!--end:payu-re-run-experiment-->"
    %}

----------------------------------------------------------------------------------------

## Monitor {{ model }} runs

{% include-markdown "includes/payu.md"
   start="<!--start:payu-monitor-->"
   end="<!--end:payu-monitor-->"
%}

----------------------------------------------------------------------------------------

## Edit {{ model }} configuration

{% include-markdown "includes/payu.md"
   start="<!-- start:payu-modif-intro-->"
   end="<!--end:payu-modif-intro-->"
%}


??? info "Specify the restart file"

    {% include-markdown "includes/payu.md"
      start="<!--start:payu-restart-choice-->"
      end="<!--end:payu-restart-choice-->"
    %}

??? info "Specify the compute project and storage location"

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-compute-storage-project-->"
       end="<!--end:payu-compute-storage-project-->"
    %}

??? info "Modify PBS resources"

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-PBS-resources-->"
       end="<!--end:payu-PBS-resources-->"
    %}

??? info "Syncing output data"

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-sync-->"
       end="<!--end:payu-sync-->"
    %}    

??? info "Pruning model restarts"

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-restart-prune-->"
       end="<!--end:payu-restart-prune-->"
    %}    

??? info "Collation of ocean output files"

    !!! tip 
    
        Diagnostic and restart files produced by the ocean component, MOM, in {{model}} are not tiled. The collation is not needed and disabled by default in the {{model}} configurations.

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-collate-->"
       end="<!--end:payu-collate-->"
    %}

??? info "_Payu_ options for advanced users"

    {% include-markdown "includes/payu.md"
       start="<!--start:payu-advance-options-->"
       end="<!--end:payu-advance-options-->"
    %}

    ??? info "Run for less than one year for testing purposes"
    
        #### Run for less than one year for testing purposes {: #shorter-runs .no-toc }

        When debugging model changes, it is common to reduce the run length to minimise resource consumption and obtain faster feedback. To run the model for a single month, set runtime to
        
        ```yml
            runtime:
                years: 0
                months: 1
                days: 0
        ```

## Edit the model components' configuration

??? info "Edit the physics options"

    ### Edit the physics options

    To modify the physics of an {{model}} component or the variables saved to its output, edit the component's configuration files, located in a subfolder of the _control_ directory.


    To change the input files used by a model (e.g., topography and atmospheric forcings), update the corresponding file paths in the `config.yaml`. This may also require changes to the submodel configuration files.

??? info "Create a custom {{ model }} build"

    ### Create a custom {{ model }} build

    All executables required to run {{ model }} are pre-built into independent configurations using _Spack_.<br>
    To customise {{ model }}'s build (e.g., to incorporate source-code changes to a component), see [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code#{{model|lower}}0).

??? info "Controlling the diagnostics output by the model"

    ### Controlling the diagnostics output by the model

    Choosing which variables to save involves balancing future analysis needs against storage requirements. The variables saved, and their output frequency, can be configured in each submodel’s _control_ directory. 
    
    Each submodel's _control_ directory contains _detailed_ and _standard_ output presets in its `diagnostic_profiles` subdirectory (e.g., `~/{{model|lower}}/{{config_example}}/ice/diagnostic_profiles` for the sea ice submodel). The _CMIP7_ profiles request variables used in CMIP7 experiments, with a larger number of variables at higher frequencies, while the standard profiles limit output to variables more commonly used across the community. Details of the variables saved by each preset are available in [this Hive Forum topic](https://forum.access-hive.org.au/t/preset-output-profiles-for-esm1-5/3629).
    
    Select a preset output profile by pointing the following symbolic links to the desired profile:
    
     * `STASHC` in the atmosphere _control_ directory.
     * `diag_table` in the ocean _control_ directory.
     * `ice_history.nml` in the ice _control_ directory.
    
    For example, to select the _detailed_ output profile for the atmosphere submodel:
    <terminal-window>
        <terminal-line data="input">cd ~/{{model|lower}}/{{config_example}}/atmosphere</terminal-line>
        <terminal-line data="input">ln -sf diagnostic_profiles/STASHC_detailed STASHC</terminal-line>
    </terminal-window>

## Get Help

For questions or help with {{ model }}, post a topic in the Earth System Model category of the
[Earth System Model category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/esm/earth-system-model/72).<br>
For assistance from ACCESS-NRI, follow the [guidelines on how to get help](/about/user_support/#still-need-help).

<custom-references>
- Build infrastructure: [https://github.com/access-nri/access-esm1.6](https://github.com/access-nri/access-esm1.6)
- NCI documentation: [https://opus.nci.org.au/](https://opus.nci.org.au/)
- Payu documentation: [https://payu.readthedocs.io/en/latest/usage.html](https://payu.readthedocs.io/en/latest/usage.html)
</custom-references>
