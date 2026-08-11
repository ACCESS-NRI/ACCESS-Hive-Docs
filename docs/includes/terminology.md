<!--start:terminology-conf-vs-exp-->
### _Configuration_ and _experiment_ definitions

The terms _configuration_ and _experiment_ are not interchangeable although they are closely related.

- A _configuration_ defines a specific way to run the model it relates to.<br> 
  It is therefore defined by:
  
     - model version and build (model executable(s))
     - set of input files (ancillaries, forcings, restarts)
     - set of physical and modelling options for each model component, such as namelists, configuration files and MPI layout.
  
    Changing any one of these elements creates a new configuration.

- An _experiment_ is a realisation of a configuration: a series of sequential runs that generate model data over a span of model time.
<!--start:terminology-conf-vs-exp-->

