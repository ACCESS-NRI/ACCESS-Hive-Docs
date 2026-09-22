
{% set ACCESS_MODEL = "ACCESS-OM3" %}
{% set ACCESS_PACKAGE = "MOM6" %}
{% set ACCESS_MODEL_URL = "https://github.com/ACCESS-NRI/ACCESS-OM3" %}
{% set use_spack = "/getting_started/spack" %}
[ACCESS models]: /models
[OM3 config]: models/access_models/access-om/#access-om3
[MOM6 component]: /models/model_components/ocean/#mom6
[gadi]: https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi#id-0.WelcometoGadi-Overview
[spack-configuration-scopes-documentation]: https://spack.readthedocs.io/en/latest/configuration.html#configuration-scopes

!!! warning
    This step is *not* required if you *only* want to run an ACCESS released model configuration. If you are looking for information on how to run a model, refer to the [Run a Model](/models/run_a_model) section.

# Modify and build an ACCESS model's source code on Gadi

This page is for users needing to change the source code and recompile ACCESS models. ACCESS-NRI supports building ACCESS models in two ways:

 - Create prereleases for an ACCESS Model. Very low learning curve for GitHub familiar users. If you want to modify and build a model, while maintaining a clear record of your changes and being able to share the modified builds with others, refer to [Create Prereleases and Releases for an ACCESS Model](/models/build_a_model/create_a_prerelease) instead (X minutes). Suited to modifying dependency versions (e.g. openmpi version) or build variants. This process requires less Spack understanding and will be more intuitive to GitHub users.
 - Using Spack "develop" on Gadi. This approach suits users who are making source code changes and need to repeatedly modify the source code, git bisect complicated bugs, recompile it and run tests. This option also requires setting up a Spack develop environment (Y minutes). This process has fewer pre-requisites and does not require ACCESS-NRI `write` access.

