[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs

<!--start:cylc8-prerequisites-->
- [hr22](https://my.nci.org.au/mancini/project/hr22/join)
<!--end:cylc8-prerequisites-->

<!--start:cylc8-compatibility-mode-->
!!! warning
   
    {{model}} is transitioning to a _Cylc8_ workflow from a _Cylc7_ workflow. At this point, the configuration is using _Cylc8_ in compatibility-mode with _Cylc7_. This means the configuration can be run with _Cylc7_ or _Cylc8_ to allow experienced users the time to understand how to use _Cylc8_. However, we are only giving the instructions with _Cylc8_ as all users should get familiar with _Cylc8_ as we phase out _Cylc7_.
<!--end:cylc8-compatibility-mode-->

<!--start:cylc8-about-->
The _Rose/Cylc_ workflow management tool consists of two components:

* The [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) (pronounced ‘silk’) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA). _Cylc_ is a workflow manager that automatically executes tasks according to the model's configuration. It also monitors all tasks, reporting any errors that may occur.
* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UKMO which configures tasks for the _Cylc_ engine. _Rose_ is a toolkit that can be used to view, edit and run some of the [ACCESS models](/models/access_models).

A set of tasks configured by _Rose_ to run with the _Cylc8_ engine is called a _workflow_ in _Cylc8_. For coherence with other workflow managers used to run some ACCESS models, we refer to these _workflows_ as _configurations_.
<!--end:cylc8-about-->

### Run directory and files organisation

<!--start:cylc8-expdir-files-->
The data organisation for _Cylc_ was chosen to separate the smaller text files that define a configuration and the larger binary input and output files needed for an experiment.

This means the configuration definition can be tracked with Git, and so is easy to back up and share. It also optimises the use of different filesystems on high-performance computers. Finally, this layout ensures several experiments that share common executables and input data can be run simultaneously.

#### Experiment directory
_Cylc_ creates an _experiment_ directory under `$HOME/cycl-run/`, named from your experiment. This directory is organised as follows:

```
.
├── _cylc-install
├── run1
└── runN -> run1
```

- `_cylc-install` contains a symbolic link to the source of the experiment. This is needed by _Cylc_.
- `run1` is the actual installation of the experiment for _Cylc_. New installations of the experiment will create a new numbered run directory.
- `runN` is a symbolic link that points to the latest installation of the experiment.

#### _Run directory_, `runN`
On _Gadi_, all files created at run time are stored in a location,  determined by the configuration (`root_dir`). This location is usually chosen to be on the `/scratch` filesystem to have a large enough storage space, temporary storage and quick, reliable read and write operations from the PBS scheduler.

The run directory (`run1` in the previous example) contains a copy of the configuration as well as symbolic links to directories under the _tasks work_ directory for easy access. The _tasks work_ directory is the location of the _work_ directories for all experiment's tasks. In this example, the user has chosen to locate their experiment's _work_ directory under `/scratch/$PROJECT/$USER`

```
.
├── run1
│   ├── app
│   ├── bin
│   ├── log -> /scratch/$PROJECT/$USER/cylc-run/{{experiment_name}}/run1/log
│   ├── meta
│   ├── opt
│   ├── README.md
│   ├── rose-suite.conf
│   ├── rose-suite.conf_nci_gadi
│   ├── rose-suite.info
│   ├── share -> /scratch/$PROJECT/$USER/cylc-run/{{experiment_name}}/run1/share
│   ├── site
│   ├── suite.rc
│   ├── suite-tests-graph.rc
│   ├── suite-tests-runtime.rc
│   └── work -> /scratch/$PROJECT/$USER/cylc-run/{{experiment_name}}/run1/work
```

- `log/job/` &rarr; the directory where all the job log files are stored: the job file itself, the job output file and the job error file
- `share/` &rarr; where the tasks can read or write files shared by other tasks

    - `share/data/History_Data/` &rarr; where the simulation output files are located
    - `share/data/History_Data/netCDF` &rarr; where the simulation output files post-processed in netCDF format are located
- `work/` &rarr; contains task work directories, i.e. the current working directories of running tasks. These are removed automatically if empty when a task finishes.
<!--end:cylc8-expdir-files-->

## Access _Rose/Cylc_
<!--start:cylc8-module-->
Make the `rose` and `cylc` executables available by loading the _Cylc_ module:

```
module use /g/data/hr22/modulefiles
module load cylc/8.6.3
```
<!--end:cylc8-module-->

## Validate the configuration

<!--start:cylc8-validate-->
Before running an experiment, it is recommended to validate the configuration to ensure its compatibility with _Cylc_ 8. For this, you can run:

```
cylc validate <experiment-name>
```

??? example "Example: validate local copy"

    To validate a local copy, named {{experiment_name}}, of the configuration {{config_branch}}:

    <terminal-window>
        <terminal-line data="input">cylc validate my-am3-expt</terminal-line>
        <terminal-line>WARNING - Backward compatibility mode ON - support for suite.rc files will be removed at 8.7.0</terminal-line>
        <terminal-line>WARNING - Obsolete config items were automatically deleted. Please check your workflow and remove them permanently.</terminal-line>
        <terminal-line>WARNING - Deprecated config items were automatically upgraded. Please alter your workflow to use the new syntax.</terminal-line>
        <terminal-line>WARNING -  * (8.0.0) [visualization] - DELETED (OBSOLETE)</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][install_ancil][events]mail events: timeout</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][install_ainitial][events]mail events: timeout</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][recon][events]mail events: timeout</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][atmos_main][events]mail events: timeout</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][netcdf_conversion][events]mail events: timeout</terminal-line>
        <terminal-line>WARNING - Invalid event name(s) for [runtime][housekeeping][events]mail events: timeout</terminal-line>
        <terminal-line>Valid for cylc-8.6.3</terminal-line>
    </terminal-window>
