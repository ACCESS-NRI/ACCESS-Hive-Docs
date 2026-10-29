# Evaluation-Driven Model Development

The next generation of ACCESS models (ACCESS-OM3, ACCESS-CM3 and ACCESS-AM3) is being evaluated **in the open**, by the community and ACCESS-NRI working together.
ACCESS-CM3 is the precursor to ACCESS-ESM3.

- Each model has a shared GitHub repository where anyone can propose a diagnostic, build a figure and comment on results.
- Contributors can become co-authors on the model description paper.
- Diagnostics of high community value are re-run on each new simulation, so they feed directly back into model development.

This means model development is shaped by researchers' needs.
The diagnostics you prioritise and the parameter changes you propose feed into the next model run, so the resulting model is more likely to have reduced biases for your application of interest.

???+ tip "Open to everyone, at every stage"
    Contributions from people of all career stages and backgrounds are highly encouraged: students, early-career researchers, engineers, domain scientists and first-time _GitHub_ users.
    You don't need to be a coder. A comment, a discussion point or a suggested experiment is a contribution too.

## Overview: Ways to get involved

Pick the level that suits the time you have. Every level is valuable. Select a step to jump to its section below.

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
        <span>Turn a diagnostic idea into a figure that is re-run on new simulations.</span>
        <span class="ladder-needs">Needs: <i>GitHub</i> and an NCI account with project access</span>
    </a>
    <a href="#4-run-sensitivity-tests">
        <span class="ladder-number">4</span>
        <span class="bold">Run sensitivity tests</span>
        <span>Run your own experiments exploring specific parameter choices, to feed into model development.</span>
        <span class="ladder-needs">Needs: all of the above, plus an NCI compute project</span>
    </a>
</div>
<div class="contribution-ladder-axis"><span>Less time</span><span>More time and coding</span></div>

### 1. Attend the meetings

The easiest way to get involved is to come along to a meeting: turn up, listen, and pick up a small task.
Each forum thread below has the latest joining details, including _Zoom_ links.

