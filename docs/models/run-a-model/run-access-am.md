{% set model = "ACCESS-AM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-am3-configs" %}
{% set github_ssh = "git@github.com:ACCESS-NRI/access-am3-configs.git" %}
{% set configs_docs = "https://access-om3-configs.access-hive.org.au" %}
{% set example_branch = "main" %}

# Run ACCESS-AM3

## Quick Start

{{ model }} configurations are hosted on the [access-am3-configs]({{ github_configs }}) Github repository and use the [_Rose/Cylc_ workflow tool]()**[TODO] Link to rose/cylc docs when published**.

* _Cylc_ version: 7
* Repository: {{ github_ssh }}
* Branch: {{ example_branch }}

Required NCI projects:
* [access](https://my.nci.org.au/mancini/project/access/join)
* [ki32](https://my.nci.org.au/mancini/project/ki32/join)
* [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
* [vk83](https://my.nci.org.au/mancini/project/vk83/join)
* [xp65](https://my.nci.org.au/mancini/project/xk65/join)
