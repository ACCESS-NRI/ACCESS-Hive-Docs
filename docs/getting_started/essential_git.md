# Essential Git Commands

## Introduction

Not sure which Git command to use next? This guide is a quick reference for everyday Git workflows, including contributions to ACCESS-NRI repositories.

Designed for users with some familiarity with Git, it helps you find **which commands to use, when and how**, whether you need to:

- Inspect commits and changes
- Work with branches
- Fetch and integrate remote changes
- Temporarily save unfinished work
- Manage or undo changes to Git history

!!! note
    The examples below use generic branch names such as `main` and `feature`. Replace these with the branch names used in your repository.

!!! info
    Square brackets in command syntax, such as `[<remote>]`, indicate optional arguments; don't type the brackets.

## Find the right Git command
Use the diagram below to find commonly used Git commands by task. 

```mermaid
flowchart LR
    A("What are you trying to do?")

    A --> B("🛠️ Setup & share changes")
    A --> C("🔍 Inspect your changes")
    A --> D("⬇️ Get remote changes")
    A --> E("🌿 Work with branches")
    A --> F("📦 Temporarily save changes")
    A --> G("⚠️ Undo or reset changes")

    B --> B1("git clone → git add → git commit → git push")
    C --> C1("git status · git diff · git log · git show")
    D --> D1("git fetch · git pull")
    E --> E1("git switch · git merge · git rebase")
    F --> F1("git stash")
    G --> G1("git reset")

    classDef primary stroke:#F9A61C,stroke-width:1.5px
    classDef setup stroke:#005B94,stroke-width:1.5px
    classDef inspect stroke:#01ADEE,stroke-width:1.5px
    classDef update stroke:#009C95,stroke-width:1.5px
    classDef branch stroke:#A5CD3A,stroke-width:1.5px
    classDef stash stroke:#9370DB,stroke-width:1.5px
    classDef reset stroke:#D9534F,stroke-width:1.5px

    %% Category links
    click B href "#setup-share-changes"
    click C href "#inspect-your-changes"
    click D href "#get-remote-changes"
    click E href "#work-with-branches"
    click F href "#temporarily-save-changes"
    click G href "#undo-or-reset-changes"

    class A primary
    class C,C1 inspect
    class D,D1 update
    class E,E1 branch
    class F,F1 stash
```

## Core Git commands at a glance

Here are a few core Git commands that are useful to keep handy in everyday Git workflows. For more details, please refer to the link in the command.

