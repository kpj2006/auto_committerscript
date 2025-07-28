# 🔁 Auto Committer Bot

A lightweight Git automation tool that commits files from a predefined list into a Git branch every few minutes. Ideal for gradually pushing changes like refactored files, notes, or generated content.

---

## 🚀 Features

- ✅ Automatically commits files line-by-line from `commit_list.txt`
- 🔄 Scheduled every 5 minutes using Python's `schedule` module
- 📤 Pushes commits to a specified Git branch
- 🧾 Logs detailed timestamps, stdout, stderr, and exit codes
- ❌ Exits gracefully when all files are committed

---

## 🛠️ Requirements

- Python 3.7+
- Git installed
- Bash (use Git Bash for Windows)
- Python module: `schedule`

Install the required Python module:
```bash
pip install schedule

```

## ✏️ step 1. copy and paste both file auto_committer.py and staged_commit.sh:



## ✏️ Step 2: Configure Paths
Open the file: staged_commit.sh
Update the following:

```bash
# Change this to your local repo path
REPO_DIR="/absolute/path/to/your/git/project"

# Change this to your target Git branch (e.g., main, dev)
BRANCH="main"
Windows (Git Bash) path example:
REPO_DIR="/c/Users/john/project-folder"
```
## ✏️ Step 3: Update Python Script (Optional)
In auto_committer.py, change this if your .sh file is in another path:

```bash
from pathlib import Path

# Path to the bash script relative to this file
SCRIPT_PATH = Path(__file__).parent / "staged_commit.sh"
```
✅ If both files are in the same directory, no changes needed.

## 📝 Step 4: Add Your Files to Commit
In commit_list.txt, list one file per line that you want committed one by one:

```bash
README.md
src/app.py
notes/architecture.txt
```
These should be relative to your Git repo directory, not the automation script directory.

## ▶️ Step 5: Run the Bot
Run the Python script using:

```bash
python auto_committer.py
```
This will:

-Trigger every 5 minutes

-Commit one file at a time

-Push it to the Git branch

-Remove the committed file from the list

Exit when done

## 🔍 Example Terminal Output
```bash
[2025-07-28 14:00:00] 🔄 Triggered auto_commit()
[2025-07-28 14:00:00] 🚀 Running: bash staged_commit.sh
[2025-07-28 14:00:01] 📤 Exit Code: 0
[2025-07-28 14:00:01] 🧾 STDOUT:
[main abc1234] ➕ Auto commit: README.md
 1 file changed, 10 insertions(+)
 create mode 100644 README.md
 ```
## 🧹 Auto Exit
Once all files are committed and the list is empty:

```bash
✅ All files committed. Nothing left.
📦 No files left. Exiting.
```
## 💡 Tips
Use this for slow-roll releases, content scheduling, or mass updates

Combine with cron or GitHub Actions for more advanced automation

## 📘 License
This project is licensed under the MIT License.

## 🙋‍♂️ Maintainer
Developed with ❤️ by Karun Pacholi
For issues, suggestions, or contributions – feel free to open a PR or issue!