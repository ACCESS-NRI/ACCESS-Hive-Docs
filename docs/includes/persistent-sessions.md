<!--start:pers-session-about-->
NCI provides a service called [_persistent sessions_](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions) to enable long running processes, like _Cylc_, to stay active even when the user disconnects from _Gadi_.

It is recommended to have only one active persistent session at any given time, as multiple _Cylc_ sessions can use the same persistent session.

Persistent sessions are terminated during NCI's quarterly maintenance and must be restarted afterwards. You can give the new session the same name as the previous one to minimise additional setup.<!--end:pers-session-about-->

<!--start:pers-session-start-->
### Start a new persistent session

Start a new persistent session by running:

```
persistent-sessions start -p <project> <name>
```

where `<project>` is the project you want to start the session under, and `<name>` is the name you want to give your persistent session. 

!!! warning
    Persistent session names support only a limited character set. Use alphanumeric characters only - no spaces or underscores.

<terminal-window data="input">
    <terminal-line>persistent-sessions start -p &lt;project&gt; &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

Persistent session names use the following format: <br>
`<name>.<$USER>.<project>.ps.gadi.nci.org.au`.<br>
Persistent session are also assigned a unique identifier, referred to here as `<persistent-session-uuid>`.

!!! tip
    If `-p <project>` is omitted, your [default project](/getting_started/set_up_nci_account/#change-default-project-on-gadi) `$PROJECT` will be used.

!!! tip 
    The project assigned to a persistent session does not need to match the project used to run the ACCESS model configuration. A single persistent session can also run multiple simulations simultaneously.<br>

!!! tip
  
    When restarting a persistent session after a _Gadi_ outage, such as a quarterly maintenance, reuse the same name as before to avoid additional setup. You do not need to assign the persistent session to _Cylc_ again. Check `~/.persistent-sessions/cylc-session` to confirm the name and reuse it.
<!--end:pers-session-start-->

<!--start:pers-session-assign-->
### Assign the persistent session to _Cylc_ (once only) {: #assign-the-persistent-session-to-cylc }

Once the persistent session is running, assign it to _Cylc_ by inserting its label into `~/.persistent-sessions/cylc-session`. Run the following command, replacing `<name>` and `<project>` with the values used to create the persistent session.

```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

You can check that this worked with:

```
cat ~/.persistent-sessions/cylc-session
```

For example, if user `abc123` starts a persistent session named `ForCylc` under the project `tm70`, the command is:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">ForCylc.abc123.tm70.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

For more information on how to assign the persistent session, refer to [Specify Target Session for Cylc8](https://opus.nci.org.au/spaces/DAE/pages/252674295/Run+Cylc8+Suites#RunCylc8Suites-SpecifyTargetSession).
<!--end:pers-session-assign-->

<!--start:pers-session-setup-->
### Setup connection between _Gadi_ and _Cylc_
!!! tip

    Although this step is only required the first time you use _Cylc_, you can repeat it at any time without adverse effects if you are unsure whether your setup is correct.

For security reasons, communication between _Gadi_ and the persistent session is restricted. Before using _Cylc_, you need to create a dedicated SSH key by running the following command:

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

After a period of inactivity, you may need to check whether your _Cylc_ persistent session is still active. To list your active persistent sessions, use:

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
    When you terminate a persistent session, any model running in that session will stop. Before terminating a session, check whether you have any active model runs.
<!--end:pers-session-terminate-->
