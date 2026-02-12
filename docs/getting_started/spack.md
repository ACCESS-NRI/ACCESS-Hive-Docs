!!! danger
    This page is tailored to experienced users and collaborators developing ACCESS models.<br>
    This step is *not* required if you *only* want to run a model. If you are looking for information on how to run a model, refer to the [Run a Model](/models/run_a_model) section.

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
    The steps in this section only need to be done once.

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
git clone https://github.com/ACCESS-NRI/spack.git --branch releases/v1.1
git clone https://github.com/ACCESS-NRI/spack-config.git --branch main
```

### Link Spack configuration files to the Spack instance

```
ln -s -r -v spack-config/v1.1/gadi/* spack/etc/spack/
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
. spack-config/spack-enable.bash
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

```
[ACCESS-TEST] $ spack find
==> In environment /g/data/$PROJECT/$USER/test-v1.1.1-docs/ACCESS-TEST
==> 1 root specs
-- no arch / no compilers ---------------------------------------
 -  access-test

==> 0 installed packages
==> 0 concretized packages to be installed (show with `spack find -c`)
```

```
[ACCESS-TEST] $ spack concretize -f --fresh
==> Fetching https://ghcr.io/v2/spack/bootstrap-buildcache-v2.2/blobs/sha256:2b43bf55db86d86ac4b5f49ae909d5a479a846e3db301c12dbfcc0ee088e0f33
==> Fetching https://ghcr.io/v2/spack/bootstrap-buildcache-v2.2/blobs/sha256:526d468db326aea1e36183b68a7f81cc5fa8094b03162baab76b9fbf88567f60
==> Installing "clingo-bootstrap@=spack~apps~docs+ipo+optimized+python+static_libstdcpp build_system=cmake build_type=Release commit=2a025667090d71b2c9dce60fe924feb6bde8f667 generator=make patches:=bebb819,ec99431 platform=linux os=centos7 target=x86_64" from a buildcache
==> Concretized 1 spec:
 -   uhzojqi  access-test@git.2025.09.000=2025.09.000+mpi build_system=bundle commit=7e4b4ddab9e17ef8080ed99f4fc069aed65615cb platform=linux os=rocky8 target=x86_64 
 -   tqipco4      ^access-test-component@main~ipo+mpi build_system=cmake build_type=Release commit=19cbd388607dc3d1f4d989e1b3b1e3b73445d131 generator=make platform=linux os=rocky8 target=x86_64 %fortran=oneapi@2025.2.0
[e]  mujmtqs          ^cmake@3.31.6~doc+ncurses+ownlibs~qtgui build_system=generic build_type=Release platform=linux os=rocky8 target=x86_64 
 -   ixud2sr          ^compiler-wrapper@1.0 build_system=generic platform=linux os=rocky8 target=x86_64 
[e]  vuczjrb          ^glibc@2.28 build_system=autotools platform=linux os=rocky8 target=x86_64 
 -   tkjgj5m          ^gmake@4.4.1~guile build_system=generic platform=linux os=rocky8 target=x86_64 %c=oneapi@2025.2.0
[e]  mq7p2hd          ^intel-oneapi-compilers@2025.2.0~amd+envmods~nvidia build_system=generic platform=linux os=rocky8 target=x86_64 
 -   u3ougvf          ^intel-oneapi-runtime@2025.2.0 build_system=generic platform=linux os=rocky8 target=x86_64 
 -   bmm7r6l              ^gcc-runtime@15.1.0 build_system=generic platform=linux os=rocky8 target=x86_64 
[e]  g6f4l7z                  ^gcc@15.1.0~binutils+bootstrap~graphite~mold~nvptx~piclibs~profiled~strip build_system=autotools build_type=RelWithDebInfo languages:='c,c++,fortran' platform=linux os=rocky8 target=x86_64 
[e]  ubzln4f          ^openmpi@4.1.5+atomics~cuda~cxx~cxx_exceptions~debug+fortran~gpfs~internal-hwloc~internal-libevent~internal-pmix~ipv6~java~lustre~memchecker~openshmem~orterunprefix~rocm+romio+rsh~static~two_level_namespace+vt+wrapper-rpath build_system=autotools fabrics:=none romio-filesystem:=none schedulers:=none platform=linux os=rocky8 target=x86_64 
```

```
[ACCESS-TEST] $ spack install
[+] /apps/cmake/3.31.6 (external cmake-3.31.6-mujmtqs66bqhzcljyokay5gjhouhzgic)
==> No binary for compiler-wrapper-1.0-ixud2srhgiuagq3k7w346tsabbealrja found: installing from source
==> Installing compiler-wrapper-1.0-ixud2srhgiuagq3k7w346tsabbealrja [2/11]
==> Fetching https://mirror.spack.io/_source-cache/archive/a5/a5ff4fcdbeda284a7993b87f294b6338434cffc84ced31e4d04008ed5ea389bf
    [100%]   30.08 KB @   11.6 MB/s
==> No patches needed for compiler-wrapper
==> compiler-wrapper: Executing phase: 'install'
==> compiler-wrapper: Successfully installed compiler-wrapper-1.0-ixud2srhgiuagq3k7w346tsabbealrja
  Stage: 0.07s.  Install: 0.03s.  Post-install: 0.20s.  Total: 0.37s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/compiler-wrapper-1.0-ixud2srhgiuagq3k7w346tsabbealrja
[+] /usr (external glibc-2.28-vuczjrbyzfif5nzgt5gqbrdrzaioihy6)
==> intel-oneapi-compilers@2025.2.0 : has external module in ['intel-compiler-llvm/2025.2.0']
[+] /apps/intel-tools/.packages/2025.2.0.575 (external intel-oneapi-compilers-2025.2.0-mq7p2hdwp3jz3at5qyaeun4csqwjghh2)
==> gcc@15.1.0 : has external module in ['gcc/15.1.0']
[+] /apps/gcc/15.1.0/wrappers (external gcc-15.1.0-g6f4l7zob7gi5hnduqrc7m7lpwslgiz3)
==> openmpi@4.1.5 : has external module in ['openmpi/4.1.5']
[+] /apps/openmpi/4.1.5 (external openmpi-4.1.5-ubzln4fyaveasthybe62jlck23soyhad)
==> No binary for gcc-runtime-15.1.0-bmm7r6lkfxqislzdkrl7juy2jgjmiboq found: installing from source
==> Installing gcc-runtime-15.1.0-bmm7r6lkfxqislzdkrl7juy2jgjmiboq [7/11]
==> No patches needed for gcc-runtime
==> gcc-runtime: Executing phase: 'install'
==> gcc-runtime: Successfully installed gcc-runtime-15.1.0-bmm7r6lkfxqislzdkrl7juy2jgjmiboq
  Stage: 0.00s.  Install: 2.85s.  Post-install: 0.33s.  Total: 3.25s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/gcc-runtime-15.1.0-bmm7r6lkfxqislzdkrl7juy2jgjmiboq
==> No binary for intel-oneapi-runtime-2025.2.0-u3ougvfqcvostnjs4crekptewk7zzebc found: installing from source
==> Installing intel-oneapi-runtime-2025.2.0-u3ougvfqcvostnjs4crekptewk7zzebc [8/11]
==> No patches needed for intel-oneapi-runtime
==> intel-oneapi-runtime: Executing phase: 'install'
==> intel-oneapi-runtime: Successfully installed intel-oneapi-runtime-2025.2.0-u3ougvfqcvostnjs4crekptewk7zzebc
  Stage: 0.00s.  Install: 2.90s.  Post-install: 0.23s.  Total: 3.19s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/intel-oneapi-runtime-2025.2.0-u3ougvfqcvostnjs4crekptewk7zzebc
==> No binary for gmake-4.4.1-tkjgj5mjr7c6lwakcxc7bvbjyhiir5z7 found: installing from source
==> Installing gmake-4.4.1-tkjgj5mjr7c6lwakcxc7bvbjyhiir5z7 [9/11]
==> Fetching https://mirror.spack.io/_source-cache/archive/dd/dd16fb1d67bfab79a72f5e8390735c49e3e8e70b4945a15ab1f81ddb78658fb3.tar.gz
    [100%]    2.35 MB @   28.0 MB/s
==> No patches needed for gmake
==> gmake: Executing phase: 'install'
==> gmake: Successfully installed gmake-4.4.1-tkjgj5mjr7c6lwakcxc7bvbjyhiir5z7
  Stage: 0.86s.  Install: 1m 10.94s.  Post-install: 0.16s.  Total: 1m 12.04s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/gmake-4.4.1-tkjgj5mjr7c6lwakcxc7bvbjyhiir5z7
==> No binary for access-test-component-main-tqipco4m6gr76hnjttlr3shjzfix32g4 found: installing from source
==> Installing access-test-component-main-tqipco4m6gr76hnjttlr3shjzfix32g4 [10/11]
==> No patches needed for access-test-component
==> access-test-component: Executing phase: 'cmake'
==> access-test-component: Executing phase: 'build'
==> access-test-component: Executing phase: 'install'
==> access-test-component: Successfully installed access-test-component-main-tqipco4m6gr76hnjttlr3shjzfix32g4
  Stage: 1.81s.  Cmake: 15.36s.  Build: 3.36s.  Install: 0.15s.  Post-install: 0.13s.  Total: 20.93s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/access-test-component-main-tqipco4m6gr76hnjttlr3shjzfix32g4
==> No binary for access-test-git.2025.09.000=2025.09.000-uhzojqiue66luxzlvzaxi66k3rqaa7qq found: installing from source
==> Installing access-test-git.2025.09.000=2025.09.000-uhzojqiue66luxzlvzaxi66k3rqaa7qq [11/11]
==> No patches needed for access-test
==> access-test: Executing phase: 'install'
==> access-test: Successfully installed access-test-git.2025.09.000=2025.09.000-uhzojqiue66luxzlvzaxi66k3rqaa7qq
  Stage: 0.00s.  Install: 0.00s.  Post-install: 0.13s.  Total: 0.22s
[+] /g/data/$PROJECT/$USER/test-v1.1.1-docs/release/linux-x86_64/access-test-git.2025.09.000_2025.09.000-uhzojqiue66luxzlvzaxi66k3rqaa7qq
==> Updating view at /g/data/$PROJECT/$USER/test-v1.1.1-docs/ACCESS-TEST/.spack-env/view
```


### Check installed packages

```
spack find
```

```
[ACCESS-TEST] $ spack find
==> In environment /g/data/$PROJECT/$USER/test-v1.1.1-docs/ACCESS-TEST
==> 1 root specs
-- no arch / no compilers ---------------------------------------
[+] access-test@git.2025.09.000=2025.09.000

-- linux-rocky8-x86_64 / %c=oneapi@2025.2.0 ---------------------
gmake@4.4.1

-- linux-rocky8-x86_64 / %fortran=oneapi@2025.2.0 ---------------
access-test-component@main

-- linux-rocky8-x86_64 / no compilers ---------------------------
access-test@git.2025.09.000=2025.09.000  glibc@2.28
cmake@3.31.6                             intel-oneapi-compilers@2025.2.0
compiler-wrapper@1.0                     intel-oneapi-runtime@2025.2.0
gcc@15.1.0                               openmpi@4.1.5
gcc-runtime@15.1.0
==> 11 installed packages
==> 0 concretized packages to be installed (show with `spack find -c`)
```

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
git -C spack fetch --all -Pp
git -C spack reset --hard origin/releases/v1.1
git -C spack-config pull
. spack-config/spack-enable.bash
spack repo update
```

## Set up Spack v0.22 on Gadi (DEPRECATED)

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
git clone https://github.com/ACCESS-NRI/spack-packages.git --branch api-v1
git clone https://github.com/ACCESS-NRI/spack-config.git --branch main
```

### Link Spack configuration files to the Spack instance

```
ln -s -r -v spack-config/v0.22/gadi/* spack/etc/spack/
```

!!! success
    Your _Spack_ setup is complete!

For instructions on how to build an ACCESS model using _Spack_, refer to [Modify and build an ACCESS model's source code](/models/build_a_model/build_source_code).

## Enable Spack v0.22 (DEPRECATED)

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

## Test Spack v0.22 (OPTIONAL) (DEPRECATED)

To test that your Spack installation works as expected, we will create an `ACCESS-TEST` environment and build the relevant packages (this will take approximately 30 minutes). Then, we will uninstall all the packages and remove the environment.


### Clone a Spack environment

```
git clone https://github.com/ACCESS-NRI/ACCESS-TEST.git --branch api-v1
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
    <terminal-line directory="[ACCESS-TEST]" class="spack" data="input" lineDelay=600>spack find</terminal-line>
    <terminal-line lineDelay=500><span class="spack-indigo">\==></span> In environment test</terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 1 root specs</terminal-line>
    <terminal-line><span class="spack-grey keep-blanks"> - </span> access-test<span class="spack-cyan">@git.2025.04.000=2025.04.000</span></terminal-line>
    <terminal-line></terminal-line>
    <terminal-line><span class="spack-indigo">\==></span> 0 installed packages</terminal-line>
    <!-- spack concretize -->
    <terminal-line lineDelay=600 directory="[ACCESS-TEST]" class="spack" data="input">spack concretize -f --fresh</terminal-line>
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
        <span class="spack-indigo">\==></span> Updating view at /g/data/\$PROJECT/\$USER/spack/0.22/environments/test/.spack-env/view</terminal-line>
    </terminal-line>
    <!-- spack install -->
    <terminal-line directory="[ACCESS-TEST]" class="spack" lineDelay=2000 data="input">
        spack install
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">glibc-2.28-5elnsoiqgcg5k5zmmwsp33bmnmaa3g5p</span> <span class="spack-highlighted">[1/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/glibc-2.28-5elnsoiqgcg5k5zmmwsp33bmnmaa3g5p
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">cmake-3.24.2-vc4y4c64s55j5u6kp37ciw2hcghuxhhc</span> <span class="spack-highlighted">[2/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/cmake-3.24.2-vc4y4c64s55j5u6kp37ciw2hcghuxhhc
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span class="spack-highlighted">Installing</span> <span class="spack-green">openmpi-4.1.5-qg5spmhetxnuvtyi7nuobd3nv7zwnu5f</span> <span class="spack-highlighted">[3/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/openmpi-4.1.5-qg5spmhetxnuvtyi7nuobd3nv7zwnu5f
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">gmake-4.4.1-j6yscmmcn3qws7n35klote7rivw7foa6</span> <span class="spack-highlighted">[4/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/gmake-4.4.1-j6yscmmcn3qws7n35klote7rivw7foa6
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">access-test-component-main-bcixn5z6ou7vlnogzgyy5z23jb4qeunx</span> <span class="spack-highlighted">[5/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/access-test-component-main-bcixn5z6ou7vlnogzgyy5z23jb4qeunx
    </terminal-line>
    <terminal-line>
        <span class="spack-indigo bold">\==></span> <span   class="spack-highlighted">Installing</span> <span class="spack-green">access-test-git.2025.04.000_2025.04.000-ih4cowpiz2kv6tnz4rkualxuly54tizr</span> <span class="spack-highlighted">[6/6]</span>
    </terminal-line>
    <terminal-line>
        <span class="spack-green">[+]</span> /g/data/\$PROJECT/\$USER/spack/0.22/release/linux-rocky8-x86_64/intel-2021.10.0/access-test-git.2025.04.000_2025.04.000-ih4cowpiz2kv6tnz4rkualxuly54tizr
    </terminal-line>
</terminal-window>

!!! info
    The full output has been truncated for brevity.

### Check installed packages

```
spack find
```
<terminal-window lineDelay=0>
    <terminal-line directory="[ACCESS-TEST]" class="spack" data="input" lineDelay=600>spack find</terminal-line>
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
rm -rf ACCESS-TEST
```

## Update Spack v0.22 on Gadi (DEPRECATED)

Keep your Spack instance up-to-date by doing the following:

```
cd /g/data/$PROJECT/$USER/spack/0.22
git -C spack fetch --all -Pp
git -C spack reset --hard origin/releases/v0.22
git -C spack-config pull
git -C spack-packages pull origin api-v1
```

<custom-references>
- [https://spack.readthedocs.io/en/latest/](https://spack.readthedocs.io/en/latest/)
</custom-references>
