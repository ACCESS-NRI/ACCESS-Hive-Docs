!!! info
    You only need _Spack_ if you intend to _modify and build_ an ACCESS model's source code. To run an existing released model configuration, refer to [Run a Model](/models/run_a_model) instead.

!!! warning
    **20/05/2026:** If you previously set up a personal _Spack_ instance by following the instructions on this page, note that the recommended method for enabling _Spack_ on _Gadi_ has changed. Please review the updated instructions below.

# How to use Spack on Gadi for building ACCESS models

[Spack](https://spack.io/about/) is a build-from-source package manager, specifically designed to simplify the installation of scientific software on supercomputers. _Spack_ allows users to build ACCESS models directly from the source code, swap model components, and carry out development testing that involves modifying the source code.

ACCESS-NRI has installed and configured a shared _Spack_ instance on _Gadi_ so that users do *not* need to create and maintain their own _Spack_ instance.

To use _Spack_, please familiarise yourself with the [essential Spack commands](https://spack.readthedocs.io/en/latest/package_fundamentals.html) used for [Listing Available Packages](https://spack.readthedocs.io/en/latest/package_fundamentals.html#listing-available-packages) and [Seeing Installed Packages](https://spack.readthedocs.io/en/latest/package_fundamentals.html#seeing-installed-packages). Alternatively, follow the instructions in the [Test Spack](#test-spack-optional) section below.

## Prerequisites

- **NCI Account**<br>
    These instructions are tailored specifically for _Gadi_. To use _Spack_ on _Gadi_, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **Membership of the `vk83` project**<br>
    The shared _Spack_ instance is distributed through `/g/data/vk83`. Request membership through [my.nci.org.au](https://my.nci.org.au/mancini/project/vk83).

- **A project with writable `/g/data` and `/scratch` space**<br>
    _Spack_ installs your builds under `/g/data/$PROJECT/$USER/spack/` and stages source code under `/scratch/$PROJECT/$USER/`. Building a full model can consume a lot of storage, so check your quota with `lquota` before starting.

## Enable Spack

Estimated time to complete: 1 minute

!!! warning
    The ACCESS-NRI shared Spack instance is configured to use `/g/data/$PROJECT/$USER/spack/$SPACK_VERSION` for temporary and permanent files. If your default project ID changes, then _Spack_ will not be using the temporary and permanent files created with your previous project ID. This is particularly relevant for _Spack_ workflows run through PBS jobs using multiple projects.

```
module use /g/data/vk83/modules
module load spack
```

## Test Spack (OPTIONAL)

<!--
- concretize
  - 34.28user 3.59system 1:00.02elapsed 63%CPU (0avgtext+0avgdata 1139152maxresident)k
- install
  - 16.80user 41.52system 2:11.29elapsed 44%CPU (0avgtext+0avgdata 74824maxresident)k
- uninstall
  - 2.31user 1.71system 0:09.16elapsed 43%CPU (0avgtext+0avgdata 70972maxresident)k
-->

Estimated time to complete: 5 minutes

!!! info
    When you install a package, _Spack_ first checks whether an identical build already exists in the `upstream`. If it does, that build is reused instead of being recompiled.

To test that _Spack_ works as expected, clone the `ACCESS-TEST` repository and use it as a _Spack_ `independent environment` to install the relevant packages. The _Spack_ environment rules are defined in the `ACCESS-TEST/spack.yaml` file. If the packages are already installed in an [upstream](https://spack.readthedocs.io/en/latest/chain.html) they will not be rebuilt.

### Find all installed Spack packages

```
spack find
```

### Find all local Spack packages

```
spack find --install-tree local
```

### Find all upstream Spack packages

```
spack find --install-tree upstream
```

### Clone a Spack environment

Change directory (`cd`) to the location where you want the `ACCESS-TEST` repository to reside. For example, `/g/data/$PROJECT/$USER/`
```
git clone https://github.com/ACCESS-NRI/ACCESS-TEST.git
```

### Activate the environment
Activate the _Spack_ environment inside the `ACCESS-TEST` directory by running:
```
spack env activate -p ./ACCESS-TEST
```
<terminal-window>
    <terminal-line data="input">spack env activate -p ./ACCESS-TEST</terminal-line>
    <terminal-line data="input" directory="[ACCESS-TEST]" class="spack" lineDelay=0></terminal-line>
</terminal-window>

### Compile packages

<!-- When Spack implements a command to disable and re-enable Spack upstreams, we should consider providing that information here -->

!!! warning
    Some of the commands below might take several minutes to complete.

```
spack concretize -f
spack install
```

!!! tip
    To understand the Spack concretization output, refer to: [What do the symbols at the start of spack concretize output mean?](https://forum.access-hive.org.au/t/access-nri-spack-cheat-sheet/5942#p-20566-what-do-the-symbols-at-the-start-of-spack-concretize-output-mean-17)

<terminal-window lineDelay=0>
    <!-- spack concretize -->
    <terminal-line lineDelay=600 directory="[test]" class="spack" data="input">spack concretize -f</terminal-line>
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
spack find --install-tree local
```

<terminal-window lineDelay=0>
    <!-- spack find -->
    <terminal-line directory="[test]" class="spack" data="input" lineDelay=600>spack find --install-tree local</terminal-line>
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
    <terminal-line><span class="spack-indigo">\==></span> 0 concretized packages to be installed (show with &#96;spack find -c&#96;)</terminal-line>
</terminal-window>

!!! info
    The animation above is a generalised example of the expected output, shortened and modified for clarity. Your actual output might vary.

### Find executables

Packages installed into an environment are linked into that environment's view.

```
ls ./ACCESS-TEST/.spack-env/view/bin
```
### Cleanup
```
spack uninstall --all
spack env deactivate
rm -rf ACCESS-TEST
```

## Develop a Model

For instructions on how to build an ACCESS model using _Spack_, refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code).

## Troubleshooting

Please refer to the [ACCESS-NRI Spack Cheat Sheet](https://forum.access-hive.org.au/t/access-nri-spack-cheat-sheet/5942) for further help on _Spack_. If your question remains unanswered, please ask on the [Hive-Forum](https://forum.access-hive.org.au/) or refer to [User support](/about/user_support).

## Advanced users

Please refer to [ACCESS-NRI's Spack configuration](https://github.com/ACCESS-NRI/spack-config) for details on how the release and shared _Spack_ instances are installed and configured.

To use _Spack_ outside of _Gadi_, please refer to the [Spack 101 Tutorial](https://spack-tutorial.readthedocs.io/en/latest/).

<custom-references>
- [https://spack.readthedocs.io/en/latest/](https://spack.readthedocs.io/en/latest/)
</custom-references>