<!--end:cylc8-validate-->

## Run the experiment

<!--start:cylc8-run-->
ACCESS model configurations run on _Gadi_ through [PBS jobs][PBS job] submissions. They often comprise several tasks, such as running the model, post-processing the output, etc. For long experiments, the simulation is also split in smaller periods that are run one after the other. _Cylc_ controls the sequence of the tasks and the repetitions.

In _Cylc8_, running a workflow is a two-step process, first you need to install the experiment directory and then run the workflow:

```bash
cylc install <experiment_name>
cylc play <experiment_name>
```

??? example "Example: Running the experiment {{experiment_name}}"

    <terminal-window>
        <terminal-line data="input">cylc install {{experiment_name}}</terminal-line> 
        <terminal-line>WARNING - Backward compatibility mode ON - support for suite.rc files will be removed at 8.7.0</terminal-line>
        <terminal-line>INSTALLED {{experiment_name}}/run1 from \$HOME/roses/{{experiment_name}}</terminal-line>
        <terminal-line data="input">cylc play {{experiment_name}}</terminal-line>
        <terminal-line> ▪ ■  Cylc Workflow Engine 8.6.3</terminal-line> 
        <terminal-line> ██   Copyright (C) 2008-2026 NIWA</terminal-line> 
        <terminal-line>▝▘    & British Crown (Met Office) & Contributors</terminal-line> 
        <terminal-line></terminal-line> 
        <terminal-line>Using the cylc session am3tests.\$USER.\$PROJECT.ps.gadi.nci.org.au</terminal-line> 
        <terminal-line></terminal-line> 
        <terminal-line>Loading cylc/8.6.3</terminal-line> 
        <terminal-line> Loading requirement: mosrs-setup/2.0.1</terminal-line> 
        <terminal-line>INFO - Extracting job.sh to \$HOME/cylc-run/my-am3-expt/run1/.service/etc/job.sh</terminal-line>
</terminal-window>

??? info "Validate, Install and Play in one command `cylc vip`"

    _Cylc_ provides compound commands to make routine operations easier. The `cylc vip` command stands for Validate, Install, Play. It allows to run the workflow in one command:

    ```
    cylc vip <experiment_name>
    ```
<!--end:cylc8-run-->

## Monitor the experiment

<!--start:cylc8-monitor-about-->
_Cylc_ 8 provides three ways to monitor the experiment:

- the command line interface (CLI): You can start, stop, query, and control workflow, in every possible way, from the command line. Use the built-in help of the _Cylc_ commands to learn more on how to use it. 
- the terminal user interface (TUI): it is a graphical interface running in a terminal that is auto-updated by _Cylc_ and allows you to view your experiment, monitor the status of the tasks, access the job log files and interact with the flow of the experiment.
- the graphical user interface (GUI): it has different views you can use to examine your workflows, including a Cylc scan menu allowing you to switch between workflows.

??? info "_Cylc_ TUI"

    To launch the TUI, run `cylc tui`. It will show all the experiments currently running or stopped. You can navigate through the TUI using the keyboard. Keys are indicated at the bottom of the TUI.

??? info "_Cylc_ GUI"

    !!! warning

        The _Cylc_ GUI is only available from the ARE VDI Desktop and not from the _Gadi_ login nodes.

    To launch the _Cylc_ GUI from an ARE VDI terminal, with the _Cylc_ module loaded, simply run:

    ```
    cylc gui
    ```

    You can then navigate between workflows using the list on the left.

??? info "Task and Job states"

    For more information on the symbols and colours used in the TUI and GUI to inform on the tasks and jobs status, please see the [_Cylc_ documentation](https://cylc.github.io/cylc-doc/latest/html/user-guide/running-workflows/tasks-jobs-ui.html#task-job-states)
    
<!--end:cylc8-monitor-about-->
