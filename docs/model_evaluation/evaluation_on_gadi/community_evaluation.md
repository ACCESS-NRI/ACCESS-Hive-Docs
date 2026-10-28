# Community Evaluation of ACCESS-CM3, AM3 and OM3

The next generation of ACCESS models is being evaluated **in the open**, by the community and ACCESS-NRI working together.
Each model has a shared GitHub repository where anyone can propose a diagnostic, build a figure, comment on results and become a co-author on the model description paper.
These figures feed directly back into model development: diagnostics of high community value are re-run on each new simulation.

<figure>
    <img src="/assets/model_evaluation/community_evaluation/community_figures_montage.jpg" alt="Collage of community-created ACCESS-CM3 and ACCESS-OM3 evaluation figures" class="white-background round-edges">
    <figcaption>
        A selection of community-created evaluation figures: ideal age tracer sections, El Niño/La Niña events, old-vs-new model Antarctic shelf properties, an ENSO scorecard against CMIP6 and observations, North Atlantic salinity and hemispheric sea-ice volume.
    </figcaption>
</figure>

???+ tip "Open to everyone, at every stage"
    Contributions from people of all career stages and backgrounds are highly encouraged: students, early-career researchers, engineers, domain scientists and first-time _GitHub_ users.
    You don't need to be a coder. A comment, a discussion point or a suggested experiment is a contribution too.

## Is this the right workflow for you?

There are two complementary kinds of model evaluation. Both are valid, and the difference is fit for purpose rather than capability.

