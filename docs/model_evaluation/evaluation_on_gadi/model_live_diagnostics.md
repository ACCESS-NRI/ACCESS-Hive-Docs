# Model Live Diagnostics

## What is Model Live Diagnostics?

<i>Model Live Diagnostics</i> is a simple, accessible and easy-to-use Jupyter notebook-based framework for the ACCESS modelling community to monitor, visualise and evaluate the behaviour of models in real time (<i>live</i>) while they run on <i>Gadi</i>.

In addition to monitoring a live model, the package also provides the functionality to load, visualise and compare legacy ACCESS model data with the live model.

Below, we show an example of the Model Live Diagnostics Tool. For more information and tutorials, please visit <a href="https://med-live-diagnostics.readthedocs.io/en/latest/index.html" target="_blank">Model Diagnostics Documentation</a>.
<!-- <div class="card-container">
    <a href="https://med-live-diagnostics.readthedocs.io/en/latest/index.html" class="vertical-card aspect-ratio2to1" target="_blank">
        <div class="card-image-container">
            <img src="../../../assets/ACCESS_NRI_full_logo.png" alt="ACCESS-NRI Model Diagnostics Documentation" class="img-contain white-background with-padding"></img>
        </div>
        <div class="card-text-container bold ">Model Diagnostics Documentation</div>
    </a>
</div> -->

## Example: Monitoring total seawater mass of an ACCESS-CM2 run

This example provides a brief demonstration of how the Model Live Diagnostics tool can be use to monitor the progress of an [ACCESS Coupled Model 2 (ACCESS-CM2)](/models/run_a_model/run_access-cm2) run.

To start a session that automatically checks for new model output within a given period of 20 minutes: 

```
import med_diagnostics
session = med_diagnostics.session.CreateModelDiagnosticsSession(model_type='CM2', model_path='path/to/your/live/model/data/output', period=20)
```

<div class="note">
         For more details on paths and packages refer to the <a href="https://med-live-diagnostics.readthedocs.io/en/latest/index.html" target="_blank">ACCESS-NRI Model Diagnostics documentation</a>.
</div>

When the session starts, you will see the following session summary:

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/tutorial_image_1.png" alt="Output of the Model Live Diagnostics after a session has been started and a new catalogue is being built." width="75%"/>
</div>

<div class="note">
         The blue status message box appears while the new intake catalogue is being built from the live model data. Depending on the size of the model data, this can take several minutes.
</div>

Once the live model data catalogue has been successfully built, the blue status message will update.
<br>
The orange status message will report the time and date of the last live model catalogue build, as shown below:
<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/tutorial_image_2.png" alt="Output of the Model Live Diagnostics after the catalogue has been built." width="75%"/>
</div>

All available datasets for the selected model will be listed in the dropdown menu. 
<br>
Select the dataset that you want to monitor (e.g., `ocean_scalar.1mon`) and click `Load dataset`.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/tutorial_image_3.png" alt="Output of the Model Live Diagnostics with a dropdown menu of available datasets." width="75%"/>
</div>

Once loaded, a plot will display the first data variable selected from the list. 
<br>
Use the dropdown menu to select and plot any available model variables listed.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/tutorial_image_4.png" alt="Plot of total liquid seawater mass over time of the ‘live’ ACCES CM2 run." width="75%"/>
</div>

The plot above shows the users own 'live' data so doesn't have a name. It is also possible to load and compare <i>legacy data</i>, such as other previous ACCESS-CM2 model runs (<i>by578</i> and <i>by578a</i> etc.)

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/tutorial_image_7.png" alt="Plot of total liquid seawater mass over time of the ‘live’ ACCES CM2 run when compared to legacy model data." width="75%"/>
</div>
