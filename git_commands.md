# Git Commands and Their Functions

## Initialization
- `git init`  
  Initializes a new Git repository in the current directory.

## Configuration
- `git config --global user.name "Your Name"`  
  Sets the global username.
- `git config --global user.email "your@example.com"`  
  Sets the global email.

## Staging and Committing
- `git add <filename>`  
  Adds a file to the staging area.
- `git add .`  
  Adds all modified and new files to the staging area.
- `git commit -m "Your message"`  
  Commits the staged changes with a message.

## Remote Repository
- `git remote add origin <repo-url>`  
  Adds a remote repository named `origin`.
- `git push -u origin main`  
  Pushes the committed code to the `main` branch and sets the upstream.

## Pulling and Cloning
- `git pull`  
  Fetches and merges changes from the remote repository.
- `git clone <repo-url>`  
  Clones a repository into a new directory.

## Branching
- `git branch`  
  Lists all local branches.
- `git checkout -b <branch-name>`  
  Creates and switches to a new branch.
- `git merge <branch-name>`  
  Merges the specified branch into the current one.

## Status and Logs
- `git status`  
  Shows the status of changes (tracked/untracked/staged).
- `git log`  
  Displays the commit history.

## Reset and Revert
- `git reset --hard <commit>`  
  Resets to a specific commit and discards all changes.
- `git revert <commit>`  
  Creates a new commit that undoes changes made in a specific commit.