| | During model development (this page) | Intercomparison and benchmarking |
|---|---|---|
| **Style** | Flexible notebooks and scripts on [ARE](/getting_started/are) | Automated, reproducible and scalable recipes |
| **Data** | Native ACCESS model output | [CMORised](https://access-moppy.readthedocs.io/en/latest/) output |
| **Focus** | ACCESS models, compared against observations and previous model generations | Full ensembles and multi-model comparisons, including CMIP |
| **Tools** | Familiar _Python_ libraries, or any language | [ESMValTool](/model_evaluation/evaluation_on_gadi/esmvaltool_workflow), [ILAMB](/model_evaluation/evaluation_on_gadi/ilamb_workflow) and the [Rapid Evaluation Framework (REF)](https://dashboard.climate-ref.org/) |

## Ways to get involved

Pick the level that suits the time you have. Every level is valuable.

<div class="contribution-ladder">
    <div>
        <span class="ladder-number">1</span>
        <span class="bold">Attend the meetings</span>
        <span>Share figures, propose diagnostics and help set priorities.</span>
        <span class="ladder-needs">Needs: <i>Zoom</i> and an <a href="https://forum.access-hive.org.au/">ACCESS-Hive Forum</a> account</span>
    </div>
    <div>
        <span class="ladder-number">2</span>
        <span class="bold">Give feedback on GitHub</span>
        <span>Comment on figures in issues, suggest a metric or review a pull request.</span>
        <span class="ladder-needs">Needs: a <a href="https://github.com/signup">GitHub</a> account</span>
    </div>
    <div>
        <span class="ladder-number">3</span>
        <span class="bold">Create analysis notebooks</span>
        <span>Turn a diagnostic idea into a figure that is re-run on new simulations.</span>
        <span class="ladder-needs">Needs: <i>GitHub</i> and an <a href="/getting_started/set_up_nci_account">NCI account</a> with project access</span>
    </div>
    <div>
        <span class="ladder-number">4</span>
        <span class="bold">Run sensitivity tests</span>
        <span>Test a parameter or configuration change for the next model run.</span>
        <span class="ladder-needs">Needs: all of the above, plus an NCI compute project</span>
    </div>
</div>
<div class="contribution-ladder-axis"><span>Less time</span><span>More time and coding</span></div>

## The evaluation repositories

All three repositories share the same pattern: request write access, find a diagnostic in the _mega-issue_, add a notebook and share your figure.
Choose a model below for its links.

<div class="tabLabels" label="community-evaluation-models" style="margin-bottom: 0.5rem;">
    <button id="cm3">ACCESS-CM3</button>
    <button id="am3">ACCESS-AM3</button>
    <button id="om3">ACCESS-OM3</button>
</div>
<div tabcontentfor="cm3" markdown>
Coupled model evaluation, with [ACCESS-CM2](/models/access_models/access-cm) as the baseline for comparison.

- **Repository:** [ACCESS-Community-Hub/access-cm3-paper-1](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/new?template=add-user-request-to--access-cm3-1-repository-.md)
- **Find a diagnostic:** [CM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-cm3-paper-1/issues/1)
- **Simulations to evaluate:** [ACCESS-CM3 experiments](https://access-cm3-configs.readthedocs.io/Experiments/)
- **Meetings:** the monthly _CM3 Dev-Eval Working Group_. Joining details and minutes are in [this forum thread](https://forum.access-hive.org.au/t/cm3-dev-eval-working-group-meeting-minutes/5393).
- **NCI projects:** `zv30`, `p73`, `eg3`, `ct11`, `ik11`
</div>
<div tabcontentfor="am3" markdown>
<!-- TODO (AM3 team, GitHub user paocorrales): please review/expand the AM3 content below (baseline model, meetings, NCI projects). -->
Atmosphere-only model evaluation, currently focused on the high-resolution (N512) configuration.

- **Repository:** [ACCESS-Community-Hub/access-am3-evaluation](https://github.com/ACCESS-Community-Hub/access-am3-evaluation)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/new?template=add-user-request-to--access-cm3-1-repository-.md)
- **Find a diagnostic:** [AM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-am3-evaluation/issues/1)
- **Current focus:** [AM3 high-resolution evaluation](https://forum.access-hive.org.au/t/we-need-your-help-am3-hi-res-evaluation/6438)
- **Meetings:** there is no standing public meeting yet. Ask to be looped in on the [forum thread](https://forum.access-hive.org.au/t/we-need-your-help-am3-hi-res-evaluation/6438).
</div>
<div tabcontentfor="om3" markdown>
Ocean–sea ice model evaluation, with [ACCESS-OM2](/models/access_models/access-om) as the baseline for comparison.

- **Repository:** [ACCESS-Community-Hub/access-om3-paper-1](https://github.com/ACCESS-Community-Hub/access-om3-paper-1)
- **Request write access:** [open an access request issue](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/new?template=add-user-request-to--access-om3-paper-1--repository-.md)
- **Find a diagnostic:** [OM3 mega-issue](https://github.com/ACCESS-Community-Hub/access-om3-paper-1/issues/23)
- **Simulations to evaluate:** [ACCESS-OM3 experiments](https://access-om3-configs.access-hive.org.au/latest/Experiments/)
- **Browse the latest evaluation:** [access-om3-paper-1.readthedocs.io](https://access-om3-paper-1.readthedocs.io/latest/)
- **Meetings:** the monthly _ACCESS-OM3 model evaluation team_. Announcements are in [this forum thread](https://forum.access-hive.org.au/t/access-om3-model-evaluation-team-announce/4476).
- **NCI projects:** `zv30`, `p73`, `ol01`, `ik11`, `av17`

!!! warning
    This repository uses a _git_ submodule. Clone it with `git clone --recurse-submodules`.
</div>

## From diagnostic idea to figure

Each repository's `README` is the step-by-step guide. In outline:

<div class="workflow-steps">
    <div><span class="workflow-number">1</span><span class="bold">Request access</span><span>Open an access request issue in the repository</span></div>
    <div><span class="workflow-number">2</span><span class="bold">Find a diagnostic</span><span>Claim or suggest one in the mega-issue</span></div>
    <div><span class="workflow-number">3</span><span class="bold">Clone the repository</span><span>On <i>Gadi</i>, then start an <a href="/getting_started/are">ARE</a> session</span></div>
    <div><span class="workflow-number">4</span><span class="bold">Write a notebook</span><span>Start from the template notebook</span></div>
    <div><span class="workflow-number">5</span><span class="bold">Commit and push</span><span>To <code>main</code>, or to a branch with a pull request for review</span></div>
    <div><span class="workflow-number">6</span><span class="bold">Share and get credit</span><span>Post your figure and commit hash in its issue, and add your name to <code>CITATION.cff</code></span></div>
</div>

Notebooks don't need to be polished to be useful. Each repository's `notebooks` folder accepts work at three levels:

- `polished-python`: follows the template notebook and runs automatically on new simulations.
- `sandbox-python`: _Python_ analysis that doesn't (yet) follow the template. A great place to start.
- `non-python`: any language or tool that makes a figure.

## Support

- Ask questions in the working group meetings or on the [ACCESS-Hive Forum](https://forum.access-hive.org.au/).
- In-person "buddies" at most partner institutions can help you get started or suggest what to work on.
- For general help, see [User support](/about/user_support).
