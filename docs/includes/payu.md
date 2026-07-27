[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[Run a Model]: /models/run_a_model

# Run Models Using Payu

## About

<!--start:about-->
[_payu_](https://github.com/payu-org/payu) is a workflow manager tool for running numerical models in supercomputing environments. It is an open-source software, distributed under an Apache 2.0 Licence.

For in-depth information about _payu_, check its [technical documentation](https://payu.readthedocs.io/en/stable/). 

### Terminology

Before explaining how _payu_ works for the ACCESS models, it is worth explaining the difference between configurations and experiments as well as the terminology for the data organisation for _payu_'s experiments.

#### Configuration versus experiment

The terms _configuration_ and _experiment_ are not interchangeable although they are closely related.

A _configuration_ defines a specific way to run the model it relates to. 
A configuration is defined by:

- model version and build (model executable(s))
- set of input files (ancillaries, forcings, restarts)
- set of physical and modelling options for each model component, such as namelists, configuration files and MPI layout

Changing any one of these elements creates a new configuration

An _experiment_ is a realisation of a configuration: a series of sequential runs that generate model data over a span of model time.

#### Data organisation and _payu_'s directories designation

!!! info
    _payu_ creates all the directories it needs. Therefore, they do not need to be created beforehand.

The data organisation for _payu_ was chosen to separate the smaller text files that define a _configuration_ and the larger binary input and output files needed for an _experiment_. 

This means the _configuration_ definition can be tracked with git, and so is easy to back up and share.  It also optimises the use of different filesystems on high-performance computers. Finally, this layout ensures several _experiments_ that share common executables and input data can be run simultaneously.  

A representation of the data organisation for _payu_ is given in the following diagram:

<!-- Diagram created from Lucid chart: https://lucid.app/users/login#/login -->
<!-- It can be edited by any Lucid's member (free account), at this link: https://lucid.app/lucidchart/ccebf957-8915-4344-a832-426427451c00/edit?viewport_loc=-159%2C129%2C2067%2C1113%2C0_0&invitationId=inv_1c8cccfd-b20e-4b2f-977a-a74b0b8355ae -->

![payu directory structure](/assets/payu_directory_structure.svg){: class="example-img" loading="lazy"}

As shown in the diagram, the general layout of a _payu_-supported model run consists of two main directories:

- The _control_ directory contains the model configuration and is the directory from which the model run is started.  
  This directory contains information to manage the simulation and the scientific options that define the algorithms used in the model component or the diagnostics saved by the model component. The simulation is orchestrated from a main `config.yaml` file contained in this directory. The files specific to each model component are either located directly in the _control_ directory if the model has one model component, or in subdirectories if the model has several model components. The `submodels` section of the `config.yaml` file specifies the name of the submodels and of the subdirectories containing the pertinent files. To modify these options please refer to the configurations documentation of the respective model component.
- The _laboratory_ directory contains all data from _payu_ experiments of the same model. By default, it is `/scratch/$PROJECT/$USER/<model_name>`. `$PROJECT` and `$USER` are environment variables on _Gadi_ that points to your [default project](/getting_started/set_up_nci_account/#change-default-project-on-gadi) and your username respectively. This location can be changed.
<!--See the section on [modifying the PBS resources](#modify-pbs-resources) to learn how to change the _laboratory_ location. (Should the include be cut to allow adding this sentence and link?)-->

!!! tip

    On _Gadi_, it is good practice to put experiment _control_ directories in your `$HOME` directory as this is the only filesystem that is actively backed-up. There is a 10GB limit for home directories, but the _control_ directory only contains text files and symlinks, and so uses relatively little space (<1MB). The _laboratory_ directory is on `/scratch` which is optimised for fast reading and writing of large data and where there is adequate space available for large model output.

    If you decide to locate your _control_ directory under `/g/data`, be aware of [some complications](https://forum.access-hive.org.au/t/changing-project-codes-for-payu-control-directories-under-g-data/6566) linked to that choice.

Inside the _laboratory_ directory, there are two subdirectories of particular interest: 

- _work_ &rarr; for temporary storage of files needed by the model while it runs. _payu_ creates and removes directories and files in this directory upon successful completion of runs. It is left untouched in case of error to facilitate the identification of the cause of the model failure
- _archive_ &rarr; for storing the output following each successful run. The output, log and restart files are automatically transferred from _work_ to _archive_ upon successful completion of runs.

The _archive_ and _work_ directories for an experiment are most easily accessed through the symbolic links created in the _control_ directory.

!!! warning
    Files on the `/scratch` drive, such as the _laboratory_ directory, might be deleted if not accessed for several days. All experiments which are to be kept should be moved to `/g/data/` by enabling the `sync` step in _payu_.

##### Output and restart files organisation

Within each of the _work_ and _archive_ directories, _payu_ automatically creates a unique subdirectory for each experiment. Within each experiment subdirectory, the output and restart subfolders are called `outputXXX` and `restartXXX`, respectively, where _XXX_ is the run number starting from `000`. Model components are further separated into subdirectories within the output and restart directories.

##### Error and output log files

**PBS output files**

When the model fails or completes a run, PBS writes the standard output and error streams to two files inside the _control_ directory: `<jobname>.o<job-ID>` and `<jobname>.e<job-ID>`, respectively.

These files usually contain logs about _payu_ tasks, and give an overview of the resources used by the job.<br>
To move these files to the _archive_ directory, use the following commmand:

```
payu sweep
```

**Model log files**

While the model is running, the standard output and error streams are saved to file in the _control_ directory. You can examine the contents of these log files to check on the status of a run as it progresses (or after a failed run has completed).

!!! warning
    At the end of a successful run, the model log files are archived to the _archive_ directory and will no longer be found in the _control_ directory. If they remain in the _control_ directory after the PBS job for a run has completed, it means the run has failed.

<!--end:about-->

## Prerequisites for _payu_

- **NCI account**<br>
    Before running a _payu_ experiment, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Join NCI projects**<br>
    Join the following project by requesting membership on its NCI project page:

<!--start:projects-->
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
<!--end:projects-->
    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

    !!! warning
        Different model configurations will likely require you to **join additional projects**. Please refer to the [Run a Model][Run a Model] page of your chosen model for the list of additional projects.

<!--start:access-payu-->
### Accessing _payu_

_Payu_ on _Gadi_ is available through a dedicated environment in the _vk83_ project.<br>
After joining the _vk83_ project, load the _payu_ module:

    module use /g/data/vk83/modules
    module load payu

To check that _payu_ is available, run:

    payu --version
<!--end:access-payu-->

## Run an experiment

### Get the model configuration

<!--start:get-config-payu-->
To get a local copy of a configuration, you need to:

- Know the `<repository>` and `<branch>` name the configuration is stored under on GitHub. 
- Create where on Gadi to store all your _payu_ experiments, `<configurations-directory>`, typically a folder under `$HOME`. This directory must exist before running _payu_.
- Choose a directory name to store the experiment, `<control-directory>` (created by _payu_). The `control` directory is a git repository. Experiments are saved as branches in this repository, making it possible to use the same `control` directory for several experiments. For this reason, we recommend to always set the `<local-branch>`. For more information refer to this [payu tutorial](https://forum.access-hive.org.au/t/access-om2-payu-tutorial/1750#select-experiment-12).
- Choose a name for your experiment, `<local-branch>`. It is recommended to choose a descriptive name, specific to your experiment. Note that the experiment name will be formed using the _control_ directory's name and this `<local-branch>` name.

Then, you can get the chosen configuration using `payu clone`.
<!--end:get-config-payu-->

<!--start:payu-clone-example-->
For example, if you want to do a sensitivity experiment in {{model}} using the configuration {{config_example}}. You decide the following:

- `<repository>` and `<branch>`: base your experiment off the branch, {{config_example}}, from the repository, {{github_configs}}
- `<configurations-directory>`: store all your {{model}} configurations under `~/{{model}}/`
- `<local-branch>`: name your branch `expt1`. For a real case, a more explicit name is recommended.
- `<control-directory>`: store the configurations for this research project under `my-project-expts`. For a real case, a more explicit name is recommended.

To get the configuration as chosen, run:

<terminal-window>
    <terminal-line data="input">mkdir -p ~/{{model}}/</terminal-line>
    <terminal-line data="input">cd ~/{{model}}/</terminal-line>
    <terminal-line data="input">payu clone</terminal-line>
    <terminal-line><span class="payu-yellow">Welcome to the Payu Clone Wizard!</span></terminal-line>
    <terminal-line><span class="payu-yellow">Press 'Ctrl+C' at any time to exit.</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Please enter the URL of the repository, or the local path of a configuration you want to clone:</span>  (e.g., https://github.com/payu-org/bowl1.git or /path/to/local/experiment; 'Tab' to browse, '/' to enter folder) <span class="payu-dark-yellow"> {{github_configs}}</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Do you want to clone the repo based on:</span> <span class="payu-dark-yellow">An existing branch</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Please enter the name of the branch you want to clone ('Tab' to browse all branches):</span> <span class="payu-dark-yellow">{{config_example}}</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">How would you like to name your local experiment directory?</span> <span class="payu-dark-yellow"> my-project-expts</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu red">Is this a new experiment?</span> (If yes, payu will create a new branch.) <span class="payu-dark-yellow">Yes</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">What would you like to name your new branch</span>  (Note: this won't be shared to the online repository automatically) <span class="payu-dark-yellow">expt1</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Do you want to specify a custom restart path? (If no, the default restart/initial conditions will be used.)</span> <span class="payu-dark-yellow">No</span></terminal-line>
    <terminal-line><span class="payu-yellow">Running command:</span></terminal-line>
    <terminal-line><span class="payu-yellow">\`payu clone -B {{config_example}} -b expt1 {{github_configs}} my-project-expts\`</span></terminal-line>
    <terminal-line>Cloned repository from {{github_configs}} to directory: /home/561/\$USER/payu-control/{{model}}/my-project-expts</terminal-line>
    <terminal-line>Created and checked out new branch: expt1</terminal-line>
    <terminal-line>laboratory path:  /scratch/\$PROJECT/\$USER/{{model}}</terminal-line>
    <terminal-line>binary path:  /scratch/\$PROJECT/\$USER/{{model}}/bin</terminal-line>
    <terminal-line>input path:  /scratch/\$PROJECT/\$USER/{{model}}/input</terminal-line>
    <terminal-line>work path:  /scratch/\$PROJECT/\$USER/{{model}}/work</terminal-line>
    <terminal-line>archive path:  /scratch/\$PROJECT/\$USER/{{model}}/archive</terminal-line>
    <terminal-line>Updated metadata. Experiment UUID: 14058c5c-d0dd-49dd-841a-cbec42b7391e</terminal-line>
    <terminal-line>Added archive symlink to /scratch/\$PROJECT/\$USER/{{model}}/archive/my-project-expts-expt1-14058c5c</terminal-line>
    <terminal-line>To change directory to control directory run:</terminal-line>
    <terminal-line>  cd my-project-expts</terminal-line>
</terminal-window>

!!! tip
    Anyone using a configuration is advised to clone only a single branch (as shown in the example above) and not the entire repository.
<!--end:payu-clone-example-->

<!--start:payu-test-config-->
### Test the configuration

To verify everything is set correctly, it is recommended to first test the configuration as-is.

You can test the setup and paths are correct by running `payu setup` from the _control_ directory:

    payu setup

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

This command: 
  
  - creates the _laboratory_ and `work` directories based on the experiment configuration
  - generates manifests
  - reports useful information to the user, such as the location of the _laboratory_ where the `work` and `archive` directories are located

This can help to isolate issues such as permission problems accessing files and directories, missing files or malformed/incorrect paths.


To test the configuration, execute the following command from within the `control` directory:

    payu run -f

This will submit a single [PBS job][PBS job] to the queue. 

!!! tip
    `payu run` will error out if a non-empty `work` directory for your experiment already exists (from a failed attempt or from running [`payu setup`].<br>
    The `-f` option to `payu run` lets the model run in all cases and delete any existing data under `work`.
<!--end:payu-test-config-->

<!--start:payu-run-experiment-->
### Run the experiment

An experiment consists of a series of sequential runs, with each run continuing from where the previous run ended.
_payu_ supports automatically running a fixed number of runs using the `-n` option:  

    payu run -n <number-of-runs>

This will run the configuration `number-of-runs` consecutive times for the configured run length. This way, the *total experiment length* will be `run-length * number-of-runs`. The `run-length` (i.e. the duration of each individual run) is defined in the configuration settings and its specification is model-dependent.
For example, to run an experiment for a total of 50 years using a configuration with a 5-year _run length_, the `number-of-runs` should be set to `10`:

    payu run -n 10

!!! tip  
    _payu_ has no concept of model time, it is up to the user to determine the `number-of-runs` for the required *total experiment length*.  
    `number-of-runs` should be an integer > 0.<br>  

<!--end:payu-run-experiment-->
## Monitor the experiment

<!-- old instructions-->
Alternatively, you can also use the PBS `job-ID` to monitor the job using the PBS commands available from NCI. 

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

The default name of your job is the name of the _payu_ [_control_ directory](#control-directory).<br>
This can be changed by altering the `jobname` in the [PBS resources section](#modify-pbs-resources) of the `config.yaml` file.

_S_ indicates the status of your run, where:

- _Q_ &rarr; Job waiting in the queue to start
- _R_ &rarr; Job running
- _E_ &rarr; Job ending
- _H_ &rarr; Job on hold

If there are no jobs listed with your `jobname` (or if no job is listed), your run either successfully completed or was terminated due to an error.<br>
For more information, check [NCI documentation](https://opus.nci.org.au/display/Help/FAQ+1%3A+Why+My+Jobs+are+NOT+Running).
<!-- old instructtions-->
<!--start:payu-monitor-->
_payu_ provides the [`payu status`](https://payu.readthedocs.io/en/stable/usage.html#monitoring-payu-jobs) command for monitoring jobs. This command can return the scheduler job ID and the stage the _payu_ run is currently at. When the job is complete, it displays the exit statuses from the model and overall _payu_ run, and points to the PBS log files. 

!!! note
    `payu status` is available in _payu_ versions `1.2.0` and above. This command does not yet support monitoring post-processing jobs from the configuration (e.g., `payu collate` and `payu sync`).

??? abstract "Example outputs from `payu status`"

    Example output from `payu status` for a running simulation:
    
    ```
        ========================================  
        Run: 8  
          Job ID:            running_example.gadi-pbs  
          Run ID:            xxxx  
          Stage:             model-run  
          Current Expt Time: 1950-10-01T00:00:00  
          Exit Status:       0 (Success)  
          Model Exit Code:   0 (Success)  
          Output Log:        /home/189/USER/expt.o100  
          Error Log:         /home/189/USER/expt.3100  
          Job File:          /scratch/\$PROJECT/USER/archive/expt-branch—6dhash/payu_jobs/8/run/running_example.gadi-pbs.json  
        ========================================  
    ```
    
    Example output from `payu status` for an archived simulation:

    
    ```
        ========================================
        Run: 8
          Job ID:            archive_example.gadi-pbs
          Run ID:            xxxx
          Stage:             archive
          Total Queue Time:  0h 1m 7s
          Model Finish Time: 1950-10-01T00:00:00
          Exit Status:       0 (Success)
          Model Exit Code:   0 (Success)
          Output Log:        /home/189/USER/expt.o100
          Error Log:         /home/189/USER/expt.3100
          Job File:          /scratch/\$PROJECT/USER/archive/expt-branch—6dhash/payu_jobs/8/run/archive_example.gadi-pbs.json
        ========================================
    ```

To monitor the current queue time of a queued job, use `payu status --update`.


??? info "Stop a run"

    ### Stop a run

    If you want to manually terminate a run, you can do so by executing:
    ```
    qdel <job-ID>
    ```
    which kills the specified job without waiting for it to complete.

    !!! tip
        If you ran an experiment using `payu run -n ...` but want to stop it after the completion of the current run, you can create a file called `stop_run` in the _control_ directory.<br>  
        This will prevent _payu_ from submitting another job after the current one completes.  
<!--end:payu-monitor-->


## Edit a _payu_ configuration

<!-- start:payu-modif-intro-->
The modifications discussed in this section can change how the model and its components are configured, or the way the model is run by _payu_.

The `config.yaml` file located in the [_control_ directory](#control-directory) is the _payu_ configuration file, which controls the general model configuration. It contains several parts, some of which are more likely to need modification, and others which are rarely changed without having a deep understanding of how the model is configured.

To find out more about configuration settings for the `config.yaml` file, refer to [how to configure your experiment with payu](https://payu.readthedocs.io/en/stable/config.html).
<!--end:payu-modif-intro-->

### Change run length

Adjusting the duration of the model run is one of the most common change to apply. However, models follow different ways to adapt the duration of the run. Please refer to the [Run a Model][Run a Model] page of the model of your choice for information<br> 


<!--start:payu-restart-choice-->
### Start the run from a specific restart file {: id='specific-restart'}

To configure the experiment to start from specific restart files, add a [`restart:` entry](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) to the `config.yaml` file, specifying the path to a folder containing existing restart files.
Or to do this automatically when setting up an experiment using `payu clone` interactive, give the restart path when prompted: `Do you want to specify a custom restart path?`. 

!!! warning
    In some cases, if the supplied restart file is not fully compatible with the model configuration, experiments using a custom restart file may require additional manual adjustments to run correctly.

!!! warning
    The restart option used here will only be applied if there is no restart directory in archive, and so does not have to be removed for subsequent submissions. See [Payu docs](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) for further details.
<!--end:payu-restart-choice-->

<!--start:payu-compute-storage-project-->
### Specify the compute project and storage location {: id='compute-storage-choice'}

If you want to submit an experiment or part of an experiment using a different project for the compute resources or a non-default location for the archive directory, you will need to modify the following entries in `config.yaml`:

```yaml
# If submitting to a different project to your default, uncomment line below
# and replace PROJECT_CODE with appropriate code. This may require setting shortpath
# project: PROJECT_CODE

# Force payu to always find, and save, files in this scratch project directory
# shortpath: /scratch/PROJECT_CODE
```

For example, to run under the {{WG_project}}, uncomment the line beginning with `# project` by deleting the `#` symbol and replace `PROJECT_CODE` with `{{WG_project_code}}`:

```yaml
project: {{WG_project_code}}
```

For model configurations and output to be saved to a `/scratch` storage location other than `project` (or your default if `project` is not set) then also set `shortpath` to the desired path. 

!!! warning
    If changing the project providing the compute resources during an experiment, set the `shortpath` field so that it's the same for all runs of an experiment.
    Doing this will make sure the same `/scratch` location is used for the _laboratory_, regardless of which project is used to run the experiment.
<!--end:payu-compute-storage-project-->

<!--start:payu-PBS-resources-->
### Modify PBS resources

If the model has been altered and needs more time or memory to complete, or needs to be submitted under a different NCI project, you will need to modify the following options in the `config.yaml`:

```yaml
queue: normal
walltime: 3:00:00
mem: 1000GB
jobname: 1deg_jra55_ryf
```

These lines can be edited to change the [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained) for the [PBS job][PBS job].
<!--end:payu-PBS-resources-->

<!--start:payu-sync-->
### Syncing output data to long-term storage

The _laboratory_ directory is typically under the `/scratch` storage on _Gadi_, where [files are regularly deleted once they have been unaccessed for a period of time](https://opus.nci.org.au/pages/viewpage.action?pageId=156434436). For this reason climate model outputs need to be moved to a location with longer term storage.<br>
On _Gadi_, this is typically in a folder under a project code on `/g/data`.  

_Payu_ has built-in support to sync outputs, restarts and a copy of the _control_ directory git history to another location.<br>
This feature is controlled by the following section in the `config.yaml` file: 
```yaml
# Sync options for automatically copying data from ephemeral scratch space to 
# longer term storage
sync:
    enable: False # set base_path below and change to true
    restart: True
    base_path: none # Final sync location will be <base_path>/<experiment_name>/
    exclude:
      - '*.nc.*'
      - 'iceh.????-??-??.nc'
```
To enable syncing, change `enable` to `True`, and set `base_path` to a location on `/g/data`. _payu_ will copy output and restart folders to `<base_path>/<experiment_name>` to avoid overwriting data from other experiments by mistake. A sensible `base_path` could be: `/g/data/$PROJECT/$USER/<model>`.
<!--end:payu-sync-->

<!--start:payu-restart-prune-->
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

??? note "When `restart_freq` is not a multiplier of the model's restart frequency"

    If `restart_freq` is not a multiplier of the model's restart frequency, _payu_ will keep the first restart passed `restart_freq`. For example, a model is set to write restart files every 3 years and produces restarts on the following dates:

    - restart000: 01/01/2000  
    - restart001: 01/01/2003  
    - restart002: 01/01/2006  
    - restart003: 01/01/2009  
    - restart004: 01/01/2012  
    - restart005: 01/01/2015

    If `restart_freq` is set to `5YS` (5 years), _payu_ will keep:

    - restart000: 01/01/2000  
    - restart002: 01/01/2006 (first restart date on or after 01/01/2005)  
    - restart004: 01/01/2012 (first restart date on or after 01/01/2011)  
    - restart005: 01/01/2015 (keeps immediate restarts before 01/01/2017)  

For more information, check [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/stable/config.html#model).
<!--end:payu-restart-prune-->

<!--start:payu-advance-options-->
### _payu_ advance options

!!! warning
    The following sections in the `config.yaml` file control configuration options that are rarely modified, and often require a deeper understanding of how the model is structured to be safely changed.

#### `model` section {: .no-toc }

This section tells _payu_ which driver to use for the main `model` configuration and the location of all `input` files that are common to all its model components.

The `name` field, for the model section, is not actually used for the configuration run, so it can be safely ignored. The `name` field is used for submodels (see below).

#### `submodels` section {: .no-toc }

Coupled models may deploy the model components as multiple submodels.

This section of the _payu_ configuration file specifies the submodels, the configuration options required to execute the model component correctly and the location of all inputs required for this submodel. The configuration files specific to each submodel can be found in a `name/` subdirectory of the _control_ directory, where `name` is the value of this field in the `submodel` section of `config.yaml`. 

#### `runlog` field {: .no-toc }

```yaml
runlog: true
```

When running an experiment,  if `runlog` is set to `true`, _payu_ saves a history of the experiment. It does this using _git_, by automatically committing changes to the control directory repository.

!!! warning
    This should not be changed as it is an essential part of the provenance of an experiment.<br>
    _payu_ updates the manifest files for every run, and relies on `runlog` to save this information in the _git_ history, so there is a record of all inputs, restarts, and executables used in an experiment.

#### `userscripts` section {: .no-toc }

They are used to run scripts or subcommands at various stages of a _payu_ submission:

- `error` field: script is called if the model does not run correctly and exits with an error.
- `run` field: script is called after each model run successful execution, but prior to archiving the model output. If using `payu -n` for automatic resubmission, it is run for each submission.
- `sync` field: script is called at the start of the sync PBS job.
  
For more information about specific `userscripts` fields, check the relevant section of [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/stable/config.html#postprocessing).

#### `postscript` option {: .no-toc }
Postprocessing scripts that run after _payu_ has completed all steps of each run (for example, with `payu run -n 10`, the postscript will run 10 times). Scripts that might alter the output directory, for example, can be run as postscripts. These run in PBS jobs separate from the main model simulation.

#### Miscellaneous {: .no-toc }

The following configuration settings should never require changing:

```yaml
stacksize: unlimited
qsub_flags: -W umask=027
```
<!--end:payu-advance-options-->

<!--start:payu-collate-->
#### Collate {: .no-toc }

Rather than outputting a single diagnostic file over the whole model horizontal grid, the ocean component [MOM](/models/model_components/ocean/#modular-ocean-model-mom) typically generates diagnostic outputs as tiles, each of which spans a portion of model grid.

The `collate` section in the `config.yaml` file controls the process that combines these smaller files into a single outputfile.

```yaml
# Collation
collate:
    exe: mppnccombine.spack
    restart: true
    mem: 4GB
    walltime: 1:00:00
    mpi: false
```
Restart files are typically tiled in the same way and will also be combined together if the `restart` field is set to`true`.
<!--end:payu-collate-->

<!--start:payu-component-configuration-->
## Edit a model components' configuration

To modify the physics used by a model component, the input data or the model variables saved in the output, you will need to modify the model component's configuration files. These are located inside a subfolder of the _control_ directory, named according to the submodel's `name` specified in the `config.yaml` `submodels` section.
<!--end:payu-component-configuration-->