{% set model = "ACCESS-rAM3" %}
{% set ras_id = "u-bu503" %}
{% set oas_id = "u-dk517" %}
{% set rns_id = "u-by395" %}
{% set branch_ras = "nci_access_ram3" %}
{% set branch_rns = "nci_access_ram3" %}
{% set mosrs_config_ras = "https://code.metoffice.gov.uk/trac/roses-u/browser/b/u/5/0/3/ ~ branch" %}
{% set mosrs_config_rns = "https://code.metoffice.gov.uk/trac/roses-u/browser/b/y/3/9/5/ ~ branch" %}
{% set access_models = "/models/access_models/access-ram" %}
{% set release_notes = "https://forum.access-hive.org.au/t/access-ram3-release-information/4308/6" %}
{% set config_docs = "https://access-ram3-configs.access-hive.org.au" %}
[PBS job]: https://opus.nci.org.au/display/Help/4.+PBS+Jobs
[model components]: /models/access_models/access-ram/#model-components
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[default project]: /getting_started/set_up_nci_account#change-default-project-on-gadi

<div class="text-card-group" markdown>

[![Met Office](/assets/met_office_logo.png){: class="icon-before-text  white-background"} RAS configuration]({{mosrs_config_ras}}){: class="text-card" style=""}
[![Met Office](/assets/met_office_logo.png){: class="icon-before-text  white-background"} RNS configuration]({{mosrs_config_rns}}){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} {{ model }} configs docs]({{config_docs}}){: class="text-card"}
[:notepad_spiral:{: class="twemoji icon-before-text"} Release notes]({{release_notes}}){: class="text-card"}
</div>

# Run {{ model }}

## About

