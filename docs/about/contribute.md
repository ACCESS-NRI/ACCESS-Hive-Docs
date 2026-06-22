{% set hive_docs_repo_name = "ACCESS-Hive-Docs" %}
{% set hive_docs_repo = "https://github.com/ACCESS-NRI/" ~ "ACCESS-Hive-Docs" %}

# Contributing

**ACCESS-Hive Docs** is a community resource for users of the Australian Community Climate and Earth System Simulator (ACCESS). 

Have an idea for improvement? We'd love to have your contributions onboard! Whether you're correcting a typo, improving existing content, or adding something new, every contribution helps make the documentation more useful for the community.

!!! tip
    Not comfortable editing documentation? Simply reporting an [issue]({{hive_docs_repo}}/issues/new/choose) or suggesting an improvement is a valuable and appreciated contribution!

## How you can contribute

There are three ways to contribute:

1. **[Suggest a change or report a problem](#1-suggest-a-change-or-report-a-problem)** by opening a [GitHub issue]({{hive_docs_repo}}/issues/new/choose).
2. **[Edit a page directly (via pencil icon)](#2-edit-a-page-directly)** - quick fixes to a single page.
3. **[Larger changes](#3-larger-changes)** - new pages, restructuring, or multi-file edits.

All are equally welcome - feel free to choose whichever works best for you.

!!! info
    All contribution paths require a GitHub account — [sign up for free](https://github.com) if you don't have one.

---

### 1. Open a GitHub Issue

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

The easiest way to contribute is to open a [GitHub issue]({{hive_docs_repo}}/issues/new/choose). This is a great option if you:

- Spot a typo, error, or broken link.
- Find something confusing or unclear.
- Have an idea for improvement.
- Don't want to edit the page yourself.

Once the issue has been submitted, the **ACCESS-NRI team (or other contributors)** will be happy to take it from there.

---

### 2. Edit a page directly
For quick updates to an existing page, you can edit it directly in your browser using the *pencil* icon in the top-right corner of the website.

- Click the **edit (pencil) icon** in the top-right corner of the page you want to edit.

![Edit Pencil Icon](/assets/contributing_page/1_edit_icon2.png)

- If you are outside the [ACCESS-NRI GitHub organisation](https://github.com/ACCESS-NRI), GitHub will ask you to **fork the repository**. If you are an ACCESS-NRI GitHub organisation member, GitHub will ask you to **create a new branch**.
- Make your changes in the editor. 
- Scroll down to the **Commit changes**, add a short description, and click **Propose changes**. 
- Click **Create pull request**. 
- Add details about the proposed changes and click **Submit**.

---

### 3. Make changes locally
For larger changes or updates across multiple pages, the easiest approach is to work on a local copy of the documentation and then push your changes to GitHub when ready. This documentation is written in Markdown format and is based on the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, which is built on top of the [MkDocs](https://www.mkdocs.org/) static site generator.

!!!tip
    If you are not a member of the [ACCESS-NRI GitHub organisation](https://github.com/ACCESS-NRI), you will need to **fork** the repository first. A **fork** is your own copy of the repository on GitHub where you can make changes before proposing them back to the main repository.

#### Step 1: Fork the repository

![Fork the repository](/assets/contributing_page/fork_repo.png)

If you are outside the [ACCESS-NRI GitHub](https://github.com/ACCESS-NRI) organisation:

1. Go to the [ACCESS-Hive Docs]({{hive_docs_repo}}) repository on GitHub. 
2. Click **Fork** in the top-right corner.
3. Choose your GitHub account as the destination. 
4. Click **Create Fork**.

This creates your own copy of the repository. 

!!! info 
    [ACCESS-NRI GitHub organisation](https://github.com/ACCESS-NRI) members can **skip this step** and clone the main repository directly.


#### Step 2: Clone the repository

**Cloning** creates a local copy of the repository on your computer. Before cloning, open a **terminal** and navigate to the directory where you'd like the repository to be downloaded. 

Then, if you have **forked** the repository, you can clone your fork by clicking the green **Code button** in the top-right corner of the repository page, copying the repository URL, and then running the following command:

```bash
git clone https://github.com/YOUR_USERNAME/ACCESS-Hive-Docs.git
```

If you are an ACCESS-NRI team member, feel free to clone the main repository:

```bash
git clone https://github.com/ACCESS-NRI/ACCESS-Hive-Docs.git
```

![Clone the repository](/assets/contributing_page/clone_repo.png)

??? note "Cloning with SSH"
    If you have already configured [SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), click the green **Code** button, select **SSH**, and copy the **SSH URL**. You can then clone the repository using:
    
    ```bash
    git clone git@github.com:ACCESS-NRI/ACCESS-Hive-Docs.git
    ```

Once the repository has been **cloned**, navigate into the repository directory.

#### Step 3: Create a new branch
After cloning the repository locally, create a new branch to make your local changes and then push it to GitHub:

```
git checkout -b your-branch-name
```

```
git push --set-upstream origin your-branch-name
```

Creating a branch keeps your work separate from the main version of the documentation

#### Step 4: Make your changes
Open the repository in your editor (ex. VSCode) and make your changes. You can check which files have been modified with:

```
git status
```

#### Step 5: Preview your changes locally
Before submitting your changes, you can preview them locally using the command:

```
mkdocs serve
```

This will start a local documentation server. Open the URL shown in your terminal, usually:

```
http://127.0.0.1:8000
```

??? warning "If `mkdocs serve` command is not working"
    Execute the following command to download and install Material MkDocs and all related plugins:

    ```
    pip install -r requirements.txt
    ``` 

#### Step 6: Review your changes
Review your changes before committing:

```
git diff
```

This helps confirm that only the intended changes will be included.

#### Step 7: Commit your changes
Stage the files you changed:

```
git add path/to/file.md
```

Or stage all modified files:

```
git add .
```

Commit your changes with a short description:

```
git commit -m "my commit description"
```

#### Step 8: Push your branch to GitHub
Push your branch to GitHub using the command:

```
git push origin your-branch-name
```

#### Step 9: Open a pull request
After pushing your branch to remote, [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) using the following steps:

1. Go to the **repository** on GitHub.
2. GitHub will usually display a **prompt** to create a pull request from your branch.
3. Click **Compare & pull request**. 
4. Add a title and detailed description explaining your changes. 
5. Click **Create pull request**.

!!! tip
    Include a brief summary of what changed and why. If your changes relate to an existing issue, consider linking to it in the pull request description.

#### Step 10: Review the pull request preview

After you open a pull request, a **preview version** of the documentation is automatically generated. Once the preview has been deployed:

1. Open the **preview link** from the pull request checks, comments, or status checks.
2. **Review** your changes in the rendered documentation site.

!!! note
    The pull request preview shows how your changes will appear before they are merged, making it a great way to catch formatting or rendering issues.


## Checklist
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
