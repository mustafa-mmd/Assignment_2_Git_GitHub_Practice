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
