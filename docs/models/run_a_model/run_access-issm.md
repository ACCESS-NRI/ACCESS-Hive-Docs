{% set model = "ACCESS-ISSM" %}
{% set model_configurations = "/models/access-issm" %}
{% set release_notes = "https://github.com/ACCESS-NRI/ACCESS-ISSM/releases/tag/2025.11.0" %}

!!! release
    This is a Beta Release.
    Any model configuration and related source code mentioned in this page might change before the full release.
    Limited support is currently provided for this model. Its usage is only recommended for testing by experienced users and collaborators.

# Run {{ model }}

## About

ACCESS-ISSM is the Ice-sheet and Sea-level System Model (ISSM) maintained by ACCESS-NRI. Hosted on the [NCI _Gadi_ supercomputer](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview), ACCESS-ISSM makes centrally-managed ISSM executables available to the Australian ice sheet modelling community. ACCESS-ISSM is being used to integrate ISSM into the ACCESS climate modelling framework, with development of [ACCESS-AIS3](https://github.com/ACCESS-NRI/ACCESS-AIS3), a whole-Antarctic ISSM configuration ongoing.

While ACCESS-ISSM provides centrally-managed model executables, [pyISSM](https://github.com/ACCESS-NRI/pyISSM) is used to develop model configurations and for model execution on [NCI _Gadi_](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview). [pyISSM](https://github.com/ACCESS-NRI/pyISSM) is the Python API for ISSM, developed and managed by ACCESS-NRI. [pyISSM](https://github.com/ACCESS-NRI/pyISSM) contains various [Tutorials](https://pyissm.readthedocs.io/latest/tutorials.html) for using pyISSM.

Here, we provide guidance on getting started with pyISSM and ACCESS-ISSM on [NCI _Gadi_](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview). We provide step-by-step instructions on how to initialise an appropriate [Australian Research Environment (ARE)](https://docs.access-hive.org.au/getting_started/are/#jupyterlab) session on [NCI _Gadi_](https://opus.nci.org.au/spaces/Help/pages/90308778/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview), install pyISSM, and execute the simple ["Square Ice Shelf" pyISSM tutorial](https://pyissm.readthedocs.io/latest/tutorials/ex1_SquareIceShelf.html)

## Prerequisites

!!! warning
    To run {{ model }}, you need to be a member of a project with allocated _Service Units (SU)_. For more information, check [how to join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

- **NCI Account**<br>
    Before running {{ model }}, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [vk83](https://my.nci.org.au/mancini/project/vk83/join) - required to access ACCESS-ISSM executables
    - [xp65](https://my.nci.org.au/mancini/project/xp65/join) - required to access the ACCESS-NRI managed Conda environment containing all pyISSM dependencies

  For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

## Getting started

### Setting up your ARE JupyterLab Session
All pyISSM tutorials are presented as Jupyter Notebooks and can be executed easily using an [ARE JupyterLab session](https://docs.access-hive.org.au/getting_started/are/#jupyterlab). To start an appropriate ARE JupyterLab session go to the [ARE JupyterLab](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/jupyter/ncigadi/session_contexts/new) page and follow these steps:

- Step 1:
    Log in with your NCI Username and password. You'll be presented with a new JupyterLab session configuration, similar to the one shown below.

    ![New ARE JupyterLab Session](../../assets/run_access-issm/are_dashboard.png)

- Step 2:
    - Configure the ARE JupyterLab session with the required fields. The following entries are recommended for this simple tutorial and can be cusomtised as necessary for larger model simulations.
    
    !!! warning
        Note that the `Project` and `Storage` fields will vary depending on your chosen project with allocated Service Units. 

        - Walltime (hours): `1`
        - Queue: `normalbw`
        - Compute Size: `small`
        - Project: `<USER SELECTED PROJECT>`
        - Storage:  `gdata/xp65+gdata/vk83+<USER SELECTED PROJECT STORAGE>`

    - Click on "Show advanced settings" and enter the following field entries:
        - Module directories: `/g/data/vk83/modules /g/data/xp65/public/modules`
        - Modules: `conda/analysis3 access-issm/2025.11.0`

- Step 3:
    - Click on the _Launch_ button to launch the session. You will be prompted to your Interactive Sessions page and you will see your last requested session at the top.
    - Wait until your session starts and then click on the _Open JupyterLab_ button to open a new tab with the JupyterLab interface. Inside the JupyterLab interface, you can open a new notebook by clicking on the Python3 Notebook button in the Launcher panel (to open a new Laucher panel, click on the plus button next to your current tab).


### Setup environment requirements

Interacting with {{ model }} requires the `$ISSM_DIR` environment variable be set to use an appropriate executable. This is handled automatically when loading the {{ model }} module on _Gadi_. To set these variables in preparation for running an ISSM model, run:

```bash
module use /g/data/vk83/modules
module load access-issm/2025.11.0
```

In addition, to prevent the need for all users to maintain individual Python environments, we can leverage the `conda/analysis3` environment maintained by ACCESS-NRI. To load the Python environment, run:

```bash
module use /g/data/xp65/public/modules
module load conda/analysis3
```

### Installing pyISSM
Since [pyISSM](https://github.com/ACCESS-NRI/pyISSM) is actively being developed, it's good practice to install the latest development version directly from Github. To avoid inode limits on _Gadi_, we recommend installing pyISSM in a `gdata` location. To do so, ensure you have access to your preferred storage location and follow the below steps:

!!! warning
    In this example, we will use the sample project `tm70` and sample username `user`; however, you should replace all instances of `tm70` with your preferred `gdata` storage location and all instances of `user` with yout NCI username.

```
cd /g/data/tm70/user
git clone https://github.com/ACCESS-NRI/pyISSM.git
cd pyISSM
pip install .
```

The installation may take a few minutes. Once the installation completes successfully, you will see `Successfully installed pyissm-...`.

## Get help

For further {{ model }} assistance, have a look at [general guidance](/about/user_support/#still-need-help) on how to request help from ACCESS-NRI. Specifically, consider creating a topic in the [{{ model }} category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/cryosphere). In the case of a configuration bug, please [raise a GitHub issue](https://github.com/ACCESS-NRI/access-issm/issues/new).