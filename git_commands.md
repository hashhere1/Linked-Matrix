# Git Commands Cheat Sheet

A handy list of essential Git commands with their descriptions.

---

## Project Setup

- `git init`  
  Initialize a new Git repository in the current folder.

- `git clone <repo-url>`  
  Clone a remote repository to your local system.

---

## Configuration

- `git config --global user.name "Your Name"`  
  Set your Git username globally.

- `git config --global user.email "you@example.com"`  
  Set your Git email globally.

- `git config --list`  
  Show current Git configuration.

---

## Staging & Committing

- `git status`  
  Check the current status of files.

- `git add <filename>`  
  Stage a specific file for commit.

- `git add .`  
  Stage all changes (new, modified, deleted).

- `git commit -m "Your message"`  
  Commit changes with a message.

---

## Working with Remote Repositories

- `git remote add origin <repo-url>`  
  Add a remote repository named `origin`.

- `git push -u origin main`  
  Push changes to `main` branch and set upstream.

- `git push`  
  Push committed changes to the remote repository.

- `git pull`  
  Pull updates from the remote repository and merge.

---

## Branching

- `git branch`  
  List all branches.

- `git branch <branch-name>`  
  Create a new branch.

- `git checkout <branch-name>`  
  Switch to an existing branch.

- `git checkout -b <branch-name>`  
  Create and switch to a new branch.

- `git merge <branch-name>`  
  Merge a branch into the current one.

---

## Logs & Diffs

- `git log`  
  View commit history.

- `git log --oneline`  
  View a compact log.

- `git diff`  
  Show unstaged differences.

- `git diff --staged`  
  Show staged differences.

---

## Undo / Reset / Revert

- `git reset <file>`  
  Unstage a file (keep changes).

- `git checkout -- <file>`  
  Revert file to last committed version.

- `git reset --hard`  
  Discard all uncommitted changes (irreversible).

- `git revert <commit-hash>`  
  Create a commit that reverses an earlier one.

---

## Cleanup

- `git clean -f`  
  Remove untracked files.

- `git rm <filename>`  
  Delete and stage file for removal.

---

## GitHub (via CLI)

- `gh auth login`  
  Authenticate GitHub CLI.

- `gh repo create`  
  Create a new GitHub repository from terminal.

---
