{% set hive_docs_repo_name = "ACCESS-Hive-Docs" %}
{% set hive_docs_repo = "https://github.com/ACCESS-NRI/" ~ "ACCESS-Hive-Docs" %}

# Contribute to ACCESS-Hive Docs

**ACCESS-Hive Docs** is a resource for the *Australian Community Climate and Earth System Simulator (ACCESS)* community. We welcome all kinds of contributions! Whether you're fixing a typo, improving clarity, or adding new content - your input helps make the documentation better for everyone!

!!! tip
    You don't need to edit the documentation yourself to contribute. Simply reporting an [issue]({{hive_docs_repo}}/issues/new/choose) or suggesting an improvement is a valuable and appreciated contribution!


## How to contribute

There are three ways to contribute:

1. **[Suggest a change or report a problem](#1-suggest-a-change-or-report-a-problem)** by opening a [GitHub issue]({{hive_docs_repo}}/issues/new/choose).
2. **[Edit a page directly (via pencil icon)](#2-edit-a-page-directly)** - quick fixes to a single page.
3. **[Larger changes](#3-larger-changes)** - new pages, restructuring, or multi-file edits.

All are equally welcome - feel free to choose whichever works best for you.

!!! info "GitHub account required" 
    All contribution paths require a GitHub account — [sign up for free](https://github.com) if you don't have one.

---

### 1. Suggest a change or report a problem

The easiest way to contribute is to open a [GitHub issue]({{hive_docs_repo}}/issues/new/choose).

<div class="card-container">
    <a href="{{hive_docs_repo}}/issues/new/choose" class="horizontal-card" target="_blank">
        <div class="card-image-container">
            <img class="img-contain white-background" src="/assets/how-to-contribute-img.jpg">
        </div>
        <div class="card-text-container with-padding">
            <div class="bold">
                Raise a GitHub Issue!
            </div>
            <span class="with-padding">
                Suggest an idea, propose bug fixes, or flag missing content by raising a GitHub issue. 
            </span>
        </div>
    </a>
</div>

This is a great option if you:

- Spot a typo, error, or broken link.
- Find something confusing or unclear.
- Have an idea for improvement.
- Don't want to edit the page yourself.

Once the issue has been submitted, the ACCESS-NRI team (or other contributors) will be happy to take it from there.

---

### 2. Edit a page directly
For quick updates to an existing page, you can edit it directly in your browser using the *pencil* icon in the top-right corner of the website.

1. Click the **edit (pencil) icon** in the top-right corner of the page you want to edit.
2. If you are outside the ACCESS-NRI GitHub organisation, GitHub will ask you to **fork the repository**. If you are an ACCESS-NRI organisation member, GitHub will ask you to **create a new branch**.
3. Make your changes in the editor. 
4. Scroll down to the **Commit changes**, add a short description, and click **Propose changes**. 
5. Click **Create pull request**. 
6. Add details about the proposed changes and click **Submit**.

---

### 3. Make larger changes
For adding new pages, restructuring, or making multi-file updates, the easiest approach is to work on a local copy of the documentation and then push your changes to GitHub when ready.

When making larger changes, it may be helpful to understand the structure of the Hive Docs site. This documentation is written in Markdown format and is based on the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, which is built on top of the [MkDocs](https://www.mkdocs.org/) static site generator.

**For contributors outside ACCESS-NRI:** 
 
1. Fork the repository on GitHub   
2. Clone your fork to your computer   
3. Create a new branch   
4. Make your changes locally   
5. Commit your changes   
6. Push the branch to your fork   
7. Open a pull request   
 
**For ACCESS-NRI team members:** 
 
1. Clone the repository   
2. Create a new branch   
3. Make your changes locally   
4. Commit your changes   
5. Push your branch   
6. Open a pull request   
 
This workflow is useful for larger or multi-page updates. 


## Best Practices for
??? info "Creating issues"
    Creating clear and well-labelled issues helps contributors to quickly understand the type, purpose, and urgency of a task. 

    1. Use a clear and descriptive title that summarises the issue.

    2. Include enough context for others to understand the problem. 

    3. Keep issues focused on a single topic where possible. Smaller, targeted issues are generally easier to discuss and resolve.

??? info "Branching Workflows and Naming"
    This repository currently uses two primary branches - `main` and `development`. `main` is the production-ready branch, and `development` is the staging branch where latest changes are pushed before merging into `main` branch.

    Contributors should generally:
    - Create a feature branch from `development`.
    - Open pull requests targeting to `development`. 
    
    The `development` branch is automatically merged into `main` daily. This reduces the risk to include breaking changes into the production branch. 

    For branch naming, using consistent branch names makes it easier to identify the purpose of a branch. Recommended naming patterns include:
    - name/issue-number/short-description
    
    Example:
    - john/24/add-cosima-tutorial

    Use short, descriptive, and lowercase names separated by hyphens.

??? info "Pull Requests"
    Well-documented pull requests help reviewers understand the intent of changes and reduces the turnaround time of the review. 

    When opening a PR:
    - Provide a clear summary of the changes.
    - Explain *why* the changes were made, not just *what* changed.
    - Link related issues or discussions where relevant.
    - Include screenshots or previews if applicable.

    Smaller and focused PRs are generally preferred over very large changes, as they are easier to review, test and merge.

    Before submitting a PR, contributors are encouraged to:
    - Check formatting and links.
    - Preview documentation changes on the PR previews generated just after creating a PR.
    - Check GitHub CI is passing all checks. 

## Need help?
1. For any questions, we'd be happy to answer questions on [ACCESS-Hive Forum](https://forum.access-hive.org.au). 
2. For reporting a bug or suggesting a change, feel free to write an issue.
