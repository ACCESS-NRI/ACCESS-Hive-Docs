{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-am3-configs.access-hive.org.au" %}
{% set config_branch = "release-n96e" %}
{% set experiment_name = "my-am3-expt" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-am3-release-information/5446" %}

[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs

!!! release
    This is a [**Beta Release**](/about/releases), intended for use by experienced users and collaborators. Any model configuration and related source code information on this page may change during the release process.

<div class="text-card-group" markdown>
[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configurations]({{github_configs}}){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{configs_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

The instructions below outline how to run {{ model }} using ACCESS-NRI's software deployment pipeline, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_](https://nci.org.au/our-systems/hpc-systems).

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are licensed under the UKMO's Momentum licence. {{model}} is delivered to the community through private GitHub repositories. See the [Request access section](#request-access) for details.

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated when new releases are made available.

## Prerequisites

- **NCI account**<br>
    Before running an ACCESS model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Request access to the configurations**<br>
    To request access to the configurations repository (and associated model component repositories), please contact us [through the ACCESS-Hive Forum](https://forum.access-hive.org.au/t/request-access-to-am3-configurations/5580/13). This step will also allow us to ensure you are properly licensed to use the software.
    {: #request-access }

- **Join NCI projects**<br>

    Join the following projects by requesting membership on their respective NCI project pages:

    - [access](https://my.nci.org.au/mancini/project/access/join): : ACCESS software sharing
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join): ACCESS Models 
    - [xp65](https://my.nci.org.au/mancini/project/xp65/join): ACCESS Analysis Environments
    {% include-markdown "includes/rose_cylc8.md"
       start="<!--start:cylc8-prerequisites-->"
       end="<!--end:cylc8-prerequisites-->"
    %}

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Terminology

??? info "Understand the difference between _configuration_ and _experiment_"
    {% include-markdown "includes/terminology.md"
        start="<!--start:terminology-conf-vs-exp-->"
        end="<!--start:terminology-conf-vs-exp-->"
    %}

## _Rose/Cylc_ workflow manager

{% include-markdown "includes/rose_cylc8.md"
   start="<!--start:cylc8-compatibility-mode-->"
   end="<!--end:cylc8-compatibility-mode-->"
%}

{% include-markdown "includes/rose_cylc8.md"
   start="<!--start:cylc8-about-->"
   end="<!--end:cylc8-about-->"
%}

??? info "_Rose/Cylc_ directory and files organisation" 
 
    {% include-markdown "includes/rose_cylc8.md"
        start="<!--start:cylc8-structure-->"
        end="<!--end:cylc8-structure-->"
    %}

## Connect to _Gadi_

{% include-markdown "includes/rose_cylc.md"
    start="<!--start:cylc-gadi-->"
    end="<!--end:cylc-gadi-->"
%}

## Setup a persistent session

{% include-markdown "includes/persistent-sessions.md"
    start="<!--start:pers-session-about-->"
    end="<!--end:pers-session-about-->"
%}

??? info "Start a persistent session"

    {% include-markdown "includes/persistent-sessions.md"
        start="<!--start:pers-session-start-->"
        end="<!--end:pers-session-start-->"
    %}

??? info "Assign the persistent session to _Cylc_ (once only)"

    {% include-markdown "includes/persistent-sessions.md"
        start="<!--start:pers-session-assign-->"
        end="<!--end:pers-session-assign-->"
    %}

??? info "Setup the connection between _Cylc_ and _Gadi_ (once only)"

    {% include-markdown "includes/persistent-sessions.md"
        start="<!--start:pers-session-setup-->"
        end="<!--end:pers-session-setup-->"
    %}

??? info "List active persistent sessions"

    {% include-markdown "includes/persistent-sessions.md"
        start="<!--start:pers-session-active-->"
        end="<!--end:pers-session-active-->"
    %}

??? info "Terminate a persistent session"

    {% include-markdown "includes/persistent-sessions.md"
        start="<!--start:pers-session-terminate-->"
        end="<!--end:pers-session-terminate-->"
    %}

## Access _Rose/Cylc_

{% include-markdown "includes/rose_cylc8.md"
    start="<!--start:cylc8-module-->"
    end="<!--end:cylc8-module-->"
%}

## Get {{model}} configuration

All released {{ model }} configurations are available from the [{{ model }} configs]({{github_configs}}) GitHub repository: `{{github_configs}}`.<br>

Supported configurations:

| Configuration   | Branch name   |
|-----------------|---------------|
| Low resolution  | release-n96e  |
| High resolution | release-n512e |

{% include-markdown "includes/rose_cylc.md" 
    start="<!--start:get-github-config-->" 
    end="<!--end:get-github-config-->" 
%}

## Initial Configuration Setup

Before you can run {{ model }} configuration, you need to specify which projects you want to use for data storage and compute resources. For this, in the _configuration directory_, open the `rose-suite.conf_nci_gadi` file and change:

- `root_dir` &rarr; the path you want to use as a work directory for running the simulation. A space under `/scratch/<project>/$USER` is ideal, where `<project>` is the project associated with the current work. The directory will be created by _Cylc_ if it does not exist.
- `STORAGE_PROJECT` &rarr; must be the same project as used in the `root_dir` path.
- `COMPUTE_PROJECT` &rarr; the project you want to be charged for the compute resources.

## Validate the configuration

??? info "Validate the configuration"

    {% include-markdown "includes/rose_cylc8.md" 
        start="<!--start:cylc8-validate-->" 
        end="<!--end:cylc8-validate-->" 
    %}

## Run the experiment

{% include-markdown "includes/rose_cylc8.md"
    start="<!--start:cylc8-run-->"
    end="<!--end:cylc8-run-->"   
%}

## Monitor the experiment

{% include-markdown "includes/rose_cylc8.md"
    start="<!--start:cylc8-monitor-about-->"
    end="<!--end:cylc8-monitor-about-->"
%}

## Further Information

See [{{ model }} configuration documentation](https://access-nri.github.io/access-am3-configs-doc/) for more detailed information about {{ model }} configurations.
