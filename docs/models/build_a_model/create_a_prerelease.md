[ACCESS models]: /models
[om2 repo]: https://github.com/ACCESS-NRI/ACCESS-OM2
[om2 config]: /models/access_models/access-om/#access-om2
[mom5 component]: /models/model_components/ocean/#mom5

!!! danger
    This page is tailored to experienced users and collaborators developing ACCESS models.<br>
    This step is *not* required if you *only* want to run a model. If you are looking for information on how to run a model, refer to the [Run a Model](/models/run_a_model) section.

# Create Prereleases and Releases for an ACCESS Model

## About

The instructions below outline how to trigger automatic prerelease and release builds of an [ACCESS model][ACCESS models] by making use of the build and deployment workflows enabled by the [access-nri/build-cd repository](https://github.com/ACCESS-NRI/build-cd).

This allows, for example, quick testing of the development of a new feature in a specific ACCESS Model configuration.

The following instructions outline how to trigger a prerelease build of [ACCESS-OM2][om2 config] after modifying its [MOM5 component]. All other components of the official [ACCESS-OM2 release][om2 repo] will remain unchanged.

!!! tip
    The following instructions are valid (with simple tweaks) for all [ACCESS models].

## Prerequisites

- **Join the required projects specific to the HPC system**<br>
    For models deployed to `Gadi`, join the `vk83` project by requesting membership on the respective [vk83](https://my.nci.org.au/mancini/project/vk83/join) NCI project page.

    For more information on joining specific NCI projects, refer to [How to connect to a project](https://opus.nci.org.au/display/Help/How+to+connect+to+a+project).

- **_Write_ permissions to the related model deployment repository**<br>
    To request write permissions for a specific model deployment repository, please [contact ACCESS-NRI](/about/contact/).

## The model deployment repository

All [ACCESS models] have their deployments on HPC systems controlled by an [ACCESS-NRI's GitHub](https://github.com/ACCESS-NRI) repository, named according to the specific model.<br>
For example, the deployment of [ACCESS-OM2][om2 config] is controlled by the [ACCESS-OM2 GitHub repository][om2 repo].

The model deployment repository also enables automatic prerelease build deployments of the model whenever commits are added to one of the repository's open Pull Requests (PR).<br>
Every push to a PR triggers an isolated prerelease build deployment for the PR (every PR can be seen as a separate development configuration for the model).<br>
When a PR is merged, the related prereleases are deleted and an official release build is created.

Although the structure of different model deployment repositories can slightly differ, their top-level will always contain a:

- [`spack.yaml` file](#the-spackyaml-file)
- [`config` directory](#the-config-directory)

### The spack.yaml file

The `spack.yaml` file defines the [_Spack_ environment](https://spack.readthedocs.io/en/latest/environments.html#environments-spack-yaml-spack-lock) that constrains the versions and features (variants) of all dependencies required to build a given ACCESS model. At build time, it is [concretized](https://spack.readthedocs.io/en/latest/environments.html#concretizing) into a single set of dependencies, creating a `spack.lock` file.

For more information on the `spack.yaml` file, refer to  [ACCESS-NRI's DevDocs](https://github.com/ACCESS-NRI/dev-docs/wiki/Spack#the-spackyaml-file-spec-file).

### The config directory

The `config` directory contains a single `versions.json` file. This file allows customisation of both the version of [`access-nri/spack`](https://github.com/ACCESS-NRI/spack) used to deploy the model and the version of [`access-nri/spack-packages`](https://github.com/ACCESS-NRI/spack-packages) that will source the recipes for the _Spack_ packages.

## Trigger model prerelease and release build deployments

As mentioned above, prerelease build deployments are triggered by a push of one or more commits within a model deployment repository's open PR. When the PR is merged, a release build deployment is created.<br>
The following sequence of tasks are needed to trigger a prerelease and release build deployment for a model new feature:

#### 1. Clone the repository and create a feature branch
The first step is to clone the model deployment repository and create a feature branch, on which new features will be developed.

To clone the [ACCESS-OM2 deployment repository][om2 repo] and create a feature branch named `update_mom5_dev_build` run:
```
git clone https://github.com/ACCESS-NRI/ACCESS-OM2.git
cd ACCESS-OM2
git checkout -b update_mom5_dev_build
```
<terminal-window>
    <terminal-line data="input">git clone https://github.com/ACCESS-NRI/ACCESS-OM2.git</terminal-line>
    <terminal-line>Cloning into 'ACCESS-OM2'...</terminal-line>
    <terminal-line>remote: Enumerating objects: 442, done.</terminal-line>
    <terminal-line>remote: Counting objects: 100% (170/170), done.</terminal-line>
    <terminal-line>remote: Compressing objects: 100% (68/68), done.</terminal-line>
    <terminal-line>remote: Total 442 (delta 137), reused 110 (delta 98), pack-reused 272 (from 1)</terminal-line>
    <terminal-line>Receiving objects: 100% (442/442), 143.84 KiB | 3.79 MiB/s, done.</terminal-line>
    <terminal-line>Resolving deltas: 100% (219/219), done.</terminal-line>
    <terminal-line data="input">cd ACCESS-OM2</terminal-line>
    <terminal-line data="input" directory="ACCESS-OM2">git checkout -b update_mom5_dev_build</terminal-line>
    <terminal-line directory="ACCESS-OM2">Switched to a new branch 'update_mom5_dev_build'</terminal-line>
</terminal-window>

#### 2. Apply the modifications and commit the changes {: id="modifications"}
Modifications can then be made to the `spack.yaml` or `config/versions.json` files as needed (e.g., update packages versions, add or change variants, etc.).<br>
After making the modifications, commit the changes to the newly-created feature branch and push them to the remote repository.

In this example, we will change ACCESS-OM2's [MOM5 component] by replacing it with the version from [MOM5 `development` branch](https://github.com/ACCESS-NRI/MOM5/tree/development).
To achieve this, the following steps will be carried out:

1. Retrieve the _Git_ hash (_LONG\_HASH_) for the `development` head commit.

    !!! warning
        Currently, only _Git_ tags and commit hashes are supported for specifying component versions.<br>
        To use a _Git_ branch, its corresponding commit hash should be retrieved and used instead.

2. Update the [version of the `mom5` package](https://github.com/ACCESS-NRI/ACCESS-OM2/blob/d907f3314a9956875baaaaf2b4d7b6be6fa81926/spack.yaml#L15) in the `spack.yaml` file with the new version (i.e., `@git.LONG_HASH`).

3. It is also recommended to update the [overall ACCESS-OM2 version](https://github.com/ACCESS-NRI/ACCESS-OM2/blob/d907f3314a9956875baaaaf2b4d7b6be6fa81926/spack.yaml#L8).<br>
   This is particularly important before merging a PR as it will determine the version tag for the model new release. The format is `CALVER_YEAR.CALVER_MONTH.MINOR`.<br>
   In this example, the overall version will be updated to `git.2024.03.1`.

After completing the modifications above, the output of the command
```
git diff
```
should look like the following:
<terminal-window>
    <terminal-line data="input" directory="ACCESS-OM2">git diff</terminal-line>
    <terminal-line class="git-highlighted">diff --git a/spack.yaml b/spack.yaml</terminal-line>
    <terminal-line lineDelay=0 class="git-highlighted">index bfa6df2..be80333 100644</terminal-line>
    <terminal-line lineDelay=0 class="git-highlighted">--- a/spack.yaml</terminal-line>
    <terminal-line lineDelay=0 class="git-highlighted">+++ b/spack.yaml</terminal-line>
    <terminal-line lineDelay=0 class="git-cyan">@@ -5,14 +5,14 @@</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks"> spack:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">   # add package specs to the `specs` list</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">   specs:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks git-red">-    - access-om2@git.2024.03.0</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks git-green">+    - access-om2@git.2024.03.1</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">   packages:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    cice5:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    require:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">        - '@git.2023.10.19'</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    mom5:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    require:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks git-red">-        - '@git.2023.11.09'</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks git-green">+        - '@git.LONG_HASH'</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    libaccessom2:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">    require:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">        - '@git.2023.10.26'</terminal-line>
    <terminal-line lineDelay=0 class="git-cyan">@@ -48,8 +48,8 @@ spack:</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">        - libaccessom2</terminal-line>
    <terminal-line lineDelay=0 class="keep-blanks">        - oasis3-mct</terminal-line>
</terminal-window>

To stage and commit the changes, run:
```
git commit -am "Updated mom5 to development version."
```
<terminal-window>
    <terminal-line data="input" directory="ACCESS-OM2">git commit -am "Updated mom5 to development version."</terminal-line>
    <terminal-line>[update_mom5_dev_build 7cdac6f] Updated mom5 to development version.</terminal-line>
    <terminal-line class="keep-blanks"> 1 file changed, 4 insertions(+), 4 deletions(-)</terminal-line>
</terminal-window>

Finally, push the changes to the remote repository by executing:
```
git push --set-upstream origin update_mom5_dev_build
```
<terminal-window>
    <terminal-line data="input" directory="ACCESS-OM2">git push --set-upstream origin update_mom5_dev_build</terminal-line>
    <terminal-line>Enumerating objects: 5, done.</terminal-line>
    <terminal-line>Counting objects: 100% (5/5), done.</terminal-line>
    <terminal-line>Delta compression using up to 8 threads</terminal-line>
    <terminal-line>Compressing objects: 100% (3/3), done.</terminal-line>
    <terminal-line>Writing objects: 100% (3/3), 565 bytes | 565.00 KiB/s, done.</terminal-line>
    <terminal-line>Total 3 (delta 2), reused 0 (delta 0), pack-reused 0</terminal-line>
    <terminal-line>remote: Resolving deltas: 100% (2/2), completed with 2 local objects.</terminal-line>
    <terminal-line>remote:</terminal-line>
    <terminal-line>remote: Create a pull request for 'update_mom5_dev_build' on GitHub by visiting:</terminal-line>
    <terminal-line class="keep-blanks">remote:      https://github.com/ACCESS-NRI/ACCESS-OM2/pull/new/update_mom5_dev_build</terminal-line>
    <terminal-line>remote:</terminal-line>
    <terminal-line>To https://github.com/ACCESS-NRI/ACCESS-OM2.git</terminal-line>
    <terminal-line class="keep-blanks"> * [new branch]      update_mom5_dev_build -> update_mom5_dev_build</terminal-line>
    <terminal-line>branch 'update_mom5_dev_build' set up to track 'origin/update_mom5_dev_build'.</terminal-line>
</terminal-window>

#### 3. Open a PR
To trigger a prerelease build, [open a PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with the `main` branch of the model deployment repository as the *base*. This will start a model build attempt by [GitHub's CI/CD](https://github.com/resources/articles/devops/ci-cd) infrastructure. As a result, a comment is added by `github-actions[bot]` saying that the build is deploying.<br>
Once the deployment is [successful](#successful-deployment), you will be able to access the prerelease on the listed HPC systems by following the instructions specified in the comment's _Details and usage instructions_.

There are three main _statuses_ for a deployment that can be identified by looking at the [GitHub Environment dialog box](https://github.com/ACCESS-NRI/ACCESS-OM2/pull/94#:~:text=Show%20environments) in the related PR:

- **Successful**<br>
  A successful deployment is identified by a green (_Active_ deployment) or white (_Inactive_ deployment) icon, with the _Active_ one being the most recent deployment within the repository.<br>
  If a deployment is successful, it can be accessed on HPC systems.<br>
  ![Active deployment](/assets/create_a_prerelease/active_deployment.png){: style="max-width: 650px;" class="example-img" loading="lazy"}
  ![Inactive deployment](/assets/create_a_prerelease/inactive_deployment.png){: style="max-width: 650px;" class="example-img" loading="lazy"}
  {: #successful-deployment }

- **In Progress**<br>
  The deployment is still ongoing. It will soon become [successful](#successful-deployment) or [fail](#failed-deployment).<br>
  ![In progress deployment](/assets/create_a_prerelease/in_progress_deployment.png){: style="max-width: 650px;" class="example-img" loading="lazy"}
  {: #in-progress-deployment }

- **Failed**<br>
  The deployment failed and the CI/CD log can be viewed by clicking on [Show environments](https://github.com/ACCESS-NRI/ACCESS-OM2/pull/94#:~:text=Show%20environments) in the GitHub Environment dialog box.<br>
  ![Failed deployment](/assets/create_a_prerelease/failed_deployment.png){: style="max-width: 650px;" class="example-img" loading="lazy"}
  {: #failed-deployment }

If we open a PR to the [ACCESS-OM2 deployment repository][om2 repo] with our `update_mom5_dev_build` branch as the *base*, we will get a [comment](https://github.com/ACCESS-NRI/ACCESS-OM2/pull/94#issuecomment-2594604585). Once deployed, the prerelease build can be accessed through the module `access-om2/pr94-1`:
![GitHub bot comment](/assets/create_a_prerelease/comment.png){: class="example-img"}

!!! tip
    If further changes are required within the same PR, additional commits can be pushed onto the feature branch to create more prerelease builds. This does not remove earlier prerelease builds, allowing concurrent testing of multiple different builds.<br>
    For example, adding an additional commit to the `update_mom5_dev_build` branch (while its PR is open) will trigger another prerelease build and allow the use of the module `access-om2/pr94-2`, once deployed.

#### 4. Merge or close the PR
If the PR gets merged, an official ACCESS-NRI release build of the given model will be created, along with an associated GitHub Release.

!!! warning
    When a PR is closed (this includes merged PRs), regardless if it was merged or not, all the related prereleases deployments get removed.<br>
    You can retrieve a single prerelease build by [creating a _Spack_ environment](https://spack.readthedocs.io/en/latest/environments.html#creating-a-managed-environment) using the `spack.yaml`/`spack.lock` artifact related to the specific commit.

## Draft vs non-draft PR
The prerelease build workflow used to [trigger model prereleases](#trigger-model-prerelease-and-release-build-deployments) differs depending on whether the open PR is a _draft_ or a _regular_ PR.
The differences are summarized in the table below:

|**Type**|**Used for**|**CI Checks**|
|---|---|---|
|Regular PR|Changes to be incorporated into the default branch as a Release.|The full range of CI checks, including conformance to our restricted `spack.yaml` syntax.|
|Draft PR|Changes that are not intended for a Release, but instead being used for testing.|Minimal CI Checks, only validating that the model name and version is formatted correctly.|


## Comment Commands

Another way to trigger the CI/CD pipeline is by commenting on a model deployment repository's open PR with a specific _Comment Command_.<br>
This will trigger the CI/CD pipeline and perform certain actions, depending on the specific _Comment Command_.

!!! info
    All _Comment Commands_ must be at the beginning of the comment, without any leading spaces.

The following _Comment Commands_ are available in all model deployment repositories:

#### !bump
!!! info
    Requires the commenter to have write permissions within the repository.

##### Usage { .no-toc }

```
!bump [major|minor]
```

##### Description { .no-toc }

Convenience function that automatically bumps the overall model version in the `spack.yaml` file  and commits the result to the PR branch.<br>
The overall model version is formatted as `YEAR.MONTH.MINOR`.<br>
`!bump major` bumps the model version to the next major version, formatted as `YEAR.MONTH.0`, where `YEAR` and `MONTH` correspond to the current year and month when the comment is issued.<br>
`!bump minor` bumps the model version to the next minor version, formatted as `YEAR.MONTH.(MINOR+1)`. Here `YEAR`, `MONTH` and `MINOR` are the same as the previous version.

##### Example { .no-toc }

For example, if in Jan 2025 we commented with `!bump major` on an open PR that has its overall model version set to `git.2024.06.2`, the overall model version would be bumped to `git.2025.01.0`.<br>
If, however, we commented the PR with `!bump minor`, the overall model version would be bumped to `git.2024.06.3` regardless of the comment date.

#### !redeploy
!!! info
    Requires the commenter to have write permissions within the repository.

##### Usage { .no-toc }

```
!redeploy
```

##### Description { .no-toc }

Convenience function that triggers a new independent deployment of the `HEAD` of the model deployment repository PR branch.

This is used to trigger a new deployment when a transient error with the prerelease build process occurs (e.g., _Gadi_ is down).

## Backporting Bugfixes

The default branch of a model deployment repository usually reflects the most up-to-date changes to the model. Hence, it is always at the same level or ahead of the model's latest major release.<br>
However, it is also essential to provide a way to apply bug fixes to earlier major versions of the model. This is where dedicated `backport/YEAR.MONTH` branches come into play, allowing bug fixes to be incorporated into previous versions of the model.

For example, let's say there is a bug fix that needs to be incorporated to the [ACCESS-OM2 `2023.11.23` release](https://github.com/ACCESS-NRI/ACCESS-OM2/tree/2023.11.23).<br>
To do so, a developer should:

1. Create a `backport/2023.11` branch (if it doesn't already exist) from the `2023.11.23` tag:
    ```
    git checkout -b backport/2023.11 2023.11.23
    ```
    <terminal-window>
        <terminal-line data="input" directory="ACCESS-OM2">git checkout -b backport/2023.11 2023.11.23</terminal-line>
        <terminal-line>Switched to a new branch 'backport/2023.11'</terminal-line>
    </terminal-window>
2. Apply the bug fixes, commit and push the changes:
    ```
    git commit -am "Bug fix."
    git push --set-upstream origin backport/2023.11
    ```
    <terminal-window>
    <terminal-line data="input" directory="ACCESS-OM2">git commit -am "Bug fix."</terminal-line>
    <terminal-line>[backport/2023.11 cac60f0] Bug fix.</terminal-line>
    <terminal-line class="keep-blanks"> 1 file changed, 2 insertions(+), 1 deletions(-)</terminal-line>
    <terminal-line data="input" directory="ACCESS-OM2">git push --set-upstream origin backport/2023.11</terminal-line>
    <terminal-line>Enumerating objects: 5, done.</terminal-line>
    <terminal-line>Counting objects: 100% (5/5), done.</terminal-line>
    <terminal-line>Delta compression using up to 8 threads</terminal-line>
    <terminal-line>Compressing objects: 100% (3/3), done.</terminal-line>
    <terminal-line>Writing objects: 100% (3/3), 565 bytes | 565.00 KiB/s, done.</terminal-line>
    <terminal-line>Total 3 (delta 2), reused 0 (delta 0), pack-reused 0</terminal-line>
    <terminal-line>remote: Resolving deltas: 100% (2/2), completed with 2 local objects.</terminal-line>
    <terminal-line>remote:</terminal-line>
    <terminal-line>remote: Create a pull request for 'backport/2023.11' on GitHub by visiting:</terminal-line>
    <terminal-line class="keep-blanks">remote:      https://github.com/ACCESS-NRI/ACCESS-OM2/pull/new/backport/2023.11</terminal-line>
    <terminal-line>remote:</terminal-line>
    <terminal-line>To https://github.com/ACCESS-NRI/ACCESS-OM2.git</terminal-line>
    <terminal-line class="keep-blanks"> * [new branch]      backport/2023.11 -> backport/2023.11</terminal-line>
    <terminal-line>branch 'backport/2023.11' set up to track 'origin/backport/2023.11'.</terminal-line>
    </terminal-window>
3. Open a PR from the `backport/2023.11` branch with the fixes.<br>
   When the PR is merged, a release tagged as `2023.11.24` will be created.
