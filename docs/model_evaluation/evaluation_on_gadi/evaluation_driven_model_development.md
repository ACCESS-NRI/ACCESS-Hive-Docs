# Evaluation-Driven Model Development

The next generation of ACCESS models (ACCESS-OM3, ACCESS-CM3 and ACCESS-AM3) is being evaluated **in the open**, by the community and ACCESS-NRI working together.
ACCESS-CM3 is the precursor to ACCESS-ESM3.

- Each model has a shared GitHub repository where anyone can propose a diagnostic, build a figure and comment on results.
- Contributors can become co-authors on the respective model description paper.
- High-value community diagnostics are rerun with new simulations, feeding directly into model development.

This means model development is shaped by researchers' needs. The diagnostics you prioritise and parameter changes you propose help shape the next model run, increasing the likelihood of reduced biases for your application.

???+ tip "Open to everyone, at every career stage"
    Contributions from all career stages and backgrounds are welcome, including students, early-career researchers, engineers, domain scientists and first-time *GitHub* users. You don’t need to code to contribute: a comment, discussion point or suggested experiment can make a valuable difference.

## Ways to get involved

Choose a level that suits your time. Select a step to jump to its section.

<div class="contribution-ladder">
    <a href="#1-attend-the-meetings">
        <span class="ladder-number">1</span>
        <span class="bold">Attend the meetings</span>
        <span>Share figures, propose diagnostics and help set priorities.</span>
        <span class="ladder-needs">Needs: <i>Zoom</i> and an ACCESS-Hive Forum account</span>
    </a>
    <a href="#2-give-feedback-on-github">
        <span class="ladder-number">2</span>
        <span class="bold">Give feedback on GitHub</span>
        <span>Comment on figures in issues, suggest a metric or review a pull request.</span>
        <span class="ladder-needs">Needs: a <i>GitHub</i> account</span>
    </a>
    <a href="#3-create-analysis-notebooks">
        <span class="ladder-number">3</span>
        <span class="bold">Create analysis notebooks</span>
        <span>Turn a diagnostic idea into a figure in a shared repository.</span>
        <span class="ladder-needs">Needs: <i>GitHub</i> and an NCI account with project access</span>
    </a>
    <a href="#4-run-sensitivity-tests">
        <span class="ladder-number">4</span>
        <span class="bold">Run sensitivity tests</span>
        <span>Run your own experiments exploring specific parameter choices.</span>
        <span class="ladder-needs">Needs: all of the above, plus an NCI compute project</span>
    </a>
</div>
<div class="contribution-ladder-axis"><span>Less time</span><span>More time and coding</span></div>

### 1. Attend the meetings

Each ACCESS-Hive Forum thread below has the latest joining details, including *Zoom* links. Turn on notifications using the bell icon at the bottom of a thread to hear about upcoming meetings.

