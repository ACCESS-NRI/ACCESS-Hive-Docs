{% set model = "ACCESS-rAM3" %}
{% set ras_id = "u-bu503" %}
{% set rns_id = "u-by395" %}
{% set branch = "nci_access_ram3" %}
{% set mosrs_config_ras = "https://code.metoffice.gov.uk/trac/roses-u/browser/d/g/7/6/7/trunk" %}
{% set mosrs_config_rns = "https://code.metoffice.gov.uk/trac/roses-u/browser/d/g/7/6/8/trunk" %}
{% set model_configurations = "/models/access-ram" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-ram3-release-information/4308" %}

## Troubleshooting
The following section outlines known issues along with possible workarounds to address them where applicable.

### NaNs in error term in BiCGstab

In some cases the choice of location and time produces initial conditions of the low resolution nest that leads to an unstable model state, causing a crash with an error similar to the following:

```
????????????????????????????????????????????????????????????????????????????????
???!!!???!!!???!!!???!!!???!!!       ERROR        ???!!!???!!!???!!!???!!!???!!!
?  Error code: 1
?  Error from routine: EG_BICGSTAB
?  Error message: NaNs in error term in BiCGstab after      1 iterations
?        This is a common point for the model to fail if it
?        has ingested or developed NaNs or infinities
?        elsewhere in the code.
?        See the following URL for more information:
?        https://code.metoffice.gov.uk/trac/um/wiki/KnownUMFailurePoints
?  Error from processor: 216
?  Error number: 22
????????????????????????????????????????????????????????????????????????????????
```

If that occurs, two possible work-arounds are:

- Reduce the GAL9 timestep from `300` to `150` seconds.<br>
  To achieve this, set `rg01_rs01_m01_dt` to `150` in the `rose-suite.conf` file.<br>
  This does not have a large impact on cycle time, and can usually be reverted in subsequent cycles when the simulation is running without error.
- Change the `INITIAL_CYCLE_POINT` in the `rose-suite.conf` file to an earlier day (usually 1 day should be enough).
  This can sometimes solve the issue, though at the expense of running the model simulation for longer than was initially desired.

More on this error in the [related forum post](https://forum.access-hive.org.au/t/issues-with-access-ram-ocean-domains-u-dg767-and-nans-in-bicgstab-u-dg768/4418).

### No-land and isolated land experiments
Configuring an experiment that contains only ocean points for the inner nests, with no land at all, is not supported by the UM.
In some cases, even when small groups of isolated land points are present there is not data available for those land points in the forcing datasets.<br>
This can cause issues in the RAS suite similar to the following:

```
Calculating bi-linear interpolation coeffs
Finding coastal points
Setting coastal values
 WARNING - No source data is available in target domain
UNRESOLVED GRID POINTS IN SOIL DATASET
 Number of points unresolved is                      9
 POINT      78674 LAT   -29.0100 LONG   167.9304
 POINT      78675 LAT   -29.0100 LONG   167.9502
 POINT      79124 LAT   -29.0298 LONG   167.9304
 POINT      79125 LAT   -29.0298 LONG   167.9502
 POINT      79126 LAT   -29.0298 LONG   167.9700
 POINT      79127 LAT   -29.0298 LONG   167.9898
 POINT      79574 LAT   -29.0496 LONG   167.9304
 POINT      79575 LAT   -29.0496 LONG   167.9502
 POINT      79576 LAT   -29.0496 LONG   167.9700
 Search radius                      1
 NO DATA FROM WHICH TO SET UNRESOLVED POINTS
 ***ERROR: No source data available in target domain
```

The only work-around in this case is to choose a different domain such that the inner nest contains more land points.

More on this error in the [related forum post](https://forum.access-hive.org.au/t/issues-with-access-ram-ocean-domains-u-dg767-and-nans-in-bicgstab-u-dg768/4418).

### Stuck cylc tasks
Testing of the RAS revealed an intermittent problem: sometimes tasks in `{{ ras_id }}` remain stuck in a _submitted_ state within the _Cylc_ GUI. 
Using `qstat` revealed that they had failed, but this was not correctly reflected in the GUI.

To test this error, run:

```
cat ~/cylc-run/{{ ras_id }}/log/job/1/<task_name>/01/job.err
```

and you should get an output similar to the following:

```
/local/spool/pbs/mom_priv/jobs/140074859.gadi-pbs.SC: line 104: /g/data/hr22/apps/cylc7/cylc_7.9.9/lib/cylc/job.sh: No such file or directory
/local/spool/pbs/mom_priv/jobs/140074859.gadi-pbs.SC: line 105: cylc__job__main: command not found
```

The workaround for this is to use the _Cylc_ GUI to:

1. Set the task state to failed.
2. Set the task state to waiting.
3. Check that the task then automatically goes into submitted, then running, then succeeded.

This is an intermittent, and often unreproducible error, hence the task should succeed when resubmitted. This issue has been reported to NCI.