| Model | Meeting | How to join |
|---|---|---|
| ACCESS-OM3 | _ACCESS-OM3 Model Evaluation Team_, monthly on Thursdays | [ACCESS-OM3 model evaluation team announcements](https://forum.access-hive.org.au/t/access-om3-model-evaluation-team-announce/4476) |
| ACCESS-CM3 | _CM3 Dev-Eval Working Group_, monthly on Tuesdays | [CM3 Dev-Eval meeting minutes and joining details](https://forum.access-hive.org.au/t/cm3-dev-eval-working-group-meeting-minutes/5393) |
| ACCESS-AM3 | No standing public meeting yet | [AM3 high-resolution evaluation thread](https://forum.access-hive.org.au/t/we-need-your-help-am3-hi-res-evaluation/6438) |

At the meetings you can:

1. **Propose a discussion:** add a topic to the agenda, or bring it up on the day.
2. **Share figures:** walk the group through a plot or result and get feedback live.
3. **Suggest parameter changes:** flag a parameter or configuration change worth testing in the next model run.

???+ tip "Have an idea for the next model run?"
    Bring your parameter or configuration ideas to a meeting, or get in touch with a team lead:

    - ACCESS-OM3: [Christopher Bull](https://www.access-nri.org.au/person/christopher-bull/), Ocean Model Team Lead
    - ACCESS-CM3: [Martin Dix](https://www.access-nri.org.au/person/martin-dix/), Associate Director, Model Development
    - ACCESS-AM3: [Heidi Nettelbeck](https://www.access-nri.org.au/person/heidi-nettelbeck/), Atmosphere Model Team Leader

Turn on notifications for a thread (the bell icon at the bottom of a forum thread) to hear about each upcoming meeting.

### 2. Give feedback on GitHub

**Feedback on figures is one of the most valuable contributions you can make**, and it needs no coding: a [GitHub](https://github.com/signup) account is all you need.

1. **Browse open issues:** each repository's mega-issue tracks every diagnostic and figure in progress: [ACCESS-OM3](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23), [ACCESS-CM3](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/1) and [ACCESS-AM3](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/1).
2. **Comment directly:** question a result, suggest a metric or flag something odd, in the issue that discusses that diagnostic.
3. **Review:** comment on someone else's figure or pull request. [ReviewNB](https://www.reviewnb.com/) shows notebook changes cell by cell.

For ACCESS-OM3, you can also browse the [latest evaluation](https://access-om3-paper-1.readthedocs.io/latest/) and follow a figure's link to its GitHub issue to leave a comment.

### 3. Create analysis notebooks

Turn a diagnostic idea into a figure in one of the shared evaluation repositories.
You'll need a _GitHub_ account and an [NCI account](/getting_started/set_up_nci_account) with access to the projects listed for each model.

#### Is this the right workflow for me?

This workflow uses flexible notebooks on native model output, and is designed for the development phase.
For automated, multi-model comparisons on CMORised data, see [Intercomparison and benchmarking](/model_evaluation/evaluation_on_gadi#two-kinds-of-model-evaluation).

These strengths and limitations can help you decide whether this workflow suits your question.

???+ success "Strengths"
    - Community-prioritised assessment of ACCESS models (ACCESS-OM3, ACCESS-CM3 and ACCESS-AM3) for model development.
    - Opportunities for model description paper co-authorship.
    - Code review is optional, so you can do and share your analysis quickly. Open a pull request only if you'd like feedback on your code.
    - Centralised, reproducible analysis on [ARE](/getting_started/are), using native model output and familiar _Python_ libraries in notebooks.
    - Comparisons to previous model generations and observations.
    - The same workflow for all three models.

???+ warning "Limitations"
    - Notebooks can be tricky to maintain and review: _git_ diffs are hard to read without tools such as [ReviewNB](https://www.reviewnb.com/).
    - Focused on the ACCESS family of models, not CMIP.
    - Large multi-model comparisons and international evaluation efforts are better suited to [intercomparison and benchmarking](/model_evaluation/evaluation_on_gadi#two-kinds-of-model-evaluation) tools such as ESMValTool.

#### The evaluation repositories

All three repositories share the same pattern: request write access, find a diagnostic in the _mega-issue_, add a notebook and share your figure.
Choose a model below for its links.

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
    Diagnostics in this repository are also run on ACCESS-CM3.
    If your ocean or sea ice diagnostic is relevant to both models, add it here.

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

#### From diagnostic idea to figure

Each repository's `README` is the step-by-step guide. In outline:

<div class="workflow-steps">
    <div><span class="workflow-number">1</span><span class="bold">Request access</span><span>Open an access request issue in the repository</span></div>
    <div><span class="workflow-number">2</span><span class="bold">Find a diagnostic</span><span>Claim or suggest one in the mega-issue</span></div>
    <div><span class="workflow-number">3</span><span class="bold">Clone the repository</span><span>On <i>Gadi</i>, then start an <a href="/getting_started/are">ARE</a> session</span></div>
    <div><span class="workflow-number">4</span><span class="bold">Write a notebook</span><span>Start from the template notebook</span></div>
    <div><span class="workflow-number">5</span><span class="bold">Commit and push</span><span>To <code>main</code>, or to a branch with a pull request for review</span></div>
    <div><span class="workflow-number">6</span><span class="bold">Share and get credit</span><span>Post your figure and commit hash in its issue, and add your name to <code>CITATION.cff</code></span></div>
</div>

### 4. Run sensitivity tests

As an advanced contribution, you can run your own sensitivity experiments that feed into model development.
Unlike control experiments, these explore specific parameter choices. For an example, see the [community-run sensitivity tests for ACCESS-OM3](https://access-om3-configs.access-hive.org.au/latest/Experiments/#community-run-sensitivity-tests).

You'll need everything from the steps above, plus an NCI compute project.
Talk to a [team lead](#1-attend-the-meetings) before you start, so your results can be picked up.

## Support

- Ask questions in the [meetings](#1-attend-the-meetings) or on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/).
- In-person "buddies" at most partner institutions can help if you're stuck getting started or would like to know what to work on.
- Diagnostics of high community value can be run on new simulations during the development phase.
- For general help, see [User support](/about/user_support).
