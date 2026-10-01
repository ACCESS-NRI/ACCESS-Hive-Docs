[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
# Run models using Rose/Cylc

!!! warning
    ACCESS model configurations that run with _Rose/Cylc_ currently use _Cylc7_, with plans to upgrade to _Cylc8_. This upgrade is expected to change some aspects of the workflow described on this page. Information on the _Cylc8_ workflow will be provided once a model configuration using this version is available.

## About
The _Rose/Cylc_ workflow management tool consists of two components:

* The [Cylc](https://niwa.co.nz/environmental-information/cylc-suite-engine) (pronounced ‘silk’) task engine, developed by NIWA, is a workflow manager that automatically executes tasks according to a model configuration and monitors them for errors.
* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UKMO configures tasks for the _Cylc_ engine. _Rose_ is a toolkit that can be used to view, edit and run some of the [ACCESS models](/models/access_models).

A set of tasks configured by _Rose_ to run with the _Cylc7_ engine is called a _suite_. Every _suite_ has a unique identifier called `suite-ID` in the form `u-LLNNN`, where `L` is a letter and `N` is a number (e.g., u-ab123).

<!--start:rose-directory-->
#### Configuration directory

It is recommended to store your local copy of the configuration in your `~/roses/` directory (create the directory if it does not exist). This directory will be referred to as the *configuration directory*.
{: #configdir }

This configuration directory contains multiple subdirectories and files, including:

- `app` &rarr; directory containing specific configuration files for various model tasks.
- `meta` &rarr; directory containing the _Rose_ GUI metadata.
- `rose-suite.conf_nci_gadi` &rarr; main model configuration file.
- `rose-suite.info` &rarr; configuration information file.
- `suite.rc` &rarr; _Cylc_ control script file (Jinja2 language).
<!--end:rose-directory-->


## Prerequisites

- **NCI account**<br>
    Before running an ACCESS model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **MOSRS account**<br>
    [MOSRS](https://code.metoffice.gov.uk) is a server run by the UKMO to support collaborative development with other partners organisations. MOSRS contains the source code for some ACCESS model components and configurations, and a MOSRS account is a license requirement to run some ACCESS configurations.<br>
    To apply for a MOSRS account, please contact your [local institutional sponsor](https://opus.nci.org.au/display/DAE/Prerequisites).
    {: #mosrs-account}

    !!! warning
        The waiting time to obtain a MOSRS account can be up to 3 weeks.

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [hr22](https://my.nci.org.au/mancini/project/hr22/join)


## Connecting to Gadi

<!--start:cylc-gadi-->
You can run _Rose/Cylc_ either from a [_Gadi_ login node](#connect-via-gadi-login-node) or via an [ARE VDI session](#launch-are-vdi-desktop). 

??? info "Connect via _Gadi_ login node"

    Follow the steps to [login to _Gadi_](/getting_started/set_up_nci_account/#login-to-gadi), making sure to enable [X11 forwarding](https://some-natalie.dev/blog/ssh-x11-forwarding/), for example by adding the -X option to the `ssh` command. This allows the _Rose_ and _Cylc_ GUIs to be launched on your local machine.

    Once you are connected, skip directly to [Set up a persistent session](#set-up-a-persistent-session).

??? info "Connect via ARE VDI Desktop"

    If you are not familiar with ARE, check out the [Getting Started on ARE](/getting_started/are) page.

    !!! tip
        The ARE VDI session does not run model tasks directly; it only runs _Rose/Cylc_. The model tasks are dispatched by _Cylc_ to the compute nodes. This means the ARE VDI session requires minimal CPU and memory resources.

    Go to the [ARE VDI](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) page and launch a session with the following entries:

    - **Walltime (hours)** &rarr; `2`<br>
            Amount of hours the ARE VDI session will remain active for. This is only setup time, and does not reflect how long the actual configuration will take to run.
            
        !!! tip 
            Some model configurations may require additional setup time. The _walltime_ specified here should be sufficient for most configurations, but if your ARE session terminates before setup is complete, you can start a new ARE VDI session and continue.

    - **Queue** &rarr; `normalbw`
        
    - **Compute Size** &rarr; `tiny` (1 CPU)<br>

    - **Project** &rarr; a project of which you are a member.<br>
        The project must have allocated [_SU_](https://opus.nci.org.au/spaces/Help/pages/236881132/Allocations...). By default, this will be set to your default project `$PROJECT`.

    - **Storage** &rarr; `gdata/hr22+scratch/$PROJECT` (minimum)<br>
        The storage folders listed above are the minimum required to run _Rose/Cylc_.

    Launch the ARE session and, once it starts, click on _Launch VDI Desktop_.

    ![Launch ARE VDI session example](/assets/run_access_cm/launch_are_vdi.gif){: class="example-img" loading="lazy"}

    !!! warning
        This example is provided for reference only. Please use the resource specifications listed above when starting the ARE VDI session.
    
    Once the new tab opens, you will see a Desktop with a few folders on the left. Click the terminal icon at the top of the window to open a terminal. You should now be connected to a _Gadi_ computing node. Use this terminal for all subsequent steps in this guide.

    ![Open ARE VDI terminal example](/assets/run_access_cm/open_are_vdi_terminal.gif){: class="example-img" loading="lazy"}
<!--end:cylc-gadi-->

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

After the initial authentication, run `mosrs-auth` every 24 hours and after each new connection to _Gadi_ (e.g., a new terminal) to verify your password against the saved credentials

## Get the model configuration

Depending on the specific model, its configuration will be hosted either on _GitHub_ or MOSRS. The [Run a Model](/models/run_a_model/) documentation for the respective model will specify where the configuration is stored.<br>


### Model configurations stored on _GitHub_

<!--start:get-github-config-->
To get a local copy of the configuration of your choice, clone the _GitHub_ branch with:

```
git -C ~/roses clone {{github_configs}} -b <branch> <experiment_name>
```

where:

- `<branch>` is the name of the branch of the configuration you want to base your work on.
- `<experiment_name>` is the name of your local copy of the configuration, i.e., your _configuration directory_. _Cylc_ also uses it for the _control_ directory path.

??? example "Example: Copying the {{config_branch}} configuration"
  
    If you want a copy of the {{config_branch}} configuration for {{model}} in your `~/roses/` directory, in a _Gadi_ terminal, you would run the command:

    ```
    git -C ~/roses clone {{github_configs}} -b {{config_branch}} {{experiment_name}}
    ```

    This will create the directory `~/roses/{{experiment_name}}` that will contain a copy of the latest _{{config_branch}}_ configuration. It is recommended to choose a descriptive name for the `<experiment_name>` unlike in this example.
<!--end:get-github-config-->

If you want to make exploratory changes within the configuration, and have those changes tracked, please [fork the configuration repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and commit your changes there.<br>

!!! warning
    Configuration repositories store each configuration in their own branch, while the `main` branch only keeps minimal setup.<br>
    For this reason, when forking the repository, ensure that all branches are included by unchecking the option “Copy the `main` branch only”.

If you think your new configuration provides significant value to the broader community, refer to the respective model configuration documentation for instructions on how to have it officially supported by ACCESS-NRI.

### Model configurations stored on MOSRS

There are two ways of getting a local copy of a configuration hosted on MOSRS:

- [Local-only copy](#rosie-checkout)
- [Local and remote copy (new remote configuration)](#rosie-copy)

Both options use [Rosie](https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rosie) - a tool that uses [SVN](https://subversion.apache.org) to manage, develop, and collaborate on Rose modelling workflows. It is automatically available within the [_Rose_ setup](#rose).

If you're not sure which option to use, we recommend using the "local-only copy". The "remote and local copy" is best used if you plan to commit the suite back to the remote.

Configurations copied from MOSRS are created by default in the user's _Gadi_ home directory under `~/roses/<suite-ID>`, which is the _configuration_ directory.

#### Local-only copy {: #rosie-checkout }

```
rosie checkout <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model](/models/run_a_model/) documentation. This creates a local copy of the configuration, which is placed in the `~/roses/<suite-id>` folder.

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

Configurations obtained this way cannot be pushed back to the remote repository. This command is therefore recommended for testing and inspecting configurations.

#### Local and remote copy (new remote configuration) {: #rosie-copy }

Before creating a new remote copy of the configuration, please read [these guidelines](https://code.metoffice.gov.uk/trac/roses-u/) on what should be stored in the Rosie repository.

```
rosie copy <suite-id>/<branch>
```

where `<suite-id>` and `<branch>` are specific to the chosen model configuration and can be found in the respective [Run a Model documentation](/models/run_a_model/).

!!! tip
    To copy from the default branch (`trunk`), omit the `/<branch>` portion of the command.

After running this command, a text editor opens in your terminal, where you can define metadata for the new configuration. The default text editor is _Vim_; see [this quick guide](https://eastmanreference.com/a-quick-start-guide-for-beginners-to-the-vim-text-editor) if you are unfamiliar with it.

Metadata fields are specified as `key=value` pairs and are pre-filled with values copied from the original configuration. You can modify these values or add new ones as needed. The `owner`, `project` and `title` keys are required. 

```
owner=<MOSRS-username>
project=<project-name>
title=<suite-title>
```

After exiting the editor, confirm that you want to copy the suite:

<terminal-window>
    <terminal-line data="input">rosie copy &lt;suite-id&gt;/&lt;branch&gt;</terminal-line>
    <terminal-line>Copy "&lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;" to "u-?????"? [y or n (default)]</terminal-line> <terminal-line data="input">y</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: created at https://code.metoffice.gov.uk/svn/roses-u/&lt;suite-n/a/m/e/&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: copied items from &lt;suite-id&gt;/&lt;branch&gt;@&lt;revision&gt;</terminal-line>
    <terminal-line>[INFO] &lt;new-suite-id&gt;: local copy created at &lt;$HOME&gt;/roses/&lt;new-suite-id&gt;</terminal-line>
</terminal-window>

This creates a new remote configuration with a new `suite_id` based on the copied configuration and clones a local copy to `~/roses/<new-suite-id>`. The new configuration is independent of the original and can be modified and pushed back to the remote.

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

ACCESS model configurations run on [_Gadi_][gadi] through [PBS jobs][PBS job] submissions. They often comprise several tasks, such as checking out code repositories, compiling and building different model components, and running the model. _Cylc_ controls the workflow and sequencing of these tasks.

To run the configuration, execute the following commands:

```
rose suite-run -C ~/roses/<suite-id>
```
This launches the _Rose/Cylc_ configuration and opens the _Cylc_ GUI. If the GUI does not open when running on the login node, ensure you connected with [X11 forwarding](https://github.com/ACCESS-NRI/ACCESS-Hive-Docs/pull/1238/changes#x11-forwarding) enabled. The _Cylc_ GUI allows you to monitor and control tasks as they run and can be safely closed without affecting the model run. To reopen the GUI, run:

```
rose suite-gcontrol --name=<suite-id> &
```

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.

By default, the configuration, log files and outputs are copied to `/scratch/<project>/${USER}/cylc-run/<suite-id>`. A symbolic link to this directory is also created in your home directory under `~/cylc-run/<suite-ID>`. See the respective [Run a model](/models/run_a_model/) documentation for details on what outputs are generated and where to find them.

## Edit the model configuration

In general, the configurations of ACCESS models can be edited either by directly modifying the configuration files within the configuration directory, or by using the [_Rose_ GUI](#rosegui).

### Rose GUI

To edit the model configuration, run the following:

```
rose edit -C ~/roses/<suite-id> &
```

This opens the _Rose_ GUI, where you can modify the configuration settings. Once you are satisfied with your changes, click the _Save_ button to save the modified configuration. 
![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}

!!! tip
    The `&` is optional. It detaches the invoked process, allowing the terminal prompt to remain active while the GUI is open.


!!! warning
    Directly editing configuration files is generally discouraged for non-expert users.

For a description of some common configuration settings, see the respective [Run a model](/models/run_a_model/) documentation.

You are now ready to a run a model with _Rose/Cylc_.

[Run an ACCESS model](/models/run_a_model/){: class="text-card"}
