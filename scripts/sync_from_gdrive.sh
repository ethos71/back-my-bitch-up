#!/bin/bash

# Google Drive Sync Script
# Downloads all files from Google Drive to local repository for GitHub backup

set -e

GOOGLE_ACCOUNT="dominick.do.campbell@gmail.com"
BACKUP_DIR="$(pwd)/gdrive_backup"
DATE_STAMP=$(date +"%Y-%m-%d_%H-%M-%S")

echo "=== Google Drive to GitHub Backup Script ==="
echo "Account: $GOOGLE_ACCOUNT"
echo "Backup Directory: $BACKUP_DIR"
echo "Started at: $DATE_STAMP"
echo ""

# Check if rclone is installed
if ! command -v rclone &> /dev/null; then
    echo "ERROR: rclone is not installed."
    echo "To install rclone:"
    echo "  curl https://rclone.org/install.sh | sudo bash"
    echo ""
    echo "After installation, configure it with:"
    echo "  rclone config"
    echo "  - Choose 'n' for new remote"
    echo "  - Name it 'gdrive'"
    echo "  - Choose 'Google Drive'"
    echo "  - Follow the prompts to authenticate"
    exit 1
fi

# Check if rclone is configured for Google Drive
if ! rclone listremotes | grep -q "^gdrive:"; then
    echo "ERROR: rclone 'gdrive' remote not configured."
    echo ""
    echo "Please configure rclone with:"
    echo "  rclone config"
    echo "  - Choose 'n' for new remote"
    echo "  - Name it 'gdrive'"
    echo "  - Choose 'Google Drive'"
    echo "  - Follow the prompts to authenticate with $GOOGLE_ACCOUNT"
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "Syncing files from Google Drive..."
echo "This may take a while depending on the size of your Google Drive..."
echo ""

# Sync root files (not in folders)
echo "Syncing root files..."
rclone copy gdrive: "$BACKUP_DIR" \
    --max-depth 1 \
    -P \
    --exclude ".DS_Store" \
    --exclude "*.tmp" \
    --exclude "Thumbs.db" \
    --exclude "desktop.ini"

# Sync each main folder from Google Drive
for folder in "Keep" "Misc" "Work"; do
    echo "Syncing $folder folder..."
    rclone sync "gdrive:$folder" "$BACKUP_DIR/$folder" \
        -P \
        --exclude ".DS_Store" \
        --exclude "*.tmp" \
        --exclude "Thumbs.db" \
        --exclude "desktop.ini"
done

echo ""
echo "=== Sync Complete ==="
echo "Files have been downloaded to: $BACKUP_DIR"
echo ""
echo "Next steps:"
echo "  1. Review the synced files: ls -la $BACKUP_DIR"
echo "  2. Add files to git: git add gdrive_backup/"
echo "  3. Commit changes: git commit -m 'Backup from Google Drive - $DATE_STAMP'"
echo "  4. Push to GitHub: git push"
echo ""
echo "To automate commits, you can run: ./auto_commit.sh"
