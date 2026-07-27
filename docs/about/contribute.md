{% set hive_docs_repo_name = "ACCESS-Hive-Docs" %}
{% set hive_docs_repo_url = "https://github.com/ACCESS-NRI/" ~ hive_docs_repo_name %}

# How to Contribute

ACCESS-Hive Docs is a resource for the Australian Community Climate and Earth System Simulator (ACCESS) community. We welcome all kinds of contributions! Whether you're fixing a typo, improving existing content, or adding new content - your input helps make the documentation more useful for the community.

!!! tip
    Not comfortable editing documentation? Simply reporting a typo or suggesting an improvement by opening an [issue]({{hive_docs_repo_url}}/issues/new/choose) is a valuable and appreciated contribution!

## How you can contribute

There are three ways to contribute:

- **[Suggest a change or report a problem](#github-issue)** by opening a [GitHub issue]({{hive_docs_repo_url}}/issues/new/choose).
- **[Edit a page directly](#direct-edit)** - quick fixes to a single page.
- **[Larger changes](#large-contribution)** - new pages, restructuring, or multi-file edits.

All are equally welcome - feel free to choose whichever works best for you.

!!! info
    All contribution paths require a GitHub account — [sign up for free](https://github.com) if you don't have one.

---

### Open a GitHub Issue {: #github-issue }

<div class="card-container">
    <a href="{{hive_docs_repo_url}}/issues/new/choose" class="horizontal-card" target="_blank">
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

The easiest way to contribute is to open a [GitHub issue]({{hive_docs_repo_url}}/issues/new/choose). This is a great option if you:

- Spot a typo, error, or broken link.
- Find something confusing or unclear.
- Have an idea for improvement.
- Don't want to edit the page yourself.

Once the issue has been submitted, you are welcome (and encouraged!) to make a suggested edit via a pull request to address your issue (see contributing options 2 or 3 below), otherwise the ACCESS-NRI team or other contributors will be happy to take it from there.

---

### Edit a page directly {: #direct-edit }
For quick fixes to an existing page (e.g., typos, wording update, broken links), you can edit a page directly in your browser using the *pencil* icon in the top-right corner of the website.

- Click the **pencil icon ( :material-pencil: )** in the top-right corner of the page you want to edit.

![Edit Pencil Icon](/assets/contributing_page/edit_icon.png)

- Click _Fork this repository_.

!!! tip
    If you have write access to the [{{hive_docs_repo_name}}]({{hive_docs_repo_url}}) repository, this step will not be required.

- Make your changes in the editor. 
- When you are satisfied with your changes, click on the _Commit changes..._ button (at the top-right corner), add a _Commit message_ and an optional _Extended description_, and click _Propose changes_. GitHub will automatically create a new branch (usually called `patch-1` by default) and prompt you a screen where you can compare the changes.

!!! danger
    If you have write access to the {{hive_docs_repo_name}} repository, **do not** select _Commit directly to the development branch_! Instead, create a new branch and open a pull request so the changes can be reviewed, discussed before they are added to the shared `development` branch.

- Click _Create pull request_. 
- Add a title and details about the proposed changes and click _Create pull request_.

---

### Make changes locally {: #large-contribution }
For adding new pages, restructuring, or making multi-line updates, the easiest approach is to work on a local copy of the documentation and then push your changes to GitHub when ready. This documentation is written in Markdown format and is based on the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, which is built on top of the [MkDocs](https://www.mkdocs.org/) static site generator.

#### Step 1: Fork the repository

!!! info
    If you have write access to the [{{hive_docs_repo_name}}]({{hive_docs_repo_url}}) repository, you can skip this step.

A [GitHub fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) is your own copy of the repository on GitHub where you can make changes without affecting the original (upstream) repository. These changes can then be merged back into the upstream repository via pull requests.

![Fork the repository](/assets/contributing_page/fork-repo.png)


1. Go to the [{{hive_docs_repo_name}}]({{hive_docs_repo_url}}) repository on GitHub. 
2. Click _Fork_ in the top-right corner.
3. Choose your GitHub account and repo name as the destination (we suggest to keep the original name to avoid confusions). 
4. Click _Create fork_.

This creates your own copy of the repository on GitHub. 

#### Step 2: Clone the repository

[Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) creates a local copy of the repository on your computer.

Then, if you have **forked** the repository, you can clone your fork by clicking the green **Code button** in the top-right corner of the repository page, copying the repository URL, and then running the following command:

```bash
git clone https://github.com/YOUR_USERNAME/ACCESS-Hive-Docs.git
```

If you are an ACCESS-NRI team member, you should clone the original ACCESS-Hive-Docs repository directly:

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
After cloning the repository locally, create a new branch to make your local changes:

```
git checkout -b your-branch-name
```

Creating a branch keeps your work separate from the main version of the documentation. 


#### Step 4: Make your changes
Open the directory in your editor (e.g. VS Code), ensure you are working on your new branch (VS Code lists your current branch in the bottom left of the window) and make your edits. You can check which files have been modified with:

```
git status
```

#### Step 5: [OPTIONAL] Preview your changes locally
!!! info 
    Local previews can be really handy to see your changes rendered how they would look on the website, but they require you do install software onto your computer. If you'd prefer to avoid software installation, you can skip this step and preview your branch after you push your changes to the Hive Docs repository via a pull request (by following the remaining steps).

Execute the following command to download and install Material MkDocs and all related plugins:

```
pip install -r requirements.txt
``` 

Before submitting your changes, you can preview them locally using the command:

```
mkdocs serve
```

This will start a local documentation server. Open the URL shown in your terminal, usually:

```
http://127.0.0.1:8000
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
Once, you have committed your changes, push your branch to GitHub. The first time you push a new branch, run:

```
git push --set-upstream origin your-branch-name
```

The `--set-upstream` option links your local branch to the branch on GitHub. After this you can any future commits on the same branch with:

```
git push
```

#### Step 9: Open a pull request
After pushing your branch to remote, [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) using the following steps:

1. Go to the **repository** on GitHub (either the [main Hive Docs repository](https://github.com/ACCESS-NRI/ACCESS-Hive-Docs) for ACCESS-NRI GitHub org members or your fork of that repository for others).
2. GitHub will usually display a **prompt** to create a pull request from your branch.
3. Click **Compare & pull request**. 
4. Add a title and detailed description explaining your changes. 
5. Click **Create pull request**.

!!! tip
    Include a brief summary of what changed and why. If your changes relate to an existing issue, consider linking to it in the pull request description.

#### Step 10: Review the pull request preview

After you open a pull request, a **preview version** of the documentation is automatically generated. Once the preview has been deployed:

1. Open the **preview link** from the pull request checks, comments, or status checks.
2. **Review** your changes in the linked preview documentation site.

!!! note
    The pull request preview shows how your changes will appear before they are added to the public website, making it a great way to catch formatting or rendering issues.


## Best Practices
??? info "Creating issues"
    Creating clear and well-labelled issues helps contributors to quickly understand the type, purpose, and urgency of a task. 

    1. Use a clear and descriptive title that summarises the issue.

    2. Include enough context for others to understand the problem. 

    3. Keep issues focused on a single topic where possible. Smaller, targeted issues are generally easier to discuss and resolve.

??? info "Branching Workflows"
    The Hive Docs repository currently uses two primary branches: `main` and `development`. `main` is the production-ready branch (what is visible on the public website), and `development` is the staging branch where latest changes are pushed and previewed.

    Contributors should generally:

    - Create a branch from `development`.
    - Open pull requests with `development` as the target. 
    
    The `development` branch is automatically merged into `main` daily. This reduces the risk of having breaking changes affect the live website. 

??? info "Branch Naming"
    Using descriptive branch name makes it easier to understand what the branch is for. We recommended using the following branch name structure:
    
    - `name/issue-number/short-description`
    
    Example:
    - `bob/24/add-cosima-tutorial`


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
1. For any questions, [create a help request on the ACCESS-Hive Forum](https://forum.access-hive.org.au/new-topic?&body=%3Cdiv%20data-theme-toc%3D%22true%22%3E%3C%2Fdiv%3E%0A%0A%3C!--%20These%20are%20comments%20and%20not%20visible%20once%20you%20post.%20Ignore%20or%20delete%20sections%20if%20not%20relevant%20--%3E%0A%0A%3C!--%20Choose%20an%20appropriate%20category.%20If%20not%20sure%2C%20leave%20as%20General%20--%3E%0A%0A%23%23%20Description%20of%20request%3A%0A%0A%23%23%20Environment%3A%0A%0A%3C!--%20NCI%3F%20ARE%3F%20Gadi%20login%20node%3F%20PBS%20job%3F%20--%3E%0A%0A%3C!--%20List%20software%20versions%20--%3E%0A%0A%23%23%20What%20executed%3A%0A%0A%3C!--%20Copy%20and%20paste%20any%20commands%20and%20output%20in%20a%20code%20block%20--%3E%0A%3C!--%20For%20code%20you%20are%20writing%2C%20prepare%20a%20minimal%20reproducible%20example%20(https%3A%2F%2Fforum.access-hive.org.au%2Fdocs%3Ftopic%3D843)%20--%3E%0A%0A%23%23%20Actual%20results%3A%0A%0A%3C!--%20Copy%20full%20error%20messages%20--%3E%0A%0A%23%23%20Expected%20results%3A%0A%0A%23%23%20Additional%20info%3A&category_id=4&tags=help).

## Further Reading
- For official GitHub documentation, see [GitHub Docs](https://docs.github.com/en/get-started).
- For a more detailed, beginner-friendly introduction to Git and GitHub, see [Project Pythia - Getting Started with GitHub tutorial](https://foundations.projectpythia.org/foundations/getting-started-github/).

