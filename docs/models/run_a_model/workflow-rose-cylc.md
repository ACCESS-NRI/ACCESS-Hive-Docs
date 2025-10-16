# Run models using Rose/Cylc

## About
The _Rose/Cylc_ workflow management tool consists of two components- the [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA), and the [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UK Met Office (UKMO) which configures tasks for the _Cylc_ engine. A workflow comprised of set of tasks configured by _Rose_ to run with the _Cylc_ engine is officially called a "suite" or "workflow", depending on the version of _Cylc_. Here we refer to them as "configurations" for consistency across our different tools and avoid naming confusion as we move to _Cylc8_.

## Prerequisites

Before running a _Rose/Cylc_ configuration on Gadi, you must:

1. [Set up your NCI account](/getting_started/set_up_nci_account).
2. Apply for a MOSRS account by getting in contact with [your local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
3. Join the following NCI projects:
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
 
## Connecting to Gadi

You can run _Rose/Cylc_ either from a _Gadi_ login node, or via an [ARE VDI session](https://opus.nci.org.au/spaces/Help/pages/163250532/2.1.+Connecting+to+the+VDI). If you wish to use the Gadi login node, skip directly to the [Set up a persistent session](#set-up-a-persistent-session) section.

<div markdown id="x11-forwarding">
!!! warning "X11 Forwarding"
    If you are going to connect via the terminal directly using SSH, it is recommended to connect with `ssh -X` to enable X11 forwarding. This allows the Rose and Cylc GUIs to be launched on your local machine.
</div>

### Launch ARE VDI Desktop

The following options are recommended for your ARE VDI desktop session.

!!! tip
    The ARE VDI session does not run configuration tasks directly; it only runs _Rose/Cylc_. The configuration tasks are dispatched by _Cylc_ to the compute nodes. This means the ARE VDI session requires minimal CPU and memory resources.

- **Walltime (hours)** &rarr; `2`<br>
    Amount of hours the ARE VDI session will remain active for. This is only setup time, and does not reflect how long the actual configuration will take to run.

- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated [_Service Units (SU)_](https://opus.nci.org.au/spaces/Help/pages/236881132/Allocations...) to run your simulation. By default, this will be set to your default project `$PROJECT`.

- **Storage** &rarr; `gdata/access+gdata/hr22+gdata/ki32` (minimum)<br>
    The storage folders listed above are the minimum required to run _Rose/Cylc_.

Once the ARE VDI session opens in your browser, click the terminal icon at the top of the window to open a terminal. Use this terminal for all subsequent steps in this guide.

## Set up a persistent session

NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to enable long running processes, like the _Rose/Cylc_ manager. 

### Start a new persistent session

Start a new persistent session by running:

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. 

<terminal-window data="input">
    <terminal-line>persistent-sessions -p &lt;project&gt; start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

!!! tip
    If `-p <project>` is ommitted, your default project `$PROJECT` will be used.

The newly created persistent session is assigned a unique identifier, referred to here as `<persistent-session-uuid>`.

### Assign the persistent session to Cylc {: .no-toc }

Once the session is running, it needs to be assigned to _Cylc_. This is done by inserting the persistent session label into `~/.persistent-sessions/cylc-session`, which can be done with the following command (substituting `<name>` and `<project>` for the name and project used to create the persistent session).

```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

You can check that this worked with:

```
cat ~/.persistent-sessions/cylc-session
```

For example, if user `abc123` started a persistent session named `CM2` under the project `tm70`, then the command would be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< CM2.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">CM2.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

### List active persistent sessions {: .no-toc }

To list currently active sessions, use:

```
persistent-sessions list
```

To end a specific session, use:

```
persistent-sessions kill <persistent-session-uuid>
```

## Rose/Cylc Setup

First, load the _Cylc_ module with:

```
module use /g/data/hr22/modulefiles
module load cylc7
```

This adds the _Rose_ and _Cylc_ executables into your current environment.

### MOSRS Authentication

The ACCESS models which use _Cylc_ require a connection to the MOSRS mirror on Gadi. To connect to this mirror, you must first authenticate your MOSRS credentials with:

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

This will request the username and password you received when you created your MOSRS account.

### Get the model configuration

Next, retrieve the model configuration you want to run from a remote host. Depending on the specific model configuration, the host is _Github_ or _MOSRS_. The [Run a Model](https://docs.access-hive.org.au/models/run-a-model/) documentation for the specific model will specify which source to use for that configuration. Regardless of where the configuration comes from, it is recommended to store them in `~/roses/` (this happens automatically for configurations pulled from MOSRS).

### Model configurations stored on Github

For Github hosted configurations, the Run a Model documentation will specify the `repository` and `branch` which host the configuration. From the `~/roses` directory, clone the repository from Github with:

```
git clone <repository> -b <branch>
```

### Model configurations stored on MOSRS

For MOSRS hosted configurations, the Run a Model documentation will specify the `suite-id` and `branch` which host the configuration. Some MOSRS hosted configurations will be comprised of multiple suites e.g. rAM3, in which case multiple `<suite-id>`s will be specified.

```
rosie checkout <suite-id>
```

The configuration will appear in your current directory in the folder `<suite-id>`.

## Run the model configuration

To run the configuration, execute the following command from within the configuration directory:

```
rose suite-run
```

This launches the _Rose/Cylc_ configuration. The _Cylc_ GUI should open which you can use to inspect the state of the configuration (if you are running in the terminal directly and it doesn't appear, make sure you connected with [X11 forwarding](#x11-forwarding)). If you closed the GUI but want to re-open it, navigate to the configuration directory and run:

```
rose suite-gcontrol &
```

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.

The configuration itself, along will all generated output, is copied to `/scratch/<project>/${USER}/cylc-run/<suite-id>`. See the respective model documentation for details on what outputs are generated and where to find them in the output directory.

## Edit the model configuration

To edit the model configuration, run the following command from the configuration directory:

```
rose edit &
```

This opens the _Rose_ GUI that contains information about the configuration. The configurable options for each model configuration are described in their respective documentation pages.
