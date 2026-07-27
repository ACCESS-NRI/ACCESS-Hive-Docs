[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[Run a Model]: /models/run_a_model/index.md

# Run models using payu

## About

[_payu_](https://github.com/payu-org/payu) is a workflow manager tool for running numerical models in supercomputing environments. It is an open-source software, distributed under an Apache 2.0 Licence.

This page summarises the _payu_ capabilities that are most commonly required to run an ACCESS model's configuration on the _Gadi_ supercomputer. This page presents generic information on: 

- the setup of _payu_
- running _payu_-based ACCESS model's configurations
- monitoring a _payu_-based experiment on _Gadi_
- modifying a _payu_-based configurations for the most commonly customised aspects of the configurations
- the data organisation for a _payu_-based experiment

This page is to be used in conjunction with the Run a Model page for the chosen configuration. The Run a Model page will give information specific to that model (for example, additional requirements or configuration names and locations) as well as any information on any configurations customisation that is particular to that model.

There is also [technical documentation](https://payu.readthedocs.io/en/latest/) for how to configure _payu_. 

## Prerequisites

- **NCI account**<br>
    Before running an ACCESS model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Payu setup

_Payu_ on _Gadi_ is available through a dedicated `conda` environment in the _vk83_ project.<br>
After joining the _vk83_ project, load the `payu` module:

    module use /g/data/vk83/modules
    module load payu

To check that _payu_ is available, run:

    payu --version
    
## Get the model configuration

All model configurations are hosted on GitHub.<br>

The first step is to choose a configuration from those available and identify the branch name for that configuration, following information on the [Run a Model][Run a Model] page of your chosen model.<br>

Once you have chosen the configuration, you need to:

- identify the `<repository>` and `<branch>` name the configuration is stored under on GitHub.
- decide on a directory on Gadi to store your _payu_ configurations, `<configurations-directory>` (this directory must exist before running _payu_)
- decide on a name for your experiment, `<experiment-name>`
- decide on a directory name to store this specific configuration, `<control-directory>` (created by _payu_)

Then, you can get the chosen configuration using `payu clone`.

For example, say you want to do a sensitivity experiment to the diffusivity in ACCESS-OM2 using the configuration `release-1deg_jra55_ryf`. You decide to:

- `<repository>` and `<branch>`: base your experiment off the branch, `release-1deg_jra55_ryf`, from the repository, https://github.com/ACCESS-NRI/access-om2-configs
- `<configurations-directory>`: store the configurations under `~/access-om2/`
- `<experiment-name>`: name your experiment `diff_test1-1deg_jra55_ryf`
- `<control-directory>`: store the configuration under `diff_exps-1deg_jra55_ryf`

To get the configuration as chosen, run:
    
    mkdir -p ~/access-om2/
    cd ~/access-om2/
    payu clone -b diff_test1-1deg_jra55_ryf -B release-1deg_jra55_ryf https://github.com/ACCESS-NRI/access-om2-configs diff_exps-1deg_jra55_ryf
    cd diff_exps-1deg_jra55_ryf

!!! tip
    Anyone using a configuration is advised to clone only a single branch (as shown in the example above) and not the entire repository.

!!! tip
    _payu_ uses branches to differentiate between different experiments in the same local git repository.<br>
    For this reason, it is recommended to always set the cloned branch name, `<experiment_name>` (`diff_test1-1deg_jra55_ryf` in the example above), to something meaningful for the planned experiment.<br>
    For more information refer to this [payu tutorial](https://forum.access-hive.org.au/t/access-om2-payu-tutorial/1750#select-experiment-12).

## Directory structure for _payu_-supported model runs

The general layout of a _payu_-supported model run consists of two main directories:

- The _control_ directory contains the model configuration and serves as the execution directory for running the model. You created the _control_ directory when you cloned the configuration you want to use.
- The _laboratory_ directory, where all the model components reside. It is typically `/scratch/$PROJECT/$USER/<model_name>` and is created by _payu_. `$PROJECT` and `$USER` are environment variables on _Gadi_ that points to your default project and your username respectively.

This separates the small text configuration files from the larger binary outputs and inputs. In this way, the _control_ directory can be in the `$HOME` directory (as it is the only filesystem actively backed-up on _Gadi_). The quotas for `$HOME` are low and strict, which limits what can be stored there, so it is not suitable for larger files.

The _laboratory_ directory is a shared space for a user's _payu_ experiments using the same model. Inside the _laboratory_ directory there are two areas:

- `work` &rarr; for temporary storage of files needed by the model while it runs. _payu_ creates and removes directories and files in this directory upon successful completion of runs.
- `archive` &rarr; for storing the output following each successful run.

Within each of the above directories, _payu_ automatically creates subdirectories uniquely named according to the experiment being run.<br>
_Payu_ also creates symbolic links in the _control_ directory pointing to the `archive` and `work` directories.

This design allows multiple self-resubmitting experiments that share common executables and input data to be run simultaneously.

!!! warning
    Files on the `/scratch` drive, such as the _laboratory_ directory, might get deleted if not accessed for several days and the `/scratch` drive is limited in space. For these reasons, all model runs which are to be kept should be moved to `/g/data/` by enabling the `sync` step in _payu_. To know more refer to [Syncing output data](#syncing-output-data).

!!! info
    `payu` will create all the directories it needs. They do not need to be created beforehand.

## Run the configuration

_payu_ manages the experiment through a [PBS job][PBS job] that it self-submits.

To run a configuration, execute the following command from within the *control* directory:

    payu run

This will submit a single job to the queue. Refer to the [Run a Model][Run a Model] page for your chosen model to learn how to set the length of the simulation.

!!! tip
    `payu run` will error out if a non-empty `work` directory for your experiment already exists (from a failed attempt or from running `payu setup`).<br>
    You can add the `-f` option to `payu run` to let the model run in all cases and delete any existing data under `work`.

## Run an experiment

An experiment consists of a series of subsequent runs with each run continuing from where the previous one ended.
To conduct an experiment, use the `-n` option to submit a series of runs until the desired length of the experiment is reached:

    payu run -n <number-of-runs>

This will run the configuration `number-of-runs` consecutive times for the configured run length. This way, the *total experiment length* will be `run-length * number-of-runs`. 

For example, to run an experiment for a total of 50 years with a default run length of 5 years, the `number-of-runs` should be set to `10`:

    payu run -n 10

## Monitor the experiment

_payu_ provides the `payu status` command for monitoring jobs (see [documentation](https://payu.readthedocs.io/en/1.2.0/usage.html#monitoring-payu-jobs)). This command can return the scheduler job ID, and the stage the payu run is currently at. When the job is complete, it displays the exit statuses from the model and overall payu run, and points to the PBS log files. 

!!! note
   `payu status` is available in _payu_ versions 1.2.0 and later. This command does not yet support monitoring post-processing jobs from the configuration, e.g. `payu collate` and `payu sync`.


You can also use the PBS `job-ID` to monitor the job using the PBS commands available from NCI. 

To print out information on the status of a specific job, you can execute the following command:
```
qstat <job-ID>
```
<terminal-window>
    <terminal-line data="input">qstat &lt;job-ID&gt;</terminal-line>
    <terminal-line linedelay=500 class="keep-blanks">Job id                 Name             User              Time Use S Queue</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">---------------------  ---------------- ----------------  -------- - -----</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;control_directory_name&gt;   &lt;$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
</terminal-window>

To show the status of all your submitted [PBS jobs][PBS job], you can execute the following command:
```
qstat
```

<terminal-window>
    <terminal-line data="input">qstat</terminal-line>
    <terminal-line linedelay=500 class="keep-blanks">Job id                 Name             User              Time Use S Queue</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">---------------------  ---------------- ----------------  -------- - -----</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;job-name&gt;   &lt;\$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;job-name&gt; &lt;\$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
    <terminal-line linedelay=0 class="keep-blanks">&lt;job-ID&gt;.gadi-pbs      &lt;job-name&gt; &lt;\$USER&gt;           &lt;time&gt;   R normal-exec</terminal-line>
</terminal-window>

The default name of your job is the name of the _payu_ _control_ directory.<br>
This can be changed by altering the `jobname` in the [PBS resources section](#modify-pbs-resources) of the `config.yaml` file.

_S_ indicates the status of your run, where:

- _Q_ &rarr; Job waiting in the queue to start
- _R_ &rarr; Job running
- _E_ &rarr; Job ending
- _H_ &rarr; Job on hold

If there are no jobs listed with your `jobname` (or if no job is listed), your run either successfully completed or was terminated due to an error.<br>
For more information, check [NCI documentation](https://opus.nci.org.au/display/Help/FAQ+1%3A+Why+My+Jobs+are+NOT+Running).

### Stop a run

If you want to manually terminate a run, you can do so by executing:
```
qdel <job-ID>
```
which kills the specified job without waiting for it to complete.

!!! tip
    If you specified you want the job to resubmit itself several times but want to stop after the completion of the current process, you can create a file called `stop_run` in the _control_ directory.<br>
    This will prevent _payu_ from submitting another job.

### Error and output log files

#### PBS output files {: .no-toc }
When the model completes a run, PBS writes the standard output and error streams to two files inside the _control_ directory: `<jobname>.o<job-ID>` and `<jobname>.e<job-ID>`, respectively.

These files usually contain logs about _payu_ tasks, and give an overview of the resources used by the job.<br>
To move these files to the `archive` directory, use the following commmand:
```
payu sweep
```

#### Model log files {: .no-toc }

While the model is running, _payu_ saves the model standard output and error streams in the _control_ directory. Refer to the [Run a Model][Run a Model] page for the model you are using for the list of logging filenames for your model.<br>
You can examine the contents of these files to check on the status of a run as it progresses (or after a failed run has completed).

!!! warning
    At the end of a successful run these log files are archived to the `archive` directory and will no longer be found in the _control_ directory. If they remain in the _control_ directory after the PBS job for a run has completed, it means the run has failed.

### Trouble-shooting

If _payu_ doesn't run correctly for some reason, a good first step is to run the following command from within the _control_ directory:

    payu setup

This command will: 
  
  - create the _laboratory_ and `work` directories based on the experiment configuration
  - generate manifests
  - report useful information to the user, such as the location of the _laboratory_ where the `work` and `archive` directories are located

<terminal-window>
    <terminal-line data="input">payu setup</terminal-line>
    <terminal-line>laboratory path: /scratch/\$PROJECT/\$USER/access-om2</terminal-line>
    <terminal-line>binary path: /scratch/\$PROJECT/\$USER/access-om2/bin</terminal-line>
    <terminal-line>input path: /scratch/\$PROJECT/\$USER/access-om2/input</terminal-line>
    <terminal-line>work path: /scratch/\$PROJECT/\$USER/access-om2/work</terminal-line>
    <terminal-line>archive path: /scratch/\$PROJECT/\$USER/access-om2/archive</terminal-line>
    <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
    <terminal-line>Loading restart manifest: manifests/restart.yaml</terminal-line>
    <terminal-line>Loading exe manifest: manifests/exe.yaml</terminal-line>
    <terminal-line>Setting up atmosphere</terminal-line>
    <terminal-line>Setting up ocean</terminal-line>
    <terminal-line>Setting up ice</terminal-line>
    <terminal-line>Setting up access-om2</terminal-line>
    <terminal-line>Checking exe and input manifests</terminal-line>
    <terminal-line>Updating full hashes for 3 files in manifests/exe.yaml</terminal-line>
    <terminal-line>Creating restart manifest</terminal-line>
    <terminal-line>Writing manifests/restart.yaml</terminal-line>
    <terminal-line>Writing manifests/exe.yaml</terminal-line>
</terminal-window>

This can help to isolate issues such as permissions problems accessing files and directories, missing files or malformed/incorrect paths.

## Outputs organisation

At the end of a successful model run, output files, restart files and log files are moved from the `work` directory to the `archive` directory.<br>
Symbolic links to these directories are also provided in the _control_ directory for convenience.

If a model run is unsuccessful, the `work` directory is left untouched to facilitate the identification of the cause of the model failure.

Outputs and restarts are stored in subfolders within the `archive` directory, subdivided for each run of the model.<br>
Output and restart folders are called `outputXXX` and `restartXXX`, respectively, where _XXX_ is the run number starting from `000`.

Model components are separated into subdirectories within the output and restart directories.

## Edit a _payu_ configuration

The modifications discussed in this section can change how the model and its components are configured, or the way the model is run by _payu_.

The `config.yaml` file located in the _control_ directory is the _payu_ configuration file, which controls the general model configuration. It contains several parts, some of which it is more likely will need modification, and others which are rarely changed without having a deep understanding of how the model is configured.

To find out more about configuration settings for the `config.yaml` file, refer to [how to configure your experiment with payu](https://payu.readthedocs.io/en/latest/config.html).

### Change run length

_Gadi_ imposes a maximum wall time for submitted jobs. This means most experiments need several jobs to simulate the total time required.<br>
As seen previously in [Run an experiment](#run-an-experiment), _payu_ handles this by splitting a simulation in sections and automatically running each section one after the other in separate jobs. As such the total run length is the product of:

- the run length of each individual submission. This is set differently depending on the model, so refer to the [Run a Model][Run a Model] page for details. It is important to set this run length so that the simulation finishes within the maximum wall time for the job (set with the `walltime` entry in the `config.yaml` file) and for the queue (refer to [NCI's documentation](https://opus.nci.org.au/spaces/Help/pages/236881198/Queue+Limits...)).
- the number of automatic resubmissions by _payu_. This is set through the command line option `-n`. It defaults to 1 and there is no limit on this number.

### Start the run from a specific restart file {: id='specific-restart'}

To configure the experiment to start from specific restart files, add a [`restart:` entry](https://payu.readthedocs.io/en/latest/config.html#miscellaneous) to the `config.yaml` file, specifying the path to a folder containing existing restart files.
Or, to do this automatically when setting up an experiment, add the `-r` flag to the `payu clone` command. 

!!! warning
    In some cases, if the supplied restart file is not fully compatible with the model configuration, experiments using a custom restart file may require additional manual adjustments to run correctly.

!!! warning
    The restart option used here will only be applied if there is no restart directory in archive, and so does not have to be removed for subsequent submissions. See [Payu docs](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) for further details.

### Modify PBS resources

If the model has been altered and needs more time or memory to complete, or needs to be submitted under a different NCI project, you will need to modify the following options in the `config.yaml`:

```yaml
# If submitting to a different project to your default, uncomment line below
# and replace PROJECT_CODE with appropriate code. This may require setting shortpath
# project: PROJECT_CODE

# Force payu to always find, and save, files in this scratch project directory
# shortpath: /scratch/PROJECT_CODE

queue: normal
walltime: 3:00:00
mem: 1000GB
jobname: 1deg_jra55_ryf
```

These lines can be edited to change the [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained) for the [PBS job][PBS job].

For example, to run under the `ol01` project (COSIMA Working Group), uncomment the line beginning with `# project` by deleting the `#` symbol and replace `PROJECT_CODE` with `ol01`:

```yaml
project: ol01
```

For model configurations and output to be saved to a `/scratch` storage allocation other than `project` (or your default if `project` is not set) then also set `shortpath` to the desired path. 

!!! warning
    If changing the project providing the compute resources during an experiment, set the `shortpath` field so that it's the same for all runs of an experiment.
    Doing this will make sure the same `/scratch` location is used for the _laboratory_, regardless of which project is used to run the experiment.

### Syncing output data to long-term storage

The _laboratory_ directory is typically under the `/scratch` storage on _Gadi_, where [files are regularly deleted once they have been unaccessed for a period of time](https://opus.nci.org.au/pages/viewpage.action?pageId=156434436). For this reason climate model outputs need to be moved to a location with longer term storage.<br>
On _Gadi_, this is typically in a folder under a project code on `/g/data`.  

_Payu_ has built-in support to sync outputs, restarts and a copy of the _control_ directory git history to another location.<br>
This feature is controlled by the following section in the `config.yaml` file: 
```yaml
# Sync options for automatically copying data from ephemeral scratch space to 
# longer term storage
sync:
    enable: False # set path below and change to true
    restart: True
    path: none # Set to location on /g/data or a remote server and path (rsync syntax)
    exclude:
      - '*.nc.*'
      - 'iceh.????-??-??.nc'
```
To enable syncing, change `enable` to `True`, and set `path` to a location on `/g/data`, where _payu_ will copy output and restart folders. A sensible `path` could be: `/g/data/$PROJECT/$USER/<model>/experiment_name/`.

### Pruning model restarts

By default, restart files are created at the end of each run, allowing subsequent simulations to resume from a previously saved model state. However, restart files can occupy significant disk space, and keeping all of them throughout an entire experiment is often not necessary. 

If disk space is limited, consider using _payu_'s restart files pruning feature, controlled by the `restart_freq` field of the `config.yaml`.
By default, every `restart_freq`, _payu_ removes intermediate restart files, keeping only:

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

For example, to preserve the ability to restart the model every 50 model-years, set:
```yaml
restart_freq: '50YS'
```

The most recent sequential restarts are retained, and only deleted after a permanently archived restart file has been produced.

!!! note
    If `restart_freq` is not a multiplier of the model's restart frequency, _payu_ will keep the first restart passed `restart_freq`. For example, a model is set to write restart files every 3 years and produces restarts on the following dates:

    - restart000: 01/01/2000  
    - restart001: 01/01/2003  
    - restart002: 01/01/2006  
    - restart003: 01/01/2009  
    - restart004: 01/01/2012  
    - restart005: 01/01/2015

    If `restart_freq` is set to `5YS` (5 years), _payu_ will keep:

    - restart000: 01/01/2000  
    - restart002: 01/01/2006 (first restart >= 01/01/2005)  
    - restart004: 01/01/2012 (first restart >= 01/01/2011)  
    - restart005: 01/01/2015 (keeps immediate restarts < 01/01/2017)  

For more information, check [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/latest/config.html#model).

### Other configuration options

!!! warning
    The following sections in the `config.yaml` file control configuration options that are rarely modified, and often require a deeper understanding of how the model is structured to be safely changed.

#### Model configuration {: .no-toc }

This section tells _payu_ which driver to use for the main `model` configuration and the location of all `input` files that are common to all its model components.

```yaml
name: common
model: access-om2
input: /g/data/ik11/inputs/access-om2/input_20201102/common_1deg_jra55
```

The `name` field, for the model section, is not actually used for the configuration run, so it can be safely ignored. The `name` field is used for submodels (see below).

#### Submodels {: .no-toc }

Coupled models deploy multiple submodels, a.k.a. the model components.

This section of the _payu_ configuration file specifies the submodels, the configuration options required to execute the model correctly and the location of all inputs required for this submodel.

Each submodel contains additional configuration options that are read in when the submodel is running. These options are specified in the subfolder of the _control_ directory whose name matches the submodel's `name` (e.g., configuration options for the `ocean` submodel are in the `ocean` sub-directory).

Refer to the [Run a Model][Run a Model] page of a chosen model for details of the submodels' configurations used by this model.

#### Runlog {: .no-toc }

```yaml
runlog: true
```
When running a new configuration, _payu_ automatically commits changes with _git_ if `runlog` is set to `true`.

!!! warning
    This should not be changed as it is an essential part of the provenance of an experiment.<br>
    _payu_ updates the manifest files for every run, and relies on `runlog` to save this information in the _git_ history, so there is a record of all inputs, restarts, and executables used in an experiment.

#### Userscripts {: .no-toc }

```yaml
userscripts:
    error: tools/resub.sh
    run: rm -f resubmit.count
    sync: /g/data/vk83/apps/om2-scripts/concatenate_ice/concat_ice_daily.sh 
```

A dictionary to run scripts or subcommands at various stages of a _payu_ submission:

- `error` gets called if the model does not run correctly and returns an error code.
- `run` gets called after the model successful execution, but prior to model output archive.
- `sync` gets called at the start of the sync pbs job. For more information refer to [Syncing output data](#syncing-output-data).
  
For more information about specific `userscripts` fields, check the relevant section of [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/latest/config.html#postprocessing).

## Edit a model components' configuration

Each of the model components contains additional configuration options that are read in when the model component is running.<br>
These options are typically useful to modify the physics used in the model, the input data, or the model variables saved in the output files.

These configuration options are specified in files located inside a subfolder of the _control_ directory, named according to the submodel's `name` specified in the `config.yaml` `submodels` section (e.g., configuration options for the _ocean_ component are in the `ocean` sub-directory).<br>
To modify these options please refer to the User Guide of the respective model component.
