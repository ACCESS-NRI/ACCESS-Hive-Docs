[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview

# Run models using Rose/Cylc

!!! warning
    ACCESS models configurations that run with _Rose/Cylc_ currently use _Cylc7_, with intentions to upgrade to _Cylc8_. The upgrade is expected to change some aspects of the workflow described on this page. Updated information about the _Cylc8_ workflow will be provided once a model configuration using this version becomes available.

## About
The _Rose/Cylc_ workflow management tool consists of two components:

* The [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) (pronounced ‘silk’) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA). Cylc is a workflow manager that automatically executes tasks according to the model's main cycle script `suite.rc`. _Cylc_ controls how the job will be run and manages the time steps of each model component. It also monitors all tasks, reporting any errors that may occur.
* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UK Met Office (UKMO) which configures tasks for the _Cylc_ engine. Rose is a toolkit that can be used to view, edit, or run an ACCESS modelling suite.

A set of tasks configured by _Rose_ to run with the _Cylc7_ engine is called a _suite_.


## Prerequisites

- **NCI account**<br>
    Before running an ACCESS model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).<br> _Time estimate: ~5 minutes to sign up, ~a few hours for the account to be set up._

- **MOSRS account**<br>
    The [Met Office Science Repository Service (MOSRS)](https://code.metoffice.gov.uk) is a server run by the UKMO to support collaborative development with other partners organisations. MOSRS contains the source code for some ACCESS model components and configurations, and a MOSRS account is a license requirement to run some ACCESS configurations.<br>
    To apply for a MOSRS account, please contact your [local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
    {: #mosrs-account}

    !!! warning
    The waiting time to obtain a MOSRS account may be 2-3 weeks.

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [hr22](https://my.nci.org.au/mancini/project/hr22/join)

    _Time estimate: up to ~2 days_


 ## Quick guide to setting up Rose/Cylc

 These are the basic steps to set up Rose/Cylc before running an ACCESS model. For more detailed explanations and extra setup information, please refer to the sections below, starting with [Connecting to Gadi](#connecting-to-gadi).

- **Start a new [_persistent session_](https://opus.nci.org.au/display/Help/Persistent+Sessions)**<br> 
    In a [Gadi][gadi] login node or from an ARE terminal instance run:
    ```
    persistent-sessions start -p <project> <name>
    ```

    Further instructions in [Set up a persistent session](#set-up-a-persistent-session) below.

- **Assign the _persistent session_ to Cylc**<br>
    Run the following command:
    ```
    cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
    ```

    !!! tip
        This step should only be done once - you can run multiple Cylc sessions from the same persistent session.

    Further instructions in [Assign the persistent session to Cylc](#assign-the-persistent-session-to-cylc) below.

- **Rose/Cylc setup**<br>
    To get the required _Rose/Cylc_ setup, run:
    ```
    module use /g/data/hr22/modulefiles
    module load cylc7
    ```

    Further instructions in [Rose and Cylc executables](##rose-and-cylc-executables) below.

- **MOSRS authentication**<br>
    Authenticate using your MOSRS credentials:
    ```
    mosrs-auth
    ```

    Further instructions in [MOSRS authentication](#mosrs-authentication) below.

## Connecting to Gadi

You can run _Rose/Cylc_ either from a [_Gadi_ login node](#connect-via-gadi-login-node), or via an [ARE VDI session](#launch-are-vdi-desktop). 

### Connect via Gadi login node

<div markdown id="x11-forwarding">
!!! warning "X11 Forwarding"
    When connecting via SSH from a terminal, it is recommended to enable [X11 forwarding](https://some-natalie.dev/blog/ssh-x11-forwarding/), for example by adding the -X option to the `ssh` command. This allows the _Rose_ and _Cylc_ GUIs to be launched on your local machine.
</div>

Once you've connected, skip directly to [Set up a persistent session](#set-up-a-persistent-session).

### Launch ARE VDI Desktop

If you are not familiar with ARE, check out the [Getting Started on ARE](/getting_started/are) section.

!!! tip
    The ARE VDI session does not run model tasks directly; it only runs _Rose/Cylc_. The model tasks are dispatched by _Cylc_ to the compute nodes. This means the ARE VDI session requires minimal CPU and memory resources.

Go to the [ARE VDI](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) page and launch a session with the following entries:

- **Walltime (hours)** &rarr; `2`<br>
    Amount of hours the ARE VDI session will remain active for. This is only setup time, and does not reflect how long the actual configuration will take to run.

- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated [_Service Units (SU)_](https://opus.nci.org.au/spaces/Help/pages/236881132/Allocations...). By default, this will be set to your default project `$PROJECT`.

- **Storage** &rarr; `gdata/hr22+scratch/$PROJECT` (minimum)<br>
    The storage folders listed above are the minimum required to run _Rose/Cylc_.

Launch the ARE session and, once it opens in your browser, click on _Launch VDI Desktop_. 

![Launch ARE VDI session example](/assets/run_access_cm/launch_are_vdi.gif){: class="example-img" loading="lazy"}

Once the new tab opens, you will see a Desktop with a few folders on the left. Click the terminal icon at the top of the window to open a terminal. You should now be connected to a _Gadi_ computing node. Use this terminal for all subsequent steps in this guide.

![Open ARE VDI terminal example](/assets/run_access_cm/open_are_vdi_terminal.gif){: class="example-img" loading="lazy"}


## Set up a persistent session

NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to enable long running processes, like _Cylc_, to stay active even when the user disconnects from _Gadi_.

It is recommended to have only one active persistent session at any given time, as multiple _Cylc_ sessions can use the same persistent session.

Note that persistent sessions are terminated during the quarterly maintenance at NCI and will need to be restarted afterwards. The new persistent session can be given the same name as used previously.

### Start a new persistent session

Start a new persistent session by running (from either a _Gadi_ login node or an ARE VDI terminal instance):

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. 

!!! warning
    Persistent session names accept only a limited set of characters. We recommend using only alpha-numeric characters without spaces or underscores.

<terminal-window data="input">
    <terminal-line>persistent-sessions start -p &lt;project&gt; &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

The label of a newly-created _persistent session_ has the following format: <br>
`<name>.<$USER>.<project>.ps.gadi.nci.org.au`.

!!! tip
    If `-p <project>` is omitted, your [default project](/getting_started/set_up_nci_account/#change-default-project-on-gadi) `$PROJECT` will be used.


!!! tip
    While the project assigned to a _persistent session_ does not have to be the same as the project used to run the ACCESS model configuration, it does need to have allocated _Service Units (SU)_.<br>

The project assigned to a _persistent session_ does not have to be the same as the project used to run the ACCESS model configuration. The newly created persistent session is assigned a unique identifier, referred to here as `<persistent-session-uuid>`.

### Assign the persistent session to Cylc

Once the session is running, it needs to be assigned to _Cylc_. This is done by inserting the persistent session label into `~/.persistent-sessions/cylc-session`, which can be done with the following command (substituting `<name>` and `<project>` with the name and project used to create the persistent session).

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

For more information on how to specify the target session, refer to [Specify Target Session with Cylc7 Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites#RunCylc7Suites-SpecifyTargetSession).

### List active persistent sessions {: .no-toc }

To list your currently active sessions, use:

```
persistent-sessions list
```
### Terminate a persistent session {: .no-toc }

To end a specific session, use:

```
persistent-sessions kill <persistent-session-uuid>
```

!!! tip
    Logging out of a *Gadi* login node or an ARE VDI terminal instance will not affect your _persistent session_.

!!! warning
    When you terminate a _persistent session_, any model running on that session will stop. Therefore, you should check whether you have any active model runs before terminating a _persistent session_.

## Set up Rose/Cylc

### Rose and Cylc executables

Make the `rose` and `cylc` executables available by loading the _Cylc_ module:

```
module use /g/data/hr22/modulefiles
module load cylc7
```

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

After the first authentication, you will need to run `mosrs-auth` every 24 hours and for every new connection to _Gadi_ (e.g., new terminal) to verify your password against the saved credentials.

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

Both options use [Rosie](https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rosie) - an [SVN](https://subversion.apache.org) repository wrapper with a set of options specific for ACCESS modelling suites. It is automatically available within the [_Rose_ setup](#rose).

If you're not sure which option to use, we recommend using the "local-only copy". The "remote and local copy" is best used if you plan to commit the suite back to the remote.

Suites are, by default when copying from MOSRS, created in the user's _Gadi_ home directory under `~/roses/<suite-ID>`.
This path will be referred to as the *suite directory*.
{: #suitedir }

The suite directory contains multiple subdirectories and files, including:

- `app` &rarr; directory containing the configuration files for various tasks within the suite.
- `meta` &rarr; directory containing the GUI metadata.
- `rose-suite.conf` &rarr; main suite configuration file.
- `rose-suite.info` &rarr; suite information file.
- `suite.rc` &rarr; _Cylc_ control script file (Jinja2 language).

#### Local-only copy {: #rosie-checkout }

```
rosie checkout <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model](/models/run_a_model/) documentation. This creates a local copy of the configuration, which is placed in the `~/roses/<suite-id>` folder.

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

Configurations obtained in this way cannot be pushed back to the remote. Therefore, the use of this command is recommended for testing and examining configurations.

#### Local and remote copy (new remote configuration) {: #rosie-copy }

Before creating a new remote copy of the configuration, please read [these guidelines](https://code.metoffice.gov.uk/trac/roses-u/) on what should be stored in the Rosie repository.

```
rosie copy <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model documentation](/models/run_a_model/).

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

After running this command, a text editor will open in your terminal, where you can define metadata for the new configuration (the default text editor is _Vim_, and [this quick guide](https://eastmanreference.com/a-quick-start-guide-for-beginners-to-the-vim-text-editor) is a good reference if you're unfamiliar with it). The metadata fields are expressed as `key=value` pairs, pre-filled with values copied from the original configuration. You can modify these values or add new metadata as needed. Note that `owner`, `project` and `title` are required keys. 
```
owner=<MOSRS-username>
project=<project-name>
title=<suite-title>
```

When you exit the editor, you will have to confirm that you want to copy the suite:

<terminal-window>
    <terminal-line data="input">rosie copy &lt;suite-id&gt;/&lt;branch&gt;</terminal-line>
    <terminal-line>Copy "&lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;" to "u-?????"? [y or n (default)]</terminal-line> <terminal-line data="input">y</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: created at https://code.metoffice.gov.uk/svn/roses-u/&lt;suite-n/a/m/e/&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: copied items from &lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: local copy created at &lt;$HOME&gt;/roses/&lt;new-suite-id&gt;</terminal-line>
</terminal-window>

This creates a new remote configuration with a new `suite_id` (based off the copied configuration) and clones a copy of it locally in the `~/roses/<new-suite-id>` folder. Configurations created in this way are separate from the original copied configuration and can be modified and pushed back to the remote.

To push a configuration back to the remote, from within the configuration directory run:

```
fcm commit
```


For additional `rosie` options, run:
```
rosie help
```

## Run the model configuration
!!! warning
    Before running a configuration, make sure to follow the initial setup for it (e.g., setting the correct compute project and storage resources). For details, follow the instructions relative to your specific model in the [Run a model](/models/run_a_model) page.

To run the configuration:

```
cd ~/roses/<suite-id>
rose suite-run
```

This moves you into the configuration directory, launches the _Rose/Cylc_ configuration and opens the _Cylc_ GUI (if you are running on the login node and the GUI doesn't appear, make sure you connected with [X11 forwarding](#x11-forwarding) enabled). If you closed the GUI and want to re-open it, run:

```
cd ~/roses/<suite-id>
rose suite-gcontrol &
```

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.

By default, the configuration, log files and outputs are copied to `/scratch/<project>/${USER}/cylc-run/<suite-id>`. See the respective [Run a model](/models/run_a_model/) documentation for details on what outputs are generated and where to find them.

## Edit the model configuration

To edit the model configuration, run the following:

```
cd ~/roses/<suite-id>
rose edit &
```

This opens the _Rose_ GUI, where the configuration settings can be modified. Once you are happy with the changes, save the modified configuration by clicking on the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}. 

Alternatively, you can edit the configuration files within the configuration directory directly using your chosen editor.

!!! warning
    Directly modifying configuration files with an editor is usually discouraged for non-expert users.

For a description of some common configuration settings, see the respective [Run a model](/models/run_a_model/) documentation.

You are now ready to a run a model with _Rose/Cylc_.

[Run an ACCESS model](/models/run_a_model/){: class="text-card"}
