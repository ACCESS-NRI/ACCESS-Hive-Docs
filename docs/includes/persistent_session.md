To support the use of long-running processes, such as ACCESS model runs, NCI provides a service on _Gadi_ called [persistent sessions](https://opus.nci.org.au/display/Help/Persistent+Sessions).

To run {{ model }}, you need to start a persistent session and set it as the target session for the model run.

### Start a new persistent session
To start a new persistent session on _Gadi_, using either a login node or an ARE terminal instance, run the following command:
```
persistent-sessions start <name>
```

This will start a persistent session with the given `name` that runs under your [default project](/getting_started/set_up_nci_account#change-default-project-on-gadi).<br>
If you want to assign a different project to the persistent session, use the option `-p`:
```
persistent-sessions start -p <project> <name>
```

!!! tip
    While the project assigned to a persistent session does not have to be the same as the project used to run the {{ model }} configuration, it does need to have allocated _Service Units (SU)_.<br>
    For more information, check how to [Join relevant NCI projects](/getting_started/set_up_nci_account#join-relevant-nci-projects).

<terminal-window data="input">
    <terminal-line>persistent-sessions start &lt;name&gt;</terminal-line>
    <terminal-line data="output">session &lt;persistent-session-uuid&gt; running - connect using</terminal-line>
    <terminal-line data="output">&emsp;ssh &lt;name&gt;.&lt;$USER&gt;.&lt;project&gt;.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

To list all active persistent sessions run:
```
persistent-sessions list
```

<terminal-window data="input">
    <terminal-line>persistent-sessions list</terminal-line>
    <terminal-line data="output">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;UUID&emsp;&emsp;PROJECT&emsp;&ensp;&ensp;ADDRESS&emsp;&emsp;&emsp;&emsp;CPUTIME&emsp;MEMORY</terminal-line>
    <terminal-line data="output">&lt;persistent-session-uuid&gt;&emsp;&lt;project&gt;&emsp;10.9.0.62&emsp;00:00:05.213&emsp;30.5M</terminal-line>
</terminal-window>


The label of a newly-created persistent session has the following format: <br>
`<name>.<$USER>.<project>.ps.gadi.nci.org.au`.

### Specify {{ model }} target persistent session

After starting the persistent session, it is essential to assign it to the {{ model }} run.<br>
The easiest way to do this is to insert the persistent session label into the file `~/.persistent-sessions/cylc-session`.<br>
You can do it manually, or by running the following command (by substituting `<name>` with the name given to the persistent session, and `<project>` with the project assigned to it):
```
cat > ~/.persistent-sessions/cylc-session <<< "<name>.${USER}.<project>.ps.gadi.nci.org.au"
```

For example, if the user `abc123` started a persistent session named `cylc` under the project `xy00`, the command will be:

<terminal-window data="input">
    <terminal-line>cat > ~/.persistent-sessions/cylc-session <<< cylc.abc123.xy00.ps.gadi.nci.org.au</terminal-line>
    <terminal-line data="input" linedelay="1000">cat ~/.persistent-sessions/cylc-session</terminal-line>
    <terminal-line data="output">cylc.abc123.xy00.ps.gadi.nci.org.au</terminal-line>
</terminal-window>

For more information on how to specify the target session, refer to [Specify Target Session with Cylc7 Suites](https://opus.nci.org.au/display/DAE/Run+Cylc7+Suites#RunCylc7Suites-SpecifyTargetSession).

!!! tip
    You can simultaneously submit multiple {{ model }} runs using the same persistent session without needing to start a new one. Hence, the process of specifying the target persistent session for {{ model }} should only be done once.<br>
    After specifying the {{ model }} target persistent session the first time, to run {{ model }} you just need to make sure to have an active persistent session named like the specified {{ model }} target persistent session.

### Terminate a persistent session
To stop a persistent session, run:
```
persistent-sessions kill <persistent-session-uuid>
```
!!! warning
    When you terminate a persistent session, any model running on that session will stop. Therefore, you should check whether you have any active model runs before terminating a persistent session.
