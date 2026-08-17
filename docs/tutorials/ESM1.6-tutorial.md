# Tutorial: Running ACCESS-ESM1.6


## Introduction

Welcome to the *How to run ACCESS-ESM1.6* training session. In this session, you'll get hands on experience of running and configuring ACCESS-ESM1.6, the recently released earth system model developed for Australia's contribution to the CMIP7 Assessment Fast Track. During this session, we'll cover:

* What ACCESS-ESM1.6 is, and how it differs to the older model ACCESS-ESM1.5
* How to clone and run ACCESS-ESM1.6 configurations using *payu* on Gadi
* Key *payu* commands and concepts for managing climate model simulations
* How to customise ESM1.6 configurations
* Where to find more information and get help


## Prerequisites
To complete the hands on sections of this tutorial, you will need to have:

- A current NCI account
- A GitHub account
- A MOSRS account and to have completed the [UKMO EULA signing instructions](https://forum.access-hive.org.au/t/accessing-ukmo-licensed-models/6168)
- Be a member of the NCI projects:
    - `vk83`
    - `nf33`

If you haven't completed these prerequisites you're welcome to work with someone else for the hands on sections of the tutorial.


## Introduction to ACCESS-ESM1.6
ACCESS-ESM1.6 is a global coupled earth system model containing active atmosphere, ocean, sea ice, land, and biogeochemistry components. The model supports both a prescribed CO2 concentrations mode, and a fully interactive carbon mode where carbon is coupled between the model components.

ACCESS-ESM1.6 development used ACCESS-ESM1.5 as a base and brought in many significant changes. Some of the main changes include:

- A new ocean BGC model, WOMBATlite
- The CABLE2.4 land model has been updated to CABLE3, with new features including as Australian plant types <!--Todo: find out about other changes-->
- CICE4 has been replaced with CICE5, which brings bug fixes to key diagnostics. CICE5 has been configured to use the same zero layer thermodynamics scheme.
- An iceberg spreading scheme has been added, where meltwater from the icesheets is distributed both around the coast, and according to a wider iceberg melt pattern.
- Released scientific configurations have been developed to match the CMIP7 experiment protocols, including updated atmospheric forcings.
- Optimised for Gadi. While ESM1.6 is more computationally complex than ESM1.5, it runs roughly 25% faster.
- Model outputs conform to the new ACCESS-NRI data standards, with the aim of making model output simpler to work with and to improve provenance information. We'll see more of what this looks like towards the end of the session.



## Introduction to payu

payu is a workflow manager for running numerical models in supercomputing environments. Payu is designed to help users set up, run, and manage climate simulations, and provides a consistent set of commands and concepts which can be used accross several models including ACCESS-OM3 and ACCESS ESM1.6.

For in-depth information about payu, visit the [payu documentation](https://payu.readthedocs.io/en/stable/).


## Exercise 1: Activating payu on gadi
Payu is made available as a module on gadi. To enable payu commands, log onto gadi and run:
```
module use /g/data/vk83/modules
module load payu
```

To check that payu is working, you can run:

```
payu --version
```

## Exercise 2: Cloning an ACCESS-ESM1.6 configuration
Running a climate model requires you to collect a large number of files, including model executables, a collection of model input files such as grids and forcings, configuration files to control the model's scientific options, and an initial state for the model to start from. A payu *configuration* can be thought of a prebuilt bundle of all these requirements, making it easy to get a simulation running. Different scientific configurations of the model can be stored in different payu configurations.

Released ACCESS-ESM1.6 configurations are published on the ESM1.6 configurations [GitHub repository](https://github.com/ACCESS-NRI/access-esm1.6-configs), where different configurations are stored under different git branches. The branches for the released ACCESS-ESM1.6 configurations are:

- [release-piControl](https://github.com/ACCESS-NRI/access-esm1.6-configs/tree/release-piControl)
- [release-esm-piControl](https://github.com/ACCESS-NRI/access-esm1.6-configs/tree/release-esm-piControl)
- [release-historical](https://github.com/ACCESS-NRI/access-esm1.6-configs/tree/release-historical)
- [release-esm-historical](https://github.com/ACCESS-NRI/access-esm1.6-configs/tree/release-esm-historical)

The first step in running an ESM1.6 simulation is to make a local copy (i.e. clone) a configuration. To do this, you'll need to:

- Know the `<repository>` and `<branch>` name the configuration is stored under on GitHub. For this tutorial, use https://github.com/ACCESS-NRI/access-esm1.6-configs for the `<repository>`, and select a `<branch>` name from any of the above released configurations.
- Create a location on Gadi to store all your payu experiments, `<configurations-directory>`, typically a folder under $HOME. This directory must exist before running payu.
- Choose a directory name to store the experiment, `<control-directory>` (created by payu). The control directory is a Git repository.
- Choose a name for your experiment, `<local-branch>`. It is recommended to choose a descriptive name, specific to your experiment. For this tutorial, `<username>-tutorial` is an example of the local branch name you can use.


<terminal-window>
    <terminal-line data="input">mkdir -p ~/ACCESS-ESM1.6/</terminal-line>
    <terminal-line data="input">cd ~/ACCESS-ESM1.6/</terminal-line>
    <terminal-line data="input">payu clone</terminal-line>
    <terminal-line><span class="payu-yellow">Welcome to the Payu Clone Wizard!</span></terminal-line>
    <terminal-line><span class="payu-yellow">Press 'Ctrl+C' at any time to exit.</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Please enter the URL of the repository, or the local path of a configuration you want to clone:</span>  (e.g., https://github.com/payu-org/bowl1.git or /path/to/local/experiment; 'Tab' to browse, '/' to enter folder) <span class="payu-dark-yellow"> https://github.com/ACCESS-NRI/access-esm1.6-configs</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Do you want to clone the repo based on:</span> <span class="payu-dark-yellow">An existing branch</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Please enter the name of the branch you want to clone ('Tab' to browse all branches):</span> <span class="payu-dark-yellow">release-piControl</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">How would you like to name your local experiment directory?</span> <span class="payu-dark-yellow">tutorial-experiment</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu red">Is this a new experiment?</span> (If yes, payu will create a new branch.) <span class="payu-dark-yellow">Yes</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">What would you like to name your new branch</span>  (Note: this won't be shared to the online repository automatically) <span class="payu-dark-yellow"><username\>-tutorial</span></terminal-line>
    <terminal-line><span class="spack-cyan">?</span> <span class="payu-red">Do you want to specify a custom restart path? (If no, the default restart/initial conditions will be used.)</span> <span class="payu-dark-yellow">No</span></terminal-line>
    <terminal-line><span class="payu-yellow">Running command:</span></terminal-line>
    <terminal-line><span class="payu-yellow">\`payu clone -B {{config_example}} -b expt1 {{github_configs}} my-project-expts\`</span></terminal-line>
    <terminal-line>Cloned repository from {{github_configs}} to directory: /home/561/\$USER/payu-control/{{model}}/my-project-expts</terminal-line>
    <terminal-line>Created and checked out new branch: expt1</terminal-line>
    <terminal-line>laboratory path:  /scratch/\${PROJECT}/\${USER}/access-esm</terminal-line>
    <terminal-line>binary path:  /scratch/\${PROJECT}/\${USER}/access-esm/bin</terminal-line>
    <terminal-line>input path:  /scratch/\${PROJECT}/\${USER}/access-esm/input</terminal-line>
    <terminal-line>work path:  /scratch/\${PROJECT}/\${USER}/access-esm/work</terminal-line>
    <terminal-line>archive path:  /scratch/\${PROJECT}/\${USER}/access-esm/archive</terminal-line>
    <terminal-line>Updated metadata. Experiment UUID: 14058c5c-d0dd-49dd-841a-cbec42b7391e</terminal-line>
    <terminal-line>Added archive symlink to /scratch/\${PROJECT}/\${USER}/access-esm/archive/my-project-expts-expt1-14058c5c</terminal-line>
    <terminal-line>To change directory to control directory run:</terminal-line>
    <terminal-line>  cd my-project-expts</terminal-line>
</terminal-window>

Lastly `cd` into the newly created *control directory*.

## Exercise 3: Setting project for computation and storage

By default, payu will use your currently active project on Gadi for computation and storage. To check what project you are using, you can run

```
echo $PROJECT
```

For this training session, we'll be using resources from project `nf33`. Payu allows you to select a non-default project in the `config.yaml` file, which is the main configuration file used to control a payu simulation. We'll go through more details of what you can control in the `config.yaml` file after we've set off the simulations.


To change the computation and storage project, make the following change:


```diff
# If submitting to a different project to your default, uncomment line below
# and replace PROJECT_CODE with appropriate code. This may require setting shortpath
-# project: PROJECT_CODE
+project: nf33
```

## Exercise 4: Checking the configuration is working
To verify everything is set up correctly, it is recommended to first test the configuration as is. You can test the setup and paths are correct by running payu setup from the control directory:

```
payu setup
```

<terminal-window>
    <terminal-line data="input">payu setup</terminal-line>
    <terminal-line>laboratory path: /scratch/\${PROJECT}/\${USER}/access-esm</terminal-line>
    <terminal-line>binary path: /scratch/\${PROJECT}/\${USER}/access-esm/bin</terminal-line>
    <terminal-line>input path: /scratch/\${PROJECT}/\${USER}/access-esm/input</terminal-line>
    <terminal-line>work path: /scratch/\${PROJECT}/\${USER}/access-esm/work</terminal-line>
    <terminal-line>archive path: /scratch/\${PROJECT}/\${USER}/access-esm/archive</terminal-line>
    <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
    <terminal-line>Loading restart manifest: manifests/restart.yaml</terminal-line>
    <terminal-line>Loading exe manifest: manifests/exe.yaml</terminal-line>
    <terminal-line>Setting up atmosphere</terminal-line>
    <terminal-line>Setting up ocean</terminal-line>
    <terminal-line>Setting up ice</terminal-line>
    <terminal-line>Setting up access-esm1.6</terminal-line>
    <terminal-line>Checking exe and input manifests</terminal-line>
    <terminal-line>Updating full hashes for 3 files in manifests/exe.yaml</terminal-line>
    <terminal-line>Creating restart manifest</terminal-line>
    <terminal-line>Writing manifests/restart.yaml</terminal-line>
    <terminal-line>Writing manifests/exe.yaml</terminal-line>
</terminal-window>


## Exercise 5: Running the simulation
To set off a one year simulation of your configuration, run:
```
payu run -f
```


**Note**: `payu run` will issue an error if a non-empty work directory for your experiment already exists (from a failed attempt or from running `payu setup`).
The `-f` option to payu run lets the model run in all cases and deletes any existing data in the work directory. We're using `-f` in this case as we had already run `payu setup`.

**Note:** To run several years in succession, you can use `payu run -f -n <nyears>`. Each separate 1 year run segment will start from where the previous one finished. In this tutorial, we'll just do a single one year simulation.


The one year simulation will take around 55 minutes to complete. The data post processing which runs in a separate job can take up to another hour, and so we may not get final outputs from our simulations by the end of the session.


While the simulations are running, we'll discuss some more features of payu and ACCESS-ESM1.6.


## Exercise 6: Understanding payu's directory structure

Let's take a brief look at the directories payu creates when it runs a model simulation.

The top-level directory containing the `config.yaml` file is called the *control directory*. In our control directory, we should see two symlinks to locations on `scratch`: the `archive` directory, which will store the model output and restart files atn the end of the run, and the `work` directory, the temporary workspace used by the in progress simulation.

For a detailed explanation of the directory structure used by payu, take a look at  <!--TODO: add link--> HOW TO RUN DOCS SECTION.

In the following exercises we'll look into how payu sets up and organises the `work` directory.

1. In the `config.yaml` file, you'll see lists of filepaths associated with each model component, for example:
    ```yaml

     - name: atmosphere
       model: um
       ncpus: 256
       exe: um_hg3.exe
       input:
         - /g/data/vk83/configurations/inputs/access-esm1p5/share/atmosphere/spectral/resolution_independent/2020.05.19/spec3a_sw_hadgem1_6on
         ...

     - name: ocean
       model: mom
       ncpus: 240
       exe: mom5_access_cm
       input:
         - /g/data/vk83/configurations/inputs/access-esm1p6/modern/share/ocean/biogeochemistry/global.1deg/2025.09.22/SFe_Hamiltonetal2020_monthly_clim.nc
         ...
    ```

    Take a look through the `work` directory. How has payu used the above two filepaths when creating the `work` directory?
    <details>
    <summary>Hint</summary>
     Take a look in the `work/atmosphere/INPUT` and `work/ocean/INPUT` directories.
    </details>


2. How has payu used the `config.yaml` settings `exe: um_hg3.exe` and `exe: mom5_access_cm` when creating the `work` directory?
   <details>
   <summary>Hint</summary>
    These specify the names of executables for the atmosphere and ocean components. Take a look in `work/atmosphere` and `work/ocean`. 
   </details>

3. The `atmosphere` subdirectory of the control directory contains a configuration file `namelists`. What has payu done with this file when setting up the `work` directory?
   <details>
   <summary>Hint</summary>
    Take a look in `work/atmosphere`
   </details>

4. What do the files in the `manifests` directory under the control directory contain? When would this information have been filled in?
   <details>
   <summary>Hint</summary>
    How do the filepaths in the `input.yaml` relate to the filepaths in the `config.yaml` file. The `md5` fields contain [md5 hashes](https://en.wikipedia.org/wiki/MD5) calculated for each of the hashes, and can be used to verify that input files have not been changed.
   </details>



## Excercise 7: Check the status of your simulation
Simulations can crash for many different reasons including transient problems on Gadi, numerical instabilities in the model, or problems with the way we've set up the configuration. To check where a simulation is up to, or if it has crashed, payu provides the `payu status` command. 

`payu status`  will tell us whether a simulation is queued, running, successfully completed, or crashed, and if it's still running it will report the current model date.

Check where your simulation is up to by running:

```
payu status
```
from your control directory.

## Configuring an ESM1.6 simulation


### The `config.yaml` file
The `config.yaml` controls how payu sets up, runs, and archives a simulation. We'll only touch on a small selection of of the settings in this tutorial, but we recommend reading the HOW TO RUN DOCS and [payu documentation](https://payu.readthedocs.io/en/stable/config.html) for details on everything you can control from the `config.yaml` file.

#### Compute project and storage location
We've already modified our `config.yaml` file to use project PROJECT for the both the computation and storage resources. However it's common to need to use one project for computation and another for storage. To set this up, you can specify

```yaml
project: <COMPUTE PROJECT>
shortpath: /scratch/<STORAGE PROJECT>
```

#### The restart file
The following line specifies the initial restart file used in the `release-esm-piControl` experment:

```yaml
restart: /g/data/vk83/configurations/inputs/access-esm1p6/modern/pre-industrial-emissions/restart/2026.02.23
```

#### Restart pruning
By default, restart files are created at the end of each run, allowing subsequent simulations to resume from a previously saved model state. However, restart files can occupy significant disk space, and keeping all of them throughout an entire experiment is often not necessary. Payu can be configured to only keep a subset of the restarts according to a selected frequency.

The setting below tells payu to only keep every 10th year's restart files:

```yaml
restart_freq: 10YS
```

#### Syncing model outputs
The `archive` directory is typically under the `/scratch` storage on Gadi, where files are regularly deleted once they have not been accessed for a period of time. It's common to copy a simulations outputs over to a location on `/g/data` to preserve them while doing analysis.

Rather than copying the outputs manually, you can use the `sync` settings to get payu to automatically sync the outputs and restart files to a specified location at the end of each run segment.

For example, the following changes will sync the archived data to a location on `/g/data/PROJECT/

```diff
# Sync options for automatically copying data from ephemeral scratch space to
# longer term storage
sync:
-   enable: False # set path below and change to true
+   enable: True
    restarts: True
-   base_path: null # Set to location on /g/data (e.g., /g/data/$PROJECT/$USER/)
+   base_path: /g/data/PROJECT/<user>/tutorial_experiments/

```


### Configuring individual submodels

Configuration files for each of ESM1.6's submodels can be found in the `ocean`, `atmosphere`, `ice` and `coupler` directories within the control directory.

Customising the configuring components usually requires in-depth knowledge of the components, and the [Hive Forum](https://forum.access-hive.org.au/) can be a good place to seek advice fromt the wider community and ACCESS-NRI staff.


## Exercise 8: Running a custom configuration

A selection of restart files from the ESM1.6 CMIP7 piControl experiment are available in <!--TODO: fill in location--> LOCATION ON JQ44.

1. Clone the `release-piControl` configuration, and set the compute project to PROJECT
2. Set your experiment to use a selected restart from the above location
3. Set payu to sync the model outputs and restarts to `/g/data/PROJECT/<user>/tutorial_experiments`
4. The pre-industrial atmospheric CO2 MMR of 4.3189e-04 is specified in a setting called `CO2_MMR`. Find where this is set, and change it to a value of your choice
5. Run your simulation – check back tomorrow and if everything has worked you should find a copy of your outputs in `/g/data/PROJECT/<user>/tutorial_experiments`.



## ACCESS-ESM1.6 outputs and the ACCESS-NRI data spec
ACCESS-ESM1.6 is the first model whose outputs adhere to the new ACCESS-NRI data specifications. The goal of these specifications is to ensure that  model output from different ACCESS models have both consistent structure and metadata, and to improve ease of use for working with the data.

Key changes in ACCESS-ESM1.6's output data compared to ESM1.5 include:

- Single variable files are produced for all three model components.
- Outputs for all model components follow a consistent naming scheme, with core metadata embedded in the names. For example:

   - **ocean**: `access-esm1p6.mom5.2d.psiu.1mon.mean.1850.nc`
   - **atmosphere**: `access-esm1p6.um7p3.2d.fld_s03i237.1mon.mean.1850.nc`
   - **ice**:  `access-esm1p6.cice5.3d.siitdconc.1mon.mean.1850.nc`
- Consistent provenance data is added to the netCDF global attributes:
    ```
    :base_configuration = "dev-preindustrial+concentrations" ;
    :contact = "<email-address>" ;
    :Conventions = "CF-1.11,ACDD-1.3" ;
    :data_specification = "ACCESS-Output Data Specification v0.1.0-alpha" ;
    :date_created = "2026-08-11T02:21:26Z" ;
    :date_metadata_modified = "2026-08-11T02:22:15Z" ;
    :date_modified = "2026-08-11T02:22:15Z" ;
    :experiment_repo = "https://github.com/ACCESS-NRI/access-esm1.6-configs" ;
    :experiment_uuid = "0dab21b3-892f-41dd-afb4-21198a7ef648" ;
    ```

Take a look at the output in <!--TODO put some output somewhere accessible--> DIRECTORY to see how the model output data is structured, and feel free to raise any questions with NRI staff. See [the data specifications documentation](https://access-output-data-specifications.readthedocs.io/en/latest/specification/) for further details on the ACCES-NRI data specifications.


## Exercise 9: Runlogs, manifests, and experiment provinence
A core principle of payu's design is to make experiment provenance easy. Payu automatically tracks configuration settings, input, restart, and executable paths throughout an experiment, recording this information with git.

This information can be used in many different ways, an example of which we'll see in the (made up) example of below:


*I've been running a historical simulation using a custom volcanic forcing input file `volcts_cmip7.dat`. I inadvertently modified the file part way through the experiment, and will need to rerun the the years after it changed. Unfortunately, I don't know when during the simulation the input file changed.*

**TODO: move outputs to somewhere accessible**
*Using either the output directories in `/scratch/tm70/sw6175/access-esm/archive/custom_volcanic-custom-volcanic-5a0df8c5`, or the published experiment repository in https://github.com/blimlim/runlog_example, can you work out at which point the volcanic forcing file changed?*,

*Hint: Take a look at the files found in the manifest directories.*


!!! note
    While this example is a little contrived (payu will guard against changes to the input files when the `manifest: reproduce: input: true` option is included in the `config.yaml`), there have been several times during the development of ESM1.6 where the experiment runlogs have been helpful for investigating similar issues. 


## Further resources and getting help

This session has been a brief introduction to running ACCESS-ESM1.6 with payu. We've only had time to introduce the basics, and you may be interested to learn more about creating custom ESM1.6 configurations and more advanced payu features, including:

- Customising submodel configurations
- Modifying model source code and building your own executables
- Controlling model output variables
- Sharing payu experiments with git and GitHub
- Advanced experiment workflows with payu

For details on some of these topics, please take a look at:
- The *How to run ACCESS-ESM1.6* documentation page <!--Add link when ready-->
- The [ACCESS-ESM1.6 configuration docs](https://access-esm1p6-configs.access-hive.org.au/)
- The [payu documentation](https://payu.readthedocs.io/en/stable/)
- For information on the model's scientific configuration, there will be a model description paper published in the future.


ACCESS-NRI staff are also available to answer your questions on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/). If you have any questions related to ACCESS-ESM1.6, you are welcome to add a help request on the Forum.



