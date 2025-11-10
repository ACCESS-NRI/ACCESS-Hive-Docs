# Run models using Rose/Cylc

## About
The _Rose/Cylc_ workflow management tool consists of two components:

* The [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA)* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UK Met Office (UKMO) which configures tasks for the _Cylc_ engine. 

A set of tasks configured by _Rose_ to run with the _Cylc_ engine is called a _suite_ (for _Cylc 7_) or _workflow_ (for _Cylc 8_).

!!! warning
    ACCESS models configurations that run with _Rose/Cylc_ use _Cylc7_, with intentions to upgrade to _Cylc8_. The upgrade is expected to change some aspects of the workflow described on this page. Updated information about the _Cylc8_ workflow will be provided once a model configuration using this version becomes available.

## Prerequisites

- **NCI account**<br> 
    Before running an ACCESS model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **MOSRS account**<br>
    The [Met Office Science Repository Service (MOSRS)](https://code.metoffice.gov.uk) is a server run by the UKMO to support collaborative development with other partners organisations. MOSRS contains the source code for some ACCESS model components and configurations, and a MOSRS account is a license requirement to run some ACCESS configurations.<br>
    To apply for a MOSRS account, please contact your [local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
    {: #mosrs-account}

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [hr22](https://my.nci.org.au/mancini/project/hr22/join)
    
## Connecting to Gadi

You can run _Rose/Cylc_ either from a _Gadi_ login node, or via an [ARE VDI session](https://opus.nci.org.au/spaces/Help/pages/163250532/2.1.+Connecting+to+the+VDI). If you wish to use the _Gadi_ login node, skip directly to [Set up a persistent session](#set-up-a-persistent-session).

<div markdown id="x11-forwarding">
!!! warning "X11 Forwarding"
    If using a terminal to connect directly using SSH, it is recommended to connect with `ssh -X` to enable X11 forwarding. This allows the _Rose_ and _Cylc_ GUIs to be launched on your local machine.
</div>

### Launch ARE VDI Desktop

!!! tip
    The ARE VDI session does not run configuration tasks directly; it only runs _Rose/Cylc_. The configuration tasks are dispatched by _Cylc_ to the compute nodes. This means the ARE VDI session requires minimal CPU and memory resources.

The following options are recommended for your ARE VDI desktop session:

- **Walltime (hours)** &rarr; `2`<br>
    Amount of hours the ARE VDI session will remain active for. This is only setup time, and does not reflect how long the actual configuration will take to run.

- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated [_Service Units (SU)_](https://opus.nci.org.au/spaces/Help/pages/236881132/Allocations...) to run your simulation. By default, this will be set to your default project `$PROJECT`.

- **Storage** &rarr; `gdata/hr22, scratch/$PROJECT` (minimum)<br>
    The storage folders listed above are the minimum required to run _Rose/Cylc_.

Once the ARE VDI session opens in your browser, click the terminal icon at the top of the window to open a terminal. Use this terminal for all subsequent steps in this guide.

## Set up a persistent session

NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to enable long running processes, like _Cylc_, to stay active even when the user disconnects from _Gadi_.

It is recommended to only have one active persistent session at any one time as several _Cylc_ sessions can use the same persistent session.

Note that persistent sessions are terminated during the quarterly maintenance at NCI and will need to be restarted afterwards. The new persistent session can be given the same name as used previously.

### Start a new persistent session

Start a new persistent session by running:

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. 

!!! warning
    Persistent session names accept only a limited set of characters. We recommend using only alpha-numeric characters without spaces or underscores.

<terminal-window data="input">
    <terminal-line>persistent-sessions -p &lt;project&gt; start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

!!! tip
    If `-p <project>` is ommitted, your default project `$PROJECT` will be used.

Persistent sessions can run simulations using compute and storage resources from any project, independently of the project used for the persistent session itself. The newly created persistent session is assigned a unique identifier, referred to here as `<persistent-session-uuid>`.

### Assign the persistent session to Cylc {: .no-toc }

Once the session is running, it needs to be assigned to _Cylc_. This is done by inserting the persistent session label into `~/.persistent-sessions/cylc-session`, which can be done with the following command (substituting `<name>` and `<project>` for the name and project used to create the persistent session).

```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

You can check that this worked with:

```
cat ~/.persistent-sessions/cylc-session
```

For example, if user `abc123` started a persistent session named `ForCylc` under the project `tm70`, then the command would be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

### List active persistent sessions {: .no-toc }

To list currently active sessions, use:

```
persistent-sessions list
```
### Terminate a persistent sessions {: .no-toc }

To end a specific session, use:

```
persistent-sessions kill <persistent-session-uuid>
```

## Rose/Cylc Setup

### Rose and Cylc executables

Make the `rose` and `cylc` executables available by loading the _Cylc_ module:

```
module use /g/data/hr22/modulefiles
module load cylc7
```

where `<version>` is the version of _Cylc_ used by the respective configuration.

### MOSRS Authentication

The ACCESS models which use _Cylc_ require a connection to the MOSRS mirror on _Gadi_. To connect to this mirror, you must first authenticate your MOSRS credentials with:

```
mosrs-auth
```

This will request the username and password you received when you created your MOSRS account.

<terminal-window>
    <terminal-line data="input">mosrs-auth</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: You need to enter your MOSRS credentials here so that GPG can cache your password.</terminal-line>
    <terminal-line>Please enter the MOSRS password for &lt;MOSRS-username&gt;:</terminal-line>
    <terminal-line lineDelay=1500>Checking your credentials using Subversion. Please wait.</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: Successfully accessed Subversion with your credentials.</terminal-line>
    <terminal-line lineDelay=100><span style="color: #559cd5;">INFO</span>: Checking your credentials using rosie. Please wait.</terminal-line>
    <terminal-line lineDelay=500><span style="color: #559cd5;">INFO</span>: Successfully accessed rosie with your credentials.</terminal-line>
</terminal-window>

After the first authentication, you will need to run `mosrs-auth` every 24 hours and for every new connection to _Gadi_ (e.g. new terminal) to verify your password against the saved credentials.

## Get the model configuration

Depending on the specific model, its configuration will be hosted either on _GitHub_ or MOSRS. The [Run a Model](/models/run_a_model/) documentation for the respective model will specify where the configuration is stored.<br>

Regardless of where the configuration comes from, it is recommended to store the local copy in the `~/roses/` directory (this happens automatically for configurations pulled from MOSRS).

### Model configurations stored on _GitHub_

For _GitHub_ hosted configurations, get a local copy by cloning the _GitHub_ repository with:

```
git -C ~/roses clone <repository> -b <branch>
```

where `<repository>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model](/models/run_a_model/) documentation.

If you want to make exploratory changes within the configuration, and have those changes tracked, please [fork the configuration repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and commit your changes there.<br>
If you think your new configuration provides significant value to the broader community, refer to the respective model configuration documentation for instructions on how to have it officially supported by ACCESS-NRI.

### Model configurations stored on MOSRS

There are two ways of getting a local copy of a configuration hosted on MOSRS:

- [Local-only copy](#rosie-checkout)
- [Local and remote copy (new remote configuration)](#rosie-copy)


#### Local-only copy {: #rosie-checkout }

```
rosie checkout <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model](/models/run_a_model/) documentation. This creates a local copy of the configuration, which is placed in the `~/roses/<suite-id>` folder.

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

Configurations obtained in this way cannot be pushed back to the remote, so use of this command is recommended for testing and examining configurations.

#### Local and remote copy (new remote configuration) {: #rosie-copy }

Before creating a new remote copy of the configuration, please read [these guidelines](https://code.metoffice.gov.uk/trac/roses-u/) on what should be stored in the Rosie repository.

```
rosie copy <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model documentation](/models/run_a_model/).

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

After running this command, a text editor will open in your terminal, where you can define metadata for the new configuration (the default text editor is _Vim_, and [this quick guide](https://eastmanreference.com/a-quick-start-guide-for-beginners-to-the-vim-text-editor) is a good reference is you're unfamiliar with it). The metadata fields are expressed as `key=value` pairs, pre-filled with values copied from the original configuration. You can modify these values or add new metadata as needed. Note that `owner`, `project` and `title` are required keys. 
```
owner=<MOSRS-username>
project=<project-name>
title=<suite-title>
```

When you exit the editor, you will have to confirm that you want to copy the suite:

<terminal-window>
    <terminal-line data="input">rosie copy <suite-id>/<branch></terminal-line>
    <terminal-line>Copy "&lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;" to "u-?????"? [y or n (default)]</terminal-line> <terminal-line data="input">y</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: created at https://code.metoffice.gov.uk/svn/roses-u/&lt;suite-n/a/m/e/&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: copied items from &lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: local copy created at &lt;$HOME&gt;/roses/&lt;new-suite-id&gt;</terminal-line>
</terminal-window>

This creates a new remote configuration with a new `suite_id` (based off the copied configuration) clones a copy of it locally in the `~/roses/<new-suite-id>` folder. Configurations created in this way are separate from the original copied configuration and can be modified and pushed back to the remote.

To push a configuration back to the remote, from within the configuration directory run:

```
fcm commit
```

## Run the model configuration

To run the configuration, execute the following command from within the configuration directory:

```
rose suite-run
```

This launches the _Rose/Cylc_ configuration and opens the _Cylc_ GUI (if you are running on the login node and the GUI doesn't appear, make sure you connected with [X11 forwarding](#x11-forwarding) enabled). If you closed the GUI but want to re-open it, navigate to the configuration directory and run:

```
rose suite-gcontrol &
```

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.

By default, the configuration, log files and outputs are copied to `/scratch/<project>/${USER}/cylc-run/<suite-id>`. See the respective [Run a model](https://docs.access-hive.org.au/models/run_a_model/) documentation for details on what outputs are generated and where to find them.

## Edit the model configuration

To edit the model configuration, run the following command from the configuration directory:

```
rose edit &
```

This opens the _Rose_ GUI that contains information about the configuration settings. For a description of the simple configuration settings, see the respective [Run a model](https://docs.access-hive.org.au/models/run_a_model/) documentation.

Once settings have been modified in the _Rose_ GUI, save them by clicking on the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.