| Command | Example Usage | Purpose |
|---|---|---|
| [`git add`](https://git-scm.com/docs/git-add) | `git add <file>` | Stage changes for commit. |
| [`git branch`](https://git-scm.com/docs/git-branch)|  `git branch -a` | List all branches |
| [`git clone`](https://git-scm.com/docs/git-clone) | `git clone <url> <local_dir>` | Copy a remote repository to your local machine|
| [`git commit`](https://git-scm.com/docs/git-commit) | `git commit -m "<message>"` | Save staged changes as a new commit. |
| [`git diff`](https://git-scm.com/docs/git-diff) | `git diff origin/<branch>` | Visualise source code differences |
| [`git fetch`](https://git-scm.com/docs/git-fetch) | `git fetch [<remote>]` | Update remote tracking branches |
| [`git log`](https://git-scm.com/docs/git-log) | `git log [-c]` | Show the history of the repository |s
| [`git merge`](https://git-scm.com/docs/git-merge) | `git merge <feature-branch>` | Combines the histories of two branches |
| [`git pull`](https://git-scm.com/docs/git-pull) | `git pull` | updates the local branch to match the remote |
| [`git push`](https://git-scm.com/docs/git-push)| `git push` | Push local commits to the remote repository. |
| [`git rebase`](https://git-scm.com/docs/git-rebase) | `git rebase <branch>` | Moves your branch commits on top of another branch |
| [`git reset`](https://git-scm.com/docs/git-reset) | `git reset --hard origin/<branch>` | Reset branch to match another branch state |
| [`git show`](https://git-scm.com/docs/git-show) | `git show <commit>` | Look into a specific Git commit |
| [`git status`](https://git-scm.com/docs/git-status) | `git status` | Show status of current working tree. |
| [`git switch`](https://git-scm.com/docs/git-switch) | `git switch [-c] <branch>` | Switch the HEAD to a different branch |
| [`git stash`](https://git-scm.com/docs/git-stash) | `git stash [push\|pop\|apply]` | Temporarily save changes into stash space |

## Setup & share changes

### Git clone

The `git clone` command creates a local copy of an existing repository, including its commit history.

#### When to use {: .no-toc }

- To start working on an existing repository.
- To create a local copy of a remote repository for development or contribution.

#### How to use {: .no-toc }

To clone a repository, run:

```bash
git clone <url>
```

By default, Git creates a directory with the same name as the repository. To specify a different local directory, use:

```bash
git clone <url> <local_dir>
```

For example:

```bash
git clone https://github.com/ACCESS-NRI/ACCESS-Hive-Docs.git
```

### Git add

The `git add` command stages changes to be included in the next commit.

#### When to use {: .no-toc }

- To prepare new or modified files for a commit.
- To selectively include changes in the next commit.
- To stage files after resolving merge or rebase conflicts.

#### How to use {: .no-toc }

To stage changes to a specific file:

```bash
git add <file>
```

To stage all changes in the repository:

```bash
git add -A
```

To interactively select which changes to stage:

```bash
git add -p
```

!!! tip

    Use `git status` to check which changes have been staged, or `git diff --staged` to review the changes before committing.

### Git commit

The `git commit` command records staged changes in the local repository's history.

#### When to use {: .no-toc }

- To record a meaningful set of changes.
- To save staged changes before sharing them with others.

#### How to use {: .no-toc }

Once the relevant changes have been staged using `git add`, run:

```bash
git commit -m "<message>"
```

For example:

```bash
git commit -m "Update installation instructions"
```

To modify the most recent commit, use:

```bash
git commit --amend
```

!!! warning

    Amending a commit rewrites its history. Avoid amending commits that other people are already working from.

### Git push

The `git push` command uploads local commits to a remote repository.

#### When to use {: .no-toc }

- To share local commits with others.
- To publish a newly created branch to a remote repository.
- To update an existing pull request with additional commits.

#### How to use {: .no-toc }

If the current branch already has an upstream branch configured, simply run:

```bash
git push
```

To push a branch to a specific remote repository:

```bash
git push <remote> <branch>
```

When pushing a newly created branch for the first time, use:

```bash
git push -u origin <branch>
```

The `-u` (or `--set-upstream`) option establishes a tracking relationship with the remote branch, allowing subsequent pushes and pulls without explicitly specifying the remote and branch.

## Inspect your changes

### Git log

#### When to use {: .no-toc }

Use `git log` to see the history of the repository.

#### How to use {: .no-toc }

The basic command is 
```
git log
```
and you may add some optional flags such as `[<--oneline>]` to display each commit on a single line,
`[<--graph>]` to display the commit history as a graph.
An example of `git log --graph --online` is shown below:

<div markdown="0">
<terminal-window lineDelay="200">
    <terminal-line data="input">git log --graph --oneline</terminal-line>
    <terminal-line>* <span class="nri-orange-color">a8f3c21</span> (<span class="git-cyan">HEAD</span> -&gt; <span class="git-green">main</span>) Add documentation</terminal-line>
    <terminal-line>*   <span class="nri-orange-color">b7e2d14</span> Merge branch 'feature-login'</terminal-line>
    <terminal-line><span class="git-red">|</span><span class="git-green">\</span></terminal-line>
    <terminal-line><span class="git-red">|</span> * <span class="nri-orange-color">c9d4a62</span> (<span class="git-green">feature-login</span>) Add unit tests</terminal-line>
    <terminal-line><span class="git-red">|</span> * <span class="nri-orange-color">e5f6b31</span> Add feature</terminal-line>
    <terminal-line>* <span class="git-green">|</span> <span class="nri-orange-color">d4a2f81</span> Update README</terminal-line>
    <terminal-line><span class="git-red">|</span><span class="git-green">/</span></terminal-line>
    <terminal-line>* <span class="nri-orange-color">f1b2c34</span> Initial project setup</terminal-line>
</terminal-window>
</div>

### Git show

The `git show` command lets you look into specific Git objects, usually one commit.

#### When to use {: .no-toc }

- You already know the commit you care about and want to see its message, metadata and diff in one shot.
- You want to see what a specific file looked like at a specific past commit.
- You want to double-check a tag's message and what commit it points to.

#### How to use {: .no-toc }
```
git show <commit>
```

Running only `git show` will display details about the most recent commit.

`<commit>` can be any Git reference (e.g., commit hash, branch name, tag, references like `HEAD~2`, etc.).

You can also specify a single file after the Git reference, to see that file's version at that point in time:
```
git show <commit>:<file-path>
```

### Git diff

#### When to use {: .no-toc }

Run `git diff` to visualise the source code differences. 

#### How to use {: .no-toc }

A useful command to see the difference between the local branch and the remote branch:
```
git diff origin/<branch>
```
A good step before pushing the local branch to the remote branch.

To display the difference in a graphical diff program, run `git difftool -y --tool=<program>`. 
For example, if you want to use the program `meld`, then run:
```
git difftool -y --tool=meld
```

## Get remote changes

### Git fetch

The `git fetch` command updates your remote tracking branches.

#### When to use {: .no-toc }

At the beginning of your work and before switching branches.

Use `git fetch` to:

- To update remote tracking branches when your workspace has uncommitted changes that you don't want to disturb or `stash`.

- To update remote tracking branches when your local repository clone has become stale.


#### How to use {: .no-toc }

To fetch updates from the remote repository, simply run
```
git fetch
```
This assumes that you have only one *remote*. It is also a good practice to keep branches *pruned*. Use
```
git fetch -p
```
to remove any remote-tracking references that no longer exist on the remote.
The full command uses an optional *remote* and an optional *branch*, e.g.:
```
git fetch [<remote>] [<branch>]
```

!!! tip
    Unlike `git pull`, `git fetch` does not merge or rebase changes into your current branch. This makes it useful when you want to inspect remote updates before integrating them.

### Git pull

The `git pull` command updates your remote tracking branches *and* updates the local branch in your current workspace to match the remote.

#### When to use {: .no-toc }

At the beginning of your work and before switching branches.

Use `git pull`:

- To update the local branch in your current workspace when the branch is clean and there are no uncommitted changes and no potential merge conflicts from the remote tracking branch.

- To update the local branch when you are prepared to deal with merge conflicts coming from the remote tracking branch.

#### Recommended usage {: .no-toc }

Before running `git pull`, make sure you are on the local branch that you want to update. Then run
```
git pull
```
Warning: If your local and remote branches have diverged, `git pull` by default reports an error asking you to specify how to reconcile the divergent branches.
To reapply your local commits on top of the latest remote commits, use:
```
git pull --rebase
```
instead. See `git merge` and `git rebase` here for more details. The full command also uses an optional *remote* and an optional *branch*, e.g.:
```
git pull [<remote>] [<branch>]
```

## Work with branches

### Git switch

Git switch allows us to switch the `HEAD` to a different branch.

#### When to use {: .no-toc }

- To create a new branch.
- To switch to an existing branch, either local or remote.


#### How to use {: .no-toc }

##### Create a new branch {: .no-toc }

To create a new branch that doesn't exist locally or on the remote repository:
```
git switch -c <new_branch_name> [<source_branch>]
```

This creates the new branch and switches to it.

##### Switch to an existing branch {: .no-toc }

To switch to a branch that already exists locally, simply use:
```
git switch <existing_branch>
```

If this branch only exist on the remote directory but not locally, please use:
```
git switch --track origin/<existing_branch>
```

### Git merge
`git merge` combines the histories of two branches. If the branches have diverged, Git will usually create a merge commit that keeps the history of both branches.

```mermaid
%%{init: {"themeVariables": {"git0": "#0077CC", "git1": "#A5CD3A"}}}%%
gitGraph
    commit id: "A"
    branch feature
    commit id: "D"
    checkout main
    commit id: "B"
    commit id: "C"
    checkout feature
    commit id: "E"
    checkout main
    merge feature id: "M"
```

#### When to use {: .no-toc }

- To combine completed work from another branch.
- When preserving the existing branch history is useful.
- When working on a shared branch where rewriting existing commits should be avoided.

#### How to use {: .no-toc }

First, switch to the branch that should receive the changes:

```
git switch <target-branch>
```

Then merge the other branch:

```
git merge <branch-to-merge>
```

For example:

```
git switch main
git merge feature-branch
```

If Git cannot combine the changes automatically, it will report a merge conflict. Resolve the conflicting files, stage them, and complete the merge:

```
git add <resolved-file>
git commit
```

### Git rebase

`git rebase` moves your branch commits so they are replayed on top of another branch. This can create a cleaner, more linear history.

A common workflow is to update a feature branch with the latest changes from `main`:

```
git switch feature-branch
git fetch origin
git rebase origin/main
```

Conceptually, this changes a history like:


Before rebase:

```mermaid
%%{init: {"themeVariables": {"git0": "#0077CC", "git1": "#A5CD3A"}}}%%
gitGraph
    commit id: "Commit A"
    branch feature
    commit id: "Commit D"
    checkout main
    commit id: "Commit B"
    commit id: "Commit C"
    checkout feature
    commit id: "Commit E"
```

After rebase:

```mermaid
%%{init: {"themeVariables": {"git0": "#0077CC", "git1": "#A5CD3A"}}}%%
gitGraph
    commit id: "Commit A"
    commit id: "Commit B"
    commit id: "Commit C"
    branch feature
    commit id: "Commit D'"
    commit id: "Commit E'"
```

#### When to use {: .no-toc }

- To update a feature branch with recent changes from another branch.
- To keep feature branch history relatively linear.
- To tidy local work before it is merged.

#### Resolving rebase conflicts {: .no-toc }

If Git finds a conflict during the rebase, resolve the affected files and stage them:

```
git add <resolved-file>
```

Then continue:

```
git rebase --continue
```

To cancel the rebase and return to the state before it started:

```
git rebase --abort
```

??? warning "Rebasing: things to keep in mind"

    - **Avoid rebasing shared branches.** Rebase rewrites commit history, which can cause problems for others working from the same commits.

    - **Rebase your own feature branches when appropriate.** It can help incorporate upstream changes and maintain a linear commit history.
    
    - **Be careful when pushing rebased commits.** If your feature branch has already been pushed, you may need to update the remote branch using `git push --force-with-lease`. This checks whether the remote branch has changed unexpectedly before updating it, reducing the risk of overwriting someone else's work.

## Temporarily save changes

### Git stash

Git stash works as a temporary save button. It lets us save changes that we are not ready to commit, so we can temporarily switch to other work without committing unfinished changes to the Git history.

#### When to use {: .no-toc }

- If working on one branch and needing to switch to another branch.
- To pull updates from the remote repository, when local changes are not ready to commit.
- If working on the wrong branch, to move those changes to the correct branch.

#### How to use {: .no-toc }

#### 1. Save changes {: .no-toc }

To save our current changes in the stash, with a message to help us remember what they are:
```
git stash push -m "Message for myself Nov 13th"
```
Think of this as putting our changes into a virtual drawer and leaving a sticky note on it. 
By default, `git stash` saves changes to tracked files that are modified or deleted. 
Untracked files are not included unless we explicitly ask Git to include them.

#### 2. List stashes {: .no-toc }

To see all the stashes you have created:
```
git stash list
```
We may see something like:
```
stash@{0}: On main: WIP: Message for myself Nov 13th
stash@{1}: On dev: update documentation
```

To check the content of one specific stash, for example, `{0}`:
```
git stash show -p stash@{0}
```
 {: .no-toc }

To bring the changes from the most recent stash onto our current branch:
```
git stash pop
```
or
```
git stash apply
```
The latter command leaves a copy in the stash.


#### 4. Clean up stash {: .no-toc }

To delete a specific stash:
```
git stash drop stash@{0}
```
Or to clean up all stashes:
```
git stash clear
```

## Undo or reset changes

### Git reset

#### When to use {: .no-toc }

Use `git reset` when the state of the branch needs to be changed to the state of another branch. e.g., synchronising two branches. 
This command is to be used carefully because it may delete the state of the current branch by changing its history and discarding uncommitted changes. 

#### How to use {: .no-toc }
```
git reset --hard origin/<branch>
```
is a useful command to reset the local branch to match the remote branch.
