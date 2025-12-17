# Back My Bitch Up

This repository stores yearly backups from Google Takeout (Google Photos, Google Drive, etc.) on GitHub.

**Quick Access:** Use `@back-my-bitch-up` or alias `bmbu` to load the full project context and repeatable yearly process.

## Current Status

- **Last Full Year Archived:** 2024
- **Total Archives:** 125 files organized by year (2014-2024)
- **Total Size:** ~9.4GB
- **Next Scheduled Run:** 2025 (January 2026)

## Repository Structure

```
scripts/                 # All automation scripts
├── create_yearly_archives.py
├── auto_commit.sh
└── sync_from_gdrive.sh
docs/                    # All documentation
└── CHANGELOG.md
data/                    # All data files
├── takeout/
│   ├── source/          # Original Google Takeout zip files (temporary)
│   ├── archives/        # Yearly archives (<100MB each, committed to git)
│   │   ├── 2014_part01.zip
│   │   ├── 2015_part01.zip
│   │   ├── ...
│   │   └── 2024_part15.zip
│   └── extracted_media/ # Legacy directory
└── gdrive_backup/       # Google Drive backup data
```

## Annual Backup Process

### 1. Download from Google Takeout

**When:** Once per year after the year completes (e.g., January 2026 for 2025 data)

1. Go to https://takeout.google.com/
2. Click **"Deselect all"**
3. Select services to backup:
   - ✓ Google Photos
   - ✓ Google Drive
   - ✓ Any other desired services
4. Click **"Next step"**
5. Configure export settings:
   - **Delivery method:** "Send download link via email"
   - **Frequency:** "Export once"
   - **File type:** ".zip"
   - **File size:** "50 GB" (recommended)
6. Click **"Create export"**
7. Wait for email (usually a few hours, up to 24 hours for large libraries)
8. Download all .zip files to `data/takeout/source/` directory

**Note:** Downloads are available for 7 days after creation. Google Takeout includes all data at full quality with metadata (EXIF, captions, etc.)

### 2. Create Yearly Archives

Process downloaded files into yearly archives under 100MB:

```bash
python3 scripts/create_yearly_archives.py
```

**What it does:**
- Extracts files from `data/takeout/source/*.zip`
- Organizes by year using filename patterns and metadata
- Creates archives <100MB in `data/takeout/archives/`
- Skips files >95MB (logged in output)

**Expected output:**
- Summary of files per year
- List of created archives with sizes
- Any skipped large files

### 3. Review & Verify

```bash
# Check new archives
ls -lh data/takeout/archives/2025_part*.zip

# Verify all under 100MB
find data/takeout/archives -name "*.zip" -size +100M

# Count total
ls data/takeout/archives/*.zip | wc -l
```

### 4. Update Documentation

Update this README:
- "Last Full Year Archived" → new year
- "Total Archives" → new count
- "Total Size" → new total
- "Next Scheduled Run" → following year

### 5. Commit to GitHub

```bash
git add README.md data/takeout/archives/YYYY_part*.zip
git commit -m "Add YYYY yearly archives

- Processed N files from Google Takeout
- Created X archives under 100MB
- Total size: Y GB"
git push origin main
```

### 6. Cleanup

After successful push:

```bash
# Remove temporary extraction
rm -rf data/takeout/temp_extract

# Remove or archive source files (they're large)
rm data/takeout/source/*.zip
# OR move to external backup:
# mv data/takeout/source/*.zip /path/to/external/backup/
```

## Files

- `.github/agents/back-my-bitch-up.md` - Full project context and instructions (use `bmbu` alias)
- `.github/prompts/back-my-bitch-up.md` - System prompt configuration
- `scripts/create_yearly_archives.py` - Script to organize takeout into yearly archives
- `scripts/auto_commit.sh` - Helper script for git commits
- `scripts/sync_from_gdrive.sh` - Google Drive sync script
- `docs/CHANGELOG.md` - Version history
- `data/` - All data files (takeout, gdrive_backup)

## Data Recovery

To restore data from archives:

```bash
# Clone repository
git clone https://github.com/ethos71/back-my-bitch-up.git

# Extract specific year
cd back-my-bitch-up/data/takeout/archives
unzip 2023_part*.zip -d ~/restored_2023_photos/
```

## Troubleshooting

**Archives too large?**
- Edit `scripts/create_yearly_archives.py`
- Reduce `MAX_SIZE` from 95MB to 80MB
- Re-run script

**Files in wrong year?**
- Add filename patterns to `extract_year_from_filename()` in `scripts/create_yearly_archives.py`
- Re-run script

**Push fails?**
- Commit and push in smaller batches
- Push one year at a time
- Consider Git LFS for files >50MB

## Technical Details

- **GitHub file limit:** 100MB per file (archives are 95MB max)
- **Year detection:** Extracts from filename patterns (e.g., `20220517_130347.jpg` → 2022)
- **Fallback:** Uses file modification time if no pattern matches
- **Compression:** ZIP format with deflate compression
