{% set model = "ACCESS-OM3" %}
{% set github_configs = "https://github.com/ACCESS-NRI/access-om3-configs" %}
{% set configs_docs = "https://access-om3-configs.access-hive.org.au" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-om2-release-information/4494/" %}
{% set example_branch = "release-MC_25km_jra_ryf" %}
{% set example_folder = "25km_jra_ryf" %}
[cosima]: https://cosima.org.au
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[payu]: https://github.com/payu-org/payu
[model components]: /models/access_models/access-om/#model-components-{{ model }}
[model configurations]: /models/access_models/access-om/#access-om3
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview

!!! release
    This is a **Beta Release**.<br>
    Any model configuration and related source code mentioned in this page might change before the full release.<br>
    Limited support is currently provided for this model. Its usage is only recommended for testing by experienced users and collaborators. For a supported and validated model and configuration, see [Run ACCESS-OM2](/models/run_a_model/run_access-om2) instead.

<div class="text-card-group" markdown>
[:fontawesome-brands-github:{: class="twemoji icon-before-text"} {{ model }} configurations]({{github_configs}}){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{configs_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

{{ model }} is an ocean-sea ice model. More information is available in the [{{ model }} overview][model configurations].

The instructions below outline how to run {{ model }} using ACCESS-NRI's deployed software, on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_][gadi].

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are open source, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1")![CC icon](https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"}![BY icon](https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1){: style="height:1em;margin-left:0.2em;vertical-align:text-top;"} and available on [ACCESS-NRI GitHub]({{github_configs}}).

Detailed documentation on the configurations can be found in the [{{ model }} configuration documentation]({{configs_docs}}).

## Prerequisites

!!! warning
    To run {{ model }}, you need to be a member of a project with allocated _Service Units (SU)_. For more information, check [how to join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

- **NCI Account**<br> 
    Before running {{ model }}, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [qv56](https://my.nci.org.au/mancini/project/qv56/join)
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
    - [xp65](https://my.nci.org.au/mancini/project/xp65/join)

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

- **Payu**<br>
    [Payu][payu] is a workflow management tool for running numerical models in supercomputing environments, for which there is extensive [documentation](https://payu.readthedocs.io/en/latest/).<br>
    _Payu_ on _Gadi_ is available through a dedicated `conda` environment in the _vk83_ project.<br>
    After joining the _vk83_ project, load the `payu` module:
    
        module use /g/data/vk83/modules
        module load payu

    To check that _payu_ is available, run:

        payu --version
    
    <terminal-window>
        <terminal-line data="input">payu --version</terminal-line>
        <terminal-line lineDelay="1000">1.1.7</terminal-line>
    </terminal-window>

----------------------------------------------------------------------------------------


## Download and run {{ model }} configuration

{{ model }} configurations run on [_Gadi_][gadi] through a [PBS job][PBS job] submission managed by [_payu_][payu].

The general layout of a _payu_ supported model run consists of two main directories:

- The _control_ directory contains the model configuration and serves as the execution directory for running the model (in this example, the cloned directory `~/access-om3/{{example_folder}}`).
- The _laboratory_ directory, where all the model components reside. For {{ model }}, it is typically `/scratch/$PROJECT/$USER/access-om3`.

This separates the small text configuration files from the larger binary outputs and inputs. In this way, the _control_ directory can be in the `$HOME` directory (as it is the only filesystem actively backed-up on _Gadi_). The quotas for `$HOME` are low and strict, which limits what can be stored there, so it is not suitable for larger files.

The _laboratory_ directory is a shared space for all _payu_ experiments using the same model.<br>
Inside the _laboratory_ directory there are two subdirectories:

- `work` &rarr; a directory where _payu_ automatically creates a temporary subdirectory while the model is run. The temporary subdirectory gets created as part of a run and then removed after the run succeeds.
- `archive` &rarr; the directory where the output is stored following each successful run.

Within each of the above directories _payu_ automatically creates subdirectories uniquely named according to the experiment being run.<br>
_Payu_ also creates symbolic links in the _control_ directory pointing to the `archive` and `work` directories.

This design allows multiple self-resubmitting experiments that share common executables and input data to be run simultaneously.

If you want to modify your configuration, refer to [Edit {{ model }} configuration](#edit-{{ model.lower() }}-configuration).

!!! admonition warning
    Files on the `/scratch` drive, such as the _laboratory_ directory, might get deleted if not accessed for several days and the `/scratch` drive is limited in space. For these reasons, we strongly recommend that all model runs which are to be kept should be moved to `/g/data/` by enabling the _sync_ step in _payu_. To know more refer to [Syncing output data](#syncing-output-data).


----------------------------------------------------------------------------------------

### Get {{ model }} configuration

All released {{ model }} configurations are available from the [{{ model }} configs]({{ github_configs }}) GitHub repository; released configurations (`release-` in the branch name) are tested and supported by ACCESS-NRI. More information about the available configurations and the naming scheme of the branches can be found in the  [{{ model }} configs]({{ github_configs }}) GitHub repository.

The first step is to choose a configuration from those available. For example, to run an ocean and sea ice configuration (MOM6-CICE6) at 25km horizontal resolution with repeat-year _JRA55_ forcing (without BGC), one should select the branch [`{{example_branch}}`](https://github.com/ACCESS-NRI/access-om3-configs/tree/{{example_branch}}). 

To clone this branch to a location on _Gadi_ and navigate to that directory, run:
    
    mkdir -p ~/access-om3
    cd ~/access-om3
    payu clone -b expt -B {{ example_branch }} {{ github_configs }} {{example_folder}}
    cd {{example_folder}}

Each released configuration has a [git tag](https://github.com/ACCESS-NRI/access-om3-configs/tags) and a corresponding branch. The branch always reflects the latest configuration release.<br>
In the example above, the `payu clone` command clones the latest release of the 25km repeat-year JRA55 MOM6 (`M`) CICE6 (`C`) configuration (` -B {{ example_branch }}`) to a directory named `{{example_folder}}` and creates a new experiment branch (`-b expt`).<br>
If you want work with an older release (for example to compare against older model output), you can clone directly from the corresponding tag using the `-s TAG_NAME` payu option instead. For further details, refer to [_payu_ documentation on cloning an experiment](https://payu.readthedocs.io/en/stable/usage.html#clone-experiment).
!!! admonition tip
    Anyone using a configuration is advised to clone only a single branch (as shown in the example above) and not the entire repository.

<terminal-window>
    <terminal-line data="input">mkdir -p ~/access-om3</terminal-line>
    <terminal-line data="input">cd ~/access-om3</terminal-line>
    <terminal-line data="input" directory="~/access-om3">payu clone -b expt -B {{ example_branch }} https://github.com/ACCESS-NRI/access-om3-configs.git {{example_folder}}</terminal-line>
    <terminal-line lineDelay=1000>Cloned repository from https://github.com/ACCESS-NRI/access-om3-configs.git to directory: .../access-om/{{example_folder}}</terminal-line>
    <terminal-line>Created and checked out new branch: expt</terminal-line>
    <terminal-line>laboratory path:  /scratch/.../access-om3</terminal-line>
    <terminal-line>binary path:  /scratch/.../access-om3/bin</terminal-line>
    <terminal-line>input path:  /scratch/.../access-om3/input</terminal-line>
    <terminal-line>work path:  /scratch/.../access-om3/work</terminal-line>
    <terminal-line>archive path:  /scratch/.../access-om3/archive</terminal-line>
    <terminal-line>Updated metadata. Experiment UUID: daeee7ff-07e4-4f93-823b-cb7c6e4bdb6e</terminal-line>
    <terminal-line>Added archive symlink to /scratch/.../access-om3/archive/{{example_folder}}-expt-daeee7ff</terminal-line>
    <terminal-line data="input" directory="~/access-om3">cd {{example_folder}}</terminal-line>
    <terminal-line data="input" directory="~/access-om3/{{example_folder}}"></terminal-line>
</terminal-window>

!!! tip
    _payu_ uses branches to differentiate between different experiments in the same local `git` repository.<br>
    For this reason, it is recommended to always set the cloned branch name (`expt` in the example above) to something meaningful for the planned experiment.<br>
    For more information refer to this [payu tutorial](https://forum.access-hive.org.au/t/access-om2-payu-tutorial/1750#select-experiment-12).

### Run configuration

To run the cloned {{ model }} configuration, execute the following command from within the *control* directory:

    payu run

This will submit a single job to the supercomputer "queue" with the default run length (1 year) specified in the configuration.<br>
For information about changing the run length, refer to [Change run length and restart period](#change-run-length-and-restart-period).

<terminal-window>
    <terminal-line data="input">cd ~/access-om3/{{example_folder}}</terminal-line>
    <terminal-line directory="~/access-om3/{{example_folder}}" data="input">payu run</terminal-line>
    <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
    <terminal-line lineDelay=50>Loading restart manifest: manifests/restart.yaml</terminal-line>
    <terminal-line lineDelay=50>Loading exe manifest: manifests/exe.yaml</terminal-line>
    <terminal-line lineDelay=50>payu: Found modules in /opt/Modules/v4.3.0</terminal-line>
    <terminal-line lineDelay=50>
        qsub -q normal -P tm70 -l walltime=02:00:00 -l ncpus=240 -l mem=960GB -l jobfs=10GB -N 25km_jra55do_ry -l wd -j n -v PAYU_PATH=/g/data/vk83/apps/base_conda/envs/payu-1.1.6/bin,MODULESHOME=/opt/Modules/v4.3.0,MODULES_CMD=/opt/Modules/v4.3.0/libexec/modulecmd.tcl,MODULEPATH=/g/data/vk83/modules:/etc/scl/modulefiles:/opt/Modules/modulefiles:/opt/Modules/v4.3.0/modulefiles:/apps/Modules/modulefiles -l storage=gdata/tm70+gdata/vk83 -- /g/data/vk83/./apps/conda_scripts/payu-1.1.6.d/bin/python /g/data/vk83/apps/base_conda/envs/payu-1.1.6/bin/payu-run
    </terminal-line>
    <terminal-line lineDelay=50>&lt;job-ID&gt;.gadi-pbs</job-ID>></terminal-line>
</terminal-window>
!!! tip
    You can add the `-f` option to `payu run` to let the model run even if there is an existing non-empty `work` directory, created from a previous failed run or from running `payu setup`.

----------------------------------------------------------------------------------------

## Monitor {{ model }} runs

The `payu run` command prints out the PBS `job-ID` (formatted as `<9-digit-number>.gadi-pbs`), as the last line to the terminal.<br>
To print out information on the status of a specific job, you can execute the following command:
```
qstat <job-ID>
```
<terminal-window>
    <terminal-line data="input">qstat &lt;job-ID&gt;</terminal-line>
    <terminal-line linedelay=500 class="keep-blanks">Job id                 Name             User              Time Use S Queue</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">---------------------  ---------------- ----------------  -------- - -----</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      {{example_folder}}     &lt;$USER&gt;           &lt;time&gt;   R normalsr-exec</terminal-line>
</terminal-window>

To show the status of all your submitted [PBS jobs][PBS job], you can execute the following command:
```
qstat
```

<terminal-window>
    <terminal-line data="input">qstat</terminal-line>
    <terminal-line linedelay=500 class="keep-blanks">Job id                 Name             User              Time Use S Queue</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">---------------------  ---------------- ----------------  -------- - -----</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      {{example_folder}}     &lt;\$USER&gt;           &lt;time&gt;   R normalsr-exec</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;other-job-name&gt; &lt;\$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;other-job-name&gt; &lt;\$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
</terminal-window>

The default name of your job is determined by the `jobname` in the [PBS resources section](#modify-pbs-resources) of the `config.yaml` file (for [this](https://github.com/ACCESS-NRI/access-om3-configs/blob/release-MC_25km_jra_ryf/config.yaml) configuration it is `025km_jra55do_ryf`).

_S_ indicates the status of your run, where:

- _Q_ &rarr; Job waiting in the queue to start
- _R_ &rarr; Job running
- _E_ &rarr; Job ending
- _H_ &rarr; Job on hold

If there are no jobs listed with your `jobname` (or if no job is listed), your run either successfully completed or was terminated due to an error.<br>
For more information, check [NCI documentation](https://opus.nci.org.au/display/Help/FAQ+1%3A+Why+My+Jobs+are+NOT+Running).

!!! tip
    While the model is running, you can monitor its progress by running:
    ```
    tail -f work/log/med.log
    ```

### Stop a run

If you want to manually terminate a run, you can do so by executing:
```
qdel <job-ID>
```
which kills the specified job without waiting for it to complete.


### Error and output log files

#### PBS output files {: .no-toc }
When the model completes a run, PBS writes the standard output and error streams to two files inside the _control_ directory: `<jobname>.o<job-ID>` and `<jobname>.e<job-ID>`, respectively.

These files usually contain logs about _payu_ tasks, and give an overview of the resources used by the job.<br>
To move these files to the `archive` directory, use the following command:
```
payu sweep
```

#### Model log files {: .no-toc }

While the model is running, the model standard output and error streams are saved in the `access-om3.out` and `access-om3.err` files inside the _control_ directory.
The contents of these files show the status of a run as it progresses (or after a failed run has completed).

!!! warning
    At the end of a successful run, these log files are archived to the `archive` directory and will no longer be found in the _control_ directory. If they remain in the _control_ directory after the PBS job for a run has completed, it means the run has failed.

### Troubleshooting

If _payu_ doesn't run correctly for some reason, a good first step is to run the following command from within the _control_ directory:

    payu setup

This command will: 
  
  - create the _laboratory_ and `work` directories based on the experiment configuration
  - generate manifests
  - report useful information to the user, such as the location of the _laboratory_ where the `work` and `archive` directories are located

<terminal-window>
    <terminal-line data="input">payu setup</terminal-line>
    <terminal-line>laboratory path: /scratch/$PROJECT/$USER/access-om3</terminal-line>
    <terminal-line>binary path: /scratch/$PROJECT/$USER/access-om3/bin</terminal-line>
    <terminal-line>input path: /scratch/$PROJECT/$USER/access-om3/input</terminal-line>
    <terminal-line>work path: /scratch/$PROJECT/$USER/access-om3/work</terminal-line>
    <terminal-line>archive path: /scratch/$PROJECT/$USER/access-om3/archive</terminal-line>
    <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
    <terminal-line>Loading restart manifest: manifests/restart.yaml</terminal-line>
    <terminal-line>Loading exe manifest: manifests/exe.yaml</terminal-line>
    <terminal-line>Setting up access-om3</terminal-line>
    <terminal-line>Checking exe and input manifests</terminal-line>
    <terminal-line>Writing manifests/restart.yaml</terminal-line>
    <terminal-line>/usr/bin/bash /g/data/vk83/apps/om3-scripts/payu_config/setup.sh</terminal-line>
</terminal-window>

This can help to isolate issues such as permissions problems accessing files and directories, missing files or malformed/incorrect paths.

----------------------------------------------------------------------------------------

## {{ model }} outputs

At the end of a successful model run, output files, restart files and log files are moved from the `work` directory to the `archive` directory.<br>
Symbolic links to these directories are also provided in the _control_ directory for convenience.

If a model run is unsuccessful, the `work` directory is left untouched to help identify the cause of model failure.

Outputs and restarts are stored in subfolders within the `archive` directory, subdivided for each run of the model.<br>
Output and restart folders are called `outputXXX` and `restartXXX`, respectively, where _XXX_ is the run number starting from `000`.

Model components are separated into subdirectories within the output and restart directories.

<terminal-window>
    <terminal-line data="input">cd ~/access-om3/{{example_folder}}</terminal-line>
    <terminal-line data="input" directory="~/access-om3/{{example_folder}}">ls</terminal-line>
    <terminal-line class="ls-output-format">output000 pbs_logs restart000</terminal-line>
</terminal-window>

----------------------------------------------------------------------------------------

## Edit {{ model }} configuration

This section describes how to modify {{ model }} configuration.<br>
The modifications discussed in this section can change the way {{ model }} is run by _payu_, or how its specific [model components] are configured and coupled together.

The `config.yaml` file located in the _control_ directory is the _payu_ configuration, which controls the configuration of the experiment manager. It contains several parts, some of which it is more likely will need modification, and others which are rarely changed without having a deep understanding of how the model is configured.

To find out more about configuration settings for the `config.yaml` file, refer to [how to configure your experiment with payu](https://payu.readthedocs.io/en/latest/config.html).

### Change run length and restart period

One of the most common changes is to adjust the duration of the model run.<br>
For example, when debugging changes to a model, it is common to reduce the run length to minimise resource consumption and return faster feedback on changes.

The run length and restart period are controlled by a set of parameters in the `CLOCK_attributes` section of the `~/access-om3/{{example_folder}}/nuopc.runconfig` file:

    CLOCK_attributes::
    ﻿     ...
    ﻿     restart_n = 1
         restart_option = nyears
         ...
         stop_n = 1
         stop_option = nyears
         ...
         
The run length is controlled  by`stop_option` and `stop_n`.<br>
Common options for `stop_option` are `ndays`, `nmonths` and `nyears`. `stop_n` provides the numerical count for `stop_option`.

The restart period is controlled by `restart_option` and `restart_n`, which set *how often* restart files are written.<br>
!!! tip
    To be able to resume each run from a previous state, the model must save restart files at the end of each run. To achieve this, the `restart_*` fields should be set as a divisor of the time period defined by the `stop_*` values. For long and stable runs, disk usage can be reduced by pruning older restart files as a _payu_ post-processing step. For details, see [Pruning model restarts](/models/run_a_model/run_access-om3/#pruning-model-restarts).

For example, to run a configuration for 2 months and write restart files at the end of the run, set the following in the `~/access-om3/{{example_folder}}/nuopc.runconfig` file:

    CLOCK_attributes::
    ﻿     ...
    ﻿     restart_n = 2
         restart_option = nmonths
         ...
         stop_n = 2
         stop_option = nmonths
         ...

### Configuring MOM6 diagnostics

MOM6 diagnostic output is configured using the `diag_table` file. However, users should not edit the `diag_table` file directly. Instead, a tool is provided to generate the `diag_table` from an easily editable YAML file. This tool ensures that the `diag_table` requests MOM6 output that is formatted consistently and is suitable for postprocessing (e.g., inclusion in Intake catalogs). 

Preset `diag_table` files, along with the YAML configuration files used to generate them, can be found in the `diagnostic_profiles` subdirectory of _payu_'s _control_ directory. To create and use a custom `diag_table`, follow the instructions in `diagnostic_profiles/README.md`.

!!! warning
    MOM6 provides the ability to vertically remap diagnostics onto user-defined vertical coordinates, including density coordinates (check [MOM6 vertically remapped diagnostics documentation](https://mom6.readthedocs.io/en/main/api/generated/pages/Diagnostics.html#vertically-remapped-diagnostics) for more information). Remapping to density coordinates can add substantially to the runtime of the model. The default `diag_table` used by {{ model }} includes diagnostics remapped to density coordinates. These should be removed for performance reasons if they are not needed.


### Start the run from a specific restart file {: id='specific-restart'}

By default, the configuration will start from a "cold-start", where initial conditions are set based on observations of salinity and temperature, but all other model variables are zero.

To extend or branch off from an existing experiment, the model can be configured to start from an existing restart file.

To do this, add a [`restart:` entry](https://payu.readthedocs.io/en/latest/config.html#miscellaneous) to the `config.yaml` file, specifying the path to a folder containing existing restart files.
Or, to do this automatically when setting up an experiment, add the `-r` flag to the `payu clone` command: 

```
payu clone -b expt -B {{ example_branch }} -r ~/access-om3/prev_expt/archive/restart010 {{ github_configs }} {{example_folder}}
```

<terminal-window>
    <terminal-line data="input" directory="~/{{ model }}">payu clone -b expt -B {{ example_branch }} -r ~/{{ model }}/prev_expt/archive/restart010 {{ github_configs }} {{example_folder}}</terminal-line>
    <terminal-line lineDelay=1000>Cloned repository from {{ github_configs }} to directory: .../{{ model }}/{{example_folder}}</terminal-line>
    <terminal-line>Created and checked out new branch: expt</terminal-line>
    <terminal-line>laboratory path:  /scratch/.../{{ model }}</terminal-line>
    <terminal-line>binary path:  /scratch/.../{{ model }}/bin</terminal-line>
    <terminal-line>input path:  /scratch/.../{{ model }}/input</terminal-line>
    <terminal-line>work path:  /scratch/.../{{ model }}/work</terminal-line>
    <terminal-line>archive path:  /scratch/.../{{ model }}/archive</terminal-line>
    <terminal-line>Updated metadata. Experiment UUID: daeee7ff-07e4-4f93-823b-cb7c6e4bdb6e</terminal-line>
    <terminal-line>Added 'restart: /scratch/.../{{ model }}/archive/prev_expt/restart010' to configuration file: config.yaml</terminal-line>
    <terminal-line>Added archive symlink to /scratch/.../{{ model }}/archive/{{ example_folder }}-expt-daeee7ff</terminal-line>
    <terminal-line data="input" directory="~/{{ model }}">cd {{ example_folder }}</terminal-line>
    <terminal-line data="input" directory="~/{{ model }}/{{ example_folder }}"></terminal-line>
</terminal-window>

!!! warning
    Note that the restart flag used here will only be applied if there is no restart directory in archive, and so does not have to be removed for subsequent submissions. See [Payu docs](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) for further details.


### Modify PBS resources

If the model configuration has been altered and the experiment needs: more time to complete, more memory, or to be submitted under a different NCI project; the following section in the config.yaml requires modification:

```yaml
# If submitting to a different project to your default, uncomment line below
# and replace PROJECT_CODE with appropriate code. This may require setting shortpath
# project: PROJECT_CODE

# Force payu to always find, and save, files in this scratch project directory
# shortpath: /scratch/PROJECT_CODE

queue: normal
ncpus: 240
jobfs: 10GB
mem: 960GB

walltime: 02:00:00
```

These lines can be edited to change the [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained) for the [PBS job][PBS job].

For example, to run {{ model }} under the `ol01` project (COSIMA Working Group), uncomment the line beginning with `# project` by deleting the `#` symbol and replace `PROJECT_CODE` wih `ol01`:

```yaml
project: ol01
```

To use a `/scratch` storage allocation other than `project` (or your default if `project` is not set) then also set `shortpath` (e.g. to the desired `/scratch/PROJECT_CODE`). 


!!! warning
    If changing projects during an experiment, set the `shortpath` field so that it's consistent for all runs of an experiment.
    Doing this will make sure the same `/scratch` location is used for the _laboratory_, regardless of which project is used to run the experiment.
    <br><br>

### Syncing output data

The _laboratory_ directory is typically under the `/scratch` storage on _Gadi_, files on `/scratch` storage [are regularly deleted once they have not been accessed for a period of time](https://opus.nci.org.au/pages/viewpage.action?pageId=156434436). For this reason, it is recommended to move climate model outputs to a location with long-term storage.<br>
On _Gadi_, this is typically in a folder under a project code on `/g/data`.  

_Payu_ has built-in support to sync outputs, restarts and a copy of the _control_ directory `git` history to another location.<br>
This feature is controlled by the following section in the `config.yaml` file: 
```yaml
# Sync options for automatically copying data from ephemeral scratch space to 
# longer term storage
sync:
    enable: False # set path below and change to true
    restart: True
    path: none # Set to location on /g/data or a remote server and path (rsync syntax)
```
To enable syncing, change `enable` to `True`, and set `path` to a location on `/g/data`, where _payu_ will copy output and restart folders. A sensible `path` could be: `/g/data/$PROJECT/$USER/{{ model }}/experiment_name/`.

### Pruning model restarts

By default, {{ model }} saves restart files after each run, allowing subsequent simulations to resume from a previously saved model state. The default {{ model }} run length and restart period can be changed (see [Change run length and restart period](#change-run-length-and-restart-period)).<br>
However, restart files can occupy significant disk space, and keeping all of them throughout an entire experiment is often not necessary. If disk space is limited, consider using _payu_'s restart files pruning feature, controlled by the `restart_freq` field of the `config.yaml`.
By default, every `restart_freq` _payu_ removes intermediate restart files, keeping only: 
- the two most recent restarts
- restarts corresponding to the `restart_freq` interval
For example, a `restart_freq` set to `1YS` would keep the restart files at the end of each model year, whereas `restart_freq` set to `5YS` would keep those at the end of every fifth model year.
This approach helps reduce disk space while maintaining useful restart points across long experiments, especially useful in case of unexpected crashes.


The `restart_freq` field in the `config.yaml` can either be a number (in which case every _nth_ restart file is retained), or one of the following pandas-style datetime frequencies:

- `YS` &rarr; start of the year
- `MS` &rarr; start of the month
- `D` &rarr; day
- `H` &rarr; hour
- `T` &rarr; minute
- `S` &rarr; second

For example, to preserve the ability to restart {{ model }} every 50 model-years, set:
```yaml
restart_freq: '50YS'
```

The most recent sequential restarts are retained, and only deleted after a permanently archived restart file has been produced.

For more information, check [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/latest/config.html#model).


### Other configuration options

!!! warning
    The following sections in the `config.yaml` file control configuration options that are rarely modified, and often require a deeper understanding of how {{ model }} is structured to be safely changed.

#### Model configuration {: .no-toc }

This section tells _payu_ which driver to use for the main model configuration (`access-om3`) and the location of all input files.

```yaml
model: access-om3

exe: access-om3-MOM6-CICE6
input:
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/cice/grids/global.25km/2025.02.17/kmt.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/mosaic/global.25km/2025.01.30/ocean_hgrid.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/vertical/global.25km/2025.03.12/ocean_vgrid.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/initial_conditions/global.25km/2025.03.19/ocean_temp_salt.res.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/surface_salt_restoring/global.25km/2025.01.30/salt_sfc_restore.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/share/grids/global.25km/2025.02.17/topog.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/global.25km/2025.02.17/access-om3-25km-ESMFmesh.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/global.25km/2025.02.17/access-om3-25km-nomask-ESMFmesh.nc
    - /g/data/vk83/configurations/inputs/access-om3/share/meshes/share/2024.09.16/JRA55do-datm-ESMFmesh.nc
    - /g/data/vk83/configurations/inputs/access-om3/share/meshes/share/2024.09.16/JRA55do-drof-ESMFmesh.nc
    - /g/data/vk83/prerelease/configurations/inputs/access-om3/cmeps/remap_weights/global.25km/2025.02.17/access-om3-25km-rof-remap-weights.nc
    - /g/data/vk83/experiments/inputs/JRA-55/RYF/v1-4/data
```

#### Runlog {: .no-toc }

```yaml
runlog: true
```
When running a new configuration, _payu_ automatically commits changes with `git` if `runlog` is set to `true`.

!!! warning
    This should not be changed as it is an essential part of the provenance of an experiment.<br>
    _payu_ updates the manifest files for every run, and relies on `runlog` to save this information in the `git` history, so there is a record of all inputs, restarts and executables used in an experiment.

#### Userscripts {: .no-toc }

```yaml
userscripts:
    setup: /usr/bin/bash /g/data/vk83/apps/om3-scripts/payu_config/setup.sh
    archive: /usr/bin/bash /g/data/vk83/apps/om3-scripts/payu_config/archive.sh
```

Can specify run scripts or subcommands to be run at various stages of a _payu_ submission.

- `setup` gets called if after model setup, but prior to model execution.
- `archive` gets called after the model execution, but prior to model output archive.
  
For more information about specific `userscripts` fields, check the relevant section of [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/latest/config.html#postprocessing).

### Create a custom {{ model }} build
All the executables needed to run {{ model }} are pre-built using _Spack_.<br>
To customise {{ model }}'s build (for example, to run {{ model }} with changes in the source code of one of its component), refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code#{{model|lower}}).
## Get Help

For further {{ model }} assistance, have a look at [general guidance](/about/user_support/#still-need-help) on how to request help from ACCESS-NRI. Specifically, consider creating a topic in the [COSIMA category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/cosima/29). In the case of a configuration bug, please file a [GitHub issue here](https://github.com/ACCESS-NRI/access-om3-configs/issues/new?assignees=&labels=External&projects=&template=blank.md&title=). <br>

<custom-references>
- [https://cosima.org.au](https://cosima.org.au)
- [https://payu.readthedocs.io/en/latest/usage.html](https://payu.readthedocs.io/en/latest/usage.html)
- [https://github.com/access-nri/access-om3](https://github.com/access-nri/access-om3)
- [https://opus.nci.org.au/](https://opus.nci.org.au/)
</custom-references>
