# Python Git Practice – Notes

## What I Learned

This file was created on the `feature-notes` branch to demonstrate branching in Git.

### Key Git Commands

```bash
# Check status of your repo
git status

# Stage all files
git add .

# Commit with a message
git commit -m "your message here"

# Create a new branch
git checkout -b feature-notes

# Merge a branch into master
git checkout master
git merge feature-notes

# Push to GitHub
git push origin master
```

### Why Use Branches?
Branches let you work on new features or experiments without affecting the
main codebase. Once the feature is ready, you merge it back in.

---

## Git Workflow Summary

1. `git init` → Start a new repository
2. `git add .` → Stage all changes
3. `git commit -m "message"` → Save a snapshot
4. `git branch feature-name` → Create a branch
5. `git checkout feature-name` → Switch to it
6. `git merge feature-name` → Merge it back
7. `git push origin master` → Upload to GitHub

## Important Git Concepts

| Concept | Description |
|---------|-------------|
| Repository | A folder tracked by Git |
| Commit | A saved snapshot of changes |
| Branch | An independent line of development |
| Merge | Combining two branches together |
| Remote | A hosted version on GitHub |
| Clone | Download a remote repository |
| Pull | Fetch + merge remote changes |
| Push | Upload local commits to remote |
