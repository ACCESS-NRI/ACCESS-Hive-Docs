{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-am3-configs.access-hive.org.au" %}
{% set example_branch = "main" %}

# Run {{ model }}

## Quick Start

!!! warning
    If you have not yet read the guide on using the _Rose/Cylc_ tool, please read our [_Rose/Cylc_ documentation](/models/run-a-model/rose-cylc.md) before continuing.

!!! warning
    These configurations are based off licensed configurations from the UK Met Office (UKMO). This means the configurations repository is private. To request access to the configurations repository (and associated model component repositories), please contact us [through the forum]().

{{ model }} configurations are hosted on the [access-am3-configs]({{ github_configs }}) _GitHub_ repository and use the [_Rose/Cylc_ workflow tool](/models/run-a-model/rose-cylc). The _Cylc_ version and remote host location are:

* [_Cylc_ version](/models/run-a-model/rose-cylc/#rose-and-cylc-executables): 7
* [Repository](/models/run-a-model/rose-cylc/#model-configurations-stored-on-github): {{ github_ssh }}
* [Branch](/models/run-a-model/rose-cylc/#model-configurations-stored-on-github): {{ example_branch }}

In addition to the projects specified in the [_Rose/Cylc_ documentation](/models/run-a-model/rose-cylc/#prerequisites), the following project memberships are required:
* [access](https://my.nci.org.au/mancini/project/access/join)
* [ki32](https://my.nci.org.au/mancini/project/ki32/join)
* [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
* [vk83](https://my.nci.org.au/mancini/project/vk83/join)
* [xp65](https://my.nci.org.au/mancini/project/xp65/join)

See the [model configuration documentation](https://access-nri.github.io/access-am3-configs-doc/) for more detailed information about the configuration.
