# Set Up your NCI Account

The steps in this section are aimed at new users who would like to do any of the following tasks:

- Run their own experiment
- Analyse model data outputs
- Browse observational data catalogues
- Evaluate model performance
- Perform other tasks involving ACCESS models or evaluation tools


## Create an NCI user account

Most of the data and models you will need are available at the [National Computing Infrastructure (NCI)](https://nci.org.au/about-us/who-we-are).<br>
To access these, you need an [NCI account](https://opus.nci.org.au/display/Help/How+to+create+an+NCI+user+account). If you do not have one, [sign up here](https://my.nci.org.au/mancini/signup/0").

!!! warning
    You will need an institutional email address with an organisation that allows access to NCI (e.g., an Australian university, ACCESS-NRI, CSIRO, BoM, CLEX, etc.).
    
Once you sign up, you will be assigned a _username_ (e.g., `ab1234`).


## Join relevant NCI projects

NCI provides multiple [services](https://nci.org.au/our-services) that are necessary for climate research. These include the access to supercomputing resources, data storage, and data collections management.

For technical reasons, to access either of these services you need to join a specific `project`.
Each project has an ID (e.g. `xp65`), which is what the term _project_ actually refers to.

If you are interested in datasets and data collections, you can browse the [NCI Data Catalogue](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/search) and follow the [NCI Data Catalogue User Guide](https://opus.nci.org.au/display/Help/Data+Catalogue+User+Guide).

To run models on _Gadi_ instead, you need to join a project with computing resources, also called _Service Units (SU)_. The project ID will be provided by your supervisor, research project or institution.

To join a project, search for it on [NCI website](https://my.nci.org.au/mancini/project-search) and request membership.

!!! tip
    The first project you join will become your default one. If you would like to change this, check out [how to change your default project on Gadi](/getting_started/set_up_nci_account#change-default-project-on-gadi).

There are several NCI projects that may be relevant to you, depending on the tasks you want to carry out.<br>
For tasks supported by ACCESS-NRI (e.g., running a supported model configuration, using a supported model evaluation tool, etc.), you will find a list of relevant projects to join in the pages relative to each respective task.


## Login to Gadi
<div class="tabLabels" label="systems">
    <button id="macos">MacOS</button>
    <button id="linux">Linux</button>
    <button id="windows">Windows</button>
</div>
Operations involving model runs and data collections take place on the [_Gadi_ supercomputer](https://nci.org.au/our-systems/hpc-systems).

### Prerequisites
- **Internet connection**
- **Terminal with built-in SSH**<br>
    <span tabcontentfor="linux">Linux</span><span tabcontentfor="macos">MacOS</span><span tabcontentfor="windows">Windows 10 (or later)</span> operative system already has a terminal with built-in SSH.<br>
    <div tabcontentfor="windows" markdown>
    Users of Windows 9 (or earlier) can install [Windows Subsystems for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl).
    
    !!! tip
        Alternatively, you can login through the [ARE Gadi Terminal](https://are.nci.org.au/pun/sys/shell/ssh/gadi.nci.org.au).<br>
        However, it is recommended that you connect to _Gadi_ from your local machine's terminal without using ARE. 
    </div>
<div tabcontentfor="windows" markdown>

- **git-bash**<br>
  You can install `git` and `git-bash` at [this link](https://git-scm.com/downloads).
</div>


To login to _Gadi_ using [SSH](https://en.wikipedia.org/wiki/Secure_Shell), on your **local machine's terminal** run the following command, replacing `<your-NCI-username>` with your NCI _username_ (e.g., `ab1234`):

```
ssh <your-NCI-username>@gadi.nci.org.au
```

You will be prompted to enter your NCI password, and then you will be connected to _Gadi_:
<terminal-window lineDelay=0>
    <terminal-line data="input" lineDelay=300>ssh &lt;your-NCI-username&gt;@gadi.nci.org.au</terminal-line>
    <terminal-line lineDelay=300>&lt;NCI-username&gt;@gadi.nci.org.au's password: <i class="icon-key" style="display: inline-block; font-size: 0.4em; transform: rotate(-90deg);"></i></terminal-line>
    <terminal-line lineDelay=3000>###############################################################################</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Welcome to the NCI National Facility!&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;This service is for authorised clients only. It is a criminal&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;offence to:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Obtain access to data without permission;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Damage, delete, alter or insert data without permission;&emsp;&nbsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;Use of this system requires acceptance of the Conditions of Use;&emsp;&emsp;&emsp;&emsp;#</terminal-line>
    <terminal-line>#&emsp;&emsp;&emsp;&emsp;published at https://nci.org.au/users/nci-terms-and-conditions-access ;&emsp;#</terminal-line>
    <terminal-line>###############################################################################</terminal-line>
    <terminal-line>|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;gadi.nci.org.au - 260,760 processor InfiniBand x86_64 cluster&emsp;&emsp;&nbsp;&nbsp;&nbsp;|</terminal-line>
    <terminal-line>===============================================================================</terminal-line>
    <terminal-line>===============================================================================</terminal-line>
    <terminal-line data="input" lineDelay=200></terminal-line>
</terminal-window>

### Automatic login

To simplify the login and avoid being prompted every time to enter your NCI password, follow these steps:

#### Create an SSH key
To create an SSH key, in your **local machine's <span tabcontentfor="windows" markdown>`git-bash` </span>terminal** run:
```
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -f ~/.ssh/id_gadi
```
You will be prompted to create a passphrase linked to the SSH key, which you will enter twice:
<terminal-window>
    <terminal-line data="input">mkdir -p ~/.ssh</terminal-line>
    <terminal-line data="input">ssh-keygen -t ed25519 -f ~/.ssh/id_gadi</terminal-line>
    <terminal-line>Generating public/private rsa key pair.</terminal-line>
    <terminal-line>Enter passphrase (empty for no passphrase):</terminal-line>
    <terminal-line lineDelay=3000>Enter same passphrase again:</terminal-line>
    <terminal-line lineDelay=3000>Your identification has been saved in &lt;$HOME&gt;/.ssh/id_gadi</terminal-line>
    <terminal-line>Your public key has been saved in &lt;$HOME&gt;/.ssh/id_gadi.pub</terminal-line>
    <terminal-line lineDelay=0>The key fingerprint is:</terminal-line>
    <terminal-line lineDelay=0>SHA256:&lt;fingerprint-code&gt; &lt;$USER@hostname&gt;</terminal-line>
    <terminal-line lineDelay=0>The key's randomart image is:</terminal-line>
    <terminal-line lineDelay=0>+--[ED25519 256]--+</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>|xxxxxxxxxxxxxxxxx|</terminal-line>
    <terminal-line lineDelay=0>+----[SHA256]-----+</terminal-line>
</terminal-window>

!!! warning
    For security reasons, it is recommended to enter a passphrase rather than leave it empty.<br>
    As you will see in the next step, you will not need to enter the passphrase every time you login to _Gadi_.

#### Add the SSH key to the SSH-agent

An SSH-agent is an SSH key manager that avoids you having to enter your passphrase every time you connect to a server.<br>
To add the SSH key to the SSH-agent, in your **local machine's <span tabcontentfor="windows" markdown>`git-bash` </span>terminal** run:

<pre><code>eval "$(ssh-agent -s)"
ssh-add <span tabcontentfor="macos" markdown>--apple-use-keychain </span>~/.ssh/id_gadi</code></pre>

You will be prompted to enter your SSH key passphrase, which will be stored inside the SSH-agent:
<terminal-window>
    <terminal-line data="input">eval "$(ssh-agent -s)"</terminal-line>
    <terminal-line>Agent pid &lt;agent-PID&gt;</terminal-line>
    <terminal-line data="input">ssh-add <span tabcontentfor="macos" markdown>--apple-use-keychain</span> ~/.ssh/id_gadi</terminal-line>
    <terminal-line>Enter passphrase for &lt;$HOME&gt;/.ssh/id_gadi:</terminal-line>
    <terminal-line lineDelay=3000>Identity added: &lt;$HOME&gt;/.ssh/id_gadi &lt;$USER@hostname&gt;</terminal-line>
    </terminal-window>
</terminal-window>
<div tabcontentfor="macos" markdown>
    
!!! warning
    If you are using a MacOS version prior to Monterey (12.0), substitute the `--apple-use-keychain` flag with `-K`.
</div>

#### Create/Update the SSH config file
The `~/.ssh/config` is a file where you can store labelled SSH configurations for different remote servers you regularly connect to, so you do not have to remember them all.<br>
To create an SSH config file and add (append) the SSH configuration for _Gadi_, in your **local machine's <span tabcontentfor="windows" markdown>`git-bash` </span>terminal** run (by replacing `<your-NCI-username>` with your NCI _username_, e.g., `ab1234`):
<pre><code>cat >> ~/.ssh/config << EOF
Host gadi
Hostname gadi.nci.org.au
User &lt;your-NCI-username&gt;
ForwardX11 true
ForwardX11Trusted yes
IdentityFile ~/.ssh/id_gadi
AddKeysToAgent yes
ForwardAgent yes
<span tabcontentfor="macos" markdown>UseKeychain yes<br></span>EOF</code></pre>

!!! warning
    If you have an existing `~/.ssh/config` file which contains hosts with wildcards  (`*`) in their names so that `gadi` would be included in the wildcard expansion (e.g., `Host *`), make sure you don't duplicate any of the SSH configuration keywords above.

#### Add the SSH key to the authorised keys
To enable automatic connection to a server, that server needs to recognise the SSH key as _authorised_. The list of authorised keys for a certain server is stored in the file `~/.ssh/authorized_keys`.<br>
To add the newly created SSH key as an _authorised_ key for _Gadi_, in your **local machine's <span tabcontentfor="windows" markdown>`git-bash` </span>terminal** run the following command:
```
ssh gadi "mkdir -p .ssh && cat >> .ssh/authorized_keys <<< '$(cat ~/.ssh/id_gadi.pub)'"
```

You will be prompted to enter your NCI password. If you did all of the above steps correctly, this should be the last time you need to do so.

!!! success
    Your automatic _Gadi_ connection is set up! 
    
    Now you should be able to connect to _Gadi_ from your **local machine's terminal** simply by running:
    ```
    ssh gadi
    ```

### Change default project on Gadi

It is recommended that you check what your default project on _Gadi_ is set to. The default project should be set to the computational project you will most likely use to run simulations/evaluations and store data.<br>
You can check which is your default project by logging into _Gadi_ and running:
```
echo $PROJECT
```

To change your default project on _Gadi_, you need to manually change the `PROJECT` field in the `~/.config/gadi-login.conf` file.<br>
Alternatively, you can run the following command **on _Gadi_'s terminal** (by substituting `<new-default-project>` with the project you want to set as default):
```
sed -i "s/\(PROJECT \)\w*/\1<new-default-project>/" ~/.config/gadi-login.conf
```

Once this is done, exit from _Gadi_ and log back in.
<br>
For example, if you want to change your default project to `tm70` on _Gadi_:
<terminal-window>
    <terminal-line data="input">echo $PROJECT</terminal-line>
    <terminal-line>&lt;old-default-project&gt;</terminal-line>
    <terminal-line data="input">sed "s/\(PROJECT \)\w*/\1tm70/" ~/.config/gadi-login.conf</terminal-line>
    <terminal-line data="input">exit</terminal-line>
    <terminal-line>logout</terminal-line>
    <terminal-line>Connection to gadi.nci.org.au closed.</terminal-line>
    <terminal-line data="input" PS1="&lt;span style='color: #9734bb;'&gt;(User PC)$ &lt;/span&gt;">ssh gadi</terminal-line>
    <terminal-line>###############################################################################</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Welcome to the NCI National Facility!&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;This service is for authorised clients only. It is a criminal&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;offence to:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Obtain access to data without permission;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Damage, delete, alter or insert data without permission;&emsp;&nbsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;Use of this system requires acceptance of the Conditions of Use;&emsp;&emsp;&emsp;&emsp;#</terminal-line>
    <terminal-line lineDelay=0>#&emsp;&emsp;&emsp;&emsp;published at https://nci.org.au/users/nci-terms-and-conditions-access ;&emsp;#</terminal-line>
    <terminal-line lineDelay=0>###############################################################################</terminal-line>
    <terminal-line lineDelay=0>|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;gadi.nci.org.au - 260,760 processor InfiniBand x86_64 cluster&emsp;&emsp;&nbsp;&nbsp;&nbsp;|</terminal-line>
    <terminal-line lineDelay=0>===============================================================================</terminal-line>
    <terminal-line lineDelay=0>===============================================================================</terminal-line>
    <terminal-line data="input">echo $PROJECT</terminal-line>
    <terminal-line>tm70</terminal-line>
</terminal-window>

<custom-references>
- [https://nci.org.au](https://nci.org.au)
- [https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi)
- [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [https://linuxize.com/post/using-the-ssh-config-file](https://linuxize.com/post/using-the-ssh-config-file)
</custom-references>

<!-- Custom style for tabs within markdown bullet point (to avoid extra space) -->
<style>
    #prerequisites + ul,
    #prerequisites + ul p:has(+ [tabcontentfor="windows"]) {
        margin-bottom: 0;
    }
    #prerequisites + ul + [tabcontentfor="windows"] > ul {
        margin-top: 0;
    }
</style>