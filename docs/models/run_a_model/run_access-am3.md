{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-am3-configs.access-hive.org.au" %}
{% set example_branch = "main" %}
{% set release_notes = "" %}

# Run {{ model }}

## About

The instructions below outline how to run {{ model }} using ACCESS-NRI's software deployment pipeline, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_](https://nci.org.au/our-systems/hpc-systems).

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are licensed under the UKMO's [Momentum licence](). {{model}} is delivered to the community through private GitHub repositories. See the [Prerequisites](#prerequisites) section for details.

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated when new releases are made available.

## Prerequisites

!!! warning
    If you have not yet read the guide on using the _Rose/Cylc_ tool, please read our [_Rose/Cylc_ documentation](/models/run-a-model/rose-cylc.md) before continuing.

In addition to the [prerequisites for _Rose/Cylc_](/models/run-a-model/rose-cylc/#prerequisites), you will need:

- **Request access to the configurations**<br>
    To request access to the configurations repository (and associated model component repositories), please contact us [through the forum](). This step will also allow us to check you are properly licensed to use the software.

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [access](https://my.nci.org.au/mancini/project/access/join)
    - [ki32](https://my.nci.org.au/mancini/project/ki32/join)
    - [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
    - [xp65](https://my.nci.org.au/mancini/project/xp65/join)

    !!! tip
        To request membership for the _ki32_mosrs_ subproject, you need to:
        
        - already be member of the _ki32_ project
        {: style="list-style-type: disc"}
        - have a [MOSRS account](#mosrs-account)
        {: style="list-style-type: disc"}

    !!! warning
        You will not be granted access to some of the projects listed here before we have checked you are properly licensed to use the software. Ensure you request access to the configurations first.

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Get {{model}} configuration

Follow the instructions in the [_Rose/Cylc_ page](/models/run-a-model/rose-cylc.md) using the following specific information in the [Models configurations stored on _GitHub_](/models/run-a-model/rose-cylc/#model-configurations-stored-on-github) section:

- [Repository](/models/run-a-model/rose-cylc/#model-configurations-stored-on-github): {{ github_ssh }}
- [Branch](/models/run-a-model/rose-cylc/#model-configurations-stored-on-github): {{ example_branch }}

## Setup the configuration

Before you can run the configuration, you need to specify which projects you want to use for data storage and compute costs. For this, in the configuration you have just retrieved from GitHub, open the `rose-suite.conf_nci_gadi` file and change:

- `root_dir` to the path you want to use as a work directory for running the simulation. A space under /scratch is ideal. The directory will be created by the suite if it does not exist.
- `STORAGE_PROJECT` must be the same project as used in the `root_dir` path.
- `COMPUTE_PROJECT` to any project you want to use for the compute cost.

## Run the configuration

See the [model configuration documentation](https://access-nri.github.io/access-am3-configs-doc/) for more detailed information about the configuration.
