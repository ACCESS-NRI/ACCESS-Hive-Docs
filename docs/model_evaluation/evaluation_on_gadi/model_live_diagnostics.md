# Model Live Diagnostics

## What is Model Live Diagnostics?

_Model Live Diagnostics_ is an easily-accessible Jupyter-notebook-based framework for the ACCESS modelling community to monitor, visualise and evaluate the behaviour of models in real time (_live_) while they run on _Gadi_.

In addition to monitoring a live model, the package also provides the functionality to load, visualise and compare legacy ACCESS model data with the live model.

???+ warning "Support Level: Supported on _Gadi_, not in active development"
    Model Live Diagnostics Tool is not in active development so support may be slow but can be used on _Gadi_.

Below, we show an example of the Model Live Diagnostics Tool. For more information and tutorials, please visit <a href="https://med-live-diagnostics.readthedocs.io/en/latest/index.html" target="_blank">Model Diagnostics Documentation</a>.


## Example: Monitoring total seawater mass of an ACCESS-OM2 run

This example provides a brief demonstration of how the Model Live Diagnostics tool can be use to monitor the progress of an [ACCESS ocean-sea ice Model 2 (ACCESS-OM2)](/models/run_a_model/run_access-om2) run.

To start a session:

```
import med_diagnostics
session = med_diagnostics.session.CreateModelDiagnosticsSession(model_type='OM2', model_path='path/to/your/live/model/data/output', period=20)
```

<div class="note">
         For more details on paths and packages refer to the <a href="https://med-live-diagnostics.readthedocs.io/en/latest/index.html" target="_blank">ACCESS-NRI Model Diagnostics documentation</a>.
</div>

When the session starts, you will see the following session summary:

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_1.png" alt="Output of the Model Live Diagnostics after a session has been started and a new catalogue is being built." width="75%"/>
</div>

<div class="note">
         The blue status message box appears while the new intake catalogue is being built from the live model data. Depending on the size of the model data, this can take several minutes.
</div>

Once the live model data catalogue has been successfully built, the blue status message will update.
<br>
The orange status message will report the time and date of the last live model catalogue build, as shown below:
<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_2.png" alt="Output of the Model Live Diagnostics after the catalogue has been built." width="75%"/>
</div>

All available datasets for the selected model will be listed in the dropdown menu. 
<br>
Select the dataset that you want to monitor and click `Load dataset`.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_3.png" alt="Output of the Model Live Diagnostics with a dropdown menu of available datasets." width="75%"/>
</div>

Once the dataset loads, the plot selection interface will adapt based on your choices. First, select a variable and a plot type. The interface will then prompt you to assign the required axes for your specific plot. If your dataset contains higher dimensions, a slider will appear, allowing you to slice the data at a specific value. Once your parameters are set, click Confirm Slices & Plot.


<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_6.png" alt="Output of the Model Live Diagnostics plot selection UI." width="75%"/>
</div>

A plot will be generated with the selected parameters.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_7.png" alt="Animation of nitrate concentration over time of the ‘live’ ACCESS-OM2 run." width="75%"/>
</div>

The plot above shows the user's own _live_ data. It is also possible to load and plot _legacy data_, such as outputs from previous ACCESS-OM2 model runs (e.g., *1deg_jra55_iaf_omip2_cycle1*).
<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_10.png" alt="Output of the Model Live Diagnostics reference plot selection UI." width="75%"/>
</div>
The plot selections above generate the following plot from the loaded reference model:

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_11.png" alt="Plot of oxygen concentration over time of the legacy model data." width="75%"/>
</div>

You can also load multiple reference datasets to compare against your live data. These can be plotted side-by-side or overlaid, allowing you to perform simple analyses, such as calculating the difference between datasets.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_12.png" alt="Output of the Model Live Diagnostics overlay reference model selection UI." width="75%"/>
</div>

Use the **Add reference model** button shown above to load as many reference models as you need. Once they are loaded, use the standard plot interface to generate your visualisations.

<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_14.png" alt="Heatmaps of nitrate concentration from the live user dataset and various reference models." width="75%"/>
</div>
<div style="text-align: center;">
    <img src="../../../assets/model_evaluation/live_diagnostics/2026tutorial_image_15.png" alt="Heatmaps showing the difference in nitrate concentration from the live user dataset and various reference models." width="75%"/>
</div>