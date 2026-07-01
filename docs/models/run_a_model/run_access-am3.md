{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-am3-configs.access-hive.org.au" %}
{% set example_branch = "release-n96e" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-am3-release-information/5446" %}

!!! release
    This is an [**Alpha Release**](/about/releases), intended for use by experienced users and collaborators. Any model configuration and related source code information on this page may change during the release process.

<div class="text-card-group" markdown>
[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configurations]({{github_configs}}){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{configs_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

The instructions below outline how to run {{ model }} using ACCESS-NRI's software deployment pipeline, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_](https://nci.org.au/our-systems/hpc-systems).

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are licensed under the UKMO's Momentum licence. {{model}} is delivered to the community through private GitHub repositories. See the [Request access prerequisite](#request-access) for details.

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated when new releases are made available.

## Prerequisites

!!! warning
    Before continuing, make sure you have read the guide on [running models using _Rose/Cylc_](/models/run-a-model/rose-cylc.md).

- **Rose/Cylc prerequisites**
  All [prerequisites for _Rose/Cylc_](/models/run_a_model/rose_cylc/#prerequisites).

- **Request access to the configurations**<br>
    To request access to the configurations repository (and associated model component repositories), please contact us [through the ACCESS-Hive Forum](https://forum.access-hive.org.au/t/request-access-to-am3-configurations/5580/13). This step will also allow us to check you are properly licensed to use the software.
    {: #request-access }

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [access](https://my.nci.org.au/mancini/project/access/join)
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
    - [xp65](https://my.nci.org.au/mancini/project/xp65/join)

    !!! warning
        You will not be granted access to some of the projects listed here before we have checked you are properly licensed to use the software. Ensure you [request access to the configurations](#request-access) first.

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Get {{model}} configuration

Follow the instructions for [Model configurations stored on _GitHub_](/models/run_a_model/rose_cylc/#model-configurations-stored-on-github) using the following specific information:

- **Repository:** {{ github_ssh }}
- **Branch:** {{ example_branch }}

## Initial Setup

Before you can run {{ model }} configuration, you need to specify which projects you want to use for data storage and compute resources. For this, in the configuration directory open the `rose-suite.conf_nci_gadi` file and change:

- `root_dir` to the path you want to use as a work directory for running the simulation. A space under `/scratch/<project>` is ideal, where `<project>` is the project associated with the current work. The directory will be created by the suite if it does not exist.
- `STORAGE_PROJECT` must be the same project as used in the `root_dir` path.
- `COMPUTE_PROJECT` to any project you want to be charged for the compute resources.

Now the configuration can be run using the [Run the model configuration](/models/run_a_model/rose_cylc/#run-the-model-configuration) instructions.

## Inspecting the outputs

The netCDF outputs are placed in `~/cylc-run/<suite-id>/share/data/History_Data/netCDF`.
The outputs in [UM Fieldsfiles format](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) are placed in `~/cylc-run/<suite-id>/share/data/History_Data`.

## Further Information

See [{{ model }} configuration documentation](https://access-nri.github.io/access-am3-configs-doc/) for more detailed information about {{ model }} configuration.
