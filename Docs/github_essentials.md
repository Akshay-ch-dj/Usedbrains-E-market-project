# The essential commands to manage git and github <!-- omit in toc -->

<!-- omit in toc -->
## Table of contents

- [Changing the remote url](#changing-the-remote-url)
- [Rollbacks](#rollbacks)
  - [Identifying old commits](#identifying-old-commits)
- [Git branching basics](#git-branching-basics)
  - [Working with branches](#working-with-branches)
  - [Merging Branches](#merging-branches)
  - [Merge conflicts](#merge-conflicts)
  - [To view the commit history as a cli graph](#to-view-the-commit-history-as-a-cli-graph)
- [Working with remote](#working-with-remote)
  - [`pull`, `merge` & `push` workflow](#pull-merge--push-workflow)

## Changing the remote url

* To change remote url to `https`.

  ```bash
  git remote set-url origin <https://-->

  # OR

  git remote add origin <https://-->

  # Then push the contents
  git push -U origin master/main
  ```

## Rollbacks

* To Rollback commits in git, use `git revert`, It is noy just an "undo", it creates a commit that contains the inverse of all the changes made in the bad-commit. So that the history of commits remain consistent, leaving a record of what happened.
* Revert latest commit using the `HEAD`(pointer to the snapshot of current commit.),\
  `git revert HEAD`\
  Always add an explanation of why the revert is being made, (let your future self know what's happening), add a **Reason for rollback**: *xxx is unidentified, giving EEE error*,

### Identifying old commits

* Check logs, to identify the commits you are looking for using `git log`, `git log -1` gives the last commit, `git log -2`(last 2) etc..
* Uses the **commit id** (HASH value using sha algorithm), from the logs or github, get the commit id and do the,\
  `git revert <id>`\
  To identify it is correct use `git show <id>`

## Git branching basics

---

* A branch at a basic level represent independent line of development in a project
* master(now:- main), is the default branch the git creates, when a new repo is initiated.
* Use `git branch`:- To view all the branches in the repo,
* with `git branch new-feature` :- A branch named "new-feature" is created,
* Use `git checkout new-feature` :- Switches to the branch "new-feature",
* Use `git checkout -b new-feature` :- Create and switch in a single command.

### Working with branches

* Always use `git status` to identify the current status and condition,
* Git changes or adds the commit to where the HEAD is pointing(branch), latest commit to other branches doesn't shows up,
* Working on a different branch, the history will only be added to that branch (also working directory), simply each branch is a pointer to specific commit in a series of snapshots.
* To delete a new branch,

  ```bash
  git push -d <remote_name> <branch_name> # remote
  git branch -d <branch_name> # local
  ```

  If there is unmerged changes left, git will indicate with an error.

### Merging Branches

* `merge` is the term git uses for combining branched data and history together.\
  `git merge`,\
  Takes independent snapshots and history of one git branch and tangle them into another.
* To do a git merge, first checkout to the master branch.\
  `git merge new-branch`\
  `git log`  (Now HEAD points at the master, both master and new-branch pointing at same commit.)
* A "**fast-forward**" merge: - Occurs when both branches got exactly same history, the latest commit only differs, (no actual data merging takes but just updating the pointers)
* A "**Three way merge**" is performed when history of branches got diverged in some way, there is no linear pth to combine them via fast-forwarding,\
* In that case, git tries to figure out how to combine both snapshots. if the changes are made on different files or different places of the same file, git simply takes both changes and put them together for the resulting merge.\
* If the changes are made on the same part of the same file, the developer needs to decide what to do/take and that is called a **merge conflict**.

### Merge conflicts

* To deal with merge conflicts, git adds some information to files shows, the data from different branches and commits, choose what to keep
* Mark the conflict as resolved in the commit.
* To deal with tricky merge conflicts that spread across multiple files, use the `git merge --abort`, to trace back to previous commit

### To view the commit history as a cli graph

* `git log --graph --oneline` (only oneline per commit)

## Working with remote

* Look at the configuration of that remote by,\
  `git remote -v`
* Default assigned name to a remote repository is "origin", to get more info on remote,
  $`git remote show origin`

* To make changes to the remote branches, we need the full cycle,
  * Pull any new changes to the local branch,
  * merge them with our changes.
  * push our changes to the repo.
* `git status` also shows the status of remote branches, at start use the `git remote show origin` (to get an idea about remote), use `git fetch` to just copies the commits done in remote repository to remote branches, not mirrored to local branches - (not to local, shows what commits others made)
* Difference between `git fetch` and `git pull`, git fetch fetches remote updates but doesn't merge, git pull fetches remote updates and merges them.(git pull = git fetch + git merge(master))
* Use `git remote update`, that also get contents of all remote branches without automatically merging any contents to local branches,

### `pull`, `merge` & `push` workflow

* After the changes made before committing to the remote, use `git remote show origin`, to get info on whether changes made in the remote by other contributors, can also look for any new added branches `git branch -r`,
* Also if needed a more precise info on the changes made out,
  * First fetch that changes to our branches(not to local), using `git remote update`.
  * Then use `git status`, for the info about the new commits etc..
  * Also use the `git log --graph --oneline --all`, to show the changes graph.
  * There are also tools that gets handy, like to gwt the differences from our branch(master) use `git diff origin/master`
* To get our change in, Do a full cycle ie,
  * pull any new changes (`git pull`) (that merges the changes to our local branches and directory)
  * merge them with our changes (`git merge` from the req <branch>)
  * Then push it back `git push`
