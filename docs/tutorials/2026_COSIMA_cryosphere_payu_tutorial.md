# Payu tutorial - COSIMA Cryosphere Workshop 2026

<div class="text-card-group" markdown>
[:fontawesome-brands-github:{: class="twemoji icon-before-text"} ACCESS-OM2 configurations](https://github.com/ACCESS-NRI/access-om2-configs){: class="text-card"}
[:material-book-open-variant:{: class="twemoji icon-before-text"} Payu documentation](https://payu.readthedocs.io/en/stable/){: class="text-card"}
[![Hive](/assets/ACCESS_icon_HIVE.png){: class="icon-before-text"} ACCESS-Hive Forum](https://forum.access-hive.org.au/){: class="text-card"}
</div>

This page contains the hands-on exercises for the payu training session. Each step lists the task, questions to think about, and the commands you'll need. The answers are hidden in collapsible boxes, so try each step yourself before you open them.

## The problem

!!! abstract "Exercise overview"
    **Goal:** Use payu to run an experiment, get comfortable with the payu workflow, and try out some of its newer features.

    **Example experiment:** Study the impact of a higher ocean-to-ice heat transfer coefficient (χ<sub>o</sub>).

    **Model:** 1-degree ACCESS-OM2 model under inter-annual forcing (repository URL: [OM2 model configuration](https://github.com/ACCESS-NRI/access-om2-configs/), remote branch name: `release-1deg_jra55_iaf`).


## Getting help

??? info "Where to get help during the exercises"

    - `payu --help`
    - `payu <subcommand> -h`, for example `payu run -h`
    - [Payu documentation](https://payu.readthedocs.io/en/stable/)
    - [ACCESS-Hive Forum](https://forum.access-hive.org.au/): please tag your post with **payu**.

??? info "Checking your experiment history with `git log`"

    Run `git log` (or `git show <commit_hash>`) in your control directory to:

    - check run commits
    - check metadata updates
    - check manifests and configuration updates

## Before you start: load payu

Log onto Gadi and load the payu module:

```
module use /g/data/vk83/modules/
module load payu
```

## Step 1: Clone the experiment

Clone the ACCESS-OM2 configuration. Please try the `payu clone` **interactive mode**.

!!! question
    For an experiment with a high χ<sub>o</sub> = 0.0065, what is a good **control directory** name and **local branch** name?

**Useful commands:**

```
payu clone
```

- Starts the interactive mode.
- A flowchart is available in the payu documentation under [Usage > Clone experiment](https://payu.readthedocs.io/en/stable/usage.html#payu-clone-interactive-mode), or enter `?` in the wizard.
- Control directory and branch naming guidance is available in the payu documentation under [Usage](https://payu.readthedocs.io/en/stable/usage.html#control-directory-and-branch-naming-guidance).

The complete (non-interactive) command is:

```
payu clone -B source_branch -b new_branch URL local_dir
```

<!-- FLAG: The cheat sheet uses the URL https://github.com/ACCESS-NRI/access-om2-configs.git, but the answer below uses https://github.com/ACCESS-NRI/accessom2-configs.git. Please confirm which is correct. -->

??? success "Answer"

    In this example, a recommended control directory name is `om2_1deg_iaf`, and the local branch name is `chio65`.

    <terminal-window>
        <terminal-line data="input">payu clone</terminal-line>
        <terminal-line><span class="payu-yellow">Welcome to the Payu Clone Wizard!</span></terminal-line>
        <terminal-line><span class="payu-yellow">Press 'Ctrl+C' at any time to exit.</span></terminal-line>
        <terminal-line><span class="payu-yellow">Enter '?' during any prompt to view the flowchart.</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Please enter URL of the repository, or local path of the configuration to clone:</span> (e.g., https://github.com/payu-org/bowl1.git, or /path/to/local/experiment; 'Tab' to browse, '/' to enter folder) <span class="payu-dark-yellow">https://github.com/ACCESS-NRI/access-om2-configs.git</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Payu will clone the repo based on:</span> <span class="payu-dark-yellow">An existing branch</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Name of the branch to clone ('Tab' to browse all branches):</span> <span class="payu-dark-yellow">release-1deg_jra55_iaf</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Please name your local control directory:</span> <span class="payu-dark-yellow">om2_1deg_iaf</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Is this a new experiment?</span> (If yes, payu will create a new branch.) <span class="payu-dark-yellow">Yes, create a new UUID as a new experiment</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Please name your new branch:</span> (Note: this won't be shared to the online repository automatically) <span class="payu-dark-yellow">chio65</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Do you want to specify a custom restart path?</span> (If no, the default restart/initial conditions will be used.) <span class="payu-dark-yellow">No</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Do you want to override the shortpath?</span> (Default is '/scratch/nf33') <span class="payu-dark-yellow">Yes</span></terminal-line>
        <terminal-line><span class="spack-cyan">&gt;&gt;</span> <span class="payu-red">Please enter the new shortpath you want to use:</span> <span class="payu-dark-yellow">/scratch/nf33</span></terminal-line>
        <terminal-line data="input">cd om2_1deg_iaf/</terminal-line>
        <terminal-line data="input">ls</terminal-line>
        <terminal-line>accessom2.nml  atmosphere  doc  LICENSE  metadata.yaml  ocean  testing</terminal-line>
        <terminal-line>archive  config.yaml  ice  manifests  namcouple  README.md  tools</terminal-line>
    </terminal-window>

## Step 2: Modify the parameters

Set χ<sub>o</sub> to 0.0065.

**Hint:** χ<sub>o</sub> is under `&thermo_nml` in `ice/cice_in.nml`.


??? success "Answer"

    ```
    vi ice/cice_in.nml
    ```

    Change `chio` to `0.0065`. Feel free to use any other editor that you prefer.

## Step 3: Configure the experiment time

Update the restart period to **1 month** in `accessom2.nml`.

??? success "Answer"

    ```
    vi accessom2.nml
    ```

    Change the restart period to:

    ```
    restart_period = 0, 1, 0
    ```

## Step 4: Configure the output syncing

Configure `sync: base_path` in `config.yaml`, for example `/g/data/nf33/$USER/…`.

??? success "Answer"

    ```
    vi config.yaml
    ```

    Update the `sync` section to:

    ```yaml
    sync:
      enable: true
      base_path: /g/data/nf33/$USER/om2_sync_archive
    ```

## Step 5: Run the experiment

!!! question
    - How long did your experiment queue for?
    - What is the experiment UUID?
    - Where is the archive stored?
    - Where is the output synced?

**Useful commands:**

```
cd control_directory
payu setup
```

- `payu setup --new-uuid` creates a new experiment UUID and a new archive directory. It meanwhile updates the archive symlink to the new archive.

```
payu sweep
```

- What error message will you get if you skip the sweep?

```
payu run
```

- `payu run -n N` schedules an experiment for N successive runs.

```
payu status
```

- For a running job, this helps you monitor the current experiment time.
- For a finished job, this helps you check the exit status.
- `payu status --update` updates the current queue time. Note that it calls `qstat`, so it's recommended to run it only once per model run.
- `payu status --paths` shows the experiment paths.

```
less metadata.yaml
```

- Check the experiment name, UUID, parent experiment, etc. Press `q` to exit.

<!-- FLAG: The cheat sheet asks "what error message will I get if I skip payu sweep?", but the answers PDF doesn't cover payu setup or payu sweep, so there is no answer for that question below. -->

??? success "Answer"

    Submit the run:

    <terminal-window>
        <terminal-line data="input">payu run</terminal-line>
        <terminal-line>laboratory path: /scratch/nf33/xxx/access-om2</terminal-line>
        <terminal-line>binary path: /scratch/nf33/xxx/access-om2/bin</terminal-line>
        <terminal-line>input path: /scratch/nf33/xxx/access-om2/input</terminal-line>
        <terminal-line>work path: /scratch/nf33/xxx/access-om2/work</terminal-line>
        <terminal-line>archive path: /scratch/nf33/xxx/access-om2/archive</terminal-line>
        <terminal-line>Found experiment archive: /scratch/nf33/xxx/access-om2/archive/om2-1deg-iaf-chio65-uu00id</terminal-line>
        <terminal-line>payu: warning: Job request includes 47 unused CPUs.</terminal-line>
        <terminal-line>payu: warning: CPU request increased from 241 to 288</terminal-line>
        <terminal-line>Loading input manifest: manifests/input.yaml</terminal-line>
        <terminal-line>Loading restart manifest: manifests/restart.yaml</terminal-line>
        <terminal-line>Loading exe manifest: manifests/exe.yaml</terminal-line>
        <terminal-line>payu: Found modules in /opt/Modules/v4.3.0</terminal-line>
        <terminal-line>——- Job submitted ——-</terminal-line>
        <terminal-line>Submitted command: qsub -q normal -P nf33 -l walltime=3:00:00 -l ncpus=288 -l mem=1000GB -N 1deg_jra55_iaf …/bin/payu-run</terminal-line>
        <terminal-line>Job ID: 10000001.gadi-pbs</terminal-line>
    </terminal-window>

    Check the queue time with `payu status --update` (see **Current** or **Total Queue Time**):

    <terminal-window>
        <terminal-line data="input">payu status --update</terminal-line>
        <terminal-line>payu: Found modules in /opt/Modules/v4.3.0</terminal-line>
        <terminal-line>========================================</terminal-line>
        <terminal-line>Run: 0</terminal-line>
        <terminal-line>  ------------- Run Info -------------</terminal-line>
        <terminal-line>  Job ID: 10000001.gadi-pbs</terminal-line>
        <terminal-line>  Run ID: exxxxxxx5</terminal-line>
        <terminal-line>  Stage: model-run</terminal-line>
        <terminal-line>  <span class="payu-dark-yellow">Total Queue Time: 0h 0m 42s</span></terminal-line>
        <terminal-line>  Current Expt Time: 1958-01-09T21:00:00</terminal-line>
        <terminal-line>  Job File: /scratch/nf33/xxxx/access-om2/archive/om2-1deg-iaf-chio65-uu00id/payu_jobs/0/run/10000001.gadipbs.json</terminal-line>
        <terminal-line>========================================</terminal-line>
    </terminal-window>

    Check the UUID, archive and sync locations with `payu status --paths` (see **Experiment UUID**, **Archive Directory** and **Sync Destination**):

    <!-- FLAG: The answers PDF shows "payu status --paths" (with a space) and labels the control directory line as "Chio65 Directory". These have been kept as in the PDF; they likely should be "payu status --paths" and "Control Directory". -->

    <terminal-window>
        <terminal-line data="input">payu status -- paths</terminal-line>
        <terminal-line>========================================</terminal-line>
        <terminal-line>Experiment Paths:</terminal-line>
        <terminal-line>  <span class="payu-dark-yellow">Experiment UUID: uu00id-7fa7-41d8-bee6-bxxxx1</span></terminal-line>
        <terminal-line>  Experiment Name: om2-1deg-iaf-chio65-uu00id</terminal-line>
        <terminal-line>  Chio65 Directory: /home/189/xxx/om2-1deg-iaf</terminal-line>
        <terminal-line>      (Where model configuration is stored)</terminal-line>
        <terminal-line>  Laboratory Path: /scratch/nf33/xxx/access-om2</terminal-line>
        <terminal-line>      (Where model's laboratory is stored)</terminal-line>
        <terminal-line>  Work Directory: /scratch/nf33/xxx/access-om2/work/om2-1deg-iaf-chio65-uu00id</terminal-line>
        <terminal-line>      (Temporary directory for experiment runs)</terminal-line>
        <terminal-line>  <span class="payu-dark-yellow">Archive Directory: /scratch/nf33/xxx/access-om2/archive/om2-1deg-iaf-chio65-uu00id</span></terminal-line>
        <terminal-line>      (Where all experiment outputs are stored)</terminal-line>
        <terminal-line>  <span class="payu-dark-yellow">Sync Destination: /g/data/nf33/xxx/somewhere/om2-1deg-iaf-chio65-uu00id</span></terminal-line>
        <terminal-line>      (Remote directory to sync outputs to)</terminal-line>
        <terminal-line>========================================</terminal-line>
    </terminal-window>

    Then wait until the run completes.

## Step 6: Continue the experiment with a higher χ<sub>o</sub>

Continue the experiment for another month with a higher χ<sub>o</sub> = 0.007.

!!! question
    How can you create a new branch based on the latest output?

**Useful commands:**

```
payu checkout -b newB -r path_to_restart source_commit
```

- Creates a new branch called `newB` that is branched off from `source_commit`, and assigns its restart to `path_to_restart`.

Other useful commands:

```
payu checkout -b new_branch source_commit
payu checkout -b new_branch source_branch
```

<!-- FLAG: In the output below the restart and old archive paths refer to "om2-1deg-iaf-control-uu00id" and the payu branch output lists a "control" branch, whereas Steps 1 and 5 use the branch "chio65" (om2-1deg-iaf-chio65-uu00id). Kept as in the PDF. -->

??? success "Answer"

    Use the archive directory from `payu status --paths` and point the restart at the `output000` folder of the first run:

    <terminal-window>
        <terminal-line data="input">payu checkout -b chio7 -r /archive/dir/found/in/payu/status/paths/output000/ chio65</terminal-line>
        <terminal-line>Created and checked out new branch: chio7</terminal-line>
        <terminal-line>laboratory path: /scratch/nf33/xxxx/access-om2</terminal-line>
        <terminal-line>binary path: /scratch/nf33/xxxx/access-om2/bin</terminal-line>
        <terminal-line>input path: /scratch/nf33/xxxx/access-om2/input</terminal-line>
        <terminal-line>work path: /scratch/nf33/xxxx/access-om2/work</terminal-line>
        <terminal-line>archive path: /scratch/nf33/xxxx/access-om2/archive</terminal-line>
        <terminal-line>Updated metadata. Experiment UUID: newuuid-9c3f-43b7-b3d2-3xxxxd</terminal-line>
        <terminal-line>Added 'restart: /scratch/nf33/xxxx/access-om2/archive/om2-1deg-iaf-control-uu00id/output000' to configuration file: config.yaml</terminal-line>
        <terminal-line>Removed archive symlink to /scratch/nf33/xxxx/access-om2/archive/om2-1deg-iaf-control-uu00id</terminal-line>
        <terminal-line>Added archive symlink to /scratch/nf33/xxxx/access-om2/archive/om2-1deg-iaf-chio7-newuuid</terminal-line>
    </terminal-window>

    Check your branches and their experiment UUIDs with `payu branch`:

    <terminal-window>
        <terminal-line data="input">payu branch</terminal-line>
        <terminal-line><span class="payu-dark-yellow">* Current Branch: chio7</span></terminal-line>
        <terminal-line>    experiment_uuid: newuuid-9c3f-43b7-b3d2-3xxxxd</terminal-line>
        <terminal-line>Branch: control</terminal-line>
        <terminal-line>    experiment_uuid: uu00id-7fa7-41d8-bee6-b942415c1bd1</terminal-line>
        <terminal-line>Branch: release-1deg_jra55_iaf</terminal-line>
        <terminal-line>    No UUID in metadata file</terminal-line>
    </terminal-window>