The below instructions show how to modify the [MOM6 component] for [ACCESS-OM3][OM3 config] and re-compile the relevant {{ACCESS_MODEL}} dependencies on [NCI](https://nci.org.au/about-us/who-we-are)'s supercomputer [_Gadi_][gadi] using the [Spack](https://spack.readthedocs.io) software manager.

!!! tip
    The following instructions are valid (with simple tweaks) for all [ACCESS models].

## Prerequisites

- **NCI account**<br>
  Before building a model, you need to [Set Up your NCI Account](/getting_started/set_up_nci_account).

- **_Spack_**<br>
  To use _Spack_ on _Gadi_, refer to [How to use Spack on Gadi for building ACCESS models]({{use_spack}}).

## Enable spack

To make _Spack_ available run:
```bash
module use /g/data/vk83/modules
module load spack
```

## Choose ACCESS model and model component to develop

We begin by choosing which ACCESS model we'd like to develop and which component part we will be modifying; in this example, we develop ACCESS-OM3 (`#MDR`) and MOM6 (`#<GitHub_name>`).

When you develop a package within a _Spack_ environment, _Spack_ needs to know _how_ that software is built. Normally, the Spack package recipe that builds MOM6 is called `access-mom6`, the Spack develop process below _replaces_ this process with a customised recipe.

Putting this together we have:

```bash
git clone https://github.com/ACCESS-NRI/ACCESS-OM3.git #MDR
cd ACCESS-OM3
MOM6_BRANCH=$(spack info access-mom6 | awk '$1=="stable" && /branch/{print $NF; exit}')
git clone -b "$MOM6_BRANCH" https://github.com/ACCESS-NRI/MOM6.git   #<GitHub_name>
spack env activate -p ./
spack develop --path ./MOM6 access-mom6@stable                       #<package_name>
```

??? question "How do I know how to specify the spack package and model component?"
    The [ACCESS-OM3/spack.yaml](https://github.com/ACCESS-NRI/ACCESS-OM3/blob/da06e5a6caabe45f7e85ea475ec61c26a8b344c8/spack.yaml#L19-L100) has a list of available packages under `packages`. This table shows some popular choices:

    | `config.yaml` spack `<package_name>` | `<GitHub_name>`                                            |
    |---------------------------------------|-----------------------------------------------------------|
    | `access-mom6`                         | `https://github.com/ACCESS-NRI/MOM6.git`                   |
    | `access-cice`                         | `https://github.com/ACCESS-NRI/CICE.git`                   |
    | `access-generic-tracers`              | `https://github.com/ACCESS-NRI/GFDL-generic-tracers.git`   |
    | `access-ww3`                          | `https://github.com/ACCESS-NRI/WW3.git`                    |

When we run this last command (`spack develop --path ./MOM6 access-mom6@stable`), Spack inserts the following customised recipe for building MOM6 in the `spack.yaml`
```yaml
  develop:
    access-mom6:
      spec: access-mom6@=stable
      path: ./MOM6
```

This is effectively telling Spack that we should build off this local version of MOM6 (i.e. using `--path`), not the version on GitHub. We thus need to edit the `spack.yaml` to use our local version, to do this comment out the `access-mom6` lines in the `spack.yaml` ([example](https://github.com/ACCESS-NRI/ACCESS-OM3/blob/da06e5a6caabe45f7e85ea475ec61c26a8b344c8/spack.yaml#L21-L26)). 

??? question "Optional: how to include the same "variants" in the local build."
    To include the variants included in `ACCESS-OM3/2026.05.004`, we would:
    ```yaml
      develop:
        access-mom6:
          spec: >-
            access-mom6@=stable
            +mom6_solo
            fflags="-march=sapphirerapids -mtune=sapphirerapids -unroll"
            cflags="-march=sapphirerapids -mtune=sapphirerapids -unroll"
          path: ./MOM6
    ```

At this point, you can make any code modifications you wish to the MOM6 source code directory (`./MOM6`). To build, proceed with:

```
spack concretize -f
spack install
```

### What if I want to use a different version of MOM6? (optional)

When you ask Spack to develop a specific version of a package — say `access-mom6@stable` — Spack
already knows exactly which point in MOM6's source code that version corresponds to. But if you clone
the MOM6 GitHub repository yourself so you have a working copy to edit, there's nothing that
automatically tells *you* which branch, tag, or commit to use. If you just clone the repository as-is,
you could easily end up with different code than the version you told Spack you're building — which
can cause confusing build errors, or worse, a model that quietly behaves differently than expected.

The commands below ask Spack directly which git reference matches the version you want, so the code
you clone always lines up with what Spack is building.

Example: "Worked example: cloning the exact MOM6 code that matches your `access-mom6` version"
```bash
    PACKAGE=access-mom6
    VERSION=stable
    REPO_URL=https://github.com/ACCESS-NRI/MOM6.git

    # Ask Spack which branch, tag, or commit this version points to
    REF=$(spack info "$PACKAGE" | awk -v v="$VERSION" '$1==v && /branch|tag|commit/{print $NF; exit}')

    # A normal clone fetches every branch, tag, and commit — so checkout works
    # no matter which kind of reference $REF turns out to be
    git clone "$REPO_URL"
    cd MOM6
    git checkout "$REF"
```

Change `VERSION` to any version listed by `spack info access-mom6` — e.g. `2026.05.003` — and the same four commands still work, whether that version tracks a branch, a tag, or a fixed commit.

TODO: Claude wrote the above, so NEED to test!!

## Output directory for compiled packages

All compiled packages will be placed in directories having the following format: `<install_tree.root>/<architecture>/<compiler.name>-<compiler.version>/<name>-<version>-<hash>`.

`<install_tree.root>` depends on the [`install_tree.root`](https://spack.readthedocs.io/en/latest/config_yaml.html#install-tree-root) configuration field. _Spack_ reads this configuration field from files in several directories, following [Spack's configuration scopes][spack-configuration-scopes-documentation].

!!! warning
    For instances of _Spack_ on _Gadi_ you should ignore the **system** scope.

For the example above, `mom5_dev` _Spack_ environment's configuration file (`spack.yaml`) contains the following lines that fall in the **environment** scope:
```yaml
config:
    install_tree:
      root: $spack/../restricted/ukmo/release
```

This means the packages built in this example can be found in `/g/data/$PROJECT/$USER/spack/1.1/spack/../restricted/ukmo/release/<architecture>/<compiler.name>-<compiler.version>/<name>-<version>-<hash>`.

## Troubleshooting build errors

Sometimes you might encounter errors while compiling the packages.<br>
_Spack_ prints out the error message and generates a full build log that can be viewed by the user. The location of the build log is shown at the end of the error message.

For example, if we try to install the `mom5_dev` environment with an error in the new `mom5` source code (in this example a `use` statement in the `<new-mom5-source-code-folder>/src/accessom_coupler/ocean_solo.F90` file has been purposely commented out to force an error in compilation), we might get an output error similar to the following:

<pre><code><spack class="spack-grey bold">...</spack>
<span class="spack-red"> >> 415    /g/data/$PROJECT/$USER/spack/1.1/environments/mom5_dev/mom5/src/access_coupler/ocean_solo.F90:224: undefined reference to `constant s_init_'</span>
<span class="spack-red"> >> 416    make: *** [Makefile:931: fms_ACCESS-CM.x] Error 1</span>
<spack class="spack-grey bold">...</spack>
See build log for details:
  /scratch/$PROJECT/$USER/tmp/path/to/the/spack-stage-mom5-git.access-esm1.5_2024.08.23_access-esm1.5-l34w7is54xzer7s4ztvb5ymgjbtduknh/spack-build-out.txt
<spack class="spack-grey bold">...</spack>
<span class="spack-red">==></span> Error: access-esm1p5-git.2024.05.1=2024.05.1-aysea5r7rbwy22lluvl64baperlokktv: Package was not installed
<span class="spack-red">==></span> Error: Installation request failed.  Refer to reported errors for failing package(s).</code></pre>

CHRIS ADDED TODAY
```bash
[cyb561.gadi-login-04: ACCESS-OM3]$ spack install
[+] /usr (external glibc-2.28-vuczjrbyzfif5nzgt5gqbrdrzaioihy6)
==> openmpi@4.1.7 : has external module in ['openmpi/4.1.7']
[+] /apps/openmpi/4.1.7 (external openmpi-4.1.7-ujbo7lsuwmz4klodpgsrdhopbuuhowb3)
==> python@3.11.7 : has external module in ['python3/3.11.7']
[+] /apps/python3/3.11.7 (external python-3.11.7-do6khcayp276ys73jr4twn4oqlstsco3)
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/compiler-wrapper-1.1.0-4vm57ydwr3x5uq2jhwsv7ltk6az3hxxs
==> intel-oneapi-compilers@2025.2.0 : has external module in ['intel-compiler-llvm/2025.2.0']
[+] /apps/intel-tools/.packages/2025.2.0.575 (external intel-oneapi-compilers-2025.2.0-vqjkrsh2v3dc2ki5pigniqxnpzrwcpu3)
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/gcc-runtime-15.1.0-r3jhjvxq3s4lt5fidxafye5utgjkvs6g
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/python-venv-1.0-42a4xj45vkukhrv56dhnexltu5jvjebo
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/intel-oneapi-runtime-2025.2.0-hyun3ledkfevkt6ezyotlc45wzufscep
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/libyaml-0.2.5-ohkj2ryp2cismkgofqovjopnb3lod5wi
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mocsy-2025.07.002-5awgzcl5rbvkk4ei62uyk66hsp3avkr7
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/libaec-1.1.4-patvd3yohb3sqh2m63t2e56o3q6p6hz3
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/zlib-ng-2.3.3-p2ctudzwaiqp6acuskgmu2h6kgvjfh6w
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/ncurses-6.6-duqycjw3ztjzg6njfzrdvnn2fzxhiwlu
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/lz4-1.10.0-pzf2vwga4yxnkxpp76uqzbzxxcpuslx4
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/pkgconf-2.5.1-zizxaust2zwsjc3p6amfvle4j7vqqekl
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/mbedtls-3.6.2-ycfkp5oxo44cr3e4obexyj4uo6mcapwc
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/snappy-1.2.1-qwtkwcddpmcko7vxptrwj7pavpijc6yo
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/bzip2-1.0.8-5umnxzum3fjmzr56pxz7rhpwx4hv6khk
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/zstd-1.5.7-fd6ey726t34uco4rkzrgcwoluryimrp7
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/gmake-4.4.1-3sr5xy6gpvmfkr4ecptiqtbmcrqnczuk
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/py-pyyaml-6.0.3-uzo74q5nduuyjey2ko444bi2qhwi54se
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/nghttp2-1.67.1-duordziageq6oev2cwnh3hc7nmlngt3b
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/c-blosc-1.21.6-ntor6vmuxx4jp7dejzypvuctslne5pw6
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/fortranxml-4.1.2-l2i2droyqjjgnrsb6ort3no7hz5cpvnk
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/hdf5-1.14.6-ustivdivi5brfjuhd7wt525vxrd6rddw
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/curl-8.18.0-q6b43w2pg4vgmyu7oivv5xjm2rgmfshg
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/netcdf-c-4.9.3-i2yg6wiht4vl5slywg25qpd3avh6mh2y
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/cmake-3.31.11-4xpsc6gicgmaz3onofzohjaau76odzd3
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/netcdf-fortran-4.6.2-yze65gmryo5aren72ydkw742yerv2ag6
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/fms-2025.03-zw6tzbdvqmqkrkizhqisi3kvstrc2vjm
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/parallelio-2.6.8-a5un5qjas4eju5dpyhobdph5lwqgx4mv
==> No binary for access-generic-tracers-2026.09.000-2y3j5xtacj46gevx23vm6pmdd2uavhhz found: installing from source
==> Installing access-generic-tracers-2026.09.000-2y3j5xtacj46gevx23vm6pmdd2uavhhz [32/39]
==> No patches needed for access-generic-tracers
==> access-generic-tracers: Executing phase: 'cmake'
==> access-generic-tracers: Executing phase: 'build'
==> access-generic-tracers: Executing phase: 'install'
==> access-generic-tracers: Successfully installed access-generic-tracers-2026.09.000-2y3j5xtacj46gevx23vm6pmdd2uavhhz
  Stage: 5.42s.  Cmake: 22.75s.  Build: 55.95s.  Install: 0.76s.  Post-install: 0.35s.  Total: 1m 25.89s
[+] /g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-generic-tracers-2026.09.000-2y3j5xtacj46gevx23vm6pmdd2uavhhz
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/esmf-8.9.1-u56mitgtfbi2qlj3x7lw7ofxj7lw4b2l
[+] /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access3-share-2026.03.002-m65pkhfhdcfromtvp3z5pwkejlcq6pp4
==> No binary for access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda found: installing from source
==> Installing access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda [35/39]
==> No patches needed for access-mom6
==> access-mom6: Executing phase: 'cmake'
==> Error: ProcessError: Command exited with status 1:
    '/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/cmake-3.31.11-4xpsc6gicgmaz3onofzohjaau76odzd3/bin/cmake' '-G' 'Unix Makefiles' '-DCMAKE_INSTALL_PREFIX:STRING=/g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda' '-DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=ON' '-DCMAKE_INSTALL_RPATH:STRING=/g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda/lib;/g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda/lib64' '-DCMAKE_PREFIX_PATH:STRING=/g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-generic-tracers-2026.09.000-2y3j5xtacj46gevx23vm6pmdd2uavhhz;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access3-share-2026.03.002-m65pkhfhdcfromtvp3z5pwkejlcq6pp4;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/cmake-3.31.11-4xpsc6gicgmaz3onofzohjaau76odzd3;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/compiler-wrapper-1.1.0-4vm57ydwr3x5uq2jhwsv7ltk6az3hxxs;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/gmake-4.4.1-3sr5xy6gpvmfkr4ecptiqtbmcrqnczuk;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mocsy-2025.07.002-5awgzcl5rbvkk4ei62uyk66hsp3avkr7;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/fms-2025.03-zw6tzbdvqmqkrkizhqisi3kvstrc2vjm;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/esmf-8.9.1-u56mitgtfbi2qlj3x7lw7ofxj7lw4b2l;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/fortranxml-4.1.2-l2i2droyqjjgnrsb6ort3no7hz5cpvnk;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/parallelio-2.6.8-a5un5qjas4eju5dpyhobdph5lwqgx4mv;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/netcdf-fortran-4.6.2-yze65gmryo5aren72ydkw742yerv2ag6;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/netcdf-c-4.9.3-i2yg6wiht4vl5slywg25qpd3avh6mh2y;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/bzip2-1.0.8-5umnxzum3fjmzr56pxz7rhpwx4hv6khk;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/c-blosc-1.21.6-ntor6vmuxx4jp7dejzypvuctslne5pw6;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/hdf5-1.14.6-ustivdivi5brfjuhd7wt525vxrd6rddw;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/libaec-1.1.4-patvd3yohb3sqh2m63t2e56o3q6p6hz3;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/lz4-1.10.0-pzf2vwga4yxnkxpp76uqzbzxxcpuslx4;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/snappy-1.2.1-qwtkwcddpmcko7vxptrwj7pavpijc6yo;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/zstd-1.5.7-fd6ey726t34uco4rkzrgcwoluryimrp7;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/zlib-ng-2.3.3-p2ctudzwaiqp6acuskgmu2h6kgvjfh6w;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/intel-oneapi-runtime-2025.2.0-hyun3ledkfevkt6ezyotlc45wzufscep;/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/gcc-runtime-15.1.0-r3jhjvxq3s4lt5fidxafye5utgjkvs6g;/apps/intel-tools/.packages/2025.2.0.575;/apps/openmpi/4.1.7' '-DCMAKE_BUILD_TYPE:STRING=Release' '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON' '-DCMAKE_INTERPROCEDURAL_OPTIMIZATION:BOOL=OFF' '-DCMAKE_POLICY_DEFAULT_CMP0090:STRING=NEW' '-DCMAKE_FIND_USE_PACKAGE_REGISTRY:BOOL=OFF' '-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON' '-DMOM6_OPENMP:BOOL=OFF' '-DMOM6_ASYMMETRIC:BOOL=OFF' '-DMOM6_ACCESS3:BOOL=ON' '-DMOM6_SOLO:BOOL=ON' '' '' '/g/data/tm70/cyb561/harshula/ACCESS-OM3/MOM6'

2 errors found in build log:
     52    -- Found PIO: /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/parallelio-2.6.8-a5un5qjas4eju5dpyhobdph5lwqgx4mv (Required is at least version "2.5.3") found components: C For
           tran
     53    -- FindPIO:
     54    --   - PIO_PREFIX [/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/parallelio-2.6.8-a5un5qjas4eju5dpyhobdph5lwqgx4mv]
     55    --   - PIO Components Found: C;Fortran
     56    -- Found ESMF: /g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/esmf-8.9.1-u56mitgtfbi2qlj3x7lw7ofxj7lw4b2l/lib/libesmf.so (found suitable version "8.9.1", minimum required is
            "8.3.0")
     57    -- Configuring done (22.8s)
  >> 58    CMake Error at src/CMakeLists.txt:21 (target_sources):
     59      Cannot find source file:
     60
     61        equation_of_state/TEOS10/gsw_chem_potential_water_t_exact.f90
     62
     63      Tried extensions .c .C .c++ .cc .cpp .cxx .cu .mpp .m .M .mm .ixx .cppm
     64      .ccm .cxxm .c++m .h .hh .h++ .hm .hpp .hxx .in .txx .f .F .for .f77 .f90
     65      .f95 .f03 .hip .ispc
     66
     67
  >> 68    CMake Error at cmake/FortranLib.cmake:5 (add_library):
     69      No SOURCES given to target: mom6shared
     70    Call Stack (most recent call first):
     71      src/CMakeLists.txt:3 (add_fortran_target)
     72
     73
     74    CMake Generate step failed.  Build files cannot be regenerated correctly.

See build log for details:
  /scratch/tm70/cyb561/tmp/spack-stage/spack-stage-access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda/spack-build-out.txt

==> Warning: Skipping build of access3-2026.03.002-vpqv7csug64ndlnkghekloq4gzqzmoin since access-mom6-stable-7p2x5g7p72kjliot4rnvqaxk7eh2mpda failed
==> Warning: Skipping build of access-om3-latest-agdyrfr2gomyrossvzqkk4op6p7rad2i since access3-2026.03.002-vpqv7csug64ndlnkghekloq4gzqzmoin failed
==> No binary for access-ww3-2026.03.001-mg7vudvw5pfpseurnsuncp657wsgbeho found: installing from source
==> Installing access-ww3-2026.03.001-mg7vudvw5pfpseurnsuncp657wsgbeho [36/39]
==> No patches needed for access-ww3
==> access-ww3: Executing phase: 'cmake'
==> access-ww3: Executing phase: 'build'
==> access-ww3: Executing phase: 'install'
==> access-ww3: Successfully installed access-ww3-2026.03.001-mg7vudvw5pfpseurnsuncp657wsgbeho
  Stage: 44.86s.  Cmake: 21.65s.  Build: 1m 17.91s.  Install: 0.60s.  Post-install: 0.21s.  Total: 2m 25.62s
[+] /g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-ww3-2026.03.001-mg7vudvw5pfpseurnsuncp657wsgbeho
==> No binary for access-cice-CICE6.6.3-2-vmceohdrnn5ulhe4ueb5b3qbzr4yef67 found: installing from source
==> Installing access-cice-CICE6.6.3-2-vmceohdrnn5ulhe4ueb5b3qbzr4yef67 [37/39]
==> No patches needed for access-cice
==> access-cice: Executing phase: 'cmake'
==> access-cice: Executing phase: 'build'
==> access-cice: Executing phase: 'install'
==> access-cice: Successfully installed access-cice-CICE6.6.3-2-vmceohdrnn5ulhe4ueb5b3qbzr4yef67
  Stage: 15.16s.  Cmake: 21.86s.  Build: 1m 27.16s.  Install: 0.54s.  Post-install: 0.19s.  Total: 2m 5.18s
[+] /g/data/tm70/cyb561/spack/1.1/release/linux-x86_64_v4/access-cice-CICE6.6.3-2-vmceohdrnn5ulhe4ueb5b3qbzr4yef67
==> Error: access-om3-latest-agdyrfr2gomyrossvzqkk4op6p7rad2i: Package was not installed
==> Updating view at /g/data/tm70/cyb561/harshula/ACCESS-OM3/.spack-env/view
==> Error: Installation request failed.  Refer to reported errors for failing package(s).
```


If the error is not obvious from the error message, see the build log for more information.

## Debugging a Model

Debugging is an important part of the development process. Using a debugger can make this process significantly easier, allowing detailed inspection of the state of the code as it is running. The debugger used in this guide is [_Linaro DDT_](https://www.linaroforge.com/linaro-ddt/) from [Linaro Forge](https://www.linaroforge.com/).

### Setting up the debugger

To connect to the debugger remotely from your workstation, you will need to set up the _Linaro Forge_ client locally. Download the client from the [Linaro Forge download](https://www.linaroforge.com/download-documentation) page, ensuring to match the version of the client with the most up-to-date version on the compute cluster (to get older versions of the client, follow the [older versions](https://www.linaroforge.com/download-forge-old-version) link). Once installed, launch the client and follow the [connecting remotely](https://www.linaroforge.com/download-forge-old-version) instructions.

!!! tip
    To check which versions of _Linaro Forge_ are available on your compute cluster, use `module avail linaro-forge`.

For Gadi, the _Linaro Forge Remote Launch Settings_ are:

- __Host Name__: `<username>@nci.org.au`
- __Remote Installation Directory__: `/apps/linaro-forge/<version>`

### Setting up the build

To debug a model through the _Linaro_ debugger, the following settings in the build's `spack.yaml` are required:

1. OpenMPI version 4 should be used. `openmpi@4.1.3` and `openmpi@4.1.7` have been tested.

2. Modify the compilation options to include debug information and prevent the compiler from re-ordering the code for the purpose of optimisation. Add the following entries to the `require` section of the components you want to debug:
    - `'fflags="-O0 -g -traceback"'`
    - `'cflags="-O0 -g -fno-omit-frame-pointer"'`

Using the `mom5_dev` example above in the context of the _ACCESS-ESM1.5_ model to debug the MOM5 component, the updated `spack.yaml` would be:

```yaml
spack:
  specs:
    - access-esm1p5@git.2024.12.0
packages:
  ...
  mom5:
    require:
      - '@git.access-esm1.5_2024.08.23=access-esm1.5'
      - 'fflags="-O0 -g -traceback"'
      - 'cflags="-O0 -g -fno-omit-frame-pointer"'
  ...
  openmpi:
    require:
      - '@4.1.3'
  ...
```
Once these changes have been made, concretize the environment by running:

```
spack concretize -f
```

Then install the environment by running:

```
spack install --keep-stage
```

!!! tip
    The `--keep-stage` option prevents _Spack_ from cleaning up the source code used to compile the executables, so it can be accessed by the debugger. Note that if you are iterating on a build, you may build up a large number of source files from successive building. These files are typically located at `/scratch/$PROJECT/$USER/tmp/spack-stage`, and should be cleaned up periodically.

!!! warning
    If you have an existing build that was built without the `--keep-stage` option, the model will need to be uninstalled and re-installed again with this option for the debugger to work properly.

This will build executables compatible with the _Linaro_ debugger.

### Running the model with the debugger enabled

The recommended way to execute a debugging run is by using [_payu_](https://github.com/payu-org/payu) as follows:

1. Locate the paths to the executables generated by the _Spack_ build by running:
    ```
    spack find --paths
    ```
    This command lists the installation directories for each package in the environment. The generated executables will be located in the installation directories at `bin/<executable_name>`. Be careful to retrieve the correct executable for packages which build multiple executables (e.g., CICE5).
    {: #exe_paths }
2. Within the `submodels` section of the model configuration's `config.yaml` file, in the `exe` field, specify the [path to its executable](#exe_paths).
3. In the `config.yaml` file, add `linaro-forge/<version>` to the `modules: load` section, by substituting `<version>` with the correct `linaro-forge` version.
4. In the `config.yaml`, turn off executable reproducibility, since adding debugging options modifies the executable, by setting `manifest: reproduce: exe: False`.
5. Tell _payu_ to pipe the run through _Linaro DDT_ by adding the following to the configuration `config.yaml`:

    ```
    mpi:
      runcmd: ddt --connect mpirun
    ```
6. Run the model with `payu run`.

!!! tip
    Alternatively, it is possible to debug from an interactive job following the [instructions from NCI](https://opus.nci.org.au/spaces/Help/pages/363659856/Linaro+Forge+HPC+Tools...). While in an interactive job, call `payu-run` instead of `payu run`. If you choose this method, in the `config.yaml` set `mpi: runcmd: ddt mpirun` instead of `mpi: runcmd: ddt --connect mpirun`.

### Changing number of processes for _Linaro DDT_
A limitation of the NCI's _Linaro Forge_ license is that the maximum number of processes permitted for a _DDT_ (or _Map_ for profiling) run is 256. For some models (e.g., ACCESS-ESM1.5) this is not sufficient to run with the default configuration. This means the MPI configuration of the components must be changed. This process is outlined below for some of the model components used in ACCESS models:

* __UM7__: In `atmosphere/um_env.yaml`, change `UM_ATM_NPROCX` and `UM_ATM_NPROCY`, which describe the number of chunks in the x and y directions, as well as `UM_NPES` to the product of `UM_ATM_NPROCX` and `UM_ATM_NPROCY`. In `config.yaml`, change the `atmosphere: ncpus` to be the same as `UM_NPES`.
* __MOM5__: In `ocean/input.nml`, change `layout` in the `&ocean_model_nml` namelist, which describes the number of chunks in the x and y directions in `nx,ny` format. In `config.yaml`, change the `ocean: ncpus` to the product of `nx` and `ny`.
* __CICE4__: To change the number of processes used by _CICE4_, the _CICE4_ executable needs to be recompiled. This requires the user to modify their own _Spack_ installation. In the user's Spack installation, in `access-spack-packages/spack_repo/access/nri/packages/cice4/package.py`, modify the entries in the `__targets` dictionary to the desired number of processes and blocks (the product of the blocks must be the same as the processes). The resulting executable name is `cice_<driver>_<grid>_<blocks>_<nprocs>p.exe`, which must be specified in the `config.yaml`. In the configuration's `ice/cice_in.nml`, change `nprocs` in the `&domain_nml` namelist to the desired number of processes. Finally, in the `config.yaml`, change the `ice: ncpus` to the desired number of processes.
* __CICE5__: To change the number of processes used by CICE5, the CICE5 executable needs to be recompiled, and the new blocksizes need to be specified. In `spack.yaml`, modify or add the [five variants _nxglob_, _nyglob_, _blckx_, _blcky_, _mxblcks_](https://github.com/search?q=repo%3AACCESS-NRI%2Faccess-spack-packages+%5C%22nxglob%5C%22+%5C%22nyglob%5C%22+%5C%22blckx%5C%22+%5C%22blcky%5C%22+%5C%22mxblcks%5C%22&type=code) to the desired number of processes and blocks. For ACCESS-ESM1.6, nprocs must be a divisor of _nxglob_(=360), therefore set _blckx = 360/nprocs_ and _mxblcks=1_. For ACCESS-OM2, there are more options (see Section 4.7 of the CICE5 [documentation](https://github.com/ACCESS-NRI/cice5/blob/master/doc/cicedoc.pdf)). In the configuration's `ice/cice_in.nml`, change `nprocs` in the `&domain_nml` namelist to the desired number of processes. Finally, in the `config.yaml`, change the executable name to the new build and change `ice: ncpus` to the desired number of processes.
* __ACCESS-OM3__: In `nuopc.runconfig` change `_ntasks` for each model component to be less than or equal to 256. Change `_rootpe` for every component to 0 (or such that `_rootpe` + `_ntasks` is less than 256). In `MOM_Input`, add `AUTO_MASKTABLE = True`, and remove entries for `MASKTABLE`, `LAYOUT` and `IO_LAYOUT`. Finally in `config.yaml`, change `ncpus` to the desired number of processes.

For the example above, the number of processes requested is larger than the number allowed by _Linaro Forge_. Therefore, changes to the atmosphere (UM) and ocean (MOM5) decompositions are required. For this reason, we will reduce the number of processes to 16 for UM and to 12 for MOM5. As CICE4 only requests 12 processes, this can be kept as is. The updated configuration would look like the following:

In `config.yaml`:
```
submodels:
    name: atmosphere
    model: um
    ncpus: 16
    exe: <path_to_UM7_install>/bin/um_hg3.exe
...
    name: ocean
    model: mom
    ncpus: 12
    exe: <path_to_MOM_install>/bin/fms_ACCESS-CM.x
...
    name: ice
    model: cice
    ncpus: 12
    exe: <path_to_CICE_install>/bin/cice_access_360x300_12x1_12p.exe
...
manifest:
  reproduce:
    exe: False

mpi:
  runcmd: ddt --connect mpirun
```

In `atmosphere/um_env.yaml`:
```
...
UM_ATM_NPROCX: '4'  # Decomposition that multiplies to 16
UM_ATM_NPROCY: '4'
UM_NPES: '16'
...
```

In `ocean/input.nml`:
```
...
&ocean_model_nml
    layout = 4,3    # Decomposition that multiplies to 12
    ...
/
...
```

<custom-references>
- [https://spack.readthedocs.io/en/latest/](https://spack.readthedocs.io/en/latest/)
- [https://spack-tutorial.readthedocs.io/en/latest/tutorial_developer_workflows.html](https://spack-tutorial.readthedocs.io/en/latest/tutorial_developer_workflows.html)
</custom-references>
