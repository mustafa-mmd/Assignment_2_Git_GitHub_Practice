# Assignment 2 – Git & GitHub Practice

**Name:** Mustafa Jamal  
**Course:** Python Programming  
**Assignment:** Git & GitHub Practice Worksheet

---

## About This Repository

This repository contains Python lecture practice files demonstrating core programming concepts learned in class. It was also used to practice Git version control workflows including:

- Initializing a Git repository
- Staging and committing changes
- Creating and merging branches
- Pushing to GitHub

---

## Files

| File | Description |
|------|-------------|
| `lec1.py` | Python basics: variables, loops, functions, Gemini AI chatbot |
| `lec2.py` | File handling and Object-Oriented Programming (OOP) |
| `lec3.py` | Simple Python print statement practice |

---

## Git Concepts Practiced

##  Configuration & Setup
* **`git config --global user.name "Your Name"`** — Set your commit name across all local repositories.
* **`git init`** — Create a brand new Git repository in the current directory.
* **`git clone [url]`** — Copy an existing remote repository to your local machine.

##  Tracking Changes
* **`git status`** — Show changed, unstaged, and staged files in your working directory.
* **`git add [file]`** — Stage a specific file, prepping it for the next commit.
* **`git reset [file]`** — Unstage a file while fully preserving its changes in your working directory.
* **`git diff`** — Show unstaged modifications between your working directory and the last commit.
* **`git diff --staged`** — Show staged modifications ready for the next commit.
* **`git commit -m "[msg]"`** — Save staged changes as a permanent project snapshot with a custom message.

##  Branching & Merging
* **`git branch [name]`** — Create an isolated branch for safe development.
* **`git checkout [branch]`** — Switch your active working branch.
* **`git merge [branch]`** — Merge the specified branch's history into your current active branch.
* **`git log`** — Display the full commit history and author logs.

##  Remote Repositories
* **`git remote add [alias] [url]`** — Link your local repository to a remote hosting server (like GitHub).
* **`git fetch [alias]`** — Download branches and commits from a remote repository without merging them.
* **`git push [alias] [branch]`** — Upload local branch commits to the remote repository.
* **`git pull`** — Fetch remote changes and instantly merge them into your current branch.


---

## Branch Structure

- `master` – Main branch with all lecture files  
- `feature-notes` – Branch created to add extra notes (merged into master)
