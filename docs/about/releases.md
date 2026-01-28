
[Hive Forum]: https://forum.access-hive.org.au
# ACCESS-NRI Release Stages

We develop and share our model configurations[^1] and tools in stages. Each stage has a different purpose and level of readiness. These terms are used to give a general indication on the state of the product you want to use and things to be aware of:
<!-- color text like table -->
- **Prototype (not shown in table):**  Early versions shared with a small group of experts to explore new ideas. These are not polished or complete, and may change quickly. 

- **Alpha:**{: .nri-danger-color } Early testing phase. The core features are in place, but things may change. No long-term support or maintenance. Feedback at this stage helps shape the product.

- **Beta:**{: .nri-orange-color } More stable versions open to a wider group. Most features and documentation are ready, and we welcome testing by anyone interested. Changes may still occur. No long-term support or maintenance.

- **Full Release:**{: .nri-green-color} Fully tested, verified and documented. Supported versions with maintenance. Bitwise reproducible.[^2]  

!!! info
    These release definitions will not be applied retroactively to any model configuration or tool release.

<div class="card-container">
    <a href="/about/release_list" class="horizontal-card">
        <div class="card-image-container">
            <img class="img-contain white-background" src="/assets/rocket_release.svg" alt="ACCESS-NRI release list">
        </div>
        <div class="card-text-container">
            <span class="bold" >ACCESS-NRI Release List</span>
            <span>
                See a list of 'full' releases and links to release notes.
            </span>
        </div>
    </a>
</div>

## Release stages for model configurations[^1]
The table below has some details for each release stage of ACCESS-NRI supported model configurations. Note that this table is valid only for model configurations, and not for tools.

<div class="release-table" markdown>

|   | ALPHA | BETA | FULL RELEASE |
|---| ----- | ---- | ------- |
|**Overall state of product**|**Unstable**|**Somewhat stable**|**Stable**|
|How to access and run the model configuration| Pre-release module | Pre-release module | Model/version module|
|Input files for configurations | Not yet managed[^3] | Managed[^3] | Managed[^3], FAIR |
|Availability & maintenance of the deployed model configuration | Short-term, for alpha testers only | Until next beta or full release | Long-term[^4] |
|User support (via [Hive Forum]) |No guarantee, for alpha testers only |Until next beta or full release |Fully supported[^4]|
|Spin-up and control experiment(s) |N/A |Under validation (if available) |Validated and published when available |
|Documentation on Hive Docs |Unpublished |Published publicly with “*beta*” caveat |Published publicly|
|Optimisation & scaling |No guarantee |In progress |Complete |
|DOI |None |None |DOI issued; any model updates receive new DOIs |
|Announcements to the community |Direct contact with alpha testers. No formal announcement. |Public post on [Hive Forum]. |Public post on [Hive Forum]. On ACCESS-NRI website, newsletter, and social media. May include a media release.|
</div>

[^1]: A model configuration is the entire setup for a model experiment run. It is the compiled model code, the parameters, and input files. It is essentially an experiment waiting to happen.
[^2]: By bitwise reproducible, we mean that a model configuration will produce the same answers if re-run on Gadi (with the same layout, number of processors, etc., all of which are specified in a model configuration).
[^3]: By managed, we mean that the input files are collected in a specific place and are incorporated into the model configuration.
[^4]: Each release will have its own timeframe for availability, maintenance, and support. The timeframe will be based on factors that include: what our users need; availability, and suitability, of new models; machine changes (older models may not be ported to new machines); overall support burden (if we support too many models our ability to update current models or develop new ones is impaired); collaborators (if we use a model component that is deprecated it may make it harder for us to support it.)