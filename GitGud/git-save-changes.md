To save the changes you've made to your local files in your local Git repository, you should use the following Git commands:

1. **`git add .`** or **`git add <file>`**

   This command stages the changes you've made, preparing them to be included in the next commit.

   - `git add .` stages **all** modified and new files in the current directory and its subdirectories.
   - `git add <file>` stages only the specific file(s) you name, giving you finer control over what gets committed.

2. **`git commit -m "Your commit message"`**

   This command records the staged changes as a new commit in your local Git repository. The `-m` flag lets you provide a short message describing what you changed and why.

### Example Workflow

Suppose you edited a file called `app.py` and created a new file called `utils.py`:

```bash
# Stage specific files
git add app.py utils.py

# Commit with a descriptive message
git commit -m "Add utility functions and update app logic"
```

Or, to stage everything at once:

```bash
# Stage all changes
git add .

# Commit
git commit -m "Add utility functions and update app logic"
```

### Useful Variations

| Command | What It Does |
|---|---|
| `git add -A` | Stages all changes, including deletions, across the entire repo |
| `git add -p` | Interactively stage individual hunks of changes (useful for partial commits) |
| `git commit -am "message"` | Combines `add` and `commit` for **tracked** files only (won't pick up new untracked files) |
| `git status` | Shows which files are staged, modified, or untracked — helpful to run before committing |
| `git diff` | Shows the exact line-by-line changes in your working directory that haven't been staged yet |

### Recommended Practice

A typical workflow looks like this:

```bash
git status              # 1. Review what has changed
git diff                # 2. Inspect the actual changes
git add .               # 3. Stage the changes
git status              # 4. Confirm what will be committed
git commit -m "message" # 5. Commit with a clear message
```

After committing, your changes are saved in your **local** repository. If you want to share them with others or back them up to a remote server (like GitHub), you would then run:

```bash
git push
```

But that step is separate from saving locally — `git add` + `git commit` is all you need to save your work in your local Git repository.
