# Australian Research Environment (ARE)

[ARE](https://are.nci.org.au) is a web-based graphical interface for performing your computational research, provided by [NCI](https://nci.org.au).<br>
ARE gives you access to NCI’s _Gadi_ supercomputer and data collections.

There are multiple applications included in ARE, but the two most used for ACCESS-related activities are [Virtual Desktop (VDI)](#vdi) and [JupyterLab](#jupyterlab).

## Prerequisites
To use ARE, you must have an NCI account and be a member of a project with computing resources (known as Service Units, or SU). For instructions on how to set up an account and join projects, refer to [Set Up your NCI Account](/getting_started/set_up_nci_account).

## Start an ARE session
<!-- Tab labels -->
<div class="tabLabels" label="are-apps" style="margin-bottom: 0.5rem;">
    <button id="vdi"><i>Virtual Desktop (VDI)</i></button>
    <button id="jupyterlab"><i>JupyterLab</i></button>
</div>
<div tabcontentfor="vdi" markdown>
To start an ARE VDI session go to the [ARE VDI Desktop](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new) page.
</div>
<div tabcontentfor="jupyterlab" markdown>
To start an ARE JupyterLab session go to the [ARE JupyterLab](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/jupyter/ncigadi/session_contexts/new) page.
</div>

### Session options
Launching an ARE session is similar to submitting an interactive [PBS job](https://opus.nci.org.au/display/Help/4.+PBS+Jobs) that enables you to connect to a _Gadi_ computing node.<br>
Hence, there are multiple [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained) and other options you can select:

- **<span id="walltime-option">Walltime (hours)</span>**<br>
    Number of hours your VDI session will run for (unless manually ended earlier).<br>
    The maximum number of hours an ARE session can run for depends on the selected Queue. For more information, check [Gadi Queue Limits](https://opus.nci.org.au/display/Help/Queue+Limits).

    !!! warning
        Once the session ends any operation still in progress on the session's computing node(s) will be immediately terminated.

- **Queue**<br>
    Gadi queue that your session will be scheduled in. For more information check [Gadi Queue Structure](https://opus.nci.org.au/display/Help/Queue+Structure).

- **Compute Size**<br>
    Amount of resources (CPUs, Memory, etc.) available to your session.<br>
    You can either choose a pre-configured option, or select a custom one (e.g., _cpus=6 mem=40G_).

- **Project**<br>
    The NCI project the ARE session will be charged to.<br>
    You must be a member of the specified project.
    
    !!! warning
        The specified project must have allocated _Service Units (SU)_.<br>
        For more information, check [how to join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

- **Storage**<br>
    `/g/data` (inserted as _gdata/&lt;project-ID&gt;_) `/scratch` (inserted as _scratch/&lt;project-ID&gt;_) data storage projects that will be available to the session.<br>
    In ARE, data storage locations need to be explicitly defined. This means that you need to insert any `/g/data` and `/scratch` project folders you want to execute data I/O operations from.<br>
    Multiple storage projects are separated by a plus (_+_) (e.g., _gdata/tm70+gdata/xp65+scratch/xp65_).
{: id="storage-option"}

    !!! warning
        Generally, you need to be a member of the specified projects to access their storage data.<br>
        If you try to access data from a project folder not included in the session's storage, you will get an error similar to the following:<br>
        `<cmd>: cannot access '</path/to/file>': No such file or directory`

- **Software**<br>
    Software licenses that are requested for your ARE session. Leave blank if no license needed.<br>
    Multiple licenses are separated by a colon (_:_).

### Advanced options
<div tabcontentfor="jupyterlab" markdown>

- **Extra arguments**<br>
    Additional arguments to pass on the JupyterLab command line (e.g., `--debug_`, `--log-level=INFO`)

- **<span id="module-directories-option">Module directories<span>**<br>
    Include module directories.<br>
    It is the eqivalent of `module use </path/to/module/directory>` run on the command line.
    
    !!! warning 
        You also need to include the project directory of each module directory in the [_Storage_](#storage-option) option.

- **Modules**<br>
    Include modules.<br>
    It is the equivalent to running `module load <module-name>` on the command line.
    
    !!! warning
        If the module is not inside _Gadi_'s default module directory `/apps/Modules/modulefiles`, you need to include the module directory in the [_Module directories_](#module-directories-option) option.

- **<span id="venv-base-option">Python or Conda virtual environment base</span>**<br>
    Path to a Python or conda base environment to be activated for the JupyterLab session.<br>
    It is the equivalent to running `source <path/to/environment/bin/activate>` on the command line.
            
    !!! warning 
        You also need to include the project directory of the virtual environment in the [_Storage_](#storage-option) option.

- **Conda environment**<br>
    Name of a specific conda environment to be activated for the JupyterLab session.<br>
    It is the equivalent to running `conda activate <environment-name>` on the command line.
            
    !!! warning
        You need to include the path to the conda base environment in the [_Python or Conda virtual environment base_](#venv-base-option) option.
</div>

- **Environment variables** <br>
    Environment variables passed to the session. Identical to the [`-v` PBS directive](https://opus.nci.org.au/display/Help/PBS+Directives+Explained#PBSDirectivesExplained--v%3Cvar=10,%22var2='A,B'%22%3E).<br>
    Multiple environment variables are separated by a comma (_,_).

- **Jobfs size**<br>
    The maximum amount of local disk available to the session.<br>
    If missing, it is automatically set to 100MB.

- **PBS flags**<br>
    Extra [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained) to be used for the ARE job submission.

- **Pre-script**<br>
    A script or executable that will be run just before starting the ARE session.

### Launch the session

1. Click on the <i>Launch</i> button to launch the session. You will be prompted to your Interactive Sessions page and you will see your last requested session at the top.

2. <span tabcontentfor="vdi" markdown> 
    Wait until your session starts and then click on the <i>Launch VDI Desktop</i> button to open a new tab with the VDI interface.<br>
    Inside the VDI interface, you can open the terminal by clicking on the black terminal icon at the top of the window.
    <img src="/assets/launch_are_vdi_desktop.gif" alt="Launch ARE VDI Desktop" class="example-img" loading="lazy"/>
    </span>
    
    <span tabcontentfor="jupyterlab">
    Wait until your session starts and then click on the <i>Open JupyterLab</i> button to open a new tab with the JupyterLab interface.<br>
    Inside the JupyterLab interface, you can open a new notebook by clicking on the Python3 Notebook button in the Launcher panel (to open a new Laucher panel, click on the plus button <img src="/assets/jupyterlab_plus_button.png" alt="Plus button" style="height:1em"/> next to your current tab).
    <img src="/assets/launch_are_jupyterlab.gif" alt="Launch ARE JupyterLab" class="example-img" loading="lazy"/>
    </span>

## Delete an ARE session
You can delete a session before its automatic expiration (based on the specified [Walltime](#walltime-option) by clicking on the session's ![Session Delete button](/assets/session_delete_button.png){: style="height:1em"} button in the [Interactive Sessions](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sessions) page.

<custom-references>
- [https://opus.nci.org.au/display/Help/ARE+User+Guide](https://opus.nci.org.au/display/Help/ARE+User+Guide)
- [https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/desktop_vnc/ncigadi/session_contexts/new)
- [https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/jupyter/ncigadi/session_contexts/new](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/jupyter/ncigadi/session_contexts/new)
</custom-references>

<!-- Add specific style to fix big gap between ul elements divided because of the tab content-->
<style>
    ul:has(#venv-base-option) {
        margin-bottom: 0;
    }
    div[tabcontentfor="jupyterlab"] + ul,
    div[tabcontentfor="jupyterlab"] + ul > li:first-child > p:first-child {
        margin-top: 0;
    }
</style>
