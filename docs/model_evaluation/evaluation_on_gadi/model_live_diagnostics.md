# Model Live Diagnostics

## What is Model Live Diagnostics?

_Model Live Diagnostics_ (MLD) is a tool for the ACCESS modelling community to monitor, visualise and evaluate ACCESS model runs on _Gadi_ while they run. 

It supports _ACCESS-CM2_, _ACCESS-CM3_, _ACCESS-OM2_, _ACCESS-OM3_, _ACCESS-ESM1.5_, _ACCESS-ESM1.6_ and _ACCESS-AM3_ output.

## What can MLD do?

A session opens an interactive interface in your notebook with four sections:

- **Load and plot user data**: plot any dataset from your own run as a line plot, heatmap or interactive heatmap, and refresh it as the run writes new output.
- **Load and plot reference models**: plot existing runs of the same model from the [ACCESS-NRI Intake Catalogue](/model_evaluation/data/finding/access_nri_intake).
- **Overlay user and reference models**: compare your run with as many reference runs as you like, and plot the difference between them.
- **Run analysis recipes**: run ready-made analyses on your run, or add your own.

![Heatmaps of a user run and several reference runs, compared in Model Live Diagnostics.](/assets/model_evaluation/live_diagnostics/mld_hivedocs_aligned.png){: style="width: 75%;" }

## Getting started

MLD is pre-installed in the [_conda/analysis3_](/getting_started/environments) environment, which requires membership of the [xp65](https://my.nci.org.au/mancini/project/xp65/join) project. In an [ARE JupyterLab session](https://are.nci.org.au/pun/sys/dashboard/batch_connect/sys/jupyter/ncigadi/session_contexts/new) using _conda/analysis3_, run:

```python
import med_diagnostics
session = med_diagnostics.session.CreateModelDiagnosticsSession()
```

Then enter the path to your model output, select its model type and click **Start Session**.

For a step-by-step walkthrough, and more information, see the [Model Live Diagnostics documentation](https://med-live-diagnostics.readthedocs.io/en/latest/).
