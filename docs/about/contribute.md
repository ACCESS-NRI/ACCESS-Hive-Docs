{% set hive_docs_repo_name = "ACCESS-Hive-Docs" %}
{% set hive_docs_repo = "https://github.com/ACCESS-NRI/" ~ "ACCESS-Hive-Docs" %}

# Contribute to ACCESS-Hive Docs

We welcome contributions from the entire ACCESS Community. Whether you're fixing a typo, improving clarity, or adding new content - your input helps make the documentation better for everyone.

!!! tip
    You don't need to edit the documentation yourself to contribute.

Simply reporting an issue or suggesting an improvement is already a valuable and appreciated contribution.

## How to contribute

This documentation is written in Markdown format and is based on the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, which is built on top of [MkDocs](https://www.mkdocs.org/) static site generator. There are two main ways to contribute:

1. **Suggest a change or report a problem** by [opening an issue](https://github.com/ACCESS-NRI/ACCESS-Hive-Docs/issues/new/choose).
2. **Edit a page directly** using the edit (pencil) icon on the top right.

Both are equally welcome - feel free to choose whichever works best for you.

### 1. Suggest a change or report a problem

If you notice something that could be improved, you can [open an issue](https://github.com/ACCESS-NRI/ACCESS-Hive-Docs/issues/new/choose) to let us know.

This is a great option if you:

- Spot a typo, error, or broken link.
- Find something confusing or unclear.
- Have an idea for improvement.
- Don't want to edit the page yourself.

Once submitted, the ACCESS-NRI team (or other contributors) would be happy to take it from there.

### 2. Edit a page
If you’d like to make the change yourself, you can edit pages directly using the edit (pencil) icon. 

When you click the edit (pencil) icon, GitHub will take you to the source file for that page. 
 
#### If you are outside ACCESS-NRI GitHub Organisation

1. You will be prompted to **fork the repository**   
2. Click **Fork this repository**   
3. GitHub will create your copy and open the file in edit mode   

Then: 
 
4. Make your changes in the editor   
5. Scroll down to the **Commit changes** section   
6. Add a short description of what you changed   
7. Click **Propose changes**   
8. Click **Create pull request**   
9. Add any additional context and submit   

#### If you are in ACCESS-NRI
 
1. You will be prompted to create a **new branch**   
2. Enter a branch name (or use the default)   
3. Make your changes   
4. Click **Propose changes**   
5. Open a pull request and add a short description 

### 3. Make larger changes (optional, advanced)
For adding new pages or making more complex updates, it can be easier to work on a local copy of the documentation.

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
