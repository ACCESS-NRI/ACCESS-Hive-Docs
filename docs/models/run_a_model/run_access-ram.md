{% set model = "ACCESS-rAM3" %}
{% set ras_id = "u-dg767" %}
{% set rns_id = "u-dg768" %}
{% set branch = "access_rel_1" %}
{% set mosrs_config_ras = "https://code.metoffice.gov.uk/trac/roses-u/browser/d/g/7/6/7/trunk" %}
{% set mosrs_config_rns = "https://code.metoffice.gov.uk/trac/roses-u/browser/d/g/7/6/8/trunk" %}
{% set access_models = "/models/access_models/access-ram" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-ram3-release-information/4308" %}
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[model components]: /models/access_models/access-ram/#model-components
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[default project]: /getting_started/set_up_nci_account#change-default-project-on-gadi

<div class="text-card-group" markdown>

[![Met Office](/assets/met_office_logo.png){: class="icon-before-text  white-background"} RAS configuration]({{mosrs_config_ras}}){: class="text-card" style=""}
[![Met Office](/assets/met_office_logo.png){: class="icon-before-text  white-background"} RNS configuration]({{mosrs_config_rns}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

{{ model }} is an ACCESS-NRI-supported configuration of the [UK Met Office (UKMO)](https://www.metoffice.gov.uk/) Regional Nesting Suite for high-resolution regional atmosphere modelling.<br>
A description of the model and its components is available in the [{{ model }} overview]({{ access_models }}/#{{ model }}).

{{ model }} comprises two suites: a [Regional Ancillary Suite (RAS)](#ras), which generates ancillary files (i.e., input files), and a [Regional Nesting Suite (RNS)](#rns) which runs the regional forecast.

The instructions below outline how to run {{ model }} using ACCESS-NRI's supported configuration, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_][gadi].<br>
The example experiment within this page focuses on a flood event in Lismore, NSW, using `ERA5-Land` [land-surface initial conditions]({{ access_models }}/#land-surface-initial-conditions-source). Its configuration is specified in [Nesting configuration]({{ access_models }}/#nesting-configuration).

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are and available on MOSRS via links at the top of this page.

[{{ model }} release notes]({{release_notes}}) are available on the ACCESS-Hive Forum and are updated when new releases are made available.

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
    - [rt52](https://my.nci.org.au/mancini/project/rt52/join)
    - [zz93](https://my.nci.org.au/mancini/project/zz93/join)
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)

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

!!! warning
    The waiting time to complete some of the above prerequisites may be 2-3 weeks.

## Quick Start guide

The following *Quick Start* guide is aimed at experienced users wanting to run {{ model }}. For more detailed instructions, please refer to the [Detailed guide](#detailed-guide).

### Required setup for running {{ model }} {: .no-toc }

- **Start a new [_persistent session_](https://opus.nci.org.au/display/Help/Persistent+Sessions)**<br> 
    In a [Gadi][gadi] login node or from an ARE terminal instance run:
    ```
    persistent-sessions start <name>
    ```
    This will use your [default project].

    For further instructions on starting a _persistent session_, refer to the [Detailed guide](#start-a-new-persistent-session).

- **Assign the _persistent session_ to Rose/Cylc workflows**<br>
    Run the following command:
    ```
    echo "<name>.${USER}.<project>.ps.gadi.nci.org.au" > ~/.persistent-sessions/cylc-session
    ```
    substituting `<name>` with the name given to your _persistent session_, and `<project>` with the project assigned to it.

    !!! tip
        This step should only be done once

    For further instructions on assigning the target _persistent session_, refer to the [Detailed guide](#specify-target-persistent-session).

- **Rose/Cylc setup**<br>
    To get the required _Rose/Cylc_ setup, run:
    ```
    module use /g/data/hr22/modulefiles
    module load cylc7
    ```

    For further instructions on getting the _Rose/Cylc_ setup, refer to the [Detailed guide](#rosecylcmosrs-setup).

- **MOSRS authentication**<br>
    Authenticate using your MOSRS credentials:
    ```
    mosrs-auth
    ```

    For further instructions on MOSRS authentication, refer to the [Detailed guide](#mosrs-authentication).

### Regional Ancillary Suite (RAS) {: .no-toc }
1. **Copy the RAS from UKMO**<br>
    ```
    rosie checkout {{ ras_id }}/{{ branch }}
    ```

    For further instructions on getting the RAS configuration, refer to the [Detailed guide](#get-the-ras-configuration).

2. **Run the RAS**<br>
    ```
    cd ~/roses/{{ras_id}}
    rose suite-run
    ```

    For further instructions on running the RAS configuration, refer to the [Detailed guide](#run-the-ras).

### Regional Nesting Suite (RNS) {: .no-toc }
1. **Copy the RNS from UKMO**<br>
    ```
    rosie checkout {{ rns_id }}/{{ branch }}
    ```

    For further instructions on getting the RNS configuration, refer to the [Detailed guide](#get-and-run-rns-configuration).

2. **Run the RNS**<br>
    From within the RNS directory:
    ```
    rose suite-run
    ```

    For further instructions on getting the RNS configuration, refer to the [Detailed guide](#get-and-run-rns-configuration).

---

## Detailed guide

### Set up an ARE VDI Desktop (optional)
!!! info 
    If you want to skip this step and run {{ model }} from _Gadi_ login node instead, refer directly to the instructions on how to [Set up _persistent session_](#set-up-persistent-session).

#### Launch ARE VDI Session  {: .no-toc }
Go to the [ARE VDI](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) page and launch a session with the following entries:

- **Walltime (hours)** &rarr; `5`<br>
    This is the amount of time the ARE VDI session will stay active for.<br>
    {{ model }} does not run directly on ARE.<br>
    This means that the ARE VDI session only needs to carry out setup steps as well as starting the run itself.
    
- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>
    As mentioned above, the ARE VDI session is only needed for setup and startup tasks, which can be easily accomplished with 1 CPU.

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated _Service Units (SU)_ to run your simulation. Usually, but not always, this corresponds to your `$PROJECT`.<br>
    For more information, refer to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

- **Storage** &rarr; `gdata/access+gdata/hr22+gdata/ki32+gdata/rt52+gdata/zz93+gdata/vk83` (minimum)<br>
    This is a list of all project data storage, joined by plus (`+`) signs, needed for the {{ model }} simulation. In ARE, storage locations need to be explicitly defined to access data from within a VDI instance.<br>
    Every {{ model }} simulation can be unique and input data can originate from various sources. Hence, if your simulation requires data stored in project folders other than the ones listed in the minimum storage above, you need to add those projects to the storage path.<br>
    For example, if your {{ model }} simulation requires data stored in `/g/data/gx60` and `/scratch/gx60`, the following should be added to the minimum storage above: `+gdata/gx60+scratch/gx60`
    
Launch the ARE session and, once it starts, click on _Launch VDI Desktop_.

![Launch ARE VDI session example](/assets/run_access_cm/launch_are_vdi.gif){: class="example-img" loading="lazy"}

#### Open the terminal in the VDI Desktop {: .no-toc }
Once the new tab opens, you will see a Desktop with a few folders on the left.<br>
To open the terminal, click on the black terminal icon at the top of the window. You should now be connected to a _Gadi_ computing node.

![Open ARE VDI terminal example](/assets/run_access_cm/open_are_vdi_terminal.gif){: class="example-img" loading="lazy"}

### Set up _persistent session_ 
To support the use of long-running processes, such as ACCESS model runs, NCI provides a service on _Gadi_ called [_persistent sessions_](https://opus.nci.org.au/display/Help/Persistent+Sessions).

To run {{ model }}, you need to start a _persistent session_ and set it as the target session for the model run.

#### Start a new _persistent session_ {: .no-toc }
To start a new _persistent session_, using either a _Gadi_ login node or an ARE terminal instance, run the following command:
```
persistent-sessions start <name>
```

This will start a _persistent session_ with the given `name` that runs under your [default project].<br>
If you want to assign a different project to the _persistent session_, use the option `-p`:
```
persistent-sessions start -p <project> <name>
```

!!! tip
    While the project assigned to a _persistent session_ does not have to be the same as the project used to run the {{ model }} configuration, it does need to have allocated _Service Units (SU)_.<br>
    For more information, check how to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

<terminal-window data="input">
    <terminal-line>persistent-sessions start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

To list all active _persistent sessions_ run:
```
persistent-sessions list
```

<terminal-window data="input">
    <terminal-line>persistent-sessions list</terminal-line>
    <terminal-line data="output">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;UUID&emsp;&emsp;PROJECT&emsp;&ensp;&ensp;ADDRESS&emsp;&emsp;&emsp;&emsp;CPUTIME&emsp;MEMORY</terminal-line>
    <terminal-line data="output">&lt;persistent-session-uuid&gt;&emsp;&lt;project&gt;&emsp;10.9.0.62&emsp;00:00:05.213&emsp;30.5M</terminal-line>
</terminal-window>


The label of a newly-created _persistent session_ has the following format: <br>
`<name>.<$USER>.<project>.ps.gadi.nci.org.au`.

#### Specify target _persistent session_ {: .no-toc }

After starting the _persistent session_, it is essential to assign it to the {{ model }} run.<br>
The easiest way to create a file `~/.persistent-sessions/cylc-session` that contains the target of the _persistent session_.<br>
You can do it manually, or by running the following command (by substituting `<name>` with the name given to the _persistent session_, and `<project>` with the project assigned to it):

```
echo "<name>.${USER}.<project>.ps.gadi.nci.org.au" > ~/.persistent-sessions/cylc-session
```

For example, if the user `abc123` started a _persistent session_ named `cylc` under the project `xy00`, the command will be:

<terminal-window data="input">
    <terminal-line>echo "cylc.abc123.xy00.ps.gadi.nci.org.au" > ~/.persistent-sessions/cylc-session
    </terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">cylc.abc123.xy00.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

For more information on how to specify the target session, refer to [Specify Target Session with Cylc7 Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites#RunCylc7Suites-SpecifyTargetSession).

!!! tip
    You can simultaneously submit multiple {{ model }} runs using the same _persistent session_ without needing to start a new one. Hence, the process of specifying the target _persistent session_ for {{ model }} should only be done once. Then, to run {{ model }}, you just need to ensure that you have an active _persistent session_ named like the target one you specified above. If the _persistent session_ is not active, simply [start one](#start-a-new-persistent-session).

#### Terminate a _persistent session_ {: .no-toc }
!!! tip
    Logging out of a *Gadi* login node or an ARE terminal instance will not affect your _persistent session_. 

To stop a _persistent session_, run:
```
persistent-sessions kill <persistent-session-uuid>
```
!!! warning
    When you terminate a _persistent session_, any model running on that session will stop. Therefore, you should check whether you have any active model runs before terminating a _persistent session_.

### Rose/Cylc/MOSRS setup

To run {{ model }}, access to multiple software and MOSRS authentication is needed.

#### Cylc setup {: #cylc .no-toc }

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
    
    Also, before loading the _Cylc_ module, make sure to have started a _persistent session_ and have assigned it to the {{ model }} workflow. For more information about these steps, refer to [Set up _persistent session_](#set-up-persistent-session).

#### Rose setup {: #rose .no-toc }
[Rose](http://metomi.github.io/rose/doc/html/index.html) is a toolkit that can be used to view, edit, or run an ACCESS modelling suite.

By completing the [_Cylc_ setup](#cylc), also _Rose_ will be automatically available. Hence, no additional step is required.

#### MOSRS authentication {: .no-toc }
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

### {{ model }} configuration
{{ model }} comprises 2 different suites: a [Regional Ancillary Suite (RAS)](#ras) and a [Regional Nesting Suite (RNS)](#rns).

Both suites within {{ model }} have a `suite-ID` in the format `u-<suite-name>`, where `<suite-name>` is a unique identifier.<br>
Typically, an existing suite is copied and then edited as needed for a particular experiment.

For more information on {{ model }}, refer to the [{{model}} configuration]({{ access_models }}/#{{ model }}) page.

!!! info 
    Many of the following steps appear in both the RAS and RNS. For this reason, these steps will be detailed only within the RAS section below, and subsequenltly linked to within the RNS section.

### Regional Ancillary Suite (RAS) {: #ras }

For the domain of interest, the RAS generates a set of ancillary files, such as initial conditions. These ancillary files are then used by the [RNS](#rns).

The `suite-ID` of the RAS is `{{ ras_id }}`.
The latest release branch is `{{ branch }}`.

#### Get the RAS configuration
[Rosie](https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rosie) is an [SVN](https://subversion.apache.org) repository wrapper with a set of options specific for ACCESS modelling suites. It is automatically available within the [_Rose_ setup](#rose).

The RAS configuration can be copied from the MOSRS repository in 2 ways:

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

##### Local-only copy {: #local-copy .no-toc }
To create a _local copy_ of the RAS from MOSRS repository, run:
```
rosie checkout {{ ras_id }}/{{ branch }}
```
<terminal-window>
    <terminal-line data="input">rosie checkout {{ ras_id }}/{{ branch }}</terminal-line>
    <terminal-line>[INFO] create: /home/565/&lt;$USER&gt;/roses</terminal-line>
    <terminal-line>[INFO] &lt;suite-ID&gt;: local copy created at /home/565/&lt;$USER&gt;/roses/{{ ras_id }}</terminal-line>
</terminal-window>
This option is mostly used for testing and examining suites.
    
##### Remote and local copy {: #remote-copy .no-toc }
To create a new copy of the RAS both _locally_ and _remotely_ in the MOSRS repository, run: 
```
rosie copy {{ ras_id }}
```
<terminal-window>
    <terminal-line data="input">rosie copy {{ ras_id }}</terminal-line>
    <terminal-line>Copy "{{ ras_id }}/trunk@&lt;trunk-ID&gt;" to "u-?????"? [y or n (default)]</terminal-line> <terminal-line data="input">y</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-ID&gt;: created at https://code.metoffice.gov.uk/svn/roses-u/&lt;suite-n/a/m/e/&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-ID&gt;: copied items from {{ ras_id }}/trunk@&lt;trunk-ID&gt;</terminal-line>
    <terminal-line>[INFO] {{ ras_id }}: local copy created at /home/565/&lt;$USER&gt;/roses/&lt;new-suite-ID&gt;</terminal-line>
</terminal-window>
When a new suite is created in this way, a _unique_ `<suite-ID>` folder is generated within the MOSRS repository and populated with descriptive information about the suite and its initial configuration.

For additional `rosie` options, run:
```
rosie help
```

#### Run the RAS
{{ model }} suites run on [_Gadi_](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview) through a [PBS job] submission.<br>
When a suite runs, its configuration files are copied in `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>`. A symbolic link to this directory is also created in the `$USER`'s home directory under `~/cylc-run/<suite-ID>`.<br>
{{ model }} suites comprise several tasks, such as checking out code repositories, compiling and building the different model components, running the model, etc. The workflow of these tasks is controlled by [_Cylc_](#cylc).

To run the RAS, execute the following command from within your RAS [suite directory](#suitedir):
```
rose suite-run
```

After the initial tasks are executed, the _Cylc_ GUI will open, where it is possible to view and control the different tasks in the suite as they are run.

!!! tip
    The _Cylc_ GUI can be safely closed without impacting the experiment run.<br>
    To open it again, run the following command from within the [suite directory](#suitedir):
```
rose suite-gcontrol
```

All steps are completed!! <br>
You will be able to check the [suite output files](#ras-output-files) after the run successfully completes.<br>
If you get errors or you can't find the outputs, [check the suite logs](#check-suite-logs) for debugging.

#### Check suite logs

It is not unusual that new users experience errors and job failures.<br>
When a suite task fails, a red icon appears next to the respective task name in the _Cylc_ GUI.<br>

To investigate the cause of a failure, or to monitor the progress of a suite, it is helpful to look at the suite's log files.

These files can be found in the directory `~/cylc-run/<suite-ID>` within a folder named `log.<TIMESTAMP>`, which is also symlinked as `log` (referred to as _logs folder_ below). Logs from previous runs of the same suite are archived as compressed files with the naming pattern `log.<TIMESTAMP>.tar.gz`.

Inside the logs folder, various files and subfolders can be found. The most relevant logs are typically:

- [Suite execution log](#suite-execution-log)
- [Task-specific logs](#task-specific-logs)

##### Suite execution log {: #suite-execution-log .no-toc }

The primary suite execution log resides in `~/cylc-run/<suite-ID>/log/suite/log`.

This file contains a chronological record of the suite's run history. Each line is a distinct log entry, generally formatted as `<TIMESTAMP> <LOG-TYPE> - [<task-name>.<cylc-cycle-point>] <status>`.

??? code "Example of a suite execution log file (click to see content)"
    ```
    2025-03-14T04:11:56Z INFO - Suite server: url=https://cylc.$USER$.$PROJECT.ps.gadi.nci.org.au:PORT/ pid=PID
    2025-03-14T04:11:56Z INFO - Run: (re)start=0 log=1
    2025-03-14T04:11:56Z INFO - Cylc version: 7.9.9
    2025-03-14T04:11:56Z INFO - Run mode: live
    2025-03-14T04:11:56Z INFO - Initial point: 01000101T0000Z
    2025-03-14T04:11:56Z INFO - Final point: 01000328T2359Z
    2025-03-14T04:11:56Z INFO - Cold Start 01000101T0000Z
    2025-03-14T04:11:56Z INFO - [make_drivers.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [install_cold.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [make_cice.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [make_mom.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [install_ancil.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [fcm_make_um.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:58Z INFO - [fcm_make_um.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [fcm_make_um.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [install_ancil.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [install_ancil.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [install_cold.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [install_cold.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_cice.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_cice.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_drivers.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_drivers.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_mom.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_mom.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:04Z INFO - [make_drivers.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_drivers.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [install_cold.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [install_cold.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [make_cice.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_cice.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [make_mom.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_mom.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [install_ancil.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [install_ancil.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [client-command] get_latest_state dm5220@gadi-login-08.gadi.nci.org.au:cylc-gui c842e8fb-017a-47ec-8706-7fef0af6d5f5
    2025-03-14T04:12:06Z INFO - [make_drivers.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:05Z for job(01)
    2025-03-14T04:12:09Z INFO - [make_cice.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:07Z for job(01)
    2025-03-14T04:12:09Z INFO - [install_ancil.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:07Z for job(01)
    2025-03-14T04:12:10Z INFO - [make2_cice.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:12:11Z INFO - [make2_cice.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:12:10Z for job(01)
    2025-03-14T04:12:11Z INFO - [make2_cice.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:14Z INFO - [make_mom.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:12Z for job(01)
    2025-03-14T04:12:15Z INFO - [make2_mom.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:12:18Z INFO - [make2_mom.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:12:15Z for job(01)
    2025-03-14T04:12:18Z INFO - [make2_mom.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:37Z INFO - [install_cold.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:35Z for job(01)
    2025-03-14T04:12:48Z INFO - [make2_mom.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:45Z for job(01)
    2025-03-14T04:12:48Z INFO - [make2_mom.01000101T0000Z] -health check settings: execution timeout=PT40M, polling intervals=PT31M,PT2M,PT7M,...
    2025-03-14T04:12:59Z INFO - [fcm_make_um.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:57Z for job(01)
    2025-03-14T04:12:59Z INFO - [fcm_make_um.01000101T0000Z] -health check settings: execution timeout=PT1H10M, polling intervals=PT1H1M,PT2M,PT7M,...
    2025-03-14T04:13:00Z INFO - [make2_cice.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:58Z for job(01)
    2025-03-14T04:13:00Z INFO - [make2_cice.01000101T0000Z] -health check settings: execution timeout=PT30M, polling intervals=PT21M,PT2M,PT7M,...
    2025-03-14T04:15:58Z INFO - [make2_cice.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:15:57Z for job(01)
    2025-03-14T04:18:19Z INFO - [make2_mom.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:18:17Z for job(01)
    2025-03-14T04:20:10Z INFO - [fcm_make_um.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:20:08Z for job(01)
    2025-03-14T04:20:11Z INFO - [fcm_make2_um.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:20:13Z INFO - [fcm_make2_um.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:20:12Z for job(01)
    2025-03-14T04:20:13Z INFO - [fcm_make2_um.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:20:37Z INFO - [fcm_make2_um.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:20:35Z for job(01)
    2025-03-14T04:20:37Z INFO - [fcm_make2_um.01000101T0000Z] -health check settings: execution timeout=PT1H10M, polling intervals=PT1H1M,PT2M,PT7M,...
    2025-03-14T04:37:11Z INFO - [fcm_make2_um.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:37:09Z for job(01)
    2025-03-14T04:37:12Z INFO - [recon.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:37:19Z INFO - [recon.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:37:14Z for job(01)
    2025-03-14T04:37:19Z INFO - [recon.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:37:53Z INFO - [recon.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:37:52Z for job(01)
    2025-03-14T04:37:53Z INFO - [recon.01000101T0000Z] -health check settings: execution timeout=PT30M, polling intervals=PT21M,PT2M,PT7M,...
    2025-03-14T04:38:28Z INFO - [recon.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:38:28Z for job(01)
    2025-03-14T04:38:29Z INFO - [coupled.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:38:30Z INFO - [coupled.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:38:30Z for job(01)
    2025-03-14T04:38:30Z INFO - [coupled.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:42:00Z INFO - [coupled.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:41:59Z for job(01)
    2025-03-14T04:42:00Z INFO - [coupled.01000101T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T04:45:28Z INFO - [coupled.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:45:27Z for job(01)
    2025-03-14T04:45:29Z INFO - [filemove.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:45:30Z INFO - [filemove.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:45:30Z for job(01)
    2025-03-14T04:45:30Z INFO - [filemove.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:12Z INFO - [filemove.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:46:11Z for job(01)
    2025-03-14T04:46:12Z INFO - [filemove.01000101T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T04:46:26Z INFO - [filemove.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:46:25Z for job(01)
    2025-03-14T04:46:27Z INFO - [history_postprocess.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:46:27Z INFO - [coupled.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:46:28Z INFO - [coupled.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:46:28Z for job(01)
    2025-03-14T04:46:28Z INFO - [coupled.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:28Z INFO - [history_postprocess.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:46:28Z for job(01)
    2025-03-14T04:46:28Z INFO - [history_postprocess.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:58Z INFO - [history_postprocess.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:46:57Z for job(01)
    2025-03-14T04:46:58Z INFO - [history_postprocess.01000101T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T04:47:09Z INFO - [coupled.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:47:09Z for job(01)
    2025-03-14T04:47:09Z INFO - [coupled.01000201T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T04:47:11Z INFO - [history_postprocess.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:47:10Z for job(01)
    2025-03-14T04:47:12Z INFO - [housekeep.01000101T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T04:47:13Z INFO - [housekeep.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:47:13Z for job(01)
    2025-03-14T04:47:13Z INFO - [housekeep.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:47:18Z INFO - [housekeep.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:47:17Z for job(01)
    2025-03-14T04:47:18Z INFO - [housekeep.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:47:21Z INFO - [housekeep.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:47:20Z for job(01)
    2025-03-14T04:50:13Z INFO - [coupled.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:50:11Z for job(01)
    2025-03-14T04:50:14Z INFO - [filemove.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:50:15Z INFO - [filemove.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:50:14Z for job(01)
    2025-03-14T04:50:15Z INFO - [filemove.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:50:54Z INFO - [filemove.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:50:52Z for job(01)
    2025-03-14T04:50:54Z INFO - [filemove.01000201T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T04:51:08Z INFO - [filemove.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:06Z for job(01)
    2025-03-14T04:51:09Z INFO - [history_postprocess.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:51:09Z INFO - [coupled.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:51:10Z INFO - [coupled.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:09Z for job(01)
    2025-03-14T04:51:10Z INFO - [coupled.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:10Z INFO - [history_postprocess.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:09Z for job(01)
    2025-03-14T04:51:10Z INFO - [history_postprocess.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:23Z INFO - [history_postprocess.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:51:22Z for job(01)
    2025-03-14T04:51:23Z INFO - [history_postprocess.01000201T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T04:51:35Z INFO - [history_postprocess.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:34Z for job(01)
    2025-03-14T04:51:36Z INFO - [housekeep.01000201T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T04:51:37Z INFO - [housekeep.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:37Z for job(01)
    2025-03-14T04:51:37Z INFO - [housekeep.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:41Z INFO - [housekeep.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:51:40Z for job(01)
    2025-03-14T04:51:41Z INFO - [housekeep.01000201T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:51:45Z INFO - [housekeep.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:43Z for job(01)
    2025-03-14T05:01:00Z INFO - [coupled.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:00:59Z for job(01)
    2025-03-14T05:01:00Z INFO - [coupled.01000301T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T05:04:40Z INFO - [coupled.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:04:39Z for job(01)
    2025-03-14T05:04:41Z INFO - [filemove.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T05:04:43Z INFO - [filemove.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:04:43Z for job(01)
    2025-03-14T05:04:43Z INFO - [filemove.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:05:25Z INFO - [filemove.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:05:24Z for job(01)
    2025-03-14T05:05:25Z INFO - [filemove.01000301T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T05:05:40Z INFO - [filemove.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:05:39Z for job(01)
    2025-03-14T05:05:41Z INFO - [history_postprocess.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T05:05:42Z INFO - [history_postprocess.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:05:42Z for job(01)
    2025-03-14T05:05:42Z INFO - [history_postprocess.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:05:57Z INFO - [history_postprocess.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:05:56Z for job(01)
    2025-03-14T05:05:57Z INFO - [history_postprocess.01000301T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T05:06:08Z INFO - [history_postprocess.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:06:07Z for job(01)
    2025-03-14T05:06:09Z INFO - [housekeep.01000301T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T05:06:10Z INFO - [housekeep.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:06:10Z for job(01)
    2025-03-14T05:06:10Z INFO - [housekeep.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:06:18Z INFO - [housekeep.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:06:16Z for job(01)
    2025-03-14T05:06:18Z INFO - [housekeep.01000301T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T05:06:20Z INFO - [housekeep.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:06:19Z for job(01)
    2025-03-14T05:06:20Z INFO - Suite shutting down - AUTOMATIC
    2025-03-14T05:06:28Z INFO - DONE
    ``` 

This file helps identify specific tasks that failed during the suite run.

!!! tip
    When a task fails, the `LOG-TYPE` will typically be `ERROR` or `CRITICAL`, instead of the more common `INFO`.

Once a specific task and _Cylc_ cycle point are identified, the task-specific logs can be inspected.

##### Task-specific logs {: .no-toc }

Logs for individual tasks are located in subfolders within the logs folder, following this path structure:
```
~/cylc-run/<suite-ID>/log/job/<cylc-cycle-point>/<task-name>/<retry-number>
```
The `<retry-number>` indicates the number of retries for the same task, with the latest retry symlinked to `NN`.

For example, logs for most recent retry of a task named `Lismore_d1000_GAL9_um_recon` at _Cylc_ cycle point `20220226T0000Z` can be found in the folder `~/cylc-run/<suite-ID>/log/job/20220226T0000Z/Lismore_d1000_GAL9_um_recon/NN`.

Within this directory, the `job.out` and `job.err` files (representing `STDOUT` and `STDERR`, respectively) can be found, along with other related log files.

!!! tip
    Within the _Cylc_ GUI, logs for a specific task can be viewed by right-clicking on the task and selecting the desired log from the _View Job Logs (Viewer)_ menu.

#### Stop, restart, reload and clean suites
In some cases, you may want to control the running state of a suite.<br>
If your _Cylc_ GUI has been closed and you are unsure whether your suite is still running, you can scan for active suites and reopen the GUI.<br>
To scan for active suites, run:
```
cylc scan
```
To reopen the _Cylc_ GUI, run the following command from within the [suite directory](#suitedir):
```
rose suite-gcontrol
```

##### STOP a suite {: .no-toc }
To shutdown a suite in a safe manner, run the following command from within the [suite directory](#suitedir):
```
rose suite-stop -y
```
Alternatively, you can directly kill the [PBS jobs][PBS job] connected to your run. To do so:

1. Check the status of all your PBS jobs:
```
qstat -u $USER
```

1. Delete any job related to your run:
```
qdel <job-ID>
```

##### RESTART a suite {: .no-toc }
There are two main ways to restart a suite:

- **_SOFT_ restart**<br>
    To reinstall the suite and reopen _Cylc_ in the same state it was prior to being stopped, run the following command from within the [suite directory](#suitedir):
    ```
    rose suite-run --restart
    ```

    !!! warning
        You may need to manually trigger failed tasks from the _Cylc_ GUI.

- **HARD restart**<br>
    To overwrite any previous runs of the suite and start afresh, run the following command from within the [suite directory](#suitedir):
    ```
    rose suite-run --new
    ```

    !!! warning
        This will overwrite all existing model output and logs for the same suite.

##### RELOAD a suite {: .no-toc }
In some cases, the suite needs to be updated without necessarily having to stop it (e.g., after fixing a typo in a file). Updating an active suite is called a _reload_, where the suite is _re-installed_ and _Cylc_ is updated with the changes. This is similar to a _SOFT_ restart, except new changes are installed, so you may need to manually trigger failed tasks from the _Cylc_ GUI.

To reload a suite, run the following command from within the [suite directory](#suitedir):
```
rose suite-run --reload
```

##### CLEAN a suite {: .no-toc }
To remove all files and folders created by the suite within the `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>` directory, run the following command from within the [suite directory](#suitedir):
```
rose suite-clean
```

Alternatively, you can achieve the same behaviour within a new submission of an experiment, by appending the `--new` option to the `rose suite-run` command:
```
rose suite-run --new
```

!!! warning
    Cleaning a suite folder will remove any non-archived data (i.e., output files, logs, executables, etc.) associated with the suite.

#### RAS output files

The RAS output ancillary files can be found in `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils`.<br>
Ancillaries are divided into folders according to each [nested region]({{ access_models }}/#nesting) name, and then further separated according to each nest (i.e., _Resolution_) name. The path of ancillaries for a specific nest (i.e., _Resolution_) is `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils/<nested_region_name>/<nest_name>`.

The example above has one `nested_region_name` called `Lismore`, 1 nest named `era5` (outer domain corresponding to _Resolution 1_), and 2 inner nests (_Resolution 2_ and _Resolution 3_) named `d1000` and `d0198`, respectively.<br>
Thus, the ancillary files directory `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils/` contains the following subdirectories:

- `Lismore/d1000`
- `Lismore/d0198`
- `Lismore/era5`

Ancillary data files are typically output in the [UM fieldsfile](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) format.

### Regional Nesting Suite (RNS) {: #rns }

The RNS uses the ancillary files produced by the RAS to run the regional forecast for the domain of interest.

The `suite-ID` of the RNS is `{{ rns_id }}`.
The latest release branch is `{{ branch }}`.

#### Get and run RNS configuration
Steps to obtain and run the RNS, as well as monitor logs, are similar to those listed above for the [RAS](#ras).<br>
The main difference is the `suite-ID`, which for the RNS is `{{ rns_id }}`.

To get the RNS configuration, follow the steps listed in [Get the RAS configuration](#get-the-ras-configuration), making sure you use the correct RNS `suite-ID` `{{ rns_id }}` when copying the suite.

To run the RNS configuration, follow the steps listed in [Run the suite](#run-the-ras).

To check the RNS suite logs, follow the steps listed in [Check suite logs](#check-suite-logs).

#### RNS output files

All the RNS output files are available in the directory `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>`. They are also symlinked in `~/cylc-run/<suite-ID>`.

The RNS output data can be found in the directory `/scratch/$PROJECT/$USER/cycl-run/<suite-ID>/share/cycle`, grouped for each [cycle](#change-run-length).<br>
Within the `cycle` directory, outputs are divided into multiple nested subdirectories in the format `<nested_region_name>/<science_configuration>/<nest_name>`, with [`<nested_region_name>`](#change-the-nested-region-name) and `<nest_name>` referring to the respective configurable options. The `<science_configuration>` is usually `GAL9` or `RAL3.2`, depending on the [nest resolution]({{ access_models }}/#model-components).

Each `<nest_name>` directory has the following subdirectories:

- `ics` &rarr; initial conditions
- `lbcs` &rarr; lateral boundary conditions
- `um` &rarr; model output data

The RNS output data files are in [UM NetCDF](https://code.metoffice.gov.uk/doc/um/vn13.8/papers/umdp_C11.pdf) format.

For example, the model output data for the first cycle (`20220226T0000Z`) of the _Lismore_ experiment (`Lismore` `nested_region_name`, using a `RAL3P2` `science_configuration` and `d0198` as a `nest_name`) can be found in `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/cycle/20220226T0000Z/Lismore/d0198/RAL3P2/um/umnsaa_pa000.nc`.

!!! tip
    The output data name format may vary depending on some configuration parameters.<br>
    To change which output variables are produced, refer to [Change the output variables](#change-the-output-variables)

### Edit {{ model }} configuration
!!! tip
    Due to the presence of two distinct suites ([RAS](#ras) and [RNS](#rns)), specific modifications might be required in either one or both.<br>
    For each of the following possible modifications, the relevant suite that needs editing is listed as a bullet point.

This section describes how to modify the {{ model }} configuration.

The modifications discussed in this section can change the way the RAS and RNS are run, or how specific [model components] are configured and coupled together.

In general, ACCESS modelling suites can be edited either by directly modifying the configuration files within the suite directory, or by using the [_Rose_ GUI](#rosegui).

!!! warning
    Unless you are an experienced user, directly modifying configuration files is usually discouraged to avoid encountering errors.

##### Rose GUI {: #rosegui }
To open the [_Rose_](#rose) GUI, run the following command from within the [suite directory](#suitedir): 
```
rose edit &
```

!!! tip
    The `&` is optional. It allows the terminal prompt to remain active while running the `Rose` GUI as a separate process in the background.

#### Change run length
- **RNS**<br>
    The RNS runs in multiple [PBS jobs][PBS job] submissions, each one constituting a _cycle_. The job scheduler automatically resubmits the suite every chosen _cycling frequency_ until the total _run length_ is reached.<br>
    
    !!! warning
        The _cycling frequency_ is currently set to `24` hours (1 day) and should be left unchanged to avoid errors.<br>
        This also means the model will run for a minimum of 1 day.
      
    The _run length_ is calculated using the `INITIAL_CYCLE_POINT` and `FINAL_CYCLE_POINT` fields.<br>
    Both these fields use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date format, with `FINAL_CYCLE_POINT` also accepting relative [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations).

    !!! warning
        `INITIAL_CYCLE_POINT` and `FINAL_CYCLE_POINT` define all the [_Cylc_ cycle points](https://cylc.github.io/cylc-doc/7.9.3/html/terminology.html?highlight=cycle%20point#cycle-points) that are set within the experiment run.<br>
        The model will always run for a full _cycling frequency_ (1 day) for each _Cylc_ cycle point.<br>
        This means, for example, that with `INITIAL_CYCLE_POINT` set to `20220226T0000Z`, and `FINAL_CYCLE_POINT` set to `+P1D` (plus 1 day), 2 _Cylc_ cycle points will be set (`20220226T0000Z` and `20220227T0000Z`). Therefore, the model will run for a total of 2 days!<br>
        To avoid running the model for longer that desired, we suggest adding `-PT1S` (minus 1 second) to the relative duration specified in the `FINAL_CYCLE_POINT` (refer to the example below).
        {: #run-length-mismatch }

    To modify these parameters within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Cycling options_. Edit the related field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
    For example, to run the experiment for 2 days starting on the 5th April 2000, set `INITIAL_CYCLE_POINT` to `20000405T0000Z` and `FINAL_CYCLE_POINT` to `+P2D-PT1S` (due to the [run length mismatch](#run-length-mismatch)).

#### Change the land-surface initial conditions source
- **RNS**<br>
    To change the [land-surface initial conditions source]({{ access_models }}/#land-surface-initial-conditions-source) within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Driving model setup_. Edit the `NCI_HRES_ECCB` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to get the land-surface initial conditions from the `BARRA-R2` dataset, set the `NCI_HRES_ECCB` field to `BARRA2-R`.

!!! warning
    When changing the land-surface initial conditions source, it is important to ensure that the configuration of the nested region aligns with the [nest configuration requirements](#nest-configuration-requirements).

#### Change the simulation region
In {{ model }}, users can perform simulations for a particular region of the Earth by configuring specific parameters for each domain of interest (referred to as _nested region_).<br>

In {{ model }}, the following parameters are supported to configure the nested regions:

- [Nested region name](#change-the-nested-region-name)
- [Nested region position](#change-the-nested-region-position)
- [Nested region's nest configuration](#change-the-nested-regions-nest-configuration)

!!! warning
    Domain-specific changes need to be consistent between RAS and RNS. Therefore, for each of the configuration parameters listed above, consistent changes to both RAS and RNS will be required.

##### Change the nested region name {: .no-toc }
- **RAS**<br>
    To change a nested region name within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Regional Ancillary Suite &rarr; Nested region 1 setup_. Edit the `rg01_name` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to set the name of the nested region to `Darwin`, set the `rg01_name` field to `Darwin`.

- **RNS**<br>
    Changing the RAS nested region name changes the [RAS output path](#ras-output-files). As a consequence, the following changes are required within the RNS:
    
    - **Ancillary directory**<br>
        To change the first nest ancillary directory within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 1 setup_. Change the `rg01_rs01_ancil_dir` field by replacing `Lismore` with the chosen RAS nested region name, and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
        The same step needs to be repeated for:
        
        - _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 2 setup_ `rg01_rs02_ancil_dir` field
        - _suite conf &rarr; Nesting Suite &rarr; Driving model setup_ `dm_ec_lam_ancil_dir` field

        For example, if the RAS nested region name was set to `Darwin`, replace `Lismore` in the `rg01_rs01_ancil_dir`, `rg01_rs02_ancil_dir` and `dm_ec_lam_ancil_dir` fields with `Darwin`.

    - **RNS nested region name**<br>
        To change the nested region name within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup_. Edit the `rg01_name` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

        For example, to set the name of the nested region to `Darwin`, set the `rg01_name` field to `Darwin`.

        !!! tip
            Changing the RNS nested region name is not strictly necessary, but it affects the [RNS outputs path](#rns-output-files). Therefore, for consistency, it is strongly recommended for RAS and RNS to have the same nested region names.

##### Change the nested region position {: .no-toc }
The nested region position is usually defined by the latitude and longitude coordinates of the nested region centre.

- **RAS**<br>
    To change the nested region centre within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Regional Ancillary Suite &rarr; Nested region 1 setup_. Edit the `rg01_centre` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to set the centre of the nested region to `-12.4` / `130.8`, set the `rg01_centre` field to `-12.4` / `130.8`.

!!! warning
    When changing the land-surface initial conditions source, it is important to ensure that the configuration of the nested region aligns with the [nest configuration requirements](#nest-configuration-requirements).

##### Change the nested region's nest configuration {: .no-toc }
Each nested region can contain multiple [nests]({{access_models}}/#nesting) (referred to as _Resolutions_ within the RAS and RNS), each of them being a separate domain where the simulation experiment is carried out.<br>
Typically, nests within the same nested region are arranged concentrically, with increasingly smaller dimensions and higher resolutions towards the innermost nests.

<div markdown id='nest-configuration-requirements'>
!!! warning
    Currently, {{model}} only supports specific nest configurations that meet the following criteria:
    
    The grid points of the RAS first inner nest (i.e., _Resolution 2_, because _Resolution 1_ always corresponds to the outer ERA5 domain) must align with those of the [land-surface initial conditions dataset]({{access_models}}/#land-surface-initial-conditions-source). Thus, the configuration of the RAS first inner nest (_Resolution 2_), including its position, dimension and resolution, need to be modified accordingly. Note that the position of a nest is also influenced by the [nested region position](#change-the-nested-region-position).
</div>

#### Change the output variables
[UM](/models/model_components/atmosphere/#unified-model-um) outputs are usually provided as a list of [STASH](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_C04.pdf) variables.<br>
Manually specifying each STASH variable can be complex. To simplify the selection process for commonly used climate analysis variables, predefined groups of STASH variables are set up, known as _stashpacks_.

- **RNS**<br>
    To toggle a _stashpack_ within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 1 setup &rarr; Config 1 setup_. Toggle a specific _stashpack_ within the `rg01_rs01_m01_stashpack` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
    Similar steps can be repeated for the _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 2 setup &rarr; Config 2 setup_ `rg01_rs02_m02_stashpack` field.<br>
    For example, to enable `stashpack 6` (that includes variables such as wind gust, mean sea level pressure and rainfall amount, for every model timestep) in all nests, set the `6th` button of both `rg01_rs01_m01_stashpack` and `rg01_rs02_m02_stashpack` fields to `true`.

## Troubleshooting
The following section outlines known issues along with possible workarounds to address them where applicable.

### NaNs in error term in BiCGstab

In some cases the choice of location and time produces initial conditions of the low resolution nest that leads to an unstable model state, causing a crash with an error similar to the following:

```
????????????????????????????????????????????????????????????????????????????????
???!!!???!!!???!!!???!!!???!!!       ERROR        ???!!!???!!!???!!!???!!!???!!!
?  Error code: 1
?  Error from routine: EG_BICGSTAB
?  Error message: NaNs in error term in BiCGstab after      1 iterations
?        This is a common point for the model to fail if it
?        has ingested or developed NaNs or infinities
?        elsewhere in the code.
?        See the following URL for more information:
?        https://code.metoffice.gov.uk/trac/um/wiki/KnownUMFailurePoints
?  Error from processor: 216
?  Error number: 22
????????????????????????????????????????????????????????????????????????????????
```

If that occurs, two possible work-arounds are:

- Reduce the GAL9 timestep from `300` to `150` seconds.<br>
  To achieve this, set `rg01_rs01_m01_dt` to `150` in the `rose-suite.conf` file.<br>
  This does not have a large impact on cycle time, and can usually be reverted in subsequent cycles when the simulation is running without error.
- Change the `INITIAL_CYCLE_POINT` in the `rose-suite.conf` file to an earlier day (usually 1 day should be enough).
  This can sometimes solve the issue, though at the expense of running the model simulation for longer than was initially desired.

More on this error in the [related forum post](https://forum.access-hive.org.au/t/issues-with-access-ram-ocean-domains-u-dg767-and-nans-in-bicgstab-u-dg768/4418).

### No-land and isolated land experiments
Configuring an experiment that contains only ocean points for the inner nests, with no land at all, is not supported by the UM.
In some cases, even when small groups of isolated land points are present there is not data available for those land points in the forcing datasets.<br>
This can cause issues in the RAS suite similar to the following:

```
Calculating bi-linear interpolation coeffs
Finding coastal points
Setting coastal values
 WARNING - No source data is available in target domain
UNRESOLVED GRID POINTS IN SOIL DATASET
 Number of points unresolved is                      9
 POINT      78674 LAT   -29.0100 LONG   167.9304
 POINT      78675 LAT   -29.0100 LONG   167.9502
 POINT      79124 LAT   -29.0298 LONG   167.9304
 POINT      79125 LAT   -29.0298 LONG   167.9502
 POINT      79126 LAT   -29.0298 LONG   167.9700
 POINT      79127 LAT   -29.0298 LONG   167.9898
 POINT      79574 LAT   -29.0496 LONG   167.9304
 POINT      79575 LAT   -29.0496 LONG   167.9502
 POINT      79576 LAT   -29.0496 LONG   167.9700
 Search radius                      1
 NO DATA FROM WHICH TO SET UNRESOLVED POINTS
 ***ERROR: No source data available in target domain
```

The only work-around in this case is to choose a different domain such that the inner nest contains more land points.

More on this error in the [related forum post](https://forum.access-hive.org.au/t/issues-with-access-ram-ocean-domains-u-dg767-and-nans-in-bicgstab-u-dg768/4418).

### Stuck cylc tasks
Testing of the RAS revealed an intermittent problem: sometimes tasks in `{{ ras_id }}` remain stuck in a _submitted_ state within the _Cylc_ GUI. 
Using `qstat` revealed that they had failed, but this was not correctly reflected in the GUI.

To test this error, run:

```
cat ~/cylc-run/{{ ras_id }}/log/job/1/<task_name>/01/job.err
```

and you should get an output similar to the following:

```
/local/spool/pbs/mom_priv/jobs/140074859.gadi-pbs.SC: line 104: /g/data/hr22/apps/cylc7/cylc_7.9.9/lib/cylc/job.sh: No such file or directory
/local/spool/pbs/mom_priv/jobs/140074859.gadi-pbs.SC: line 105: cylc__job__main: command not found
```

The workaround for this is to use the _Cylc_ GUI to:

1. Set the task state to failed.
2. Set the task state to waiting.
3. Check that the task then automatically goes into submitted, then running, then succeeded.

This is an intermittent, and often unreproducible error, hence the task should succeed when resubmitted. This issue has been reported to NCI.


## Get Help
If you have questions or need help regarding {{ model }}, consider creating a topic in the [Regional Nesting Suite category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/atmosphere/regional-nesting-suite/17).<br>
For assistance on how to request help from ACCESS-NRI, follow the [guidelines on how to get help](/about/user_support/#still-need-help).

<custom-references>
- [https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf](https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf)
- [https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html](https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html)
- [https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites)
- [https://opus.nci.org.au/display/Help/Persistent+Sessions](https://opus.nci.org.au/display/Help/Persistent+Sessions)
- [https://gmd.copernicus.org/articles/13/1999/2020/](https://gmd.copernicus.org/articles/13/1999/2020/)
</custom-references>
