# Essential Git Commands

This document is for someone who has heard about git and may be familiar with some git commands.

## Introduction

This article provides a practical reference for Git users for day-to-day development workflows, including working with ACCESS-NRI repositories.
It is not intended as a beginner introduction to Git. You can use this page as a quick reminder when you need to:

- work with local and remote branches;
- keep your branch up to date;
- temporarily put unfinished changes aside;
- inspect commits and changes;
- compare different versions of files; or
- reorganise or combine Git history.

!!! note
    The examples below use generic branch names such as `main` and `feature-branch`. Replace these with the branch names used in your repository.
!!! note
    [<argument>] mean optional argument.


## Basic git commands

Here are a few core Git commands that are useful to keep handy in everyday Git workflows. For more details, please refer to the link in the command.

| Command | Basic Usage | Manual | Common Use Case | Meaning |
|---|---|---|---|---|
| `git clone` | `git clone <url> <local_dir>` | [link](https://git-scm.com/docs/git-clone) | | Clone a remote repository to the local directory|
| `git branch`|  `git branch -a` | [link](https://git-scm.com/docs/git-branch) | | List all branches |
| `git status` | `git status` | [link](https://git-scm.com/docs/git-status) | | Show status of current working tree. |
| `git add` | `git add <file>` | [link](https://git-scm.com/docs/git-add) | | Stage changes for commit. |
| `git commit` | `git commit -m "<message>"` | [link](https://git-scm.com/docs/git-commit) | | Save staged changes as a new commit. |
| `git push`| `git push` | [link](https://git-scm.com/docs/git-push) | | Push local commits to the remote repository. |
| `git fetch` | `git fetch [<remote>]` | [link](https://git-scm.com/docs/git-fetch) | [Go to section](#git-fetch) | Update remote tracking branches |
| `git pull` | `git pull` | [link](https://git-scm.com/docs/git-pull) | [Go to section](#git-pull) | updates the local branch to match the remote |
| `git switch` | `git switch [-c] <branch>` | [link](https://git-scm.com/docs/git-switch) | [Go to section](#git-switch) | Switch the HEAD to a different branch |
| `git merge` | `git merge <feature-branch>` | [link](https://git-scm.com/docs/git-merge) | [Go to section](#git-merge) | Combines the histories of two branches |
| `git rebase` | `git rebase <branch>` | [link](https://git-scm.com/docs/git-rebase) | [Go to section](#git-rebase) | Moves your branch commits on top of another branch |
| `git stash` | `git stash [push\|pop\|apply]` | [link](https://git-scm.com/docs/git-stash) | [Go to section](#git-stash) | Temporarily save changes into stash space |
| `git reset` | `git reset --hard origin/<branch>` | [link](https://git-scm.com/docs/git-reset) | [Go to section](#git-reset) | Reset branch to match another branch state |
| `git log` | `git log [-c]` | [link](https://git-scm.com/docs/git-log) | [Go to section](#git-log) | Show the history of the repository |
| `git show` | `git show <commit>` | [link](https://git-scm.com/docs/git-show) | [Go to section](#git-show) | Look into a specific Git commit |
| `git diff` | `git diff origin/<branch>` | [link](https://git-scm.com/docs/git-diff) | [Go to section](#git-diff) | Visualise source code differences |

## Git fetch

The `git fetch` command updates your remote tracking branches.

### When to use

At the beginning of your work and before switching branches.

Use `git fetch`:
1. To update remote tracking branches when your workspace has uncommitted changes that you don't want to disturb or `stash`.
2. To update remote tracking branches when your local repository clone has become stale.

### How to use

The full command uses an optional *remote* and an optional *branch*, e.g.:
```
git fetch origin main
```
### Recommended usage

To use `git fetch`:
The command is
```
git fetch
```
(assuming that you have only one *remote*). It is also a good idea to keep branches *pruned*. Use
```
git fetch -p
```
to delete local tracking branches that refer to remote branches that have been removed.


## Git pull

The `git pull` command updates your remote tracking branches *and* updates the local branch in your current workspace to match the remote.

### When to use

At the beginning of your work and before switching branches.

Use `git pull`:
1. To update the local branch in your current workspace when the branch is clean and there are no uncommitted changes and no potential merge conflicts from the remote tracking branch.
2. To update the local branch when you are prepared to deal with merge conflicts coming from the remote tracking branch.

### Recommended usage

To use `git pull`:
Make sure that your current local branch is the one that you want to update. Then run
```
git pull
```
Warning: This can trigger a `git merge` if the remote and local branches have different commits. You might instead want to consider using
```
git pull --rebase
```
instead. See `git merge` and `git rebase` here for more details. The full command also uses an optional *remote* and an optional *branch*, e.g.:
```
git pull origin main
```

## Git switch

Git switch allows us to switch the `HEAD` to a different branch.

### When to use

- To create a new branch.
- To switch to an existing branch, either local or remote.


### How to use

#### 1. Create a new branch

To create a new branch that doesn't exist locally or on the remote repository:
```
git switch -c <new_branch_name> [<source_branch>]
```

This creates the new branch and switches to it.

#### 2. Switch to an exiting branch

To switch to a branch that already exists locally, simply use:
```
git switch <existing_branch>
```

If this branch only exist on the remote directory but not locally, please use:
```
git switch --track origin/<existing_branch>
```

## Git merge
`git merge` combines the histories of two branches. If the branches have diverged, Git will usually create a merge commit that keeps the history of both branches.

### When to use

- To combine completed work from another branch.
- When preserving the existing branch history is useful.
- When working on a shared branch where rewriting existing commits should be avoided.

### How to use
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

## Git rebase

`git rebase` moves your branch commits so they are replayed on top of another branch. This can create a cleaner, more linear history.

A common workflow is to update a feature branch with the latest changes from `main`:

```
git switch feature-branch
git fetch origin
git rebase origin/main
```

Conceptually, this changes a history like:

### When to use
- To update a feature branch with recent changes from another branch.
- To keep feature branch history relatively linear.
- To tidy local work before it is merged.

### Resolving rebase conflicts
If Git finds a conflict during the rebase, resolve the affected files and stage them:

```
git add <resolved-file>
```

Then continue:

````
git rebase --continue
```

To cancel the rebase and return to the state before it started:

```
git rebase --abort
```

_**Important note**: Rebase rewrites commit history, so avoid rebasing commits that other people are already working from on a shared branch.
For your own feature branch, rebasing before opening or updating a pull request can be useful for incorporating recent upstream changes while keeping the history straightforward._

## Git stash

Git stash works as a temporary save button. It lets us save changes that we are not ready to commit, so we can temporarily switch to other work without committing unfinished changes to the Git history.

### When to use

- If working on one branch and needing to switch to another branch.
- To pull updates from the remote repository, when local changes are not ready to commit.
- If working on the wrong branch, to move those changes to the correct branch.

### How to use

#### 1. Save changes
To save our current changes in the stash, with a message to help us remember what they are:
```
git stash push -m "Message for myself"
```
Think of this as putting our changes into a virtual drawer and leaving a sticky note on it. 
By default, `git stash` saves changes to tracked files that are modified or deleted. 
Untracked files are not included unless we explicitly ask Git to include them.

#### 2. List stashes
To see all the stashes you have created:
```
git stash list
```
We may see something like:
```
stash@{0}: On main: WIP: fix restart handling
stash@{1}: On dev: update documentation
```

To check the content of one specific stash, for example, `{0}`:
```
git stash show -p stash@{0}
```

#### 3. Apply a stash

To bring the changes from the most recent stash onto our current branch:
```
git stash pop
```
or
```
git stash apply
```
The later command leave a copy in the stash.


#### 4. Clean up stash 
To delete a specific stash:
```
git stash drop stash@{0}
```
Or to clean up all stashes:
```
git stash clear
```


## Git reset

### When to use

Use `git reset` when the state of the branch needs to be changed to the state of another branch. e.g., Synchronising two branches. This command is to be used carefully because it may delete the state of the current branch by changing its history. Refer to the manual page for details: https://git-scm.com/docs/git-reset

### How to use
```
git reset --hard origin/<branch>
```
is a useful command to reset the local branch to match the remote branch.


## Git log

### When to use

Use `git log` to see the history of the repository. Refer to the manual page for details: https://git-scm.com/docs/git-log

### How to use
```
git log -c
```
provides the output of `git log` mixed with the code changes.

-- Insert image with explanation of `git log --graph` output

## Git show

The `git show` command lets you look into specific Git objects, usually one commit.

### When to use

- You already know the commit you care about and want to see its message, metadata and diff in one shot.
- You want to see what a specific file looked like at a specific past commit.
- You want to double-check a tag's message and what commit it points to.

### How to use
```
git show <commit>
```

Running only `git show` will display details about the most recent commit.

`<commit>` can be any Git reference (e.g., commit hash, branch name, tag, references like `HEAD~2`, etc.).

You can also specify a single file after the Git reference, to see that file's version at that point in time:
```
git show <commit>:<file-path>
```

## Git diff

### When to use

`git diff` to visualise source code differences. Refer to the manual page for details: https://git-scm.com/docs/git-diff

### How to use

A useful command to see the difference between the local branch and the remote branch:
```
git diff origin/<branch>
```
A good step before pushing the local branch to the remote branch.

A useful command to display the diff in the graphical diff program `meld`. Another diff program be used by replacing `meld` with the name of the executable.
```
git difftool -y --tool=meld
```

_Last updated: YYYY-MM-DD_