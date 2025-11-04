{% set model = "ACCESS-OM3" %}

# Explainer: Workflows for users who wish to share or develop experiments and configurations

!!! Summary
    At ACCESS-NRI we want to help users share or develop experiments and configurations. Each of these tasks has subtly different workflows, we make suggestions and provide pro/cons below.

# Difference between configuration and experiment.

 - A configuration ([example](https://github.com/ACCESS-NRI/access-om3-configs/tree/release-MC_25km_jra_ryf)) contains all the elements needed to begin an experiment.

 - An experiment (e.g. ESM1.6 development run `pearseb-dev-20241220-1` [here](https://github.com/ACCESS-Community-Hub/access-esm1.6-dev-experiments/tree/pearseb-dev-20241220-1)) contains the same files as the configuration but additional files that detail how that configuration has been run (e.g. `manifests`, [example](https://github.com/ACCESS-Community-Hub/access-esm1.6-dev-experiments/commit/12dd7f7100de75437f7fa439d017ed55beed5475)). Experiments have `Runlog = true`, which means each time the model is run their is an associated commit ([example](https://github.com/ACCESS-Community-Hub/access-esm1.6-dev-experiments/commits/pearseb-dev-20241220-1/)). For further information see Payu documentation.

# To branch or fork?

There are 3 options for sharing configurations:

 1. On the `ACCESS-NRI` organisation (e.g. `ACCESS-NRI/access-om3-configs`), this requires write access to the repository. This would use a branch.
 1. On the `ACCESS-Community-Hub` organisation (e.g. `ACCESS-Community-Hub/access-esm1.6-dev-experiments`), this requires write access to the repository. This would also involve a branch.
 1. On a personal GitHub account (e.g. `joe/access-om3-configs`). This would use a fork.

Discuss pro and cons.


