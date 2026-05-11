#  Data and Model Evaluation 

This section links climate datasets, shared frameworks, diagnostics, and visualisation tools to create workflows for model evaluation. 
Standardisation through the workflows will support reproducible, transparent, scalable, and community-driven evaluation.
There are catalogues and tools supported on _Gadi_ for the ACCESS community with training resources available.

If you are new to using the Gadi supercomputer, visit the [Set Up your NCI Account](/getting_started/set_up_nci_account) section 
for instructions on how to get an account, log in, and get set up to access climate data on Gadi. 
ACCESS-NRI supports and maintains the [conda/analysis3 _Python_ environment](/getting_started/environments) 
which supports most of the evaluation and data tools described.

## Connecting Data, Evaluation and Diagnostics with Frameworks and Recipes
Climate data is at the start of any workflow. Sources include published CMIP(Coupled Model Intercomparison Project), observations,
reanalysis products and climate simulations. They need to be found, preprocessed and standardised for evaluation.

Evaluation **frameworks** provide the structure for running diagnostics, benchmarking simulations,
and comparing model performance across datasets. They are developed specifically for the climate community to leverage common data processing functions.
The determined structure allows for easier sharing and scalability of common diagnostics.

**Recipes** in this context are a set of instructions that define reusable workflows into a single reproducible analysis pipeline.
Recipes are often shared in the community for visibility and reuse, helping accelerate collaborative climate science. 
An individual recipe may take advantage of existing frameworks (e.g ESMValTool, ILAMB)
or may read data directly from file path and just use major _python_ libraries such as _xarray_ and _numpy_.

<div class="card-container">
    <a href="/model_evaluation/data" class="horizontal-card">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/model_evaluation_variables.png" alt="Data" class="img-contain white-background with-padding"></img>
        </div>
        <div class="card-text-container">
            <span class="bold" >Data</span>
            <span>
                Information on data basics, CMORisation and standardisation and finding data
            </span>
        </div>
    </a>
    <a href="/model_evaluation/evaluation_on_gadi" class="horizontal-card">
        <div class="card-image-container">
            <img src="../assets/model_evaluation/live_diagnostics/tutorial_image_4.png" alt="Model Evaluation" class="img-cover" style="object-position: left;"></img>
        </div>
        <div class="card-text-container">
        <span class="bold" >Model Evaluation</span>
            <span>
                ACCESS model evaluation including frameworks on <i>Gadi</i>, tools and diagnostic recipes.
            </span>
        </div>
    </a>
</div>

### Training Materials

The pages for each tool should have links to further documentation and some tutorials.
Also see the [Tutorials page](/tutorials/), which includes material from previous workshops and events grouped by model/tool.

### Support and new requests

For infrastructure support and requesting new diagnostics and features
reach out on the [ACCESS-HIVE Forum](https://forum.access-hive.org.au/), create a topic and tag with `#help`.
See [User support](/about/user_support) for more details.


<div class="card-container">
    <a href="/model_evaluation/community_med" class="vertical-card aspect-ratio1to1">
         <div class="card-image-container">
             <img class="img-cover" src="/assets/external-links.jpg" alt="External Resources and Links">
         </div>
         <div class="card-text-container">
         <span class="bold" >Additional Resources</span>
            <span>
                Collations of resources from the global climate community that could be useful for the ACCESS community.
            </span>
        </div>
     </a>
</div>