!!! danger
    This page is tailored to experienced users and collaborators developing ACCESS models.<br>
    This step is *not* required if you *only* want to run a model. If you are looking for information on how to run a model, refer to the [Run a Model](/models/run_a_model) section.

# Set up Spack for building ACCESS models

[Spack](https://spack.io/about/) is a build-from-source package manager, specifically designed to simplify the installation of scientific software on supercomputers.

To use _Spack_, please familiarise yourself with the [Basic Usage instructions](https://spack.readthedocs.io/en/latest/basic_usage.html) and [Environments](https://spack.readthedocs.io/en/latest/environments.html).

We also recommend that you refer to the [Spack 101 Tutorial](https://spack-tutorial.readthedocs.io/en/latest/).

## Prerequisites
- **NCI Account**<br> 
    These instructions are tailored specifically for _Gadi_. To use _Spack_ on _Gadi_, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).
- **_Bash_ shell**<br>
    The following instructions must be run in a _Bash_ shell, which is the default shell on _Gadi_.
    To check if you are using _Bash_, run:
    ```
    echo "$BASH_VERSION"
    ```
    If you see output (i.e. the _Bash_ version), you are already in a Bash shell. If there is no output, start a _Bash_ shell by running:
    ```
    bash
    ```
{: #bash_shell }

## Set up Spack on Gadi

!!! tip
    The steps in this section only need to be done once.

### Create a directory for Spack

Create a directory on the filesystem where _Spack_ will be installed (e.g. `/g/data/$PROJECT/$USER/spack/0.22`). Use the `/g/data` filesystem if you wish to run the binaries on the compute nodes.

```
mkdir -p /g/data/$PROJECT/$USER/spack/0.22
cd /g/data/$PROJECT/$USER/spack/0.22
```

### Clone the relevant git repositories

!!! info
    ACCESS-NRI maintains a [fork of Spack](https://github.com/ACCESS-NRI/spack) to enable back-porting fixes from more recent spack versions. This fork is the one used in these instructions.

```
git clone -c feature.manyFiles=true https://github.com/ACCESS-NRI/spack.git --branch releases/v0.22
git clone https://github.com/ACCESS-NRI/spack-packages.git --branch main
git clone https://github.com/ACCESS-NRI/spack-config.git --branch main
```

### Link Spack configuration files to the Spack instance

```
ln -s -r -v spack-config/v0.22/gadi/* spack/etc/spack/
```

!!! success
    Your _Spack_ setup is complete!

For instructions on how to build an ACCESS model using _Spack_, refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code).

## Enable Spack

!!! warning
    For this step, it is recommended to use a new login [_Bash_ shell environment](#bash_shell) to avoid conflicting environment variables. 
    Additionally, this step must be repeated for every new login or new shell session.

```
cd /g/data/$PROJECT/$USER/spack/0.22
module purge
. spack-config/spack-enable.bash
```

!!! warning
    There is a space between the `.` and the path to the file, as we are sourcing the file.

## Test Spack (OPTIONAL)

To test that your Spack installation works as expected, we will create an `ACCESS-TEST` environment and build the relevant packages (this will take approximately 30 minutes). Then, we will uninstall all the packages and remove the environment.


### Create a Spack managed environment

```
git clone https://github.com/ACCESS-NRI/ACCESS-TEST.git
spack env create test ACCESS-TEST/spack.yaml
```

<terminal-window>
  <terminal-line data="input">git clone https://github.com/ACCESS-NRI/ACCESS-TEST.git</terminal-line>
    <terminal-line>Cloning into 'ACCESS-TEST'...</terminal-line>
    <terminal-line>remote: Enumerating objects: 33, done.</terminal-line>
    <terminal-line>remote: Counting objects: 100% (33/33), done.</terminal-line>
    <terminal-line>remote: Compressing objects: 100% (20/20), done.</terminal-line>
    <terminal-line>remote: Total 33 (delta 12), reused 27 (delta 9), pack-reused 0 (from 0)</terminal-line>
    <terminal-line>Receiving objects: 100% (33/33), 15.92 KiB | 1.06 MiB/s, done.</terminal-line>
    <terminal-line>Resolving deltas: 100% (12/12), done.</terminal-line>
  <terminal-line data="input">spack env create test ACCESS-TEST/spack.yaml</terminal-line>
  <terminal-line><span class="spack-indigo bold">\==></span> Created environment <span class="spack-cyan">test</span> in: <span class="spack-cyan">/g/data/$PROJECT/$USER/spack/0.22/environments/test</span></terminal-line>
  <terminal-line><span class="spack-indigo bold">\==></span> Activate with: <span class="spack-cyan">spack env -p activate test</span></terminal-line>
</terminal-window>

### Activate the environment
Activate the `test` _Spack_ environment by running:
```
spack env activate -p test
```
<terminal-window>
    <terminal-line data="input">spack env activate -p test</terminal-line>
    <terminal-line data="input" directory="[test]" class="spack" lineDelay=0></terminal-line>
</terminal-window>

### Compile packages

```
spack find
spack concretize -f --fresh
spack install
```

!!! warning
    Some of the commands above might take several minutes to complete.

<terminal-window lineDelay=0>
    <!-- spack find -->
    <terminal-line directory="[test]" class="spack" data="input" lineDelay=600>spack find</terminal-line>
    <terminal-line lineDelay=500><span class="spack-indigo">\==></span> In environment test</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 1 root specs</terminal-line>
    <terminal-line><span class="spack-grey keep-blanks"> - </span> access-test<span class="spack-cyan">@git.2025.04.000=2025.04.000</span></terminal-line>
    <terminal-line></terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 0 installed packages</terminal-line>
    <!-- spack concretize -->
    <terminal-line lineDelay=600 directory="[test]" class="spack" data="input">spack concretize -f --fresh</terminal-line>
    <terminal-line lineDelay=2000><span class="spack-indigo">\==></span> Concretized access-test@git.2025.04.000=2025.04.000</terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   ih4cowp</span> access-test<span class="spack-cyan">@git.2025.04.000=2025.04.000</span><span class="spack-green">%intel@2021.10.0</span><span class="spack-indigo">+mpi build_system=bundle</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   bcixn5z    </span> <span>^access-test-component<span class="spack-cyan">@main</span><span class="spack-green">%intel@2021.10.0</span><span class="spack-indigo">\~ipo+mpi build_system=cmake build_type=Release generator=make</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   rldyvqn        </span> <span>^cmake<span class="spack-cyan">@3.24.2</span><span class="spack-green">%intel@2021.10.0</span><span class="spack-indigo">\~doc+ncurses+ownlibs build_system=generic build_type=Release</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   doeoclg        </span> <span>^gmake<span class="spack-cyan">@4.4.1</span><span class="spack-green">%intel@2021.10.0</span><span class="spack-indigo">\~guile build_system=generic</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   qg5spmh        </span> <span>^openmpi<span class="spack-cyan">@4.1.5</span><span class="spack-green">%intel@2021.10.0</span><span class="spack-indigo">\~atomics\~cuda\~cxx\~cxx_exceptions\~gpfs\~internal-hwloc\~internal-libevent\~internal-pmix\~java\~legacylaunchers\~lustre\~memchecker\~openshmem\~orterunprefix\~romio+rsh\~singularity\~static+vt+wrapper-rpath build_system=autotools fabrics=none romio-filesystem=none schedulers=none</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   5elnsoi    </span> <span>^glibc<span class="spack-cyan">@2.28</span><span class="spack-green">%intel@2021.10.0</span> <span class="spack-indigo">build_system=autotools</span> <span class="spack-pink">arch=linux-rocky8-x86_64</span>
    </terminal-line>
    <terminal-line></terminal-line>
    <terminal-line>
        <span class="spack-indigo">\==></span> Updating view at /g/data/$PROJECT/$USER/spack/0.22/environments/test/.spack-env/view</terminal-line>
    </terminal-line>
    <!-- spack install -->
    <terminal-line directory="[test]" class="spack" lineDelay=2000 data="input">
        spack install
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">glibc-2.28-5elnsoiqgcg5k5zmmwsp33bmnmaa3g5p</span> <span class="spack-highlighted">[1/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/glibc-2.28-5elnsoiqgcg5k5zmmwsp33bmnmaa3g5p
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">cmake-3.24.2-vc4y4c64s55j5u6kp37ciw2hcghuxhhc</span> <span class="spack-highlighted">[2/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/cmake-3.24.2-vc4y4c64s55j5u6kp37ciw2hcghuxhhc
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">openmpi-4.1.5-qg5spmhetxnuvtyi7nuobd3nv7zwnu5f</span> <span class="spack-highlighted">[3/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/openmpi-4.1.5-qg5spmhetxnuvtyi7nuobd3nv7zwnu5f
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">gmake-4.4.1-j6yscmmcn3qws7n35klote7rivw7foa6</span> <span class="spack-highlighted">[4/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/gmake-4.4.1-j6yscmmcn3qws7n35klote7rivw7foa6
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">access-test-component-main-bcixn5z6ou7vlnogzgyy5z23jb4qeunx</span> <span class="spack-highlighted">[5/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/access-test-component-main-bcixn5z6ou7vlnogzgyy5z23jb4qeunx
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">access-test-git.2025.04.000_2025.04.000-ih4cowpiz2kv6tnz4rkualxuly54tizr</span> <span class="spack-highlighted">[6/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/$PROJECT/$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/access-test-git.2025.04.000_2025.04.000-ih4cowpiz2kv6tnz4rkualxuly54tizr
    </terminal-line>
</terminal-window>

!!! info
    The full output has been truncated for brevity.

### Check installed packages

```
spack find
```
<terminal-window lineDelay=0>
    <terminal-line directory="[test]" class="spack" data="input" lineDelay=600>spack find</terminal-line>
    <terminal-line lineDelay=500>
        <span class="spack-indigo">\==></span> In environment test
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo">\==></span> 1 root specs
    </terminal-line>
    <terminal-line>
        <span class="spack-green"> [+] </span> access-test<span class="spack-cyan">@git.2025.04.000=2025.04.000</span>
    </terminal-line>
    <terminal-line></terminal-line>
    <terminal-line>
        <span class="spack-indigo">\==></span> installed packages
    </terminal-line>
    <terminal-line>
        -- <span class="spack-pink">linux-rocky8-x86_64</span> / <span class="spack-green">intel@2021.10.0</span> ------------------------
    </terminal-line>
    <terminal-line class="ls-output-format">
        <span class="spack-highlighted">access-test</span><span class="spack-cyan">@git.2025.04.000=2025.04.000</span> 
        access-test-component<span class="spack-cyan">@main</span> 
        cmake<span class="spack-cyan">@3.24.2</span> 
        glibc<span class="spack-cyan">@2.28</span> 
        gmake<span class="spack-cyan">@4.4.1</span> 
        openmpi@4.1.5<span class="spack-cyan">@1.5.6</span> 
    </terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 6 installed packages</terminal-line>
</terminal-window>

### Cleanup
```
spack uninstall --remove --all
spack env deactivate
spack env rm test
rm -rf ACCESS-TEST
```

## Update Spack on Gadi

Keep your Spack instance up-to-date by doing the following:

```
cd /g/data/$PROJECT/$USER/spack/0.22
git -C spack fetch --all -Pp
git -C spack reset --hard origin/releases/v0.22
git -C spack-config pull
git -C spack-packages pull
```

<custom-references>
- [https://spack.readthedocs.io/en/latest/](https://spack.readthedocs.io/en/latest/)
</custom-references>
