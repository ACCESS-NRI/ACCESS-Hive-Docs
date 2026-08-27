<!--start:pers-session-about-->
NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to enable long running processes, like _Cylc_, to stay active even when the user disconnects from _Gadi_.

It is recommended to have only one active persistent session at any given time, as multiple _Cylc_ sessions can use the same persistent session.

Persistent sessions are terminated during the quarterly maintenance at NCI and will need to be restarted afterwards. The new persistent session can be given the same name as used previously, thus limiting the need for further setup steps.
<!--end:pers-session-about-->

<!--start:pers-session-start-->
### Start a new persistent session

Start a new persistent session by running:

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. 

!!! warning
    Persistent session names accept only a limited set of characters. We recommend using only alpha-numeric characters without spaces or underscores.

<terminal-window data="input">
    <terminal-line>persistent-sessions start -p &lt;project&gt; &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

The label of a newly-created _persistent session_ has the following format: <br>
`<name>.<$USER>.<project>.ps.gadi.nci.org.au`.<br>
The newly created persistent session is assigned a unique identifier, referred to here as `<persistent-session-uuid>`.

!!! tip
    If `-p <project>` is omitted, your [default project](/getting_started/set_up_nci_account/#change-default-project-on-gadi) `$PROJECT` will be used.

!!! tip 
    The project assigned to a _persistent session_ does not have to be the same one used to run the ACCESS model configuration. In addition, the same persistent session can be used to run multiple simulations simultaneously.<br>

!!! tip
  
    When restarting a persistent session after a _Gadi_ outage, for example the quarterly maintenance, if you use the same name as before, this is the only setup step you need to do. You do not need to assign the persistent session to _Cylc_ again. You can check the name of your persistent session in `~/.persistent-sessions/cylc-session` to make sure to reuse the same name.
<!--end:pers-session-start-->

<!--start:pers-session-assign-->
### Assign the persistent session to _Cylc_ (once only) {: #assign-the-persistent-session-to-cylc }

Once the session is running, it needs to be assigned to _Cylc_. This is done by inserting the persistent session label into `~/.persistent-sessions/cylc-session`, which can be done with the following command (substituting `<name>` and `<project>` with the name and project used to create the persistent session).

```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

You can check that this worked with:

```
cat ~/.persistent-sessions/cylc-session
```

For example, if user `abc123` started a persistent session named `ForCylc` under the project `tm70`, then the command would be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

For more information on how to specify the target session, refer to [Specify Target Session for Cylc8](https://opus.nci.org.au/spaces/DAE/pages/252674295/Run+Cylc8+Suites#RunCylc8Suites-SpecifyTargetSession).
<!--end:pers-session-assign-->

<!--start:pers-session-setup-->
### Setup connection between _Gadi_ and _Cylc_
!!! tip

    Although this step is only necessary before the first time you use _Cylc_, you can follow these instructions at any time without adverse effect if you are unsure whether your setup is correct.

The communication between _Gadi_ and the _persistent session_ is restricted for security reasons. You need to create a specific ssh key before any work with _Cylc_. For this, please run the following command:

```
/g/data/hr22/bin/gadi-cylc-setup-ps -y
```

A successful completion should print out:

```
+------------------------------------------------------------------------------+
| RESULT: PASSED                                                               |
+------------------------------------------------------------------------------+
```
<!--end:pers-session-setup-->

<!--start:pers-session-active-->
### List active persistent sessions {: .no-toc }

After a period of inactivity with _Cylc_, you might need to check if your persistent session is still active.

To list your currently active sessions, use:

```
persistent-sessions list
```
<!--end:pers-session-active-->

<!--start:pers-session-terminate-->
### Terminate a persistent session {: .no-toc }

To end a specific session, use:

```
persistent-sessions kill <persistent-session-uuid>
```

!!! tip
    Logging out of a *Gadi* login node or an ARE VDI terminal instance will not affect your _persistent session_.

!!! warning
    When you terminate a _persistent session_, any model running on that session will stop. Therefore, you should check whether you have any active model runs before terminating a _persistent session_.
<!--end:pers-session-terminate-->
