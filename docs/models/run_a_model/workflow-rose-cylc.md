# The Rose/Cylc Workflow Management Tool

The _Rose/Cylc_ workflow management tool consists of two components- the [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA), and the [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UK Met Office (UKMO) which configures tasks for the _Cylc_ engine. A workflow comprised of set of tasks configured by _Rose_ to run with the _Cylc_ engine is called a "suite".

## Prerequisites

Before running a _Rose/Cylc_ suite on Gadi, you must:

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
 
## Launching a Cylc suite

There are two options for launching a _Rose/Cylc_ suite- either via the terminal directly, or via a Gadi [ARE VDI session](https://opus.nci.org.au/spaces/Help/pages/163250532/2.1.+Connecting+to+the+VDI). Both methods eventually end up in a terminal, so if you wish to use the terminal directory on a Gadi login node, skip directly to the [Set up a persistent session](#set-up-a-persistent-session) section.

!!! warning "X11 Forwarding"
    If you are going to connect via the terminal directly using SSH, it is recommended to connect with `ssh -X` to enable X11 forwarding. This allows the Rose and Cylc GUIs to be launched on your local machine.

### Launch ARE VDI Desktop

The following options are recommended for your ARE VDI desktop session. Note that the session is not running the tasks within the suite, only launching the _Rose/Cylc_ tool, which will then dispatch the tasks within the suite to the compute queue.

- **Walltime (hours)** &rarr; `2`<br>
    Amount of hours the ARE VDI session will remain active for. This is only setup time, and does not reflect how long the actual suite will take to run.

- **Queue** &rarr; `normalbw`
    
- **Compute Size** &rarr; `tiny` (1 CPU)<br>

- **Project** &rarr; a project of which you are a member.<br>
    The project must have allocated [_Service Units (SU)_](https://opus.nci.org.au/spaces/Help/pages/236881132/Allocations...) to run your simulation. Usually, but not always, this corresponds to your `${PROJECT}`.

- **Storage** &rarr; `gdata/access+gdata/xp65+gdata/hr22+gdata/ki32` (minimum)<br>
    Storage locations on Gadi that will be visible during execution of the suite. The packages listed above are the minimum required to run _Rose/Cylc_. Different models will require different storage locations, typically to have access to input data. The additional locations will be listed under `storage` on the respective [Run a Model](https://docs.access-hive.org.au/models/run-a-model/) pages.

Once the ARE VDI session opens in your browser, open the terminal by clicking the terminal icon at the top of the window. Use the terminal for the remainder of the instructions in this guide.

## Set up a persistent session

NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to facilitate long running processes, like the _Rose/Cylc_ manager. Begin a new persistent session with

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. The persistent session is given a unique identifier (referred to here as `<persistent-session-uuid>`), which you will need to end the session later.

<terminal-window data="input">
    <terminal-line>persistent-sessions -p &lt;project&gt; start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

Once the session is started, it needs to be assigned to the model run. This is done by inserting the persistent session label into `~/.persistent-sessions/cylc-session`, which can be done manually or with the command

```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

You can check that this worked with

```
cat ~/.persistent-sessions/cylc-session
```

For example, if user `abc123` started a persistent session named `CM2` under the project `tm70`, then the command would be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< CM2.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">CM2.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

Now the persistent session is set up, you can set up the _Rose/Cylc_ suite.

To list currently active suites, use:

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

Next, retrieve the model configuration you want to run from a remote host. Depending on the specific model configuration, the host is _Github_ or _MOSRS_. The [Run a Model](https://docs.access-hive.org.au/models/run-a-model/) documentation for the specific model will specify which source to use for that configuration. Regardless of where the configuration comes from, it is recommended to store them in `~/roses/` (this happens automatically for suites pulled from MOSRS).

### Github Suites

If the model configuration is hosted on Github, the Run a Model documentation will specify `repository` and `branch`, which describes where the default configuration is on Github. Move to the `~/roses` directory and pull the configuration from Github with:

```
git clone <repository> -b <branch>
```

The suite will appear in your current directory in the folder `<repository>`.

### MOSRS Suites

If the model configuration is hosted on MORSRS, the Run a Model documentation will specify `suite-id` (potentially multiple suites), which describe the suite ID(s) on the MOSRS repository. To pull from MOSRS, you must first authenticate your MOSRS credentials with:

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

Which will request your MOSRS username and password that you received when you created your MOSRS account. Once authenticated, pull the configuration from MOSRS with:

```
rosie checkout <suite-id>
```

The suite will appear in your current directory in the folder `<suite-id>`.

## Running the Suite

Now that you've pulled the suite, you can start the suite by changing into the suite directory and running:

```
rose suite-run
```

This launches the _Rose/Cylc_ suite. The _Cylc_ GUI should open which you can use to inspect the state of the suite (if you are running in the terminal directly and it doesn't appear, make sure you connected with [X11 forwarding](#x11-forwarding)). If you closed the GUI but want to re-open it, navigate to the suite directory and run:

```
rose suite-gcontrol &
```

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.

The suite itself, along will all generated output, is copied to `/scratch/<project>/${USER}/cylc-run/<suite-id>`. See the respective model documentation for details on what outputs are generated and where to find them in the output directory.

## Editing the Suite

To edit the suite configuration, move to the suite directory and run:

```
rose edit &
```

This opens the _Rose_ GUI that contains setup information for the suite. The configurable options for each model are described in their respective documentation pages.
