[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs

<!--start:cylc8-prerequisites-->
- [hr22](https://my.nci.org.au/mancini/project/hr22/join): Cylc Rose Workflow
<!--end:cylc8-prerequisites-->

<!--start:cylc8-compatibility-mode-->
!!! warning
   
    {{model}} is transitioning to a _Cylc8_ workflow from a _Cylc7_ workflow. At this point, the configuration is using _Cylc8_ in compatibility-mode with _Cylc7_. This means the configuration can be run with _Cylc7_ or _Cylc8_ to allow experienced users the time to understand how to use _Cylc8_. However, we are only giving the instructions with _Cylc8_ as all users should get familiar with _Cylc8_ while we phase out _Cylc7_.
<!--end:cylc8-compatibility-mode-->

<!--start:cylc8-about-->
The _Rose/Cylc_ workflow management tool consists of two components:

* The [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) (pronounced ‘silk’) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA). _Cylc_ is a workflow manager that automatically executes tasks according to the model's configuration. It also monitors all tasks, reporting any errors that may occur.
* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UKMO which configures tasks for the _Cylc_ engine. _Rose_ is a toolkit that can be used to view, edit and run some of the [ACCESS models](/models/access_models).

A set of tasks configured by _Rose_ to run with the _Cylc8_ engine is called a _workflow_ in _Cylc8_. For coherence with other workflow managers used to run some ACCESS models, we refer to these _workflows_ as _configurations_.
<!--end:cylc8-about-->

<!--start:cylc8-structure-->
### _Rose/Cylc_ directory and files organisation

A _Cylc_ experiment defines individual tasks as well as the relationship between these tasks, creating a tasks graph. Each task is given a name in the experiment. Using that graph, _Cylc_ can execute the tasks at the right time and in the right order. It is also possible to define a repetition sequence for a whole (or part) of a graph. This is used for {{model}} to manage simulations that are too long to be run in a single PBS script. _Cylc_ supports several installations of the same experiment. By default, these will be installed in numbered directories by default (`run1`, `run2`, etc.). _Cylc_ provides a symbolic link to the latest installation named `runN`. This can be useful when developing an experiment and testing incremental changes or for running sensitivity studies.

The data organisation for _Cylc_ was chosen to separate the smaller text files that define a configuration and the larger binary input and output files needed for an experiment.

This means the configuration definition can be tracked with _Git_, and so is easy to back up and share. It also optimises the use of different filesystems on high-performance computers. Finally, this layout ensures several experiments that share common executables and input data can be run simultaneously.

A representation of the data organisation for _Cylc_ is given in the following diagram:

<!-- Diagram created by draw.io. The SVG contains the graphic in XML format and can be opened in https://app.diagrams.net/ for editing (no account required) -->
![cylc directory structure](/assets/cylc_file_org.drawio.svg){: class="example-img" loading="lazy"}

As shown in the diagram, the general layout of a _Cylc_-supported model run consists of three main directories:

- The _configuration_ directory contains a copy of the configuration. This should be a _git_ repository and can be used to implement your own configuration modifications and record them via _git_. This directory is created by the user.
- The _control_ directory contains the model configuration and is the directory from which the model run is started. This directory contains information to manage the simulation and the scientific options that define the algorithms used in the model component or the diagnostics saved by the model component. This directory is created by _Cylc_. In the _control_ directory, you will find:

     - A copy of all the configuration files
     - Model components' configuration files, which are used to define the physics and the components' internal state used in the simulation.

- The _experiment_ directory contains all data from the experiment. This directory is created and managed by _Cylc_. Inside the _experiment_ directory, there are three subdirectories of particular interest: 
    - _log/job_ &rarr; contains the jobs' script and output and error log files for all the tasks of the _experiment_.
    - _share_ &rarr; contains data shared between tasks. Importantly, it contains the output of the model and the logs from the compilation.

        - `share/data/History_Data/` &rarr; where the simulation output files are located
        - `share/data/History_Data/netCDF` &rarr; where the simulation output files post-processed in netCDF format are located

    - _work_ &rarr; contains the current working directories of running tasks. These are removed automatically if empty when a task finishes.
    
    The _log_, _share_ and _work_ directories for an experiment are most easily accessed through the symbolic links created in the _control_ directory.

!!! tip 

    Recommended location of the _control_ and _experiment_ directories on _Gadi_.

    - _configuration_ directories. These directories should be created under $HOME/roses. This will ensure _Cylc_ can find them easily.
    - _control_ directories. These directories will be created under $HOME/cylc-run. The 10GB quota on $HOME should be sufficient as _control_ directories only contain text files and symbolic links and, hence, occupy less than 10MB.
    - _experiment_ directories. For these, `/scratch` is recommended as it is optimised for fast reading and writing of large data, and adequate space is available for large model output.

!!! warning
    Files on the `/scratch` drive, such as the _experiment_ directory, might be deleted if not accessed for [some time](https://opus.nci.org.au/spaces/Help/pages/156434436/Gadi+scratch+File+Management). All experiments which are to be kept should be moved to `/g/data/`.

#### Output and restart files organisation {: .no-toc}

The diagnostics data from the UM model is output in binary format. The output in the raw format can be found under `share/data/History_Data/`. The data is post-processed by the _experiment_ into netCDF format. This data can be found under `share/data/History_Data/netCDF`. 

The restart file from the UM model is named, `<short-name>a.astart` where \<short-name\> is a short version of the experiment name. It can be found under `share/data`.

#### Error and output log files {: .no-toc}

The log files are located under the _log_ and _work_ directories that can be accessed from the _control_ directory.

- *Task logs under `log/jobs`*

    All the tasks are run via job scripts whether they run locally or in a PBS job. You can find the job's script and output and error logs in directories following the pattern:
    
    `job/<timestamp>/<task_name>/<run_attempt>`

    Where:

    - \<timestamp> is the cycle point
    - \<task_name> is the name of the task
    - \<run_attempt> is the run attempt of the task, with NN symlinked to the latest attempt

    For example, if you are looking for the error log file of the _housekeeping_ task for the latest installation of the experiment and the simulation period starting on 1999-03-00, the file will be under: _log/job/19990300T0000Z/housekeeping/NN_.

    After completion of a job, the following files are produced:
    
    - _job_: The script used to run the task.
    - _job.out_: The standard output of the job.
    - _job.error_: Error messages from the job.
    - _job-activity.log_: Event history of the job on the scheduler.
    - _job.status_: The current status of the job.

    These files are the first place to look when diagnosing model issues.

- *Model log files for the UM and the reconfiguration*

    The model log files can be found under _work/\<timestamp>/\<task_name>/pe_output_ where:

    - \<timestamp> is the cycle point
    - \<task_name> is the name of the task

    These logs contain timestep-by-timestep output and is where most model-level errors appear (e.g. instabilities, failed reads of ancillary files) and may help to diagnose your issue.

- *PBS Logs*

   For a given task, the PBS log (sometimes referred to as "PBS out") is located in the `job.out` file as described above and can be used to retrieve PBS-level information about walltime, memory, and exit codes.
<!--end:cylc8-structure-->

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
Before running an experiment, it is recommended to validate the configuration to ensure its compatibility with _Cylc8_. For this, you can run:

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
_Cylc8_ provides three ways to monitor the experiment:

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

??? info "Task and Job status"

    For more information on the symbols and colours used in the TUI and GUI to inform on the tasks and jobs status, please see the [_Cylc_ documentation](https://cylc.github.io/cylc-doc/latest/html/user-guide/running-workflows/tasks-jobs-ui.html#task-job-states)
    
<!--end:cylc8-monitor-about-->
