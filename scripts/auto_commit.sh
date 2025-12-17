#!/bin/bash

# Automated commit script for Google Drive backups

set -e

DATE_STAMP=$(date +"%Y-%m-%d %H:%M:%S")
BACKUP_DIR="gdrive_backup"

echo "=== Auto-commit Google Drive Backup ==="
echo "Timestamp: $DATE_STAMP"
echo ""

# Check if there are changes
if [[ -z $(git status -s) ]]; then
    echo "No changes to commit."
    exit 0
fi

echo "Changes detected. Committing..."
git add "$BACKUP_DIR"
git commit -m "Google Drive backup - $DATE_STAMP"

echo ""
echo "Commit successful!"
echo "To push to GitHub, run: git push"
echo "Or to push now, run: git push origin main"
