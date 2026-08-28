<!--start:terminology-conf-vs-exp-->
### _Configuration_ and _experiment_ definitions

The terms _configuration_ and _experiment_ used in this documentation are closely related, but not interchangeable.

A _configuration_ defines a specific way of running a model. It is defined by the: 

  - model version and build (model executable(s));
  - set of input files (ancillaries, forcings, restarts); and
  - physical and modelling options for each model component, including namelists, configuration files and MPI layout.
  
Changing any one of these elements creates a new configuration.

An _experiment_ is a realisation of a configuration: a sequence of runs that generates model data over a period of model time.
<!--start:terminology-conf-vs-exp-->

