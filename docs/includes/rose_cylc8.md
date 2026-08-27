<!--start:cylc8-prerequisites-->
- [hr22](https://my.nci.org.au/mancini/project/hr22/join)
<!--end:cylc8-prerequisites-->

<!--start:cylc8-compatibility-mode-->
!!! warning
   
    {{model}} is transitioning to a _Cylc8_ workflow from a _Cylc7_ workflow. At this point, the configuration is using _Cylc8_ in compatibility-mode with _Cylc7_. This means the configuration can be run with _Cylc7_ or _Cylc8_ to allow experienced users the time to understand how to use _Cylc8_. However, we are only giving the instructions with _Cylc8_ as all users should get familiar with _Cylc8_ before we remove the compatibility with _Cylc7_.
<!--end:cylc8-compatibility-mode-->

<!--start:cylc8-about-->
The _Rose/Cylc_ workflow management tool consists of two components:

* The [_Cylc_](https://niwa.co.nz/environmental-information/cylc-suite-engine) (pronounced ‘silk’) task engine, developed by the New Zealand National Institute of Water and Atmospheric Research (NIWA). Cylc is a workflow manager that automatically executes tasks according to the model's configuration. It also monitors all tasks, reporting any errors that may occur.
* The [_Rose_](https://www.metoffice.gov.uk/research/approach/modelling-systems/rose) framework developed by the UKMO which configures tasks for the _Cylc_ engine. Rose is a toolkit that can be used to view, edit and run some of the [ACCESS models](/models/access_models).

A set of tasks configured by _Rose_ to run with the _Cylc8_ engine is called a _workflow_ in _Cylc8_.
<!--end:cylc8-about-->

