!!! danger
    This page is tailored to experienced users and collaborators developing ACCESS models.<br>
    This step is *not* required if you *only* want to run a model. If you are looking for information on how to run a model, refer to the [Run a Model](/models/run_a_model) section.

!!! tip
    **13/02/2026:** ACCESS-NRI has migrated from *Spack* `v0.22` to *Spack* `v1.1`. If you previously followed these instructions to set up *Spack* `v0.22`, you will need to repeat the setup process below to install *Spack* `v1.1`.

# Set up Spack for building ACCESS models

[Spack](https://spack.io/about/) is a build-from-source package manager, specifically designed to simplify the installation of scientific software on supercomputers.

To use _Spack_, please familiarise yourself with the [Basic Usage instructions](https://spack.readthedocs.io/en/latest/basic_usage.html) and [Environments](https://spack.readthedocs.io/en/latest/environments.html).

We also recommend that you refer to the [Spack 101 Tutorial](https://spack-tutorial.readthedocs.io/en/latest/).

Installing _Spack_ allows users to build ACCESS models directly from the source code, swap model components, and carry out development testing that involves modifying the source code.<br>
After installing _Spack_, refer to the [Build a model](https://docs.access-hive.org.au/models/build_a_model/build_source_code/) page for the next steps.

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
    The steps in this section only need to be completed once.

### Create a directory for Spack

Create a directory on the filesystem where _Spack_ will be installed (e.g. `/g/data/$PROJECT/$USER/spack/1.1`). Use the `/g/data` filesystem if you wish to run the binaries on the compute nodes.

```
mkdir -p /g/data/$PROJECT/$USER/spack/1.1
cd /g/data/$PROJECT/$USER/spack/1.1
```

### Clone the relevant git repositories

!!! info
    ACCESS-NRI maintains a [fork of Spack](https://github.com/ACCESS-NRI/spack) to enable back-porting fixes from more recent spack versions. This fork is the one used in these instructions.

```
git clone https://github.com/ACCESS-NRI/spack.git --branch access/releases/v1.1
git clone https://github.com/ACCESS-NRI/spack-config.git --branch main
```

!!! success
    Your _Spack_ setup is complete!

For instructions on how to build an ACCESS model using _Spack_, refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code).

## Enable Spack

!!! warning
    For this step, it is recommended to use a new login [_Bash_ shell environment](#bash_shell) to avoid conflicting environment variables. 
    Additionally, this step must be repeated for every new login or new shell session.

```
cd /g/data/$PROJECT/$USER/spack/1.1
module purge
. spack/share/spack/setup-env.sh
```

!!! warning
    There is a space between the `.` and the path to the file, as we are sourcing the file.

## Test Spack (OPTIONAL)

To test that your Spack installation works as expected, we will create an `ACCESS-TEST` environment and build the relevant packages (this will take approximately 30 minutes). Then, we will uninstall all the packages and remove the environment.


### Clone a Spack environment

```
git clone https://github.com/ACCESS-NRI/ACCESS-TEST.git
```

### Activate the environment
Activate the `ACCESS-TEST` _Spack_ environment by running:
```
spack env activate -p ./ACCESS-TEST
```
<terminal-window>
    <terminal-line data="input">spack env activate -p ./ACCESS-TEST</terminal-line>
    <terminal-line data="input" directory="[ACCESS-TEST]" class="spack" lineDelay=0></terminal-line>
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
    <terminal-line lineDelay=500><span class="spack-indigo">\==></span> In environment &lt;/path/to/environment/ACCESS-TEST&gt;</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 1 root specs</terminal-line>
    <terminal-line>-- <span class="spack-pink">no arch</span> / <span class="spack-green">no compilers</span> ---------------------------------------</terminal-line>
    <terminal-line><span class="spack-grey keep-blanks"> - </span> access-test</terminal-line>
    <terminal-line></terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 0 installed packages</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 0 concretized packages to be installed (show with `spack find -c`)</terminal-line>
    <!-- spack concretize -->
    <terminal-line lineDelay=600 directory="[test]" class="spack" data="input">spack concretize -f --fresh</terminal-line>
    <terminal-line>...</terminal-line>
    <terminal-line lineDelay=2000><span class="spack-indigo">\==></span> Concretized 1 spec:</terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   &lt;spec-id&gt; </span> access-test<span class="spack-cyan">@&lt;version-info&gt;</span><span class="spack-indigo">&lt;build-info&gt;</span> <span class="spack-pink">&lt;architecture-info&gt;</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   &lt;spec-id&gt;    </span> ^&lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span><span class="spack-indigo">&lt;build-info&gt;</span> <span class="spack-pink">&lt;architecture-info&gt;</span>
    </terminal-line>
    <terminal-line>...</terminal-line>
    <terminal-line>
        <span class="spack-grey keep-blanks"> -   &lt;spec-id&gt;        </span> ^&lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span><span class="spack-indigo">&lt;build-info&gt;</span> <span class="spack-pink">&lt;architecture-info&gt;</span>
    </terminal-line>
    <!-- spack install -->
    <terminal-line directory="[test]" class="spack" lineDelay=2000 data="input">
        spack install
    </terminal-line>
    <terminal-line>
        ...
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">&lt;spack-package&gt;&lt;hash&gt;</span> <span class="spack-highlighted">[1/&lt;N&gt;]</span>
    </terminal-line>
    <terminal-line>
        ...
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">&lt;spack-package&gt;&lt;hash&gt;</span> <span class="spack-highlighted">[2/&lt;N&gt;]</span>
    </terminal-line>
    <terminal-line>
        ...
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">access-test-&lt;version-info&gt;&lt;hash&gt;</span> <span class="spack-highlighted">[&lt;N&gt;/&lt;N&gt;]</span>
    </terminal-line>
    <terminal-line>
        ...
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> access-test: Successfully installed access-test-&lt;version-info&gt;&lt;hash&gt;
    </terminal-line>
    <terminal-line>
        ...
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> Updating view at &lt;/path/to/ACCESS-TEST/.spack-env/view&gt;
    </terminal-line>
</terminal-window>

!!! info
    The animation above is a generalised example of the expected output, shortened and modified for clarity. Your actual output might vary.


### Check installed packages

```
spack find
```

<terminal-window lineDelay=0>
    <!-- spack find -->
    <terminal-line directory="[test]" class="spack" data="input" lineDelay=600>spack find</terminal-line>
    <terminal-line lineDelay=500><span class="spack-indigo">\==></span> In environment &lt;/path/to/environment/ACCESS-TEST&gt;</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 1 root specs</terminal-line>
    <terminal-line>-- <span class="spack-pink">no arch</span> / <span class="spack-green">no compilers</span> ---------------------------------------</terminal-line>
    <terminal-line><span class="spack-green"> [+] </span> access-test</terminal-line>
    <terminal-line></terminal-line>
    <terminal-line>-- <span class="spack-pink">&lt;architecture-info&gt;</span> / <span class="spack-green">&lt;compilers-info&gt;</span> -----------------------</terminal-line>
    <terminal-line class="ls-output-format">
        &lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span>
        &lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span>
    </terminal-line>
    <terminal-line></terminal-line>
    <terminal-line>-- <span class="spack-pink">&lt;architecture-info&gt;</span> / <span class="spack-green">&lt;compilers-info&gt;</span> -----------------------</terminal-line>
    <terminal-line class="ls-output-format">
        &lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span>
        &lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span>
        &lt;spack-package&gt;<span class="spack-cyan">@&lt;version-info&gt;</span>
    </terminal-line>
    <terminal-line>...</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> &lt;N&gt; installed packages</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 0 concretized packages to be installed (show with `spack find -c`)</terminal-line>
</terminal-window>

!!! info
    The animation above is a generalised example of the expected output, shortened and modified for clarity. Your actual output might vary.

### Cleanup
```
spack uninstall --remove --all
spack env deactivate
rm -rf ACCESS-TEST
```

## Update Spack on Gadi

Keep your _Spack_ instance up-to-date by doing the following:

```
cd /g/data/$PROJECT/$USER/spack/1.1
find spack/etc/spack -type l -name '*.yaml' -exec rm {} \;
git -C spack fetch --all -Pp
git -C spack switch access/releases/v1.1
git -C spack reset --hard origin/access/releases/v1.1
git -C spack-config pull
. spack/share/spack/setup-env.sh
spack repo update
```

<custom-references>
- [https://spack.readthedocs.io/en/latest/](https://spack.readthedocs.io/en/latest/)
</custom-references>
