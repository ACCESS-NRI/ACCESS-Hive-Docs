{% set model = "ACCESS-CM2" %}
{% set suite_id = "u-cy339" %}
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[model components]: /models/access_models/access-cm/#model-components

# Run {{ model }}
!!! danger
    ACCESS-NRI does not maintain an official {{model}} release, but we continue to support the community in using this model where possible.

!!! warning
    **Important for _accessdev_ users!**<br>
    If you were an _accessdev_ user, make sure you are a member of [hr22](https://my.nci.org.au/mancini/project/hr22/join) and [ki32](https://my.nci.org.au/mancini/project/ki32/join) projects.<br>
    Then, refer to instructions on how to [Set up persistent session workflow for {{ model }}]({{ '#set-up-%s-persistent-session'%model.lower() }}), and how to [port suites from accessdev](#port-suites-from-accessdev).

## Prerequisites

- **NCI Account**<br> 
    Before running {{ model }}, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **_MOSRS_ account**<br>
    The [Met Office Science Repository Service (MOSRS)](https://code.metoffice.gov.uk) is a server run by the UK Met Office (UKMO) to support collaborative development with other partners organisations. MOSRS contains the source code and configurations for some model components in {{ model }} (e.g., the [UM](/models/model_components/atmosphere/#unified-model-um)).<br>
    To apply for a _MOSRS_ account, please contact your [local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
    {: #mosrs-account}

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [access](https://my.nci.org.au/mancini/project/access/join)
    - [hr22](https://my.nci.org.au/mancini/project/hr22/join)
    - [ki32](https://my.nci.org.au/mancini/project/ki32/join)
    - [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
    
    !!! tip
        To request membership for the _ki32_mosrs_ subproject, you need to:
        
        - already be member of the _ki32_ project
        {: style="list-style-type: disc"}
        - have a [MOSRS account](#mosrs-account)
        {: style="list-style-type: disc"}

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

- **Connection to an ARE VDI Desktop (optional)**<br>
    To run {{ model }}, start an [Australian Research Environment (ARE) VDI Desktop](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) session.<br>
    If you are not familiar with ARE, check out the [Getting Started on ARE](/getting_started/are) section.

## Set up an ARE VDI Desktop (optional)
To skip this step and instead run {{ model }} from _Gadi_ login node, refer to instructions on how to [Set up {{ model }} persistent session]({{ '#set-up-%s-persistent-session'%model.lower() }}).

### Launch ARE VDI Session
Go to the [ARE VDI](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) page and launch a session with the following entries:

- **Walltime (hours)** &rarr; `2`<br>
    This is the amount of time the ARE VDI session will stay active for.<br>
    {{ model }} does not run directly on ARE.<br>
    This means that the ARE VDI session only needs to carry out setup steps as well as starting the run itself. All these tasks can be done within 2 hours.
    
- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>
    As mentioned above, the ARE VDI session is only needed for setup and startup tasks, which can be easily accomplished with 1 CPU.

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated _Service Units (SU)_ to run your simulation. Usually, but not always, this corresponds to your `$PROJECT`.<br>
    For more information, refer to how to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

- **Storage** &rarr; `gdata/access+gdata/hh5+gdata/hr22+gdata/ki32` (minimum)<br>
    This is a list of all project data storage, joined by plus (`+`) signs, needed for the {{ model }} simulation. In ARE, storage locations need to be explicitly defined to access data from within a VDI instance.<br>
    Every {{ model }} simulation can be unique and input data can originate from various sources. Hence, if your simulation requires data stored in project folders other than `access`, `hh5`, `hr22` or `ki32`, you need to add those projects to the storage path.<br>
    For example, if your {{ model }} simulation requires data stored in `/g/data/tm70` and `/scratch/w40`, your full storage path will be: `gdata/access+gdata/hh5+gdata/hr22+gdata/ki32+gdata/tm70+scratch/w40`
    
Launch the ARE session and, once it starts, click on _Launch VDI Desktop_.

![Launch ARE VDI session example](/assets/run_access_cm/launch_are_vdi.gif){: class="example-img" loading="lazy"}

### Open the terminal in the VDI Desktop
Once the new tab opens, you will see a Desktop with a few folders on the left.<br>
To open the terminal, click on the black terminal icon at the top of the window. You should now be connected to a _Gadi_ computing node.

![Open ARE VDI terminal example](/assets/run_access_cm/open_are_vdi_terminal.gif){: class="example-img" loading="lazy"}

## Set up {{ model }} persistent session
To support the use of long-running processes, such as ACCESS model runs, NCI provides a service on _Gadi_ called [persistent sessions](https://opus.nci.org.au/display/Help/Persistent+Sessions).

To run {{ model }}, you need to start a persistent session and set it as the target session for the model run.

### Start a new persistent session
To start a new persistent session on _Gadi_, using either a login node or an ARE terminal instance, run the following command:
```
persistent-sessions start <name>
```

This will start a persistent session with the given `name` that runs under your [default project](/getting_started/set_up_nci_account#change-default-project-on-gadi).<br>
If you want to assign a different project to the persistent session, use the option `-p`:
```
persistent-sessions start -p <project> <name>
```

!!! tip
    While the project assigned to a persistent session does not have to be the same as the project used to run the {{ model }} configuration, it does need to have allocated _Service Units (SU)_.<br>
    For more information, check how to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

<terminal-window data="input">
    <terminal-line>persistent-sessions start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

To list all active persistent sessions run:
```
persistent-sessions list
```

<terminal-window data="input">
    <terminal-line>persistent-sessions list</terminal-line>
    <terminal-line data="output">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;UUID&emsp;&emsp;PROJECT&emsp;&ensp;&ensp;ADDRESS&emsp;&emsp;&emsp;&emsp;CPUTIME&emsp;MEMORY</terminal-line>
    <terminal-line data="output">&lt;persistent-session-uuid&gt;&emsp;&lt;project&gt;&emsp;10.9.0.62&emsp;00:00:05.213&emsp;30.5M</terminal-line>
</terminal-window>


The label of a newly-created persistent session has the following format: <br>
`<name>.<$USER&gt;.<project>.ps.gadi.nci.org.au`.

### Specify {{ model }} target persistent session

After starting the persistent session, it is essential to assign it to the {{ model }} run.<br>
The easiest way to do this is to insert the persistent session label into the file `~/.persistent-sessions/cylc-session`.<br>
You can do it manually, or by running the following command (by substituting `<name>` with the name given to the persistent session, and `<project>` with the project assigned to it):
```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

For example, if the user `abc123` started a persistent session named `cylc` under the project `xy00`, the command will be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< cylc.abc123.xy00.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">cylc.abc123.xy00.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

For more information on how to specify the target session, refer to [Specify Target Session with Cylc7 Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites#RunCylc7Suites-SpecifyTargetSession).

!!! tip
    You can simultaneously submit multiple {{ model }} runs using the same persistent session without needing to start a new one. Hence, the process of specifying the target persistent session for {{ model }} should only be done once.<br>
    After specifying the {{ model }} target persistent session the first time, to run {{ model }} you just need to make sure to have an active persistent session named like the specified {{ model }} target persistent session.

### Terminate a persistent session
To stop a persistent session, run:
```
persistent-sessions kill <persistent-session-uuid>
```
!!! warning
    When you terminate a persistent session, any model running on that session will stop. Therefore, you should check whether you have any active model runs before terminating a persistent session.

## Rose/Cylc/MOSRS setup

To run {{ model }}, access to multiple software and MOSRS authentication is needed.

### Cylc setup {: #cylc }

[_Cylc_](https://cylc.github.io/cylc-doc/7.8.8/html/index.html) (pronounced ‘silk’) is a workflow manager that automatically executes tasks according to the model's main cycle script `suite.rc`. _Cylc_ controls how the job will be run and manages the time steps of each model component. It also monitors all tasks, reporting any errors that may occur.

To get the _Cylc_ setup required to run {{ model }}, execute the following commands:
```
module use /g/data/hr22/modulefiles
module load cylc7
```
<terminal-window data="input">
    <terminal-line>module use /g/data/hr22/modulefiles</terminal-line>
    <terminal-line>module load cylc7</terminal-line>
    <terminal-line data="output">Using the cylc session &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="output"></terminal-line>
    <terminal-line data="output">Loading cylc7/24.03</terminal-line>
    <terminal-line data="output">&emsp;Loading requirement: mosrs-setup/2.0.1</terminal-line>
</terminal-window>

!!! warning
    _Cylc_ version >= `cylc7/24.03` required.<br>
    
    Also, before loading the _Cylc_ module, make sure to have started a _persistent session_ and have assigned it to the {{ model }} workflow. For more information about these steps, refer to [Set up {{ model }} persistent session]({{ '#set-up-%s-persistent-session'%model.lower() }}).

### Rose setup {: #rose }
[Rose](http://metomi.github.io/rose/doc/html/index.html) is a toolkit that can be used to view, edit, or run an ACCESS modelling suite.

By completing the [_Cylc_ setup](#cylc), also _Rose_ will be automatically available. Hence, no additional step is required.

### MOSRS authentication
To authenticate using your _MOSRS_ credentials, run:
```
mosrs-auth
```
<terminal-window>
    <terminal-line data="input">mosrs-auth</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: You need to enter your MOSRS credentials here so that GPG can cache your password.</terminal-line>
    <terminal-line>Please enter the MOSRS password for &lt;MOSRS-username&gt;:</terminal-line>
    <terminal-line lineDelay=1500>Checking your credentials using Subversion. Please wait.</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: Successfully accessed Subversion with your credentials.</terminal-line>
    <terminal-line lineDelay=100><span style="color: #559cd5;">INFO</span>: Checking your credentials using rosie. Please wait.</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: Successfully accessed rosie with your credentials.</terminal-line>
</terminal-window>

!!! warning
    This step needs to be done once for each new session (e.g., _Gadi_ login, _ARE_ terminal window)

## Get {{ model }} suite
{{ model }} comprises the model components [UM](/models/model_components/atmosphere#unified-model-um), [MOM](/models/model_components/ocean#modular-ocean-model-mom), [CICE](/models/model_components/sea-ice#cice) and [CABLE](/models/model_components/land#cable), coupled through [OASIS](/models/model_components/coupler#oasis3-mct). These components, which have different model parameters, input data and computer-related information, need to be packaged together as a _suite_ in order to run.<br>
Each {{ model }} suite has a `suite-ID` in the format `u-<suite-name>`, where `<suite-name>` is a unique identifier.<br>
For this example you can use `{{ suite_id }}`, which is a pre-industrial experiment suite.

Typically, an existing suite is copied using _Rosie_ and then edited as needed for a particular run.
[Rosie](https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rosie) is an [SVN](https://subversion.apache.org) repository wrapper with a set of options specific for ACCESS modelling suites. It is automatically available within the [_Rose_ setup](#rose).

{{ model }} configuration can be copied from the MOSRS repository in 2 ways:

- [Local-only copy](#local-copy)
- [Remote and local copy](#remote-copy)

Suites are, by default, created in the user's _Gadi_ home directory under `~/roses/<suite-ID>`.
This path will be referred to as the *suite directory*.
{: #suitedir }

The suite directory contains multiple subdirectories and files, including:

- `app` &rarr; directory containing the configuration files for various tasks within the suite.
- `meta` &rarr; directory containing the GUI metadata.
- `rose-suite.conf` &rarr; main suite configuration file.
- `rose-suite.info` &rarr; suite information file.
- `suite.rc` &rarr; _Cylc_ control script file (Jinja2 language).

### Local-only copy {: #local-copy }
To create a _local copy_ of {{ model }} suite from MOSRS repository, run:
```
rosie checkout {{ suite_id }}
```
<terminal-window>
    <terminal-line data="input">rosie checkout {{ suite_id }}</terminal-line>
    <terminal-line>[INFO] create: /home/565/&lt;$USER&gt;/roses</terminal-line>
    <terminal-line>[INFO] &lt;suite-ID&gt;: local copy created at /home/565/&lt;$USER&gt;/roses/{{ suite_id }}</terminal-line>
</terminal-window>
This option is mostly used for testing and examining suites.
    
### Remote and local copy {: #remote-copy }
To create a new copy of {{ model }} suite both _locally_ and _remotely_ in the MOSRS repository, run: 
```
rosie copy {{ suite_id }}
```
<terminal-window>
    <terminal-line data="input">rosie copy {{ suite_id }}</terminal-line>
    <terminal-line>Copy "{{ suite_id }}/trunk@&lt;trunk-ID&gt;" to "u-?????"? [y or n (default)]</terminal-line> <terminal-line data="input">y</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-ID&gt;: created at https://code.metoffice.gov.uk/svn/roses-u/&lt;suite-n/a/m/e/&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-ID&gt;: copied items from {{ suite_id }}/trunk@&lt;trunk-ID&gt;</terminal-line>
    <terminal-line>[INFO] {{ suite_id }}: local copy created at /home/565/&lt;$USER&gt;/roses/&lt;new-suite-ID&gt;</terminal-line>
</terminal-window>
When a new suite is created in this way, a _unique_ `<suite-ID>` folder is generated within the MOSRS repository and populated with descriptive information about the suite and its initial configuration.

For additional `rosie` options, run:
```
rosie help
```

## Edit {{ model }} suite configuration

This section describes how to modify the {{ model }} configuration.

The modifications discussed in this section can change the way {{ model }} is run, or how specific [model components] are configured and coupled together.

In general, ACCESS modelling suites can be edited either by directly modifying the configuration files within the suite directory, or by using the [_Rose_ GUI](#rosegui).

!!! warning
    Unless you are an experienced user, directly modifying configuration files is usually discouraged to avoid encountering errors.

### Rose GUI {: #rosegui }
To open the [_Rose_](#rose) GUI, run the following command from within the [suite directory](#suitedir): 
```
rose edit &
```

!!! tip
    The `&` is optional. It allows the terminal prompt to remain active while running the `Rose` GUI as a separate process in the background.

<terminal-window>
    <terminal-line data="input">cd ~/roses/&lt;suite-ID&gt;</terminal-line>
    <terminal-line data="input" directory="~/roses/&lt;suite-ID&gt;">rose edit &</terminal-line>
    <terminal-line class="ls-output-format">[&lt;N&gt;] &lt;PID&gt;</terminal-line>
    <terminal-line data="input" directory="~/roses/&lt;suite-ID&gt;"></terminal-line>
    <img src="/assets/run_access_cm/Rose_GUI_are.png" alt="Rose GUI" imageTime="inf" loading="lazy">
</terminal-window>
    
### Change NCI project
To ensure that your suite is run under the correct NCI project for which you are a member, edit the _Compute project_ field in _suite conf &rarr; Machine and Runtime Options_, and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}. 

For example, to run an {{ model }} suite under the `tm70` project (ACCESS-NRI), enter `tm70` in the _Compute project_ field:
![Rose change project example](/assets/run_access_cm/rose_change_project_are.gif){: class="example-img" loading="lazy"}

!!! warning
    To run {{ model }}, you need to be a member of a project with allocated _Service Units (SU)_. For more information, check how to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

### Change run length and cycling frequency

!!! warning
    Note there is a [known issue](#issues-cycling-repro) related to changing the cycling frequency. {{ model }} does not give identical results with different cycling frequencies. For example, one cycle of 12 months will not produce identical output to 12 cycles of one month. When comparing multiple experiments, they should use the same cycling frequency.

{{ model }} suites are often run in multiple steps, each one constituting a cycle. The job scheduler resubmits the suite every chosen _Cycling frequency_ until the _Total Run length_ is reached. 

To modify these parameters, navigate to _suite conf &rarr; Run Initialisation and Cycling_, edit the respective fields (using [ISO 8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format) and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

For example, to run a suite for a total of 50 years with a 1-year job resubmission, change _Total Run length_ to `P50Y` and _Cycling frequency_ to `P1Y` (the maximum _Cycling frequency_ is currently two years):

![Rose change run length example](/assets/run_access_cm/rose_change_run_length_are.gif){: class="example-img" loading="lazy"}

### Change wallclock time
The _Wallclock time_ is the time requested by the [PBS job] to run a single cycle. If this time is insufficient for the suite to complete a cycle, your job will be terminated before completing the run. Hence, if you change the _Cycling frequency_, you may also need to change the _Wallclock time_ accordingly. While the time required for a suite to complete a cycle depends on several factors, a good estimation is 4 hours per simulated year.

To modify the _Wallclock time_, edit the respective field in _suite conf &rarr; Run Initialisation and Cycling_ (using [ISO 8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format) and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

### Change warm restart date
This {{ model }} configuration uses initial conditions from a previous {{ model }} simulation, a process known as _warm restart_.<br>
The specific date of the initial conditions is set using the _Warm restart date_ parameter, formatted as `YYYYMMDD`.

To modify the _Warm restart date_, edit the respective field in _suite conf &rarr; Run Initialisation and Cycling_ and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.


## Run {{ model }} suite
{{ model }} suites run on [_Gadi_](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview) through a [PBS job] submission.<br>
When the suite runs, its configuration files are copied on _Gadi_ inside `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>` and a symbolic link to this directory is also created in the `$USER`'s home directory under `~/cylc-run/<suite-ID>`.<br>
An {{ model }} suite comprises several tasks, such as checking out code repositories, compiling and building the different model components, running the model, etc. The workflow of these tasks is controlled by _Cylc_.

### Cylc
[`Cylc`](https://cylc.github.io/cylc-doc/7.8.8/html/index.html) (pronounced ‘silk’) is a workflow manager that automatically executes tasks according to the model's main cycle script `suite.rc`. _Cylc_ controls how the job will be run and manages the time steps of each submodel. It also monitors all tasks, reporting any errors that may occur.

To run an {{ model }} suite run the following command from within the suite directory:
```
rose suite-run
```

After the initial tasks are executed, the _Cylc_ GUI will open. You can now view and control the different tasks in the suite as they are run:
<terminal-window lineDelay="50">
    <terminal-line data="input" lineDelay="300">cd ~/roses/&lt;suite-ID&gt;</terminal-line>
    <terminal-line data="input" directory="~/roses/&lt;suite-ID&gt;" lineDelay="300">rose suite-run</terminal-line>
    <terminal-line>[INFO] export CYLC_VERSION=7.9.7</terminal-line>
    <terminal-line>export ROSE_ORIG_HOST=&lt;gadi-cpu&gt;.gadi.nci.org.au</terminal-line>
    <terminal-line>[INFO] export ROSE_SITE=nci</terminal-line>
    <terminal-line>[INFO] export ROSE_VERSION=2019.01.7</terminal-line>
    <terminal-line>[INFO] create: /home/565/&lt;$USER&gt;/cylc-run/&lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO] create: log.&lt;timestamp&gt;</terminal-line>
    <terminal-line>[INFO] symlink: log.&lt;timestamp&gt; <= log</terminal-line>
    <terminal-line>[INFO] create: log/suite</terminal-line>
    <terminal-line>[INFO] create: log/rose-conf</terminal-line>
    <terminal-line>[INFO] symlink: rose-conf/&lt;timestamp&gt;-run.conf <= log/rose-suite-run.conf</terminal-line>
    <terminal-line>[INFO] symlink: rose-conf/&lt;timestamp&gt;-run.version <= log/rose-suite-run.version</terminal-line>
    <terminal-line>[INFO] create: meta</terminal-line>
    <terminal-line>[INFO] install: meta</terminal-line>
    <terminal-line>&emsp;&emsp;&emsp;&emsp;source: /home/565/&lt;$USER&gt;/roses/&lt;suite-ID&gt;/meta</terminal-line>
    <terminal-line>[INFO] install: rose-suite.info</terminal-line>
    <terminal-line>&emsp;&emsp;&emsp;&emsp;source: /home/565/&lt;$USER&gt;/roses/&lt;suite-ID&gt;/rose-suite.info</terminal-line>
    <terminal-line>[INFO] create: app</terminal-line>
    <terminal-line>[INFO] install: app</terminal-line>
    <terminal-line>&emsp;&emsp;&emsp;&emsp;source: /home/565/&lt;$USER&gt;/roses/&lt;suite-ID&gt;/app</terminal-line>
    <terminal-line>[INFO] install: suite.rc</terminal-line>
    <terminal-line>[INFO] REGISTERED &lt;suite-ID&gt; -> /home/565/&lt;$USER&gt;/cylc-run/&lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO] create: share</terminal-line>
    <terminal-line>[INFO] create: share/cycle</terminal-line>
    <terminal-line>[INFO] create: work</terminal-line>
    <terminal-line>[INFO] chdir: log/</terminal-line>
    <terminal-line>[WARN] Using the cylc session &lt;persistent-session-full-name&gt;</terminal-line>
    <terminal-line>[WARN]</terminal-line>
    <terminal-line>[WARN] Loading cylc7/23.09</terminal-line>
    <terminal-line>[WARN] &emsp;Loading requirement: mosrs-setup/1.0.1</terminal-line>
    <terminal-line>[INFO] &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&thinsp;&thinsp;.&UnderBar;.</terminal-line>
    <terminal-line>[INFO] &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&thinsp;&thinsp;| |&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;The Cylc Suite Engine [7.9.7]</terminal-line>
    <terminal-line>[INFO] .&UnderBar;&UnderBar;&UnderBar;&UnderBar;&UnderBar;.&UnderBar;. .&UnderBar;| |&UnderBar;&UnderBar;&UnderBar;&UnderBar;&UnderBar;.&emsp;&emsp;&emsp;&emsp;&emsp;&thinsp;Copyright (C) 2008-2019 NIWA</terminal-line>
    <terminal-line>[INFO] | .&UnderBar;&UnderBar;&UnderBar;| | | | | .&UnderBar;&UnderBar;&UnderBar;|&emsp;& British Crown (Met Office) & Contributors.</terminal-line>
    <terminal-line>[INFO] | !&UnderBar;&UnderBar;&UnderBar;| !&UnderBar;! | | !&UnderBar;&UnderBar;&UnderBar;. &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar; &UnderBar;</terminal-line>
    <terminal-line>[INFO] !&UnderBar;&UnderBar;&UnderBar;&UnderBar;&UnderBar;!&UnderBar;&UnderBar;&UnderBar;. |&UnderBar;!&UnderBar;&UnderBar;&UnderBar;&UnderBar;&UnderBar;! This program comes with ABSOLUTELY NO WARRANTY;</terminal-line>
    <terminal-line>[INFO] &emsp;&emsp;&emsp;&thinsp;.&UnderBar;&UnderBar;&UnderBar;! | &emsp;&emsp;&emsp;&emsp;&emsp;see `cylc warranty`. &thinsp;It is free software, you</terminal-line>
    <terminal-line>[INFO] &emsp;&emsp;&emsp;&thinsp;!&UnderBar;&UnderBar;&UnderBar;&UnderBar;&UnderBar;! &emsp;&emsp;&emsp;&emsp;&emsp;&thinsp;are welcome to redistribute it under certain</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] *** listening on https://&lt;persistent-session-full-name&gt;:&lt;port&gt;/ ***</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] To view suite server program contact information:</terminal-line>
    <terminal-line>[INFO]  $ cylc get-suite-contact &lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] Other ways to see if the suite is still running:</terminal-line>
    <terminal-line>[INFO]  $ cylc scan -n '&lt;suite-ID&gt;' &lt;persistent-session-full-name&gt;</terminal-line>
    <terminal-line>[INFO]  $ cylc ping -v --host=&lt;persistent-session-full-name&gt; &lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO]  $ ps -opid,args &lt;PID&gt;  # on &lt;persistent-session-full-name&gt;</terminal-line>
    <img src="/assets/run&UnderBar;access_cm/Cylc_GUI_are.png" alt="Cylc GUI" imageTime="inf" loading="lazy"> -->
</terminal-window>

!!! warning
    After running the command `rose suite-run`, if you get an error similar to the following:
    <pre><code><span style="color: orangered">[FAIL]</span> Suite "&lt;suite-ID&gt;" appears to be running:
    <span style="color: orangered">[FAIL]</span> Contact info from: "/home/565/&lt;$USER&gt;/cylc-run/&lt;suite-ID&gt;/.service/contact"
    <span style="color: orangered">[FAIL]</span>    CYLC_SUITE_HOST=&lt;persistent-session-full-name&gt;
    <span style="color: orangered">[FAIL]</span>    CYLC_SUITE_OWNER=&lt;$USER&gt;
    <span style="color: orangered">[FAIL]</span>    CYLC_SUITE_PORT=&lt;port&gt;
    <span style="color: orangered">[FAIL]</span>    CYLC_SUITE_PROCESS=&lt;PID&gt; /g/data/hr22/apps/cylc7/bin/python -s /g/data/hr22/apps/cylc7/cylc_7.9.7/bin/cylc-run &lt;suite-ID&gt; --host=localhost
    <span style="color: orangered">[FAIL]</span> Try "cylc stop '&lt;suite-ID&gt;'" first?</code></pre>
    you should run (by substituting `<suite-ID>` with the _suite-ID_):
    ```
    rm "/home/565/${USER}/cylc-run/<suite-ID>/.service/contact"
    ```
    before running the `rose suite-run` command again.

You are done!

If you do not get any errors, you can check the suite output files after the run is complete.<br>
You can now close the _Cylc_ GUI. To open it again, run the following command from within the suite directory:
```
rose suite-gcontrol
```

## Monitor {{ model }} runs
### Check for errors
It is quite common, especially during the first few runs, to experience errors and job failures. Running an {{ model }} suite involves the execution of several tasks, and any of these tasks could fail. When a task fails, the suite is halted and a red icon appears next to the respective task name in the _Cylc_ GUI.<br>
To investigate the cause of a failure, we need to look at the logs `job.err` and `job.out` from the suite run. There are two main ways to do so:

#### Using the _Cylc_ GUI {: .no-toc }
Right-click on the task that failed and click on _View Job Logs (Viewer) &rarr; job.err_ (or _job.out_).<br>
To access a specific task, click on the arrow next to the task to extend the drop-down menu with all the subtasks.

![Investigate Error GUI example](/assets/run_access_cm/investigate_error_gui_are.gif){: class="example-img" loading="lazy"}
    
#### Through the suite directory {: .no-toc }
The suite's log directories are stored in `~/cylc-run/<suite-ID>` as `log.<TIMESTAMP>`, and the latest set of logs are also symlinked in the `~/cylc-run/<suite-ID>/log` directory.<br>
The logs for the main job can be found in the `~/cylc-run/<suite-ID>/log/job` directory.<br>
Logs are separated into simulation cycles according to their starting dates, then divided into subdirectories according to the task name. They are then further separated into "attempts" (consecutive failed/successful tasks), where `NN` is a symlink to the most recent attempt.

In the example above, a failure occurred for the _09500101_ simulation cycle (i.e. starting date: 1st January 950) in the _coupled_ task. Hence, the `job.err` and `job.out` files can be found in the `~/cylc-run/<suite-ID>/log/job/09500101/coupled/NN` directory.
<terminal-window>
    <terminal-line data="input">cd ~/cylc-run/&lt;suite-ID&gt;</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;">ls</terminal-line>
    <terminal-line class="ls-output-format">app cylc-suite.db log log.20230530T051952Z meta rose-suite.info share suite.rc suite.rc.processed work</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;">cd log</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log">ls</terminal-line>
    <terminal-line class="ls-output-format">db job rose.conf rose-suite-run.conf rose-suite-run.locs rose-suite-run.log rose-suite-run.version suite suiterc</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log">cd job</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job">ls</terminal-line>
    <terminal-line class="ls-output-format">09500101</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job">cd 09500101</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job/09500101">ls</terminal-line>
    <terminal-line class="ls-output-format">coupled fcm_make2_um fcm_make_um install_warm make2_mom make_mom fcm_make2_drivers fcm_make_drivers install_ancil make2_cice make_cice</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job/09500101">cd coupled</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job/09500101/coupled">ls</terminal-line>
    <terminal-line class="ls-output-format">01 02 03 NN</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job/09500101">cd NN</terminal-line>
    <terminal-line data="input" directory="~/cylc-run/&lt;suite-ID&gt;/log/job/09500101/NN">ls</terminal-line>
    <terminal-line class="ls-output-format">job job-activity.log job.err job.out job.status</terminal-line>
</terminal-window>

### Model Live Diagnostics

ACCESS-NRI developed the [Model Live Diagnostics](/model_evaluation/evaluation_on_gadi/model_live_diagnostics) framework to check, monitor, visualise, and evaluate model behaviour and progress of ACCESS models currently running on _Gadi_.<br>
For a complete documentation on how to use this framework, check the [Model Live Diagnostics documentation](https://med-live-diagnostics.readthedocs.io/en/latest/index.html).

## Stop, restart and reload suites
In some cases, you may want to control the running state of a suite.<br>
If your _Cylc_ GUI has been closed and you are unsure whether your suite is still running, you can scan for active suites and reopen the GUI if desired.<br>
To scan for active suites, run:
```
cylc scan
```
To reopen the _Cylc_ GUI, run the following command from within the suite directory:
```
rose suite-gcontrol
```
<terminal-window>
    <terminal-line data="input">cylc scan</terminal-line>
    <terminal-line>&lt;suite-ID&gt; &lt;$USER&gt;@&lt;gadi-cpu&gt;.nci.org.au:&lt;port&gt;</terminal-line>
    <terminal-line data="input">cd ~/roses/&lt;suite-ID&gt;</terminal-line>
    <terminal-line data="input" directory="~/roses/&lt;suite-ID&gt;">rose suite-gcontrol</terminal-line>
    <img src="/assets/run_access_cm/Cylc_GUI_are.png" alt="Cylc GUI" imageTime="inf" loading="lazy">
</terminal-window>

### STOP a suite
To shutdown a suite in a safe manner, run the following command from within the suite directory:
```
rose suite-stop -y
```
Alternatively, you can directly kill the PBS job(s) connected to your run. To do so:

1. Check the status of all your PBS jobs:
```
qstat -u $USER
```

2. Delete any job related to your run:
```
qdel <job-ID>
```

### RESTART a suite
There are two main ways to restart a suite:

#### _SOFT_ restart {: .no-toc }
To reinstall the suite and reopen _Cylc_ in the same state it was prior to being stopped, run the following command from within the suite directory:
```
rose suite-run --restart
```

!!! warning
    You may need to manually trigger failed tasks from the _Cylc_ GUI.

<terminal-window lineDelay="50">
    <terminal-line data="input" lineDelay="300">cylc</terminal-line>
    <terminal-line data="input" lineDelay="300">cd ~/roses/&lt;suite-ID&gt;</terminal-line>
    <terminal-line data="input" directory="~/roses/&lt;suite-ID&gt;" lineDelay="300">rose suite-run --restart</terminal-line>
    <terminal-line>[INFO] export CYLC_VERSION=7.9.7</terminal-line>
    <terminal-line>[INFO] export ROSE_ORIG_HOST=&lt;gadi-cpu&gt;.nci.org.au</terminal-line>
    <terminal-line>[INFO] export ROSE_SITE=nci</terminal-line>
    <terminal-line>[INFO] export ROSE_VERSION=2019.01.2</terminal-line>
    <terminal-line>[INFO] delete: log/rose-suite-run.conf</terminal-line>
    <terminal-line>[INFO] symlink: rose-conf/&lt;timestamp&gt;-restart.conf <= log/rose-suite-run.conf</terminal-line>
    <terminal-line>[INFO] delete: log/rose-suite-run.version</terminal-line>
    <terminal-line>[INFO] symlink: rose-conf/&lt;timestamp&gt;-restart.version <= log/rose-suite-run.version</terminal-line>
    <terminal-line>[INFO] chdir: log/</terminal-line>
    <terminal-line>[WARN] Using the cylc session &lt;persistent-session-full-name&gt;</terminal-line>
    <terminal-line>[WARN]</terminal-line>
    <terminal-line>[WARN] Loading cylc7/23.09</terminal-line>
    <terminal-line class='keep-blanks'>[WARN]   Loading requirement: mosrs-setup/1.0.1</terminal-line>
    <terminal-line class='keep-blanks'>[INFO]             .\_.</terminal-line>
    <terminal-line class='keep-blanks'>[INFO]             | |              The Cylc Suite Engine [7.9.9]</terminal-line>
    <terminal-line class='keep-blanks'>[INFO] .\_\_\_\_\_.\_. .\_| |\_\_\_\_\_.        Copyright (C) 2008-2019 NIWA</terminal-line>
    <terminal-line class='keep-blanks'>[INFO] | .\_\_\_| | | | | .\_\_\_|   & British Crown (Met Office) & Contributors.</terminal-line>
    <terminal-line class='keep-blanks'>[INFO] | !\_\_\_| !\_! | | !\_\_\_.  \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_</terminal-line>
    <terminal-line class='keep-blanks'>[INFO] !\_\_\_\_\_!\_\_\_. |\_!\_\_\_\_\_!  This program comes with ABSOLUTELY NO WARRANTY;</terminal-line>
    <terminal-line class='keep-blanks'>[INFO]       .\_\_\_! |          see \`cylc warranty\`.  It is free software, you</terminal-line>
    <terminal-line class='keep-blanks'>[INFO]       !\_\_\_\_\_!           are welcome to redistribute it under certain</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] *** listening on https://&lt;persistent-session-full-name&gt;:&lt;port&gt;/ ***</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] To view suite server program contact information:</terminal-line>
    <terminal-line>[INFO]  $ cylc get-suite-contact &lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO]</terminal-line>
    <terminal-line>[INFO] Other ways to see if the suite is still running:</terminal-line>
    <terminal-line>[INFO]  $ cylc scan -n '&lt;suite-ID&gt;' &lt;persistent-session-full-name&gt;</terminal-line>
    <terminal-line>[INFO]  $ cylc ping -v --host=&lt;persistent-session-full-name&gt; &lt;suite-ID&gt;</terminal-line>
    <terminal-line>[INFO]  $ ps -opid,args &lt;PID&gt;  # on &lt;persistent-session-full-name&gt;</terminal-line>
    <img src="/assets/run_access_cm/Cylc_GUI_are.png" alt="Cylc GUI" imageTime="inf" loading="lazy">
</terminal-window>

#### _HARD_ restart {: .no-toc }
To overwrite any previous runs of the suite and start afresh, run the following command from within the suite directory:
```
rose suite-run --new
```

!!! warning
    This will overwrite all existing model output and logs for the same suite.

### RELOAD a suite
In some cases the suite needs to be updated without necessarily having to stop it (e.g., after fixing a typo in a file). Updating an active suite is called a _reload_, where the suite is _re-installed_ and _Cylc_ is updated with the changes. This is similar to a _SOFT_ restart, except new changes are installed, so you may need to manually trigger failed tasks from the _Cylc_ GUI.

To reload a suite, run the following command from within the suite directory:
```
rose suite-run --reload
```

## {{ model }} output files
All {{ model }} output files, together with work files, are available on _Gadi_ inside `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>`. They are also symlinked in `~/cylc-run/<suite-ID>`.<br>
While the suite is running, files are moved between the `share` and `work` directories.<br>
At the end of each cycle, model output data and restart files are moved to `/scratch/$PROJECT/$USER/archive/<suite-name>`.<br>
This directory contains two subdirectories:

- `history`
- `restart`
    
### Output data
`/scratch/$PROJECT/$USER/archive/<suite-name>/history` is the directory containing the model output data, which is grouped according to each model component:

- `atm` &rarr; atmosphere ([UM](/models/model_components/atmosphere#unified-model-um))
- `cpl` &rarr; coupler ([OASIS-MCT](/models/model_components/coupler#oasis3-mct))
- `ocn` &rarr; ocean ([MOM](/models/model_components/ocean#modular-ocean-model-mom))
- `ice` &rarr; sea ice ([CICE](/models/model_components/sea-ice#cice))

For the atmospheric output data, the files are typically a [UM fieldsfile](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) or netCDF file, formatted as `<suite-name>a.p<output-stream-identifier><year><month-string>`.

For the `{{ suite_id }}` suite in this example, the `atm` directory contains:
<terminal-window>
    <terminal-line data="input">cd /scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive</terminal-line>
    <terminal-line data="input" directory="/scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive">ls</terminal-line>
    <terminal-line class="ls-output-format">cy339 &lt;other-suite-name&gt; &lt;other-suite-name&gt;</terminal-line>
    <terminal-line data="input" directory="/scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive">cd cy339</terminal-line>
    <terminal-line data="input" directory="/scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive/cy339">ls</terminal-line>
    <terminal-line class="ls-output-format">history restart</terminal-line>
    <terminal-line data="input" directory="/scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive/cy339">ls history/atm</terminal-line>
    <terminal-line class="ls-output-format">cy339a.pd0950apr.nc cy339a.pd0950aug.nc cy339a.pd0950dec.nc cy339a.pd0950feb.nc cy339a.pd0950jan.nc cy339a.pd0950jul.nc cy339a.pd0950jun.nc cy339a.pd0950mar.nc cy339a.pd0950may.nc cy339a.pd0950nov.nc cy339a.pd0950oct.nc cy339a.pd0950sep.nc cy339a.pd0951apr.nc cy339a.pd0951aug.nc cy339a.pd0951dec.nc cy339a.pm0950apr.nc cy339a.pm0950aug.nc cy339a.pm0950dec.nc cy339a.pm0950feb.nc cy339a.pm0950jan.nc cy339a.pm0950jul.nc cy339a.pm0950jun.nc cy339a.pm0950mar.nc cy339a.pm0950may.nc cy339a.pm0950nov.nc cy339a.pm0950oct.nc cy339a.pm0950sep.nc cy339a.pm0951apr.nc cy339a.pm0951aug.nc cy339a.pm0951dec.nc netCDF</terminal-line>
</terminal-window>

### Restart files
The restart files can be found in the `/scratch/$PROJECT/$USER/archive/<suite-name>/restart` directory, where they are categorised according to model components (similar to the `history` folder above).<br>
The atmospheric restart files, which are [UM fieldsfiles](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf), are formatted as `<suite-name>a.da<year><month><day>_00`.

For the `{{ suite_id }}` suite in this example, the `atm` directory contains:
<terminal-window>
    <terminal-line data="input">ls /scratch/&lt;$PROJECT&gt;/&lt;$USER&gt;/archive/cy339/restart/atm</terminal-line>
    <terminal-line class="ls-output-format">cy339a.da09500201_00 cy339a.da09510101_00 cy339.xhist-09500131 cy339.xhist-09501231 </terminal-line>
</terminal-window>

Files formatted as `<suite-name>a.xhist-<year><month><day>` contain metadata information.

## Port suites from accessdev
_accessdev_ was the server used for {{ model }} run submission workflow before the update to persistent sessions.<br>
If you have a suite that was running on accessdev, you can run it using persistent sessions by carrying out the following steps:

### Initialisation step
To set the correct SSH configuration for _Cylc_, some SSH keys need to be created in the `~/.ssh` directory.<br>
To create the required SSH keys, run the following command:
```
/g/data/hr22/bin/gadi-cylc-setup-ps -y
```
!!! tip
    You only need to run this initialisation step once.

### Set host to localhost
To enable _Cylc_ to submit PBS jobs directly from the persistent session, the suite configuration should have its `host` set as `localhost`.<br>
You can manually set all occurrences of `host` to `localhost` in the suite configuration files.<br>
Alternatively, you can run the following command in the suite folder:
```
grep -rl --exclude-dir=.svn "host\s*=" . | xargs sed -i 's/\(host\s*=\s*\).*/\1localhost/g'
```

### Add _gdata/hr22_ and _gdata/ki32_ in the PBS storage directives
As the persistent sessions workflow uses files in the `hr22` and `ki32` project folders on _Gadi_, the respective folders need to be added to the `storage` directive in the suite configuration files.<br>
You can do this manually or run the following command from within the suite directory:
```
grep -rl --exclude-dir=.svn "\-l\s*storage\s*=" . | xargs sed -i '/\-l\s*storage\s*=\s*.*gdata\/hr22.*/! s/\(\-l\s*storage\s*=\s*.*\)/\1+gdata\/hr22/g ; /\-l\s*storage\s*=\s*.*gdata\/ki32.*/! s/\(\-l\s*storage\s*=\s*.*\)/\1+gdata\/ki32/g'
```

!!! warning
    Some suites might not be ported this way.<br>
    If you have a suite that was running on _accessdev_ and, even after following the steps above, the run submission fails, consider [getting help on the Hive Forum](/about/user_support/ask_on_forum).

## Known issues
Below are listed some {{ model }} known issues which will not be fixed.

- [Different cycling frequencies break reproducibility](https://forum.access-hive.org.au/t/different-cycling-frequencies-in-access-cm2-lead-to-different-solutions/4539)
{: #issues-cycling-repro }

<custom-references>
- [https://confluence.csiro.au/display/ACCESS/Using+CM2+suites+in+Rose+and+Cylc](https://confluence.csiro.au/display/ACCESS/Using+CM2+suites+in+Rose+and+Cylc)
- [https://confluence.csiro.au/display/ACCESS/Understanding+CM2+output](https://confluence.csiro.au/display/ACCESS/Understanding+CM2+output)
- [https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf](https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf)
- [https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html](https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html)
- [https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites)
- [https://opus.nci.org.au/display/Help/Persistent+Sessions](https://opus.nci.org.au/display/Help/Persistent+Sessions)
</custom-references>
