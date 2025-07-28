#!/bin/bash

REPO_DIR="/path/to/your/repo"  
BRANCH="test"
LIST_FILE="commit_list.txt"

cd "$REPO_DIR" || exit 1

# Get the next file to commit
NEXT_FILE=$(head -n 1 "$LIST_FILE")

if [ -z "$NEXT_FILE" ]; then
  echo "✅ All files committed. Nothing left."
  exit 3  # Custom exit code to signal 'done' to auto_committer.py
fi

# Add, commit, and push
git add "$NEXT_FILE"
git commit -m "➕ improve and push $NEXT_FILE"
git push origin "$BRANCH"

# Remove first line (done file)
tail -n +2 "$LIST_FILE" > tmp.txt && mv tmp.txt "$LIST_FILE"
