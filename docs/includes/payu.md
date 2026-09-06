[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs

# Run Models Using Payu

## About

<!--start:payu-about-->
[_Payu_](https://github.com/payu-org/payu) is a workflow manager tool for running numerical models in supercomputing environments. It is an open-source software, distributed under an Apache 2.0 Licence.

For in-depth information about _payu_, check its [technical documentation](https://payu.readthedocs.io/en/stable/). 
<!--end:payu-about-->

<!--start:payu-organisation-->
<!--This bit expects the host page to define the variables model and model_type-->
### Data organisation and _payu_'s directories designation

!!! tip
    _Payu_ creates all the directories it needs. Therefore, they do not need to be created beforehand.

The data organisation for _payu_ was chosen to separate the smaller text files that define a _configuration_ and the larger binary input and output files needed for an _experiment_. 

This means the _configuration_ definition can be tracked with _Git_, and so is easy to back up and share. It also optimises the use of different filesystems on high-performance computers. Finally, this layout ensures several _experiments_ that share common executables and input data can be run simultaneously.  

A representation of the data organisation for _payu_ is given in the following diagram:

<!-- Diagram created by draw.io: https://app.diagrams.net/#. The SVG file contains the XML diagram. The file can be opened in draw.io for editing. No account required -->
![payu directory structure](/assets/payu_file_org.drawio.svg){: class="example-img" loading="lazy"}

As shown in the diagram, the general layout of a _payu_-supported model run consists of two main directories:

- The _control_ directory contains the model configuration and is the directory from which the model run is started. This directory contains information to manage the simulation and the scientific options that define the algorithms used in the model component or the diagnostics saved by the model component. In the _control_ directory, you will find:

     - The `config.yaml` file, which is used to orchestrate the simulation.
     - Model components' configuration files, which are used to define the physics and the components' internal state used in the simulation:
         - If the model has only one component, these files are located directly in the _control_ directory. 
         - If the model has several components, these files are in subdirectories. The `submodels` section of the `config.yaml` file specifies the name of the submodels and of the subdirectories containing the pertinent files.
       
            To modify the model components' options, please refer to the configurations documentation of the model.
- The _laboratory_ directory contains all data from _payu_ experiments of the same model. By default, it is `/scratch/${PROJECT}/${USER}/<model_type>`. `${PROJECT}` and `${USER}` are environment variables on _Gadi_ that point to your [default project](/getting_started/set_up_nci_account/#change-default-project-on-gadi) and your username, respectively. `<model_type>` defaults to _{{model_type}}_ for the {{model}} model. This location can be changed using options in the `config.yaml` file. Inside the _laboratory_ directory, there are two subdirectories of particular interest: 
    - _work_ &rarr; for temporary storage of files needed by the model while it runs. _Payu_ creates this directory at the start of each run and removes it upon successful completion. It is left untouched in case of error to facilitate the identification of the cause of the model failure.
    - _archive_ &rarr; for storing the output following each successful run. The output, log and restart files are automatically transferred from _work_ to _archive_ upon successful completion of runs.
    
    The _archive_ and _work_ directories for an experiment are most easily accessed through the symbolic links created in the _control_ directory.

<!--See the section on [modifying the PBS resources](#modify-pbs-resources) to learn how to change the _laboratory_ location. (Should the include be cut to allow adding this sentence and link?)-->

!!! tip 

    Recommended location of _control_ and _laboratory_ on _Gadi_.

    - _control_ directories. It is recommended to put these in your `$HOME` directory as this is the only filesystem that is actively backed-up. The 10GB quota should be sufficient as _control_ directories only contain text files and symbolic links and, hence, occupy less than 1MB.

        If you decide to locate your _control_ directory under `/g/data`, be aware of [some complications](https://forum.access-hive.org.au/t/changing-project-codes-for-payu-control-directories-under-g-data/6566) linked to that choice.

    - _laboratory_ directories. For these, `/scratch` is recommended as it is optimised for fast reading and writing of large data, and adequate space is available for large model output.

!!! warning
    Files on the `/scratch` drive, such as the _laboratory_ directory, might be deleted if not accessed for [some time](https://opus.nci.org.au/spaces/Help/pages/156434436/Gadi+scratch+File+Management). All experiments which are to be kept should be moved to `/g/data/` by enabling the `sync` step in _payu_.

#### Output and restart files organisation {: .no-toc}

Within each of the _work_ and _archive_ directories, _payu_ automatically creates a unique subdirectory for each experiment. Within each experiment subdirectory, the output and restart subfolders are called `outputXXX` and `restartXXX`, respectively, where _XXX_ is the run number starting from `000`. Model components are further separated into subdirectories within the output and restart directories.

#### Error and output log files {: .no-toc}

- *PBS output files*

    When the model fails or completes a run, PBS writes the standard output and error streams to two files inside the _control_ directory: `<jobname>.o<job-ID>` and `<jobname>.e<job-ID>`, respectively. These files usually contain logs about _payu_ tasks, and give an overview of the resources used by the job.<br>

    To move these files to the _archive_ directory once the model has completed running, use the following command:

     ```
     payu sweep
     ```


- *Model log files*

    While the model is running, the standard output and error streams are saved to file in the _control_ directory. You can examine the contents of these log files to check on the status of a run as it progresses (or after a failed run     has completed).
    
    !!! warning
        At the end of a successful run, the model log files are archived to the _archive_ directory and will no longer be found in the _control_ directory. If they remain in the _control_ directory after the PBS job for a run has completed, it means the run has failed.

<!--end:payu-organisation-->

## Prerequisites for _payu_

<!--start:payu-projects-->
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
<!--end:payu-projects-->

<!--start:access-payu-->
### Accessing _payu_

_Payu_ on _Gadi_ is available through a dedicated environment in the _vk83_ project.<br>
After joining the _vk83_ project, load the _payu_ module:

    module use /g/data/vk83/modules
    module load payu

To check that _payu_ is available, run:

    payu --version
<!--end:access-payu-->

### Get the model configuration

<!--start:get-config-payu-->
Before downloading (cloning) a local copy of a configuration, you need to:  

- Know the `<repository>` and `<branch>` name of the configuration is stored under on GitHub. 
- Create a location on _Gadi_ to store all your _payu_ experiments, `<configurations-directory>`, typically a folder under `$HOME`. This directory must exist before running _payu_.
- Choose a directory name to store the experiment, `<control-directory>` (created by _payu_). The _control_ directory is a _Git_ repository. Experiments are saved as branches in this repository, making it possible to use the same _control_ directory for several experiments. For this reason, we recommend to always set the `<local-branch>`. For more information refer to this [_payu_ tutorial](https://forum.access-hive.org.au/t/access-om2-payu-tutorial/1750#select-experiment-12).
- Choose a name for your experiment, `<local-branch>`. It is recommended to choose a descriptive name, specific to your experiment. Note that the experiment name will be formed using the _control_ directory's name and this `<local-branch>` name.

Then, you can get the chosen configuration using `payu clone`.
<!--end:get-config-payu-->

<!--start:payu-clone-example-->
<!--This bit expect the host page to define the variables: model, config_example, github_configs, model_type-->
For example, if you want to run an experiment for {{model}} using the configuration *{{config_example}}*. You decide the following:

- `<repository>` and `<branch>`: base your experiment off the branch, `{{config_example}}`, from the repository, `{{github_configs}}`
- `<configurations-directory>`: store all your {{model}} configurations under `~/{{model}}/`
- `<local-branch>`: name your branch `expt1`. For a real case, a more explicit name is recommended.
- `<control-directory>`: store the configurations for this research project under `my-project-expts`. For a real case, a more explicit name is recommended.

To get this configuration, run:

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
    <terminal-line>laboratory path:  /scratch/\${PROJECT}/\${USER}/{{model_type}}</terminal-line>
    <terminal-line>binary path:  /scratch/\${PROJECT}/\${USER}/{{model_type}}/bin</terminal-line>
    <terminal-line>input path:  /scratch/\${PROJECT}/\${USER}/{{model_type}}/input</terminal-line>
    <terminal-line>work path:  /scratch/\${PROJECT}/\${USER}/{{model_type}}/work</terminal-line>
    <terminal-line>archive path:  /scratch/\${PROJECT}/\${USER}/{{model_type}}/archive</terminal-line>
    <terminal-line>Updated metadata. Experiment UUID: 14058c5c-d0dd-49dd-841a-cbec42b7391e</terminal-line>
    <terminal-line>Added archive symlink to /scratch/\${PROJECT}/\${USER}/{{model_type}}/archive/my-project-expts-expt1-14058c5c</terminal-line>
    <terminal-line>To change directory to control directory run:</terminal-line>
    <terminal-line>  cd my-project-expts</terminal-line>
</terminal-window>

!!! tip
    Anyone using a configuration is advised to clone only a single branch (as shown in the example above) and not the entire repository.
<!--end:payu-clone-example-->

<!--start:payu-test-config-->
<!--This bit expects the host page to define the variables: model_type, model-->
### Test the configuration

To verify everything is set correctly, it is recommended to first test the configuration as is.

You can test the setup and paths are correct by running `payu setup` from the _control_ directory:

    payu setup

<terminal-window>
    <terminal-line data="input">payu setup</terminal-line>
    <terminal-line>laboratory path: /scratch/\${PROJECT}/\${USER}/{{model_type}}</terminal-line>
    <terminal-line>binary path: /scratch/\${PROJECT}/\${USER}/{{model_type}}/bin</terminal-line>
    <terminal-line>input path: /scratch/\${PROJECT}/\${USER}/{{model_type}}/input</terminal-line>
    <terminal-line>work path: /scratch/\${PROJECT}/\${USER}/{{model_type}}/work</terminal-line>
    <terminal-line>archive path: /scratch/\${PROJECT}/\${USER}/{{model_type}}/archive</terminal-line>
    <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
    <terminal-line>Loading restart manifest: manifests/restart.yaml</terminal-line>
    <terminal-line>Loading exe manifest: manifests/exe.yaml</terminal-line>
    <terminal-line>Setting up atmosphere</terminal-line>
    <terminal-line>Setting up ocean</terminal-line>
    <terminal-line>Setting up ice</terminal-line>
    <terminal-line>Setting up {{model.lower()}}</terminal-line>
    <terminal-line>Checking exe and input manifests</terminal-line>
    <terminal-line>Updating full hashes for 3 files in manifests/exe.yaml</terminal-line>
    <terminal-line>Creating restart manifest</terminal-line>
    <terminal-line>Writing manifests/restart.yaml</terminal-line>
    <terminal-line>Writing manifests/exe.yaml</terminal-line>
</terminal-window>

This command: 
  
  - Creates the _laboratory_ and _work_ directories based on the experiment configuration,
  - Generates manifests, and
  - Reports useful information to the user, such as the location of the _laboratory_ where the _work_ and _archive_ directories are located.

This can help to isolate issues such as permission problems accessing files and directories, missing files or malformed/incorrect paths.


To test the configuration, execute the following command from within the _control_ directory:

    payu run -f

This will submit a single [PBS job][PBS job] to the queue. 

!!! failure
    `payu run` will issue an error if a non-empty _work_ directory for your experiment already exists (from a failed attempt or from running `payu setup`).<br>
    The `-f` option to `payu run` lets the model run in all cases and deletes any existing data in the _work_ directory.
<!--end:payu-test-config-->

### Run the experiment

<!--start:payu-run-experiment-->
An experiment consists of a series of sequential runs, with each run continuing from where the previous run ended.
_payu_ supports automatically running multiple consecutive runs using the `-n` option:  

    payu run -n <number-of-runs>

This will run the configuration `number-of-runs` consecutive times for the configured run length. This way, the *total experiment length* will be `run-length * number-of-runs`. The `run-length` (i.e. the duration of each individual run) is defined in the configuration settings and its specification is model-dependent.
For example, to run an experiment for 50 years using a configuration with a 1-year _run length_, the `number-of-runs` should be set to `50`:

    payu run -n 50

!!! tip  
    _payu_ has no concept of model time, it is up to the user to determine the `number-of-runs` for the required *total experiment length*.  
    `number-of-runs` should be an integer > 0.<br>  
<!--end:payu-run-experiment-->

<!--start:payu-optimise-PBS-->
### Minimise the number of PBS jobs

_Payu_ provides `runspersub` to control the maximum number of runs per PBS job submission.

`runspersub` controls how many years are simulated within a _single_ PBS job, reducing queueing time between jobs. You must also set `walltime` to allow sufficient time for all runs to complete. In contrast, the `-n` command-line option allows _payu_ to resubmit the simulation to a _subsequent_ PBS job.
<!--end:payu-optimise-PBS-->

<!--start:payu-runspersub-examples-->
Here are some practical examples of setting these options for different cases. All assume `runtime` is set to 1 year and that the model requires 1 to 2 hours of `walltime` per simulated model year:

- **Run 20 years with resubmission every 5 years**<br>
    Set `runspersub` to `5` and `walltime` to `06:00:00`, then run:
    ```
    payu run -f -n 20
    ```
    This submits four PBS jobs covering years 1-5, 6-10, 11-15, and 16-20.

- **Run 7 years with resubmission every 3 years**<br>
   Set `runspersub` to `3` and `walltime` to `04:00:00`, then run:
    ```
    payu run -f -n 7
    ```
    This submits three PBS jobs covering years 1-3, 4 -6, and 7.
<!--end:payu-runspersub-examples-->

<!--start:payu-continue-experiment-->
### Continue an experiment

If you already ran several years of an experiment and you want to simulate some extra years, you can do that easily by using the same _control_ directory as before and simply launching _payu_ again for the extra years. For example, if you had 100 years simulated and want to add 50 years of simulation, you can simply run:

```
payu run -n 50
```

!!! warning

    This only works if you have kept the _archive_ directory as set up by _payu_. If you have modified the _archive_ directory, you will need to manually specify the correct restart file in the `config.yaml` file.
<!--end:payu-continue-experiment-->

<!--start:payu-re-run-experiment-->
### Re-run an experiment from scratch

If you need to rerun years after correcting an error, first remove the archive directory created by payu (e.g., move, rename, archive, or delete it as appropriate). You can use `payu sweep --hard` to remove the previous experiment data, then relaunch the experiment with `payu run -n N` as before.
<!--end:payu-re-run-experiment-->

## Monitor the experiment

<!--start:payu-monitor-->
_Payu_ provides the [`payu status`](https://payu.readthedocs.io/en/stable/usage.html#monitoring-payu-jobs) command for monitoring jobs. This command returns the scheduler job ID and the current stage of the _payu_ run is currently at. When the job is complete, it displays the exit statuses from the model and overall _payu_ run, and points to the PBS log files. 

??? example "Example: outputs from `payu status`"

    Example output from `payu status` for a running simulation:
    
    ```
        ========================================
        Run: 0
        ------------- Run Info -------------
        Job ID:            174067874.gadi-pbs
        Run ID:            fe6a9f5a508caf26d56b1eda6ef9409ca45626c0
        Stage:             model-run
        Current Expt Time: 2676-01-01T21:00:00
        Job File:          /scratch/${PROJECT}/${USER}/access-esm/archive/test-dir-struct-test-dir-struct-f8f5d0f4/payu_jobs/0/run/174067874.gadi-pbs.json
        ======================================== 
    ```
    
    Example output from `payu status` for an archived simulation:

    
    ```
        ========================================
        Run: 8
          Job ID:            174067874.gadi-pbs
          Run ID:            xxxx
          Stage:             archive
          Total Queue Time:  0h 1m 7s
          Model Finish Time: 1950-10-01T00:00:00
          Exit Status:       0 (Success)
          Model Exit Code:   0 (Success)
          Output Log:        ${HOME}/expt.o174067874
          Error Log:         ${HOME}/expt.e174067874
          Job File:          /scratch/${PROJECT}/${USER}/archive/expt-branch—6dhash/payu_jobs/8/run/174067874.gadi-pbs.json
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

The `config.yaml` file located in the _control_ directory is the _payu_ configuration file, which controls the general model configuration. It contains several parts, some of which are more likely to need modification, and others which are rarely changed without having a deep understanding of how the model is configured.

To find out more about configuration settings for the `config.yaml` file, refer to [how to configure your experiment with _payu_](https://payu.readthedocs.io/en/stable/config.html).
<!--end:payu-modif-intro-->

<!--start:payu-restart-choice-->
### Start the run from a specific restart file {: id='specific-restart'}

To configure the experiment to start from specific restart files, add a [`restart:` entry](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) to the `config.yaml` file, specifying the path to a folder containing existing restart files.
Or to do this automatically when setting up an experiment using `payu clone` interactive, give the restart path when prompted: `Do you want to specify a custom restart path?`. 

!!! warning
    In some cases, if the supplied restart file is not fully compatible with the model configuration, experiments using a custom restart file may require additional manual adjustments to run correctly.

!!! warning
    The restart option used here will only be applied if there is no restart directory in archive, and so does not have to be removed for subsequent submissions. See [_payu_ docs](https://payu.readthedocs.io/en/stable/config.html#miscellaneous) for further details.
<!--end:payu-restart-choice-->

<!--start:payu-compute-storage-project-->
<!-- This bit needs the hosting page to define the variables {{WG_project}} and {{WG_project_code}}-->
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

If the model has been altered and needs more time or memory to complete, you will need to modify the following options in the `config.yaml`:

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

The _laboratory_ directory is typically under the `/scratch` storage on _Gadi_, where [files are regularly deleted once they have not been accessed for a period of time](https://opus.nci.org.au/pages/viewpage.action?pageId=156434436). For this reason, climate model outputs need to be moved to a location with longer-term storage.<br>
On _Gadi_, this is typically in a folder under a project code on `/g/data`.  

_Payu_ has built-in support to sync outputs, restarts and a copy of the _control_ directory _Git_ history to another location.<br>
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
To enable syncing, change `enable` to `True`, and set `base_path` to a location on `/g/data`. _Payu_ will copy output and restart folders to `<base_path>/<experiment_name>` to avoid overwriting data from other experiments by mistake. A sensible `base_path` could be: `/g/data/${PROJECT}/${USER}/<model>`.
<!--end:payu-sync-->

<!--start:payu-restart-prune-->
### Pruning model restarts

By default, restart files are created at the end of each run, allowing subsequent simulations to resume from a previously saved model state. However, restart files can occupy significant disk space, and keeping all of them throughout an entire experiment is often not necessary. 

If disk space is limited, consider using _payu_'s restart files pruning feature, controlled by the `restart_freq` field of the `config.yaml`.
By default, every `restart_freq`, _payu_ removes intermediate restart files, keeping only:

- Restarts corresponding to the `restart_freq` interval, and  
- All restarts created since the most recently retained restart.  

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

??? note "When `restart_freq` is not a multiple of the model's restart frequency"

    If `restart_freq` is not a multiplier of the model's restart frequency, _payu_ will keep the first restart past `restart_freq`. For example, a model is set to write restart files every 3 years and produces restarts on the following dates:

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
### _Payu_ options for advanced users

!!! warning
    The following sections in the `config.yaml` file control configuration options that are rarely modified, and often require a deeper understanding of how the model is structured to be safely changed.

??? info "`model` and `submodel` sections"

    #### `model` section {: .no-toc }

    The `model` field tells _payu_ which driver to use for the configuration. 

    The `input` field gives the location of all input files that are common to all its model components, if any. The `input` field is omitted if there are no common input files.

    The `name` field, for the model section, is not actually used for the configuration run, so it can be safely ignored or omitted. The `name` field is used for submodels (see below).

    #### `submodels` section {: .no-toc }

    Coupled models may deploy the model components as multiple submodels.

    This section of the _payu_ configuration file specifies the submodels, the configuration options required to execute the model component correctly and the location of all inputs required for this submodel. The configuration files specific to each submodel can be found in a `<name>/` subdirectory of the _control_ directory, where `<name>` is the value of the `name` field in the `submodel` section of `config.yaml`. 

??? info "`runlog` field"

    #### `runlog` field {: .no-toc }

    ```yaml
    runlog: true
    ```

    When running an experiment,  if `runlog` is set to `true`, _payu_ saves a history of the experiment. It does this using _Git_, by automatically committing changes to the control directory repository.

    !!! warning
        This should not be changed as it is an essential part of the provenance of an experiment.<br>
        _Payu_ updates the manifest files for every run, and relies on `runlog` to save this information in the _Git_ history, so there is a record of all inputs, restarts, and executables used in an experiment.

??? info "`userscripts` section"

    #### `userscripts` section {: .no-toc }

    Use the `userscripts` section to specify scripts or subcommands to run at various stages of a _payu_ submission. For example:

    - `error` field: script is called if the model does not run correctly and exits with an error.
    - `run` field: script is called after each model run successful execution, but prior to archiving the model output. If using `payu -n` for automatic resubmission, it is run for each submission.
    - `sync` field: script is called at the start of the sync PBS job.
    
    For more information about specific `userscripts` fields, check the relevant section of [_payu_ Configuration Settings documentation](https://payu.readthedocs.io/en/stable/config.html#postprocessing).

??? info "`postscript` field"

    #### `postscript` field {: .no-toc }

    Postprocessing scripts run after _payu_ has completed all steps of each run. For example, with `payu run -n 10`, the postscript will run 10 times. Scripts that might alter the output directory, for example, can be run as postscripts. These run in PBS jobs separate from the main model simulation.

??? info "Fields that should never require changing"

    #### Miscellaneous {: .no-toc }

    The following configuration settings should never require changing:

    ```yaml
    stacksize: unlimited
    qsub_flags: -W umask=027
    ```
<!--end:payu-advance-options-->

<!--start:payu-collate-->
#### Collate {: .no-toc }

The ocean component [MOM](/models/model_components/ocean/#modular-ocean-model-mom) can generate diagnostic and restart outputs in single files covering the whole model grid or as tiled files, with each tile covering part of the horizontal grid.
The `collate` section in the `config.yaml` file controls the process that combines the tiled output into a single output file.

```yaml
# Collation
collate:
    exe: mppnccombine.spack
    restart: true
    mem: 4GB
    walltime: 1:00:00
    mpi: false
```

For configurations that generate single restart and output files over the whole grid, collation is disabled as follows:

```yaml
# Collation
collate:
    enabled: false
```
<!--end:payu-collate-->

