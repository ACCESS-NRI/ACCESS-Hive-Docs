{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-am3-configs.access-hive.org.au" %}
{% set config_branch = "release-n96e" %}
{% set experiment_name = "my-am3-expt" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-am3-release-information/5446" %}

[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs

!!! release
    This is a [**Beta Release**](/about/releases) intended for experienced users and collaborators. Model configurations and related source code described on this page may change during the release process.

<div class="text-card-group" markdown>
[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configurations]({{github_configs}}){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{configs_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

The instructions below outline how to run {{ model }} using ACCESS-NRI's software deployment pipeline, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_](https://nci.org.au/our-systems/hpc-systems).

If you are unsure whether {{ model }} is the right choice for your experiment, see the overview of [ACCESS Models](/models).

{{model}} configurations are licensed under the UKMO's Momentum licence and are distributed to the community through private _GitHub_ repositories. See the [Request access section](#request-access) for details.

{{ model }} release notes are [available on the ACCESS-Hive Forum]({{release_notes}}) and are updated with each new release.

## Prerequisites

- **NCI account**<br>
    Before running an ACCESS model, you need to [set up your NCI account](/getting_started/set_up_nci_account).

- **GitHub account**<br>
    Open an account on [GitHub](https://github.com/signup) if you do not have one.

- **Request access to the configurations**<br>
    To request access to the configurations repository and associated model component repositories, contact us [through this post on the ACCESS-Hive Forum](https://forum.access-hive.org.au/t/request-access-to-am3-configurations/5580). We can also allow guide you through the licensing process required use the model as required. 
    {: #request-access }

    !!! warning

        This process can take up to 2 weeks.

- **Join NCI projects**<br>

    Request membership to the following NCI projects through their respective project pages:

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

{% include-markdown "includes/rose_cylc8.md"
    start="<!--start:cylc8-gadi-->"
    end="<!--end:cylc8-gadi-->"
%}

## Setup your _GitHub_ account

To work with {{model}}, you need to authenticate your _GitHub_ account from _Gadi_. You can enter your _GitHub_ credentials each time you interact with _GitHub_, or configure credential exchange between _Gadi_ and _GitHub_ to avoid repeated authentication. <br>
Several authentication methods are supported and work with {{model}}. This documentation assumes HTTPS authentication; if you use SSH authentication, adapt the commands accordingly. You can also configure HTTPS authentication alongside existing SSH authentication.

We recommend using the `gh` command-line interface to authenticate _GitHub_ from _Gadi_.

??? info "Setup _GitHub_ authentication on _Gadi_ with `gh`"

    1. Load the `gh` module on _Gadi_ from in a _Gadi_ or a VDI terminal:

        ```
        module use /g/data/vk83/modules
        module load gh
        ```
    
    2. Run `gh auth login` and follow the prompts to authenticate using HTTPS. As _Gadi_ does not have a browser, copy and paste the provided URL into your local browser.

        <terminal-window>
            <terminal-line data="input">gh auth login</terminal-line>
            <terminal-line>? What account do you want to log into? <span class="spack-cyan">GitHub.com</span></terminal-line>
            <terminal-line>? What is your preferred protocol for Git operations on this host? <span class="spack-cyan">HTTPS</span></terminal-line>
            <terminal-line>? How would you like to authenticate GitHub CLI? <span class="spack-cyan">Login with a web browser</span></terminal-line>
            <terminal-line></terminal-line>
            <terminal-line>! First copy your one-time code: <span class="payu-dark-yellow">XXXX-XXXX</span></terminal-line>
            <terminal-line>Press Enter to open github.com in your browser...</terminal-line>
            <terminal-line>! Failed opening a web browser at https://github.com/login/device</terminal-line>
            <terminal-line>exec: "xdg-open,x-www-browser,www-browser,wslview": executable file not found in $PATH</terminal-line>
            <terminal-line>Please try entering the URL in your browser manually</terminal-line>
        </terminal-window>

??? info "Email verification in _GitHub_ for source code modifications"

    If you plan to modify the {{model}} source code, you must have your institutional email address linked to and verified on your _GitHub_ account. Follow [_GitHub_’s instructions](https://docs.github.com/en/account-and-profile/concepts/email-addresses) to set this up. 


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

All released {{ model }} configurations are available in the [{{ model }} configs]({{github_configs}}) _GitHub_ repository: `{{github_configs}}` <br>

Supported configurations:

| Configuration                             | Branch name            |
|-------------------------------------------|------------------------|
| Low resolution based on GC9 configuration | release-n96e           |
| High resolution with climatological aerosols | release-n512e-aeroclim |

{% include-markdown "includes/rose_cylc.md" 
    start="<!--start:get-github-config-->" 
    end="<!--end:get-github-config-->" 
%}

## Initial Configuration Setup

The configuration is set up to use your default project for data storage and compute resources. To use a different project, open `rose-suite.conf` in the _configuration directory_ and change:

- `STORAGE_PROJECT` &rarr; specifies the project to use for storage. Experiment files will be stored under `/scratch/<STORAGE_PROJECT>/$USER/cylc-run`. If changing the STORAGE_PROJECT to a different project than your default, please be aware of the [additional step at installation](#run-the-experiment) explained below.
- `COMPUTE_PROJECT` &rarr; specifies the project charged for the compute resources.

For example, if you want to use the `rp23` project for storage and compute:

```
STORAGE_PROJECT='rp23'
COMPUTE_PROJECT='rp23'
```

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