{{ model }} is an ACCESS-NRI-supported configuration of the [UK Met Office (UKMO)](https://www.metoffice.gov.uk/) Regional Nesting Suite for high-resolution regional atmosphere modelling. A description of the model and its components is available in the [{{ model }} overview]({{ access_models }}/#{{ model }}).

{{ model }} comprises multiple [suites](/models/run_a_model/rose_cylc/#about): the [Regional Ancillary Suite (RAS)](#ras) and [OSTIA Ancillary Suite (OAS)](#oas) that generate ancillary files (i.e., input files), and the [Regional Nesting Suite (RNS)](#rns) which runs the regional forecast.

The instructions below outline how to run {{ model }} using ACCESS-NRI's supported configuration, specifically designed to run on the [National Computational Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are) supercomputer [_Gadi_][gadi]. The example experiment within this page focuses on a flood event in Lismore, NSW on 26 and 27 February 2022, using `BARRA` [land-surface initial conditions]({{ access_models }}/#land-surface-initial-conditions-source). For more details, see [Nesting configuration]({{ access_models }}/#nesting-configuration). 

!!! tip 
    It is recommended to run the following example first without changes. Once you are comfortable with running the model, you can modify parameters such as domain position, dates, initial-conditions source, or output variables as needed.

The {{ model }} suites are run using the Rose/Cylc workflow management tool. The [Run models using Rose/Cylc](/models/run_a_model/rose_cylc) page has instructions for how to set up and use Rose/Cylc, and the below steps link to the relevant sections.

If you are unsure whether {{ model }} is the right choice for your experiment, take a look at the overview of [ACCESS Models](/models).

All {{model}} configurations are available on MOSRS via links at the [top of this page](/models/run_a_model/run_access-ram3/).

[{{ model }} release notes]({{release_notes}}) are available on the ACCESS-Hive Forum and are updated when new releases are made available.

## Prerequisites

!!! warning
    If you are new to Rose/Cylc, make sure you have read the guide on [running models using _Rose/Cylc_](/models/run_a_model/rose_cylc) before continuing on this page.
- **Rose/Cylc prerequisites**
  All [prerequisites for _Rose/Cylc_](/models/run_a_model/rose_cylc/#prerequisites).

- **Join NCI projects**<br>
    Join the following projects by requesting membership on their respective NCI project pages:

    - [access](https://my.nci.org.au/mancini/project/access/join)
    - [ki32](https://my.nci.org.au/mancini/project/ki32/join)
    - [ki32_mosrs](https://my.nci.org.au/mancini/project/ki32_mosrs/join)
    - [rt52](https://my.nci.org.au/mancini/project/rt52/join)
    - [ob53](https://my.nci.org.au/mancini/project/ob53/join)
    - [vk83](https://my.nci.org.au/mancini/project/vk83/join)
    - [cm45](https://my.nci.org.au/mancini/project/cm45/join)


    !!! tip
        To request membership for the _ki32_mosrs_ subproject, you need to:
        
        - already be member of the _ki32_ project
        {: style="list-style-type: disc"}
        - have a [MOSRS account](/models/run_a_model/rose_cylc/#mosrs-account)
        {: style="list-style-type: disc"}

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).
    

!!! warning
    The waiting time to complete some of the above prerequisites may be 2-3 weeks.

## Quick guide

This quick guide outlines the basic steps to run {{ model }} and is tailored to users who already have some experience running {{ model }}. For new users, please refer to the [Detailed guide](#detailed-guide) below that includes more explanations and extra setup information.

1. **Start a persistent session**
    ```
    persistent-sessions start -p <project> <name>
    ```
2. **Assign the persistent session to Cylc (once only)**
    ```
    cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
    ```
3. **Get _Rose/Cylc_ executables**
    ```
    module use /g/data/hr22/modulefiles
    module load cylc7
    ```
4. **Authenticate to MOSRS**
    ```
    mosrs-auth
    ```
5. **Get the OSTIA Ancillary Suite (OAS) (optional)**
    ```
    rosie checkout {{ oas_id }}
    ```
6. **Get the Regional Ancillary Suite (RAS)**
    ```
    rosie checkout {{ ras_id }}/{{ branch_ras }}
    ```
7. **Get the Regional Nesting Suite (RNS)**
    ```
    rosie checkout {{ rns_id }}/{{ branch_rns }}
    ```
8. **Run the OAS (optional)**
    ```
    rose suite-run -C ~/roses/{{ oas_id }}
    ```
9. **Run the RAS**
    ```
    rose suite-run -C ~/roses/{{ ras_id }}
    ```
    This step can be carried out simultaneously with step 8.
10. **Run the RNS**
    
    This step must be carried out only after step 8 (optional) and 9 have successfully completed.
    ```
    rose suite-run -C ~/roses/{{ rns_id }}
    ```

## Detailed guide

### Connect to Gadi

Connect to _Gadi_ by following the [related instructions in the _Rose/Cylc_ page](/models/run_a_model/rose_cylc/#connecting-to-gadi). 

!!! warning 
    If you choose to connect via the [ARE VDI](/models/run_a_model/rose_cylc/#launch-are-vdi-desktop), consider setting **Walltime** to `5` (5 hours), as {{ model }} might require longer setup time.

### Set up a persistent session

Set up a persistent session by following the [related instructions on the _Rose/Cylc_ page](/models/run_a_model/rose_cylc/#set-up-a-persistent-session).

### Set up SSH-keys (once-only) {: .no-toc }

Follow the [initialisation step](https://opus.nci.org.au/spaces/DAE/pages/249495793/Run+Cylc7+Suites#RunCylc7Suites-InitialisationStep(once-onlyforaccessdevcompatible-mode)) to accurately set up your ssh keys so you can run the model from outside of the persistent session.
Follow the [initialisation step](https://opus.nci.org.au/spaces/DAE/pages/249495793/Run+Cylc7+Suites#RunCylc7Suites-InitialisationStep(once-onlyforaccessdevcompatible-mode)) to accurately set up your ssh keys so you can run the model from outside of the persistent session.
### Set up Rose/Cylc

Set up _Rose/Cylc_ by following the [related instructions on the _Rose/Cylc_ page](/models/run_a_model/rose_cylc/#rosecylc-setup).


### {{ model }} configuration
{{ model }} comprises multiple different suites: a [Regional Ancillary Suite (RAS)](#ras), the [OSTIA Ancillary Suite](#oas) and a [Regional Nesting Suite (RNS)](#rns).

Each suite within {{ model }} has a `suite-ID` in the format `u-<suite-name>`, where `<suite-name>` is a unique identifier.<br>
Typically, an existing suite is copied and then edited as needed for a particular experiment.

!!! info 
    Many of the following steps appear in both the RAS and RNS. For this reason, these steps will be detailed only within the RAS section below, and subsequently linked to within the RNS section.

### Regional Ancillary Suite (RAS) {: #ras }

For the domain of interest, the RAS generates a set of ancillary files, such as initial conditions. These ancillary files are then used by the [RNS](#rns).

The `suite-ID` of the RAS is `{{ ras_id }}`.
The latest release branch of the RAS is `{{ branch_ras }}`.

#### Get the RAS configuration

Get the RAS configuration by following the [related instructions in the _Rose/Cylc_ page](/models/run_a_model/rose_cylc/#model-configurations-stored-on-mosrs) using the following specific information:

- **Suite-ID:** `{{ ras_id }}`
- **Branch:** `{{ branch_ras }}`
    


#### Run the RAS

Run the RAS by following the [related instructions on the _Rose/Cylc_ page](/models/run_a_model/rose_cylc/#run-the-model-configuration).

The RAS takes about 1 hour to run. You can find estimates of the compute and storage requirements for RAS in the [{{ model }} release notes]({{release_notes}}).

All steps are completed. You have successfully run the RAS! <br>

You will be able to check the [suite output files](#ras-output-files) after the run successfully completes.<br>
If you get errors or you can't find the outputs, [check the suite logs](#check-suite-logs) for debugging.

#### Check suite logs

It is not unusual that new users experience errors and job failures.<br>
When a suite task fails, a red icon appears next to the respective task name in the _Cylc_ GUI.<br>

To investigate the cause of a failure, or to monitor the progress of a suite, it is helpful to look at the suite's log files.

These files can be found in the directory `~/cylc-run/<suite-ID>` within a folder named `log.<TIMESTAMP>`, which is also symlinked as `log` (referred to as _logs folder_ below). Logs from previous runs of the same suite are archived as compressed files with the naming pattern `log.<TIMESTAMP>.tar.gz`.

Inside the logs folder, various files and subfolders can be found. The most relevant logs are typically:

- [Suite execution log](#suite-execution-log)
- [Task-specific logs](#task-specific-logs)

##### Suite execution log {: #suite-execution-log .no-toc }

The primary suite execution log resides in `~/cylc-run/<suite-ID>/log/suite/log`.

This file contains a chronological record of the suite's run history. Each line is a distinct log entry, generally formatted as `<TIMESTAMP> <LOG-TYPE> - [<task-name>.<cylc-cycle-point>] <status>`.

??? code "Example of a suite execution log file (click to see content)"
    ```
    2025-03-14T04:11:56Z INFO - Suite server: url=https://cylc.$USER$.$PROJECT.ps.gadi.nci.org.au:PORT/ pid=PID
    2025-03-14T04:11:56Z INFO - Run: (re)start=0 log=1
    2025-03-14T04:11:56Z INFO - Cylc version: 7.9.9
    2025-03-14T04:11:56Z INFO - Run mode: live
    2025-03-14T04:11:56Z INFO - Initial point: 01000101T0000Z
    2025-03-14T04:11:56Z INFO - Final point: 01000328T2359Z
    2025-03-14T04:11:56Z INFO - Cold Start 01000101T0000Z
    2025-03-14T04:11:56Z INFO - [make_drivers.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [install_cold.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [make_cice.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [make_mom.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [install_ancil.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:56Z INFO - [fcm_make_um.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:11:58Z INFO - [fcm_make_um.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [fcm_make_um.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [install_ancil.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [install_ancil.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [install_cold.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [install_cold.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_cice.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_cice.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_drivers.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_drivers.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:11:58Z INFO - [make_mom.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:11:57Z for job(01)
    2025-03-14T04:11:58Z INFO - [make_mom.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:04Z INFO - [make_drivers.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_drivers.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [install_cold.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [install_cold.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [make_cice.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_cice.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [make_mom.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [make_mom.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [install_ancil.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:02Z for job(01)
    2025-03-14T04:12:04Z INFO - [install_ancil.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:12:04Z INFO - [client-command] get_latest_state dm5220@gadi-login-08.gadi.nci.org.au:cylc-gui c842e8fb-017a-47ec-8706-7fef0af6d5f5
    2025-03-14T04:12:06Z INFO - [make_drivers.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:05Z for job(01)
    2025-03-14T04:12:09Z INFO - [make_cice.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:07Z for job(01)
    2025-03-14T04:12:09Z INFO - [install_ancil.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:07Z for job(01)
    2025-03-14T04:12:10Z INFO - [make2_cice.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:12:11Z INFO - [make2_cice.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:12:10Z for job(01)
    2025-03-14T04:12:11Z INFO - [make2_cice.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:14Z INFO - [make_mom.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:12Z for job(01)
    2025-03-14T04:12:15Z INFO - [make2_mom.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:12:18Z INFO - [make2_mom.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:12:15Z for job(01)
    2025-03-14T04:12:18Z INFO - [make2_mom.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:12:37Z INFO - [install_cold.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:12:35Z for job(01)
    2025-03-14T04:12:48Z INFO - [make2_mom.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:45Z for job(01)
    2025-03-14T04:12:48Z INFO - [make2_mom.01000101T0000Z] -health check settings: execution timeout=PT40M, polling intervals=PT31M,PT2M,PT7M,...
    2025-03-14T04:12:59Z INFO - [fcm_make_um.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:57Z for job(01)
    2025-03-14T04:12:59Z INFO - [fcm_make_um.01000101T0000Z] -health check settings: execution timeout=PT1H10M, polling intervals=PT1H1M,PT2M,PT7M,...
    2025-03-14T04:13:00Z INFO - [make2_cice.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:12:58Z for job(01)
    2025-03-14T04:13:00Z INFO - [make2_cice.01000101T0000Z] -health check settings: execution timeout=PT30M, polling intervals=PT21M,PT2M,PT7M,...
    2025-03-14T04:15:58Z INFO - [make2_cice.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:15:57Z for job(01)
    2025-03-14T04:18:19Z INFO - [make2_mom.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:18:17Z for job(01)
    2025-03-14T04:20:10Z INFO - [fcm_make_um.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:20:08Z for job(01)
    2025-03-14T04:20:11Z INFO - [fcm_make2_um.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:20:13Z INFO - [fcm_make2_um.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:20:12Z for job(01)
    2025-03-14T04:20:13Z INFO - [fcm_make2_um.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:20:37Z INFO - [fcm_make2_um.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:20:35Z for job(01)
    2025-03-14T04:20:37Z INFO - [fcm_make2_um.01000101T0000Z] -health check settings: execution timeout=PT1H10M, polling intervals=PT1H1M,PT2M,PT7M,...
    2025-03-14T04:37:11Z INFO - [fcm_make2_um.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:37:09Z for job(01)
    2025-03-14T04:37:12Z INFO - [recon.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:37:19Z INFO - [recon.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:37:14Z for job(01)
    2025-03-14T04:37:19Z INFO - [recon.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:37:53Z INFO - [recon.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:37:52Z for job(01)
    2025-03-14T04:37:53Z INFO - [recon.01000101T0000Z] -health check settings: execution timeout=PT30M, polling intervals=PT21M,PT2M,PT7M,...
    2025-03-14T04:38:28Z INFO - [recon.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:38:28Z for job(01)
    2025-03-14T04:38:29Z INFO - [coupled.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:38:30Z INFO - [coupled.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:38:30Z for job(01)
    2025-03-14T04:38:30Z INFO - [coupled.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:42:00Z INFO - [coupled.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:41:59Z for job(01)
    2025-03-14T04:42:00Z INFO - [coupled.01000101T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T04:45:28Z INFO - [coupled.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:45:27Z for job(01)
    2025-03-14T04:45:29Z INFO - [filemove.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:45:30Z INFO - [filemove.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:45:30Z for job(01)
    2025-03-14T04:45:30Z INFO - [filemove.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:12Z INFO - [filemove.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:46:11Z for job(01)
    2025-03-14T04:46:12Z INFO - [filemove.01000101T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T04:46:26Z INFO - [filemove.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:46:25Z for job(01)
    2025-03-14T04:46:27Z INFO - [history_postprocess.01000101T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:46:27Z INFO - [coupled.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:46:28Z INFO - [coupled.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:46:28Z for job(01)
    2025-03-14T04:46:28Z INFO - [coupled.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:28Z INFO - [history_postprocess.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:46:28Z for job(01)
    2025-03-14T04:46:28Z INFO - [history_postprocess.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:46:58Z INFO - [history_postprocess.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:46:57Z for job(01)
    2025-03-14T04:46:58Z INFO - [history_postprocess.01000101T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T04:47:09Z INFO - [coupled.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:47:09Z for job(01)
    2025-03-14T04:47:09Z INFO - [coupled.01000201T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T04:47:11Z INFO - [history_postprocess.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:47:10Z for job(01)
    2025-03-14T04:47:12Z INFO - [housekeep.01000101T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T04:47:13Z INFO - [housekeep.01000101T0000Z] status=ready: (internal)submitted at 2025-03-14T04:47:13Z for job(01)
    2025-03-14T04:47:13Z INFO - [housekeep.01000101T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:47:18Z INFO - [housekeep.01000101T0000Z] status=submitted: (received)started at 2025-03-14T04:47:17Z for job(01)
    2025-03-14T04:47:18Z INFO - [housekeep.01000101T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:47:21Z INFO - [housekeep.01000101T0000Z] status=running: (received)succeeded at 2025-03-14T04:47:20Z for job(01)
    2025-03-14T04:50:13Z INFO - [coupled.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:50:11Z for job(01)
    2025-03-14T04:50:14Z INFO - [filemove.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:50:15Z INFO - [filemove.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:50:14Z for job(01)
    2025-03-14T04:50:15Z INFO - [filemove.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:50:54Z INFO - [filemove.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:50:52Z for job(01)
    2025-03-14T04:50:54Z INFO - [filemove.01000201T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T04:51:08Z INFO - [filemove.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:06Z for job(01)
    2025-03-14T04:51:09Z INFO - [history_postprocess.01000201T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:51:09Z INFO - [coupled.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T04:51:10Z INFO - [coupled.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:09Z for job(01)
    2025-03-14T04:51:10Z INFO - [coupled.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:10Z INFO - [history_postprocess.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:09Z for job(01)
    2025-03-14T04:51:10Z INFO - [history_postprocess.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:23Z INFO - [history_postprocess.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:51:22Z for job(01)
    2025-03-14T04:51:23Z INFO - [history_postprocess.01000201T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T04:51:35Z INFO - [history_postprocess.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:34Z for job(01)
    2025-03-14T04:51:36Z INFO - [housekeep.01000201T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T04:51:37Z INFO - [housekeep.01000201T0000Z] status=ready: (internal)submitted at 2025-03-14T04:51:37Z for job(01)
    2025-03-14T04:51:37Z INFO - [housekeep.01000201T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T04:51:41Z INFO - [housekeep.01000201T0000Z] status=submitted: (received)started at 2025-03-14T04:51:40Z for job(01)
    2025-03-14T04:51:41Z INFO - [housekeep.01000201T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T04:51:45Z INFO - [housekeep.01000201T0000Z] status=running: (received)succeeded at 2025-03-14T04:51:43Z for job(01)
    2025-03-14T05:01:00Z INFO - [coupled.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:00:59Z for job(01)
    2025-03-14T05:01:00Z INFO - [coupled.01000301T0000Z] -health check settings: execution timeout=PT2H10M, polling intervals=PT2H1M,PT2M,PT7M,...
    2025-03-14T05:04:40Z INFO - [coupled.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:04:39Z for job(01)
    2025-03-14T05:04:41Z INFO - [filemove.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T05:04:43Z INFO - [filemove.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:04:43Z for job(01)
    2025-03-14T05:04:43Z INFO - [filemove.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:05:25Z INFO - [filemove.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:05:24Z for job(01)
    2025-03-14T05:05:25Z INFO - [filemove.01000301T0000Z] -health check settings: execution timeout=PT15M, polling intervals=PT6M,PT2M,PT7M,...
    2025-03-14T05:05:40Z INFO - [filemove.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:05:39Z for job(01)
    2025-03-14T05:05:41Z INFO - [history_postprocess.01000301T0000Z] -submit-num=01, owner@host=localhost
    2025-03-14T05:05:42Z INFO - [history_postprocess.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:05:42Z for job(01)
    2025-03-14T05:05:42Z INFO - [history_postprocess.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:05:57Z INFO - [history_postprocess.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:05:56Z for job(01)
    2025-03-14T05:05:57Z INFO - [history_postprocess.01000301T0000Z] -health check settings: execution timeout=PT1H40M, polling intervals=PT1H31M,PT2M,PT7M,...
    2025-03-14T05:06:08Z INFO - [history_postprocess.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:06:07Z for job(01)
    2025-03-14T05:06:09Z INFO - [housekeep.01000301T0000Z] -submit-num=01, owner@host=cylc.dm5220.tm70.ps.gadi.nci.org.au
    2025-03-14T05:06:10Z INFO - [housekeep.01000301T0000Z] status=ready: (internal)submitted at 2025-03-14T05:06:10Z for job(01)
    2025-03-14T05:06:10Z INFO - [housekeep.01000301T0000Z] -health check settings: submission timeout=P3D
    2025-03-14T05:06:18Z INFO - [housekeep.01000301T0000Z] status=submitted: (received)started at 2025-03-14T05:06:16Z for job(01)
    2025-03-14T05:06:18Z INFO - [housekeep.01000301T0000Z] -health check settings: execution timeout=PT12H
    2025-03-14T05:06:20Z INFO - [housekeep.01000301T0000Z] status=running: (received)succeeded at 2025-03-14T05:06:19Z for job(01)
    2025-03-14T05:06:20Z INFO - Suite shutting down - AUTOMATIC
    2025-03-14T05:06:28Z INFO - DONE
    ``` 

This file helps identify specific tasks that failed during the suite run.

!!! tip
    When a task fails, the `LOG-TYPE` will typically be `ERROR` or `CRITICAL`, instead of the more common `INFO`.

Once a specific task and _Cylc_ cycle point are identified, the task-specific logs can be inspected.

##### Task-specific logs {: .no-toc }

Logs for individual tasks are located in subfolders within the logs folder, following this path structure:
```
~/cylc-run/<suite-ID>/log/job/<cylc-cycle-point>/<task-name>/<retry-number>
```
The `<retry-number>` indicates the number of retries for the same task, with the latest retry symlinked to `NN`.  For the RAS, the `<cylc-cycle-point>` is `1` because the jobs are run in one cycle.  For the OAS and RNS the `<cylc-cycle-point>` is the date/time of the cycle.

For example, logs for most recent retry of a task named `Lismore_d1100_ancil_um_mean_orog` at _Cylc_ cycle point `1` can be found in the folder `~/cylc-run/<suite-ID>/log/job/1/Lismore_d1100_ancil_mean_orog/NN`.

Within this directory, the `job.out` and `job.err` files (representing `STDOUT` and `STDERR`, respectively) can be found, along with other related log files.

!!! tip
    Within the _Cylc_ GUI, logs for a specific task can be viewed by right-clicking on the task and selecting the desired log from the _View Job Logs (Viewer)_ menu.

#### Stop, restart, reload and clean suites
In some cases, you may want to control the running state of a suite.<br>
If your _Cylc_ GUI has been closed and you are unsure whether your suite is still running, you can scan for active suites and reopen the GUI.<br>
To scan for active suites, run:
```
cylc scan
```
To reopen the _Cylc_ GUI, run the following command from within the [suite directory](#suitedir):
```
rose suite-gcontrol
```

##### STOP a suite {: .no-toc }
To shutdown a suite in a safe manner, run the following command from within the [suite directory](#suitedir):
```
rose suite-stop -y
```
Alternatively, you can directly kill the [PBS jobs][PBS job] connected to your run. To do so:

1. Check the status of all your PBS jobs:
```
qstat -u $USER
```

1. Delete any job related to your run:
```
qdel <job-ID>
```

##### RESTART a suite {: .no-toc }
There are two main ways to restart a suite:

- **_SOFT_ restart**<br>
    To reinstall the suite and reopen _Cylc_ in the same state it was prior to being stopped, run the following command from within the [suite directory](#suitedir):
    ```
    rose suite-run --restart
    ```

    !!! warning
        You may need to manually trigger failed tasks from the _Cylc_ GUI.

- **HARD restart**<br>
    To overwrite any previous runs of the suite and start afresh, run the following command from within the [suite directory](#suitedir):
    ```
    rose suite-run --new
    ```

    !!! warning
        This will overwrite all existing model output and logs for the same suite.

##### RELOAD a suite {: .no-toc }
In some cases, the suite needs to be updated without necessarily having to stop it (e.g., after fixing a typo in a file). Updating an active suite is called a _reload_, where the suite is _re-installed_ and _Cylc_ is updated with the changes. This is similar to a _SOFT_ restart, except new changes are installed, so you may need to manually trigger failed tasks from the _Cylc_ GUI.

To reload a suite, run the following command from within the [suite directory](#suitedir):
```
rose suite-run --reload
```

##### CLEAN a suite {: .no-toc }
To remove all files and folders created by the suite within the `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>` directory, run the following command from within the [suite directory](#suitedir):
```
rose suite-clean
```

Alternatively, you can achieve the same behaviour within a new submission of an experiment, by appending the `--new` option to the `rose suite-run` command:
```
rose suite-run --new
```

!!! warning
    Cleaning a suite folder will remove any non-archived data (i.e., output files, logs, executables, etc.) associated with the suite.

#### RAS output files

The RAS output ancillary files can be found in `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils`.<br>
Ancillaries are divided into folders according to each [nested region]({{ access_models }}/#nesting) name, and then further separated according to each nest (i.e., _Resolution_) name. The path of ancillaries for a specific nest (i.e., _Resolution_) is `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils/<nested_region_name>/<nest_name>`.

The example above has one `nested_region_name` called `Lismore`, 1 nest named `era5` (outer domain corresponding to _Resolution 1_), and 2 inner nests (_Resolution 2_ and _Resolution 3_) named `d1100` and `d0198`, respectively.<br>
Thus, the ancillary files directory `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/data/ancils/` contains the following subdirectories:

- `Lismore/d1100`
- `Lismore/d0198`
- `Lismore/era5`

Ancillary data files are typically output in the [UM fieldsfile](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) format.

### OSTIA Ancillary Suite (OAS) (optional) {: #oas }

Archived Operational Sea Surface Temperature and Sea Ice Analysis (OSTIA) data can be packaged into ancillary files for use in the RNS. Running the OAS is optional and needed only if you require daily varying and/or higher resolution SST and sea ice inputs (resolution and other details can be found on the [{{model}} configuration]({{ access_models }}/{{ model }}/#oas) page). OAS is included here in case you choose to run it.

The `suite-ID` of the OAS is `{{ oas_id }}`.

#### Get and run OAS configuration
Steps to obtain and run the OAS, as well as monitor logs, are similar to those listed above for the [RAS](#ras).<br>
The main difference is the OAS configuration specific information: 

- **Suite-ID:** {{ oas_id }}
- **Branch:** trunk (alternatively, simply omit the `/<branch>` portion when obtaining the configuration)

The OAS and RAS can run concurrently, but the RNS can only be started once both have finished. The OAS takes about 10 minutes to run. You can find estimates of the compute and storage requirements for OAS in the [{{ model }} release notes]({{release_notes}}).

To get the OAS configuration, follow the steps listed in [Get the RAS configuration](#get-the-ras-configuration), but use the OAS `suite-ID` `{{ oas_id }}` without any branch when copying the suite.

To run the OAS configuration, follow the steps listed in [Run the RAS](#run-the-ras).

To check the OAS suite logs, follow the steps listed in [Check suite logs](#check-suite-logs).

#### OAS output files

All the OAS output files are available in the `OSTIA_OUTPUT` directory specified in OAS's configuration file `rose-suite.conf`.

OAS ancillary data files are output in the [UM fieldsfile](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) format.

For example, the global OSTIA ancillary file for the first cycle (`20220226T0000Z`) of the _Lismore_ experiment can be found in `/scratch/$PROJECT/$USER/OSTIA_ANCIL/20220226T0000Z_ostia.anc`.

!!! warning
    The RNS updates OSTIA data daily at `T0600Z` (or `T06Z` in [ISO 8601 time format](https://en.wikipedia.org/wiki/ISO_8601#Times)). If the time of the `INITIAL_CYCLE_POINT` of your suite is set before `T0600Z`, you will also need OSTIA ancillary files for the day before the starting day of your suite.<br>
    For example, if a suite has the `INITIAL_CYCLE_POINT` set to `20250612T0000Z` (i.e., 12 Jun 2025 at midnight), it will also require the OSTIA ancillary files for the 11 Jun 2025.

### Regional Nesting Suite (RNS) {: #rns }

The RNS uses the ancillary files produced by the RAS and OAS to run the regional forecast for the domain of interest. Therefore, before running the RNS you must wait for the completion of the RAS and OAS (if you chose to run it). You can find estimates of the compute and storage requirements for the RNS in the [{{ model }} release notes]({{release_notes}}).

The `suite-ID` of the RNS is `{{ rns_id }}`.
The latest release branch of the RNS is `{{ branch_rns }}`.

#### Get and run RNS configuration
Steps to obtain and run the RNS, as well as monitor logs, are similar to those listed above for the [RAS](#ras).<br>
The main difference is the `suite-ID`, which for the RNS is `{{ rns_id }}`.

To get the RNS configuration, follow the steps listed in [Get the RAS configuration](#get-the-ras-configuration).

The main difference is the RNS configuration specific information: 

- **Suite-ID:** {{ rns_id }}
- **Branch:** {{ branch_rns }}


To run the RNS configuration, follow the steps listed in [Run the RAS](#run-the-ras).

To check the RNS suite logs, follow the steps listed in [Check suite logs](#check-suite-logs).

#### RNS output files

All the RNS output files are available in the directory `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>`. They are also symlinked in `~/cylc-run/<suite-ID>`.

The RNS output data can be found in the directory `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/cycle`, grouped for each [cycle](#change-run-length).<br>
Within the `cycle` directory, outputs are divided into multiple nested subdirectories in the format `<nested_region_name>/<nest_name>/<science_configuration>`, with [`<nested_region_name>`](#change-the-nested-region-name) and `<nest_name>` referring to the respective configurable options. The `<science_configuration>` is usually `GAL9` or `RAL3.2`, depending on the [nest resolution]({{ access_models }}/#model-components).

Each `<science_configuration>` directory has the following subdirectories:

- `ics` &rarr; initial conditions
- `lbcs` &rarr; lateral boundary conditions
- `um` &rarr; model output data

The RNS output data files are in [UM fieldsfile](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_F03.pdf) format.

For example, the model output data for the first cycle (`20220226T0000Z`) of the _Lismore_ experiment on this page (`Lismore` `nested_region_name`, using a `RAL3P3` `science_configuration` and `d0198` as a `nest_name`) can be found in `/scratch/$PROJECT/$USER/cylc-run/<suite-ID>/share/cycle/20220226T0000Z/Lismore/d0198/RAL3P3/um/umnsaa_pa000`.

!!! tip
    The output data name format may vary depending on some configuration parameters.<br>
    To change which output variables are produced, refer to [{{ model }} configuration documentation]({{config_docs}}/model_outputs/)


## Edit {{ model }} configuration

This section describes how to modify the {{ model }} configuration.

In general, ACCESS modelling suites can be edited either by directly modifying the configuration files within the suite directory, or by using the [_Rose_ GUI](#rosegui).

!!! warning
    Unless you are an experienced user, directly modifying configuration files is usually discouraged to avoid encountering errors.

##### Rose GUI {: #rosegui }

Basic instructions on how to edit a model configuration using the Rose GUI can be found on the [related Rose/Cylc page](/models/run_a_model/rose_cylc#rose-gui).


#### Change start date and run length {: #change-run-length }
<div markdown id="run-length-mismatch">
!!! warning
    `INITIAL_CYCLE_POINT` and `FINAL_CYCLE_POINT` define all the [_Cylc_ cycle points](https://cylc.github.io/cylc-doc/7.9.3/html/terminology.html?highlight=cycle%20point#cycle-points) that are set within the experiment run.
    
    The model will always run for a full _cycling frequency_ (1 day) for each _Cylc_ cycle point.
    
    This means, for example, that with `INITIAL_CYCLE_POINT` set to `20220226T0000Z`, and `FINAL_CYCLE_POINT` set to `+P1D` (plus 1 day), 2 _Cylc_ cycle points will be set (`20220226T0000Z` and `20220227T0000Z`). Therefore, the model will run for a total of 2 days!
    
    To avoid running the model for longer than desired, we suggest adding `-PT1S` (minus 1 second) to the relative duration specified in the `FINAL_CYCLE_POINT` such that the model runs for the number of days specified in the relative duration (refer to the example below). The _run length_ is calculated using the `INITIAL_CYCLE_POINT` and `FINAL_CYCLE_POINT` fields.
    
    Both these fields use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date format, with `FINAL_CYCLE_POINT` also accepting relative [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations).

    For example, to run the experiment for 2 days starting on 5 April 2000, set `INITIAL_CYCLE_POINT` to `20000405T0000Z` and `FINAL_CYCLE_POINT` to `+P2D-PT1S`.
</div>



- **OAS**<br>
    The RNS requires the global OSTIA ancillary files to be available on disk for each day of the run. If a simulation date/time changes such that the required global OSTIA ancillary files are not already present, the OAS must be re-run with the new date/time.
    The OAS runs in multiple [PBS jobs][PBS job] submissions with each job preparing global OSTIA ancillary information for one day.  The job scheduler automatically resubmits the suite every chosen _cycling frequency_ until the total _run length_ is reached.<br>
    
    To modify these parameters within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Ostia ancillary Generation Suite &rarr; Cycling options_. 
    Edit the related field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>

- **RNS**<br>
    The RNS runs in multiple [PBS jobs][PBS job] submissions, each one constituting a _cycle_. The job scheduler automatically resubmits the suite every chosen _cycling frequency_ until the total _run length_ is reached.<br>
    
    !!! warning
        The _cycling frequency_ is currently set to `24` hours (1 day) and should be left unchanged to avoid errors.<br>
        This also means the model will run for a minimum of 1 day.
      

    To modify these parameters within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Cycling options_. Edit the related field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
    For example, to run the experiment for 2 days starting on 5 April 2000, set `INITIAL_CYCLE_POINT` to `20000405T0000Z` and `FINAL_CYCLE_POINT` to `+P2D-PT1S` (due to the [run length mismatch](#run-length-mismatch)).

#### Change the land-surface initial conditions source
- **RNS**<br>
    To change the [land-surface initial conditions source]({{ access_models }}/#land-surface-initial-conditions-source) within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Driving model setup_. Edit the `NCI_HRES_ECCB` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to get the land-surface initial conditions from the `BARRA-R2` dataset, set the `NCI_HRES_ECCB` field to `BARRA2-R`.

!!! warning
    When changing the land-surface initial conditions source, it is important to ensure that the configuration of the nested region aligns with the [nest configuration requirements](#nest-configuration-requirements).

#### Change the simulation region
In {{ model }}, users can perform simulations for a particular region of the Earth by configuring specific parameters for each domain of interest (referred to as _nested region_).<br>

In {{ model }}, the following parameters are supported to configure the nested regions:

- [Nested region name](#change-the-nested-region-name)
- [Nested region position](#change-the-nested-region-position)
- [Nested region's nest configuration](#change-the-nested-regions-nest-configuration)

!!! warning
    Domain-specific changes need to be consistent between RAS and RNS. Therefore, for each of the configuration parameters listed above, consistent changes to both RAS and RNS will be required.

##### Change the nested region name {: .no-toc }
- **RAS**<br>
    To change a nested region name within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Regional Ancillary Suite &rarr; Nested region 1 setup_. Edit the `rg01_name` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to set the name of the nested region to `Darwin`, set the `rg01_name` field to `Darwin`.

- **RNS**<br>
    Changing the RAS nested region name changes the [RAS output path](#ras-output-files). As a consequence, the following changes are required within the RNS:
    
    - **Ancillary directory**<br>
        To change the first nest ancillary directory within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 1 setup_. Change the `rg01_rs01_ancil_dir` field by replacing `Lismore` with the chosen RAS nested region name, and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
        The same step needs to be repeated for:
        
        - _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 2 setup_ `rg01_rs02_ancil_dir` field
        - _suite conf &rarr; Nesting Suite &rarr; Driving model setup_ `dm_ec_lam_ancil_dir` field

        For example, if the RAS nested region name was set to `Darwin`, replace `Lismore` in the `rg01_rs01_ancil_dir`, `rg01_rs02_ancil_dir` and `dm_ec_lam_ancil_dir` fields with `Darwin`.

    - **RNS nested region name**<br>
        To change the nested region name within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup_. Edit the `rg01_name` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

        For example, to set the name of the nested region to `Darwin`, set the `rg01_name` field to `Darwin`.

        !!! tip
            Changing the RNS nested region name is not strictly necessary, but it affects the [RNS outputs path](#rns-output-files). Therefore, for consistency, it is strongly recommended for RAS and RNS to have the same nested region names.

##### Change the nested region position {: .no-toc }
The nested region position is usually defined by the latitude and longitude coordinates of the nested region centre.

- **RAS**<br>
    To change the nested region centre within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Regional Ancillary Suite &rarr; Nested region 1 setup_. Edit the `rg01_centre` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.

    For example, to set the centre of the nested region to `-12.4` / `130.8`, set the `rg01_centre` field to `-12.4` / `130.8`.

!!! warning
    When changing the land-surface initial conditions source, it is important to ensure that the configuration of the nested region aligns with the [nest configuration requirements](#nest-configuration-requirements).

##### Change the nested region's nest configuration {: .no-toc }
Each nested region can contain multiple [nests]({{access_models}}/#nesting) (referred to as _Resolutions_ within the RAS and RNS), each of them being a separate domain where the simulation experiment is carried out.<br>
Typically, nests within the same nested region are arranged concentrically, with increasingly smaller dimensions and higher resolutions towards the innermost nests.

<div markdown id='nest-configuration-requirements'>
!!! warning
    Currently, {{model}} only supports specific nest configurations that meet the following criteria:
    
    The grid points of the RAS first inner nest (i.e., _Resolution 2_, because _Resolution 1_ always corresponds to the outer ERA5 domain) must align with those of the [land-surface initial conditions dataset]({{access_models}}/#land-surface-initial-conditions-source). Thus, the configuration of the RAS first inner nest (_Resolution 2_), including its position, dimension and resolution, need to be modified accordingly. Note that the position of a nest is also influenced by the [nested region position](#change-the-nested-region-position).
</div>

#### Change the output variables
[UM](/models/model_components/atmosphere/#unified-model-um) outputs are usually provided as a list of [STASH](https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_C04.pdf) variables.<br>
Manually specifying each STASH variable can be complex. To simplify the selection process for commonly used climate analysis variables, predefined groups of STASH variables are set up, known as _stashpacks_.

- **RNS**<br>
    To toggle a _stashpack_ within the [Rose GUI](#rosegui), navigate to _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 1 setup &rarr; Config 1 setup_. Toggle a specific _stashpack_ within the `rg01_rs01_m01_stashpack` field and click the _Save_ button ![Save button](/assets/run_access_cm/save_button.png){: style="height:1em"}.<br>
    Similar steps can be repeated for the _suite conf &rarr; Nesting Suite &rarr; Nested region 1 setup &rarr; Resolution 2 setup &rarr; Config 2 setup_ `rg01_rs02_m02_stashpack` field.<br>
    For example, to enable `stashpack 6` (that includes variables such as wind gust, mean sea level pressure and rainfall amount, for every model timestep) in all nests, set the `6th` button of both `rg01_rs01_m01_stashpack` and `rg01_rs02_m02_stashpack` fields to `true`.



## Troubleshooting
For common known errors related to {{ model}} and possible workarounds, refer to [{{ model }} configuration documentation]({{config_docs}}/troubleshooting/).


## Get Help
If you have questions or need help regarding {{ model }}, consider creating a topic in the [Regional Nesting Suite category of the ACCESS-Hive Forum](https://forum.access-hive.org.au/c/atmosphere/regional-nesting-suite/17).<br>
For assistance on how to request help from ACCESS-NRI, follow the [guidelines on how to get help](/about/user_support/#still-need-help).<br>
For more detailed documentation see [access-ram3-configs]({{config_docs}}).

<custom-references>
- [https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf](https://nespclimate.com.au/wp-content/uploads/2020/10/Instruction-document-Getting_started_with_ACCESS.pdf)
- [https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html](https://code.metoffice.gov.uk/doc/um/latest/um-training/rose-gui.html)
- [https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites)
- [https://opus.nci.org.au/display/Help/Persistent+Sessions](https://opus.nci.org.au/display/Help/Persistent+Sessions)
- [https://gmd.copernicus.org/articles/13/1999/2020/](https://gmd.copernicus.org/articles/13/1999/2020/)
</custom-references>
