{% set example_folder = "25km_jra_ryf" %}

!!! Summary
    These instructions are intended to help users share their experiments for publication in papers. They presume the user got started using the model following the "how to run a model" documentation.

## Related issues
 - [Possibly confusing "restart" behaviour with flag in config.yaml #955](https://github.com/ACCESS-NRI/access-hive.org.au/issues/955)
 - [Hosting experiment repo on Github. Workflow for users for publications. #934](https://github.com/ACCESS-NRI/access-hive.org.au/issues/934)
 - [General how to use Payu Docs #978](https://github.com/ACCESS-NRI/access-hive.org.au/issues/978)
 - [Access Hive update: discuss flowchart of workflow for community #1036](https://github.com/ACCESS-NRI/access-hive.org.au/issues/1036)

## Detailed instructions

These instructions


For example if one [had followed](https://docs.access-hive.org.au/models/run_a_model/run_access-om3/#get-access-om3-configuration), then

```bash
mkdir -p ~/access-om3
cd ~/access-om3
payu clone -b expt -B release-MC_25km_jra_ryf https://github.com/ACCESS-NRI/access-om3-configs 25km_jra_ryf
cd 25km_jra_ryf
```

In the example above, the `payu clone` command clones the latest release of the 25km repeat-year JRA55 MOM6 (`M`) CICE6 (`C`) configuration (`-B release-MC_25km_jra_ryf`) to a directory named `25km_jra_ryf` and creates a new experiment branch (-b expt).

We then want to put the updated version of this experiment (with ther user's runlogs and configuration changes) onto their own github account.

!!! Note
    At this point in the instuctions, we are assuming changes have been made to the expt branch above. Typing `git log` should confirm this. 

The below steps walks you through the steps to push your local Git repository to a new or different remote repository.

The first step is to add the New Remote, that is, your personal GitHub account. Use the `git remote add` command to add a new remote repository:

```bash
git remote add <new-remote-name> https://github.com/username/new-repo.git
```

`username` here needs to be your GitHub username.

Check that the new remote was added:
```bash
git remote -v
```

Check the branch name used in the local repository (e.g. if you chose not to use the default above of `expt`):
```bash
git branch 
> * <current-branch-name>
> other-branch-1
> other-branch-2
```

Push your branch (e.g., `expt`) to the new remote:

```bash
git push <new-remote-name> `expt`
```

Optionally, you might prefer to not push the `expt` name to the remote. For publication purposes you may wish to give it a more meaningful name (`<preferred-new-name>`). Push the experiment to this archive, assigning a branch name that matching the conventions:
```bash
git push <new-remote-name> <current-branch-name>:<preferred-new-name>
```


Well done, your configuration and experiments should now be on GitHub. Most journals prefer for their to be a DOI or zenodo archive at this point. 

To create that follow [these steps](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content):

1. Navigate to the login page for Zenodo.
1. Click Log in with GitHub.
1. Review the information about access permissions, then click Authorize zenodo.
1. Navigate to the Zenodo GitHub page.
1. To the right of the name of the repository you want to archive, toggle the button to On.

Zenodo archives your repository and issues a new DOI each time you create a new GitHub release. Follow the steps at Managing releases in a repository to create a new one.


