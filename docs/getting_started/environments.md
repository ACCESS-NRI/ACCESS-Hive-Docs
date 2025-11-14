{% set release_notes = "https://forum.access-hive.org.au/t/access-nri-analysis3-conda-environments-new-release-announcement/4377" %}

<div class="text-card-group" markdown>
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# _conda/analysis3_ Python Environment

!!! danger
    All users are advised to [update their workflows](#update-workflows) to replace the `hh5` `conda/analysis3` environment with the `xp65` `conda/analysis3` environment as soon as possible to ensure continued support and access to the latest features. The `hh5` `conda/analysis3` environment is no longer actively maintained and, **after 30 May 2025**, may be taken down without prior notice.
   

ACCESS-NRI now supports and maintains the `conda/analysis3` _Python_ environment, housed within the [xp65 NCI project](https://my.nci.org.au/mancini/project/xp65/join). This environment includes _Python_ libraries commonly used for climate data processing and analysis, allowing users to run workflows on _Gadi_ without having to manage package installations themselves. This is the continuation of the environments formerly [maintained by CLEX](#acknowledgements) within the `hh5` NCI project.


## How to use the _xp65_ _conda/analysis3_ environment
 There are 3 main ways to use the `conda/analysis3` environment:  

1. [Command line and shell scripts](#manually-load-the-environment) 
2. [PBS job](#use-the-environment-within-a-pbs-job)
3. [ARE](#use-the-environment-within-are)

!!! tip
    If you only want to update your workflows from the previous `hh5` `conda/analysis3` environment, refer to [Update your workflows](#update-workflows) below.

### Manually load the environment {: #manually-load-the-environment }
  For each new session within a _Gadi_ login node, [ARE VDI](/getting_started/are/#vdi) terminal, or in a shell script, run:
  ```
  module use /g/data/xp65/public/modules
  module load conda/analysis3
  ```

!!! tip
    If you have previously added commands to load the `hh5` `conda/analysis3` environment within your `.bashrc` or `.bash_profile` file, we strongly recommend **completely removing those lines**, 
    as programmatically loading environments that way might lead to unexpected interference with other processes on _Gadi_.<br><br>
    A safer approach is to define a [Bash alias](https://tldp.org/LDP/abs/html/aliases.html) or shell function that runs your desired series of commands. 
    You can then manually invoke the alias whenever needed.<br>
    For example, you can add the following line to your `.bashrc` or `.bash_profile` file:
    ```sh
    alias analysis3='module use /g/data/xp65/public/modules && module load conda/analysis3'
    ```
    Then, within any session, you can simply run `analysis3` to load the environment.

### Use the environment within a PBS job  {: #use-the-environment-within-a-pbs-job }
In a [PBS job submission script](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-SubmissionScriptExample) (including usage within _rose/cylc_ workflows), in addition to adding the `module use` and `module load` lines above, add `gdata/xp65` to your storage flag:
```
#PBS -l storage=gdata/xp65
```
!!! tip
    Multiple storage projects are separated by a plus (`+`): 
    ```
    #PBS -l storage=scratch/tm70+gdata/xp65
    ```

### Use the environment within ARE  {: #use-the-environment-within-are }
<div class="tabLabels" label="are">
    <button id="are-jupyterlab">ARE JupyterLab</button>
    <button id="are-vdi">ARE VDI</button>
</div>
<div tabcontentfor='are-jupyterlab' markdown>
When launching an [ARE JupyterLab](/getting_started/are/#jupyterlab) instance:

1. Under _Storage_, add  `gdata/xp65`.<br>
    If you have other storage locations, use a plus sign (`+`) (e.g., `+gdata/xp65`).
2. Under _Advanced options_:
    - In "Module directories", add `/g/data/xp65/public/modules/`
    - In "Modules", add `conda/analysis3`
</div>
<div tabcontentfor='are-vdi' markdown>
When launching an [ARE VDI](/getting_started/are/#vdi) instance:

1. Under _Storage_, add  `gdata/xp65`.<br>
    If you have other storage locations, use a plus sign (`+`) (e.g., `+gdata/xp65`).
2. Under _PBS flags_, add `-v SINGULARITY_OVERLAYIMAGE=/g/data/xp65/public/apps/med_conda/envs/$(readlink /g/data/xp65/public/apps/med_conda/envs/analysis3).sqsh`
    
    !!! warning
        This will only work if you load the latest `analysis3` environment using `module load conda/analysis3`.<br>
        If you want to [load a specific version](#load-a-specific-environment-version), the `SINGULARITY_OVERLAYIMAGE` env variable will need to specify the exact version in the format: `/g/data/xp65/public/apps/med_conda/envs/analysis3-YY-MM.sqsh`.
</div>



## How to switch from the _hh5_ to the _xp65_ _conda/analysis3_ environment  {: #update-workflows }
If you have workflows that use the `hh5` `conda/analysis3` environment, follow the steps below to update them to use the `xp65` `conda/analysis3` environment instead:

1. If you have not already, **[request membership to the xp65 project](https://my.nci.org.au/mancini/project/xp65/join)**
2. **Replace all instances of `hh5` with `xp65`**
3. **Make sure you are loading a correct version**<br>
   The  `xp65` `conda/analysis3` environment versioning might differ from the old `hh5` `conda/analysis3` one. Therefore, if you were loading a specific version (e.g., `conda/analysis3-23.10`), make sure to [specify a valid version](#load-a-specific-environment-version) for the `xp65` `conda/analysis3` environment.


## Advanced usage

### Two Series of Environments: _conda/analysis3_ and _conda/analysis3-edge_

There are two parallel series of environments:

- **_conda/analysis3_**<br>
    A stable environment designed for long-term usability with well-tested, reliable package versions.
- **_conda/analysis3-edge_**<br>
    A cutting-edge environment with the latest available packages, ideal for those needing the most up-to-date software and features.

These series offer flexibility: use `conda/analysis3` for stability, or `conda/analysis3-edge` for the latest updates.

### Load a specific environment version

The `xp65` `conda/analysis3` environment follows the versioning format `conda/analysis3-YY-MM`, where `YY` represents the last two digits of the release year and `MM` indicates the release month.

#### Command line and PBS 

When [manually loading the environment](#manually-load-the-environment) or [within a PBS job](#use-the-environment-within-a-pbs-job), you can load a particular version by explicitly specifying its release year and month (e.g., to load the April 2025 environment, specify `conda/analysis3-25.04`).<br>
If you do not specify a version (e.g. using `conda/analysis3` rather than `conda/analysis3-YY.MM`) the latest (i.e., previous month's) frozen environment version will be loaded. We encourage those who want the newest features to help us test the current version by explicitly loading the current month’s environment. <br>
 <terminal-window>
    <terminal-line data="input">module use /g/data/xp65/public/modules</terminal-line>
    <terminal-line data="input">module load conda/analysis3</terminal-line>
    <terminal-line></terminal-line>
    <terminal-line>Loading conda/analysis3-25.06</terminal-line>
    <terminal-line>    Loading requirement: singularity</terminal-line>
  </terminal-window>

!!! note 
    For _rose/cylc_ workflows, it is not recommended to specify a particular version of the environment (i.e. use `conda/analysis3` and not `conda/analysis3-YY.MM`).

#### ARE Jupyterlab

When launching an [ARE Jupyterlab session](#are-jupyterlab), you only need to include `conda/analysis3`. If you would like to specify a particular environment version, you can do so for each notebook by switching kernels inside the ARE instance.

!!! tip
    The same version naming structure can be applied to the `conda/analysis3-edge` environment.

## Acknowledgements 

These environments, developed and maintained by the CLEX CMS team, have proven very valuable to the community over the years. We commend and thank the CMS team for implementing this very successful service and supporting it for the whole community.




