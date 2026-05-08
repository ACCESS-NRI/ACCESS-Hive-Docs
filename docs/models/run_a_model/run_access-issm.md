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
    - Log in with your NCI Username and password. You'll be presented with a new JupyterLab session configuration, similar to the one shown below.

    ![New ARE JupyterLab Session](../../assets/run_access-issm/are_dashboard.png)

- Step 2:
    - Configure the ARE JupyterLab session with the required fields. The following entries are recommended for this simple tutorial and can be cusomtised as necessary for larger model simulations.

        - Walltime (hours): `1`
        - Queue: `normalbw`
        - Compute Size: `small`
        - Project: `<USER SELECTED PROJECT>`
        - Storage:  `gdata/xp65+gdata/vk83`

    !!! warning
        Note that the `Project` field will vary depending on your chosen project with allocated Service Units. 

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
Since [pyISSM](https://github.com/ACCESS-NRI/pyISSM) is actively being developed, we recommend installing the latest development version directly from Github.

!!! warning
    These instructions install pyISSM into your `$HOME` directory on NCI _Gadi_. You may adjust the installation location if you prefer.

To install pyISSM, simply run the following in a new terminal (accessed from the JupyterLab Launcher panel):
```bash
cd ~
git clone https://github.com/ACCESS-NRI/pyISSM.git
cd pyISSM
pip install .
```

The installation may take a few minutes. Once the installation completes successfully, you will see `Successfully installed pyissm-...`.

### Run the "Square Ice Shelf" Tutorial
You're now ready to get started with pyISSM and execute your first ISSM model using ACCESS-ISSM! You can run this directly using the `~/pyISSM/tutorials/ex1_SquuareIceShelf.ipynb` file (using the file explorer of your ARE JupyterLab Session to navigate to the file), or by copying the code blocks below into a new Jupyter notebook. The below code blocks are taken directly from the tutorial notebook.

!!! info
    Code blocks below are formatted such that the output generated by the code block is indented, as follows:
    ```python
    Code here
    ```
    > Output here


#### Import required Python modules
Import pyISSM and other required Python modules as follows:

```python
import os
import pyissm
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
```

#### Configure your modelling environment
By default, the Square Ice Shelf tutorial is designed to be executed on NCI _Gadi_. To ensure your modelling environment is configured correctly, execute the following cell:

```python
## Set required paths
tutorial_dir = str(Path.home() / 'pyISSM' / 'tutorials')
asset_dir = tutorial_dir + '/assets'
execution_dir = tutorial_dir + '/models'

# Check that execution directory exists. If not, create it
if not os.path.isdir(execution_dir):
    os.mkdir(execution_dir)

# Print the paths for visibility
print(f"The following `tutorial_dir` is set: {tutorial_dir}")
print(f"The following `asset_dir` is set: {asset_dir}")
print(f"The following `execution_dir` is set: {execution_dir}")
```

If pyISSM was installed in your `$HOME` directory (as described above), you should see an output like this:

> The following `tutorial_dir` is set: ~/home/<CODE>/<USER>/pyISSM/tutorials
> The following `asset_dir` is set: /home/<CODE>/<USER>/pyISSM/tutorials/assets
> The following `execution_dir` is set: /home/<CODE>/<USER>/pyISSM/tutorials/models


where `<CODE>` is your NCI _Gadi_ group code and `<USER>` is your NCI username.

#### Initialise an empty model
To begin building an ISSM model, we first initialise an empty model. For more information about the `md` object, refer to the [Introduction to pyISSM tutorial](https://github.com/ACCESS-NRI/pyISSM/blob/main/tutorials/1_pyISSM_intro.ipynb).

```python
# Create an empty model
md = pyissm.model.Model()

# Inspect the empty model
md
```

Inspecting the empty ISSM model object (`md`) will provide an overview of all available model fields

> ISSM Model Class                         
>                                             
>               mesh:  mesh properties         
>               mask:  defines grounded and floating elements 
>           geometry:  surface elevation, bedrock topography, ice thickness, ... 
>          constants:  physical constants      
>                smb:  surface mass balance    
>      basalforcings:  bed forcings            
>          materials:  material properties     
>             damage:  damage propagation laws 
>           friction:  basal friction / drag properties 
>       flowequation:  flow equations          
>       timestepping:  timestepping for transient models 
>     initialization:  initial guess / state   
>              rifts:  rifts properties        
>         solidearth:  solidearth inputs and settings 
>                dsl:  dynamic sea level       
>              debug:  debugging tools (valgrind, gprof 
>            verbose:  verbosity level in solve 
>           settings:  settings properties     
>           toolkits:  PETSc options for each solution 
>            cluster:  cluster parameters (number of CPUs...) 
>   balancethickness:  parameters for balancethickness solution 
>      stressbalance:  parameters for stressbalance solution 
>      groundingline:  parameters for groundingline solution 
>          hydrology:  parameters for hydrology solution 
>      masstransport:  parameters for masstransport solution 
>            thermal:  parameters for thermal solution 
>        steadystate:  parameters for steadystate solution 
>          transient:  parameters for transient solution 
>           levelset:  parameters for moving boundaries (level-set method) 
>            calving:  parameters for calving  
>    frontalforcings:  parameters for frontalforcings 
>                esa:  parameters for elastic adjustment solution 
>           sampling:  parameters for stochastic sampler 
>               love:  parameters for love solution 
>           autodiff:  automatic differentiation parameters 
>          inversion:  parameters for inverse methods 
>                qmu:  Dakota properties       
>                amr:  adaptive mesh refinement properties 
>   outputdefinition:  output definition       
>            results:  model results           
>       radaroverlay:  radar image for plot overlay 
>      miscellaneous:  miscellaneous fields    
>  stochasticforcing:  stochasticity applied to model forcings 


#### Create a model mesh
The first step when building any ISSM model is to generate a model mesh. This contains the information onto which all model fields and parameters are stored. Here, we use an `*.exp` file to define the outline of our model domain and generate a triangular mesh with a resolution of 50 km.

```python
# Build a model mesh using the domain outline (SquareShelf_DomainOutline.exp) with a resolution of 50 km.
md = pyissm.model.mesh.triangle(md,
                                domain_name = asset_dir + '/Exp/SquareIceShelf_DomainOutline.exp',
                                resolution = 50000
                               )

# Inspect the created mesh
md.mesh
```

> 2D tria Mesh (horizontal):
>       Elements and vertices:
>          numberofelements       : 614             -- number of elements
>          numberofvertices       : 340             -- number of vertices
>          elements               : (614, 3)        -- vertex indices of the mesh elements
>          x                      : (340,)          -- vertices x coordinate [m]
>          y                      : (340,)          -- vertices y coordinate [m]
>          edges                  : N/A             -- edges of the 2d mesh (vertex1 vertex2 element1 element2)
>          numberofedges          : 0               -- number of edges of the 2d mesh
>
>       Properties:
>          vertexonboundary       : (340,)          -- vertices on the boundary of the domain flag list
>          segments               : (64, 3)         -- edges on domain boundary (vertex1 vertex2 element)
>          segmentmarkers         : (64,)           -- number associated to each segment
>          vertexconnectivity     : (340, 101)      -- list of elements connected to vertex_i
>          elementconnectivity    : (614, 3)        -- list of elements adjacent to element_i
>          average_vertex_conne...: 25              -- average number of vertices connected to one vertex
>
>       Extracted model:
>          extractedvertices      : N/A             -- vertices extracted from the model
>          extractedelements      : N/A             -- elements extracted from the model
>
>       Projection:
>          lat                    : N/A             -- vertices latitude [degrees]
>          long                   : N/A             -- vertices longitude [degrees]
>          epsg                   : 0               -- EPSG code (ex: 3413 for UPS Greenland, 3031 for UPS Antarctica)
>          scale_factor           : N/A             -- Projection correction for volume, area, etc. computation

We can visualise the mesh as follows:

```python
# Plot the mesh with customised options
fig, ax = pyissm.plot.plot_mesh2d(md,
                                  color = 'blue',
                                  linewidth = 0.5,
                                  show_nodes = True,
                                  node_kwargs = {'s': 20,
                                                 'color': 'red',
                                                 'alpha': 0.5})

# We can interact with the plot using standard matplotlib functions
ax.set_xlabel('X Coordinate (m)')
ax.set_ylabel('Y Coordinate (m)')
ax.set_title('Square Ice Shelf Mesh')
```

> ![Model mesh](../../assets/run_access-issm/model_mesh.png)

#### Model mask

## Get help

For further {{ model }} assistance, have a look at [general guidance](/about/user_support/#still-need-help) on how to request help from ACCESS-NRI. Specifically, consider creating a topic in the [{{ model }} category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/cryosphere). In the case of a configuration bug, please [raise a GitHub issue](https://github.com/ACCESS-NRI/access-issm/issues/new).