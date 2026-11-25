# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 was to practise the core Git workflow (`status`, `add`, `commit`, `log`), explain the difference between staging and committing, create and commit changes on a separate branch named `update-about`, understand how Pull Requests work on GitHub, and build a personal Git command glossary.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| Check repository status (`git status`) | Shows which branch I am currently on, which files were modified or untracked, and which changes are staged for the next commit. |
| Stage selected changes (`git add <file>`) | Places specific edited or newly created files into the staging area (index) to include them in the upcoming commit snapshot. |
| Create a commit (`git commit -m "..."`) | Permanently saves the currently staged snapshot into the local repository history with a descriptive message. |
| View commit history (`git log --oneline`) | Displays previous commits in reverse chronological order along with their short commit hashes and messages. |

**Difference between staging (`git add`) and committing (`git commit`):**  
Staging is like packing selected items into a box before shipping—you decide exactly which modified files belong together in the next snapshot, and you can still adjust or unstage them. Committing seals that box and records it permanently into the repository's version history.

---

### Task 6.2 — Create and use a branch
- Created and switched to a new branch named `update-about` using `git switch -c update-about`.
- Updated the root `README.md` on `update-about` by adding a **"My Learning"** section summarizing three key concepts learned across Missions 0–5.
- Checked `git status`, staged `README.md`, and committed the update with `"Add My Learning section to root README on update-about branch"`.
- Switched back to `main` (`git switch main`) so the feature branch stays isolated for Pull Request review.

---

### Task 6.3 — Create a Pull Request
- **What a branch is:** A branch is an independent line of development that lets you work on new edits or experiments without disturbing the stable `main` branch.
- **What a Pull Request (PR) is:** A Pull Request is a GitHub collaboration request proposing to merge changes from one branch (such as `update-about`) into another branch (such as `main`), giving teammates or instructors a place to inspect the diff, leave comments, and approve before merging.
- **Why they are useful in team projects:** Multiple people can work on separate features simultaneously without overwriting each other's code, and every change gets reviewed before entering `main`.
- **PR status:** The `update-about` branch is committed locally and prepared to push (`git push -u origin update-about`) so a Pull Request from `update-about` into `main` can be opened directly on GitHub (not yet merged unless requested by the instructor).

---

### Task 6.4 — Build your Git command glossary

| Git operation | One-line explanation in my own words |
|---|---|
| Initialise a repository (`git init`) | Turns a regular local folder into a Git-tracked repository by creating a `.git` history store. |
| Check status (`git status`) | Reports the active branch and lists untracked, modified, and staged files. |
| Stage changes (`git add`) | Marks chosen file changes so they are included in the next commit. |
| Commit changes (`git commit`) | Records a permanent snapshot of staged changes with a descriptive message. |
| View history (`git log`) | Lists past commits, authors, timestamps, and commit messages in the repository. |
| Create or list branches (`git branch`) | Displays existing branches or creates a new branch pointer at the current commit. |
| Switch branches (`git switch`) | Moves your working directory onto a different branch (and `-c` creates it first). |
| Publish changes (`git push`) | Uploads local commits and branches to a remote repository such as GitHub. |
| Retrieve remote changes (`git pull`) | Downloads new commits from a remote branch and integrates them into your current local branch. |

## 3. Commands / tools used
- `git status`, `git add`, `git commit -m`, `git log --oneline --graph --all` — Used to track and inspect mission history.
- `git switch -c update-about`, `git switch main`, `git branch -a` — Used to create, commit to, and switch between branches cleanly.
- Text editor — Updated the root `README.md` on `update-about` and documented Mission 6.

## 4. My understanding
Git separates modifying files, choosing what to stage, and committing snapshots so developers never lose work or mix unrelated changes. Branches and Pull Requests build on that by letting people propose, review, and discuss updates safely before merging them into `main`.

## 5. Difficulties faced
Keeping track of which branch I was currently editing on when switching between `update-about` and `main` required careful checking so edits landed on the right branch.

## 6. How I resolved them
I ran `git branch` and `git status` before every edit and commit, and inspected `git log --oneline --graph --all` afterward to confirm `update-about` diverged cleanly from `main`.

## 7. Evidence / files
- `mission-06-git-github/README.md`
- Branch `update-about` (commit `8da11cf` adding `## My Learning` to root `README.md`)
- [Git status, branches, and commit graph screenshot](../evidence/mission-06/01-git-status-log-branch.png)
- [Git branch and Pull Request workflow diagram](../evidence/mission-06/02-branch-pr-workflow.png)

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Status:** Committed locally on `main`; branch `update-about` ready to push for Pull Request on GitHub.