| Model | Meeting | How to join |
|---|---|---|
| ACCESS-OM3 | _ACCESS-OM3 Model Evaluation Team_ | [ACCESS-OM3 model evaluation team announcements](https://forum.access-hive.org.au/t/access-om3-model-evaluation-team-announce/4476) |
| ACCESS-CM3 | _CM3 Dev-Eval Working Group_ | [CM3 Dev-Eval meeting minutes](https://forum.access-hive.org.au/t/cm3-dev-eval-working-group-meeting-minutes/5393) |
| ACCESS-AM3 | Meeting details TBC | [AM3 high-resolution evaluation](https://forum.access-hive.org.au/t/we-need-your-help-am3-hi-res-evaluation/6438) |

At meetings you can propose a topic, share figures for live feedback and suggest parameter changes to test in the next model run.

### 2. Give feedback on GitHub

Feedback on figures requires no coding; all you need is a [GitHub](https://github.com/signup) account.
Each repository has a _mega-issue_ that tracks diagnostics and figures in progress: [ACCESS-OM3](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23), [ACCESS-CM3](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/1) and [ACCESS-AM3](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/1).
Comment on results, suggest metrics or review others' pull requests.

For ACCESS-OM3, you can also browse the [latest evaluation](https://access-om3-paper-1.readthedocs.io/latest/) and follow a figure's link to its GitHub issue to leave a comment.

### 3. Create analysis notebooks

Contribute a diagnostic notebook to one of the shared evaluation repositories.
Each repository's `README` explains how to request access, which NCI projects you need and how to add a notebook.

#### The evaluation repositories

All three repositories follow the same workflow: request write access, choose a diagnostic from the *mega-issue*, add a notebook and share your figure. Select a model below to get started.

<div class="tabLabels" label="evaluation-driven-development-models" style="margin-bottom: 0.5rem;">
    <button id="om3">ACCESS-OM3</button>
    <button id="cm3">ACCESS-CM3</button>
    <button id="am3">ACCESS-AM3</button>
</div>
<div tabcontentfor="om3" markdown>
Ocean–sea ice model evaluation, with [ACCESS-OM2](/models/access_models/access-om) as the baseline for comparison.

- **Repository:** [ACCESS-Community-Hub/access-om3-paper-1](https://github.com/ACCESS-Community-Hub/access-om3-paper-1)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/new?template=add-user-request-to--access-om3-paper-1--repository-.md)
- **Find a diagnostic:** [OM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23)
- **Simulations to evaluate:** [ACCESS-OM3 experiments](https://access-om3-configs.access-hive.org.au/latest/Experiments/)
- **Browse the evaluation:** see the [latest simulation's evaluation](https://access-om3-paper-1.readthedocs.io/latest/), or browse past simulations through the _Evaluation_ link on each run in the [ACCESS-OM3 experiments](https://access-om3-configs.access-hive.org.au/latest/Experiments/) table.
- **NCI projects:** `zv30`, `p73`, `ol01`, `ik11`, `av17`

!!! info
    Diagnostics in this repository also run on ACCESS-CM3. If your ocean or sea ice diagnostic applies to both models, contribute it here.

!!! warning
    This repository uses a _git_ submodule. Clone it with `git clone --recurse-submodules`.
</div>
<div tabcontentfor="cm3" markdown>
Coupled model evaluation, with [ACCESS-CM2](/models/access_models/access-cm) as the baseline for comparison.

- **Repository:** [ACCESS-Community-Hub/access-cm3-paper-1](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/new?template=add-user-request-to--access-cm3-1-repository-.md)
- **Find a diagnostic:** [CM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/1)
- **Simulations to evaluate:** [ACCESS-CM3 experiments](https://access-cm3-configs.readthedocs.io/Experiments/)
- **NCI projects:** `zv30`, `p73`, `eg3`, `ct11`, `ik11`

!!! info
    Ocean and sea ice diagnostics from the ACCESS-OM3 repository, and atmosphere diagnostics from the ACCESS-AM3 repository, are also run on ACCESS-CM3.
    If your diagnostic is relevant to ACCESS-OM3 or ACCESS-AM3 as well, add it to that repository instead.

!!! warning
    This repository uses a _git_ submodule. Clone it with `git clone --recurse-submodules`.
</div>
<div tabcontentfor="am3" markdown>
<!-- TODO (AM3 team, GitHub user paocorrales): please review/expand the AM3 content below (baseline model, meetings, NCI projects). -->
Atmosphere-only model evaluation, currently focused on the high-resolution (N512) configuration.

- **Repository:** [ACCESS-Community-Hub/access-am3-evaluation](https://github.com/ACCESS-Community-Hub/access-am3-evaluation)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/new?template=add-user-request-to--access-cm3-1-repository-.md)
- **Find a diagnostic:** [AM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/1)
- **Current focus:** [AM3 high-resolution evaluation](https://forum.access-hive.org.au/t/we-need-your-help-am3-hi-res-evaluation/6438)

!!! info
    Diagnostics in this repository are also run on ACCESS-CM3.
    If your atmosphere diagnostic is relevant to both models, add it here.
</div>

### 4. Run sensitivity tests

As an advanced contribution, run sensitivity experiments to test specific parameter choices and feed results into model development. See the [community-run ACCESS-OM3 sensitivity tests](https://access-om3-configs.access-hive.org.au/latest/Experiments/#community-run-sensitivity-tests) for an example.
You'll need an NCI compute project. If you're unsure whether your results can be incorporated, raise it at a [meeting](#1-attend-the-meetings) first.

## Support

<!-- TODO: confirm the wording below with the ACCESS-OM3, ACCESS-CM3 and ACCESS-AM3 teams and MED before merging. -->

These are community projects, and support and maintenance arrangements are specific to each project.
They are not maintained by the ACCESS-NRI Model Evaluation and Diagnostics (MED) team.

- **Who supports the workflows:** each repository is run by its model team. Ask questions at the [meetings](#1-attend-the-meetings) or in the relevant mega-issue.
- **After the paper is published:** notebooks remain available alongside the model description paper as a record of the analysis. There is no commitment to keep every notebook working with new simulations or software environments; the model teams may choose to maintain diagnostics that stay useful for ongoing model development.
- **General help:** for help with _Gadi_, ARE or ACCESS-NRI software environments, see [User support](/about/user_support/) or post on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/).
