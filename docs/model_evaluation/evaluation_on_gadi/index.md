# Model Evaluation on Gadi

Model evaluation is about measuring how fit for purpose a particular model is. Model evaluation in climate science is the process of assessing the performance and reliability of computational models that simulate the Earth's climate system. It involves comparing model predictions to observed data to determine the model's accuracy and usefulness. In doing so, we can understand how well a model represents real-world climate processes and make predictions about future climate trends. Such rigorous model evaluation allows scientists to identify model strengths, weaknesses and uncertainties, as well as refine models to enhance their predictive capabilities. 

## Data workflows
FAIR (Findable, Accessible, Interoperable and Reusable) data is required for model evaluation. 
Some of these evaluation workflows use data tools and catalogues outlined in the [ACCESS data](/model_evaluation/data) section.
[ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/) can also be integrated with these evaluation frameworks on _Gadi_.
[Observations](/model_evaluation/data/observations) have been collated for model evaluation so that they can be ingested directly
by the frameworks on _Gadi_.

## Use on Gadi
Model evaluation is tipically carried out using _Python_. Therefore, scientists need suitable _Python_ environments for their workflows, which need to be managed and maintained with the required dependencies for open source and developing software.
ACCESS-NRI supports the `conda/analysis3` environment in the `xp65` NCI project which includes commonly used _Python_ libraries and have these evaluation frameworks already installed.

<div class="card-container">
    <a href="/getting_started/environments" class="horizontal-card">
        <div class="card-image-container">
            <img src="/assets/python_logo.png" alt="Python environment" class="img-contain white-background" ></img>
        </div>
        <div class="card-text-container bold">conda/analysis3 Environment</div>
    </a>
</div>

## Evaluation Frameworks

ACCESS-NRI currently provides support for the following model evaluation frameworks on <i>Gadi</i>:

<div class="card-container">
    <a href="/model_evaluation/evaluation_on_gadi/esmvaltool_workflow" class="horizontal-card">
        <div class="card-image-container">
            <img src="../../assets/model_evaluation/logo_esmvaltool.png" alt="ESMValTool" class="img-cover"></img>
        </div>
        <div class="card-text-container">
            <!-- <span class="bold" >ESMValTool</span> -->
            <span>
                Earth System Model eValuation Tool framework supported on Gadi via analysis3
            </span>
        </div>
    </a>
    <a href="/model_evaluation/evaluation_on_gadi/ilamb_workflow" class="horizontal-card">
        <div class="card-image-container">
            <img src="../../assets/model_evaluation/logo_ilamb.png" alt="ILAMB" class="img-cover"></img>
        </div>
        <div class="card-text-container">
            <!-- <span class="bold" >ILAMB</span> -->
            <span>
                International Land Model Benchmarking framework supported on Gadi via analysis3
            </span>
        </div>
    </a>
</div>

## Evaluation recipes
These recipes provide workflows to reproduce diagnostics calculations and analysis visualisations of model outputs. 
This allows scientists to construct their own evaluation workflows by building upon existing community workflows.

They can use common _python_ libraries, more specifc packages, leverage APIs to work with evaluation frameworks or a combination.
Diagnostic calculations can be ported between these methods depending on a user's familiarity with them. 
An advantage of using standard frameworks includes the scalability for bulk running on multiple different datasets. 
This is a principle for the development of the [Rapid Evaluation Framework(REF)](https://dashboard.climate-ref.org/) for CMIP7.

<div class="card-container">
    <a href="/model_evaluation/evaluation_on_gadi/recipes" class="horizontal-card">
        <div class="card-image-container">
            <img class="white-background" src="/assets/model_evaluation/esmvaltool/fig-9-8.png" alt="Near surface temperature">
        </div>
        <div class="card-text-container bold">
            <span class="bold">Evaluation recipes</span>
            <span>
                A collection of shared repositories with community recipes.
            </span>
        </div>
    </a>
</div>

### Contributing to recipes and diagnostics
All evaluation recipes on community papers are open for contribution. To contribute to a specific evaluation framework or recipe, follow the contribution guidelines in its GitHub repository.<br>
General steps include:

1. Opening an issue in the relevant repository to discuss your idea
2. Submitting a Pull Request to add your recipe, documentation, and links 

### Support
To get further support on Model Evaluation on _Gadi_, refer to [User support](/about/user_support/) and reach out on
[ACCESS-Hive Forum](https://forum.access-hive.org.au/)


## More Evaluation Tools

<div class="card-container">
    <a href="/model_evaluation/evaluation_on_gadi/access_vis" class="horizontal-card">
        <div class="card-image-container">
            <img src="/assets/model_evaluation/clouds.png" alt="CloudsGlobe" class="img-cover"></img>
        </div>
        <div class="card-text-container">
            <span class="bold">ACCESS-Vis</span>
            <span>
                A package for advanced visualisations, including interactive 3D climate data visualisations
            </span>
        </div>
    </a>
    <a href="/model_evaluation/evaluation_on_gadi/model_live_diagnostics" class="horizontal-card">
        <div class="card-image-container">
            <img src="../../assets/model_evaluation/live_diagnostics/tutorial_image_4.png" alt="Model Live Diagnostics" class="img-contain white-background"></img>
        </div>
        <div class="card-text-container">
            <span class="bold">Model Live Diagnostics</span>
            <span>
                A framework to monitor, visualise and evaluate the behaviour of models in real time.
            </span>
        </div>
    </a>
</div>

