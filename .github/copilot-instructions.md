# Cloud Backup Project - Copilot Instructions

**Alias: `cb`** (use this to quickly reference this project context)

## Project Overview

This repository stores yearly backups from Google Takeout (Google Photos, Google Drive, etc.) on GitHub. Files are organized by year and split into archives under 100MB to comply with GitHub's file size limits.

## Current Status

- **Last Full Year Archived:** 2024
- **Total Archives:** 125 files (2014-2024)
- **Total Size:** ~9.4GB
- **Next Scheduled Run:** 2025 (to be processed after year completes)

## Annual Backup Process (REPEATABLE)

### 1. Download from Google Takeout

**Timing:** Run this process once per year, after the year completes (e.g., run in January 2026 to capture 2025 data)

1. Go to https://takeout.google.com/
2. Click "Deselect all"
3. Select data to backup:
   - Google Photos ✓
   - Google Drive ✓
   - Any other desired services
4. Click "Next step"
5. Configure export settings:
   - Delivery method: "Send download link via email"
   - Frequency: "Export once"
   - File type: ".zip"
   - File size: "50 GB" (recommended)
6. Click "Create export"
7. Wait for email (usually a few hours, up to 24 hours)
8. Download all .zip files to `takeout/source/` directory

### 2. Process Archives

Run the archive creation script:

```bash
cd /home/dominick/workspace/cloud-backup
python3 create_yearly_archives.py
```

This will:
- Extract files from `takeout/source/*.zip`
- Organize files by year based on filename patterns and metadata
- Create archives under 100MB in `takeout/archives/`
- Files >95MB are automatically skipped (logged in output)

**Expected Output:**
- New yearly archives in `takeout/archives/YYYY_partNN.zip` format
- Summary showing file counts and sizes per year
- List of any skipped large files

### 3. Review Archives

Verify the created archives:

```bash
# Check archive count and sizes
ls -lh takeout/archives/YYYY_part*.zip

# Verify all under 100MB
find takeout/archives -name "*.zip" -size +100M

# Count total archives
ls takeout/archives/*.zip | wc -l
```

### 4. Update Documentation

Update README.md:
- Set "Last Full Year Archived" to the newly processed year
- Update "Total Archives" count
- Update "Total Size"
- Update "Next Scheduled Run" to following year

### 5. Commit to GitHub

```bash
git add README.md takeout/archives/YYYY_part*.zip
git commit -m "Add YYYY yearly archives

- Processed N files from Google Takeout
- Created X archives under 100MB
- Total size: Y GB"
git push origin main
```

### 6. Cleanup

After successful push to GitHub:

```bash
# Remove temporary extraction directory (if exists)
rm -rf takeout/temp_extract

# Archive or remove source files (they're large)
# Option 1: Move to external backup
mv takeout/source/*.zip /path/to/external/backup/

# Option 2: Delete (data is now in yearly archives on GitHub)
rm takeout/source/*.zip
```

## File Organization

```
takeout/
├── source/              # Original Google Takeout zip files (temporary)
├── archives/            # Yearly archives <100MB (committed to git)
│   ├── 2014_part01.zip
│   ├── 2015_part01.zip
│   ├── ...
│   └── 2024_part15.zip
└── extracted_media/     # Legacy directory (can be removed)
```

## Important Notes

### Year Detection Logic

The script identifies year from filenames using these patterns:
- `20220517_130347.jpg` → 2022
- `signal-2018-10-06.jpg` → 2018
- `PXL_20210522_040825770.mp4` → 2021
- Falls back to file modification time if no pattern matches

### GitHub Limits

- **File size limit:** 100MB per file
- **Repository size:** No hard limit, but keep reasonable (<10GB recommended)
- Archives are set to max 95MB to safely stay under limit

### Troubleshooting

**If archives are too large:**
1. Edit `create_yearly_archives.py`
2. Reduce `MAX_SIZE = 95 * 1024 * 1024` to smaller value (e.g., 80MB)
3. Re-run script

**If files are categorized to wrong year:**
1. Check filename patterns in the script
2. Add new pattern to `extract_year_from_filename()` function
3. Re-run script

**If push fails due to size:**
- GitHub may reject very large pushes
- Commit and push in smaller batches (e.g., by year)
- Consider GitHub LFS for files >50MB (requires setup)

## Recovery Instructions

If you need to restore data:

1. Clone this repository
2. Extract specific year archives:
   ```bash
   cd takeout/archives
   unzip 2023_part*.zip -d ~/restored_2023_photos/
   ```

## Maintenance

**Annual Tasks:**
- ✅ Download Google Takeout data (January after year completes)
- ✅ Run archive creation script
- ✅ Review and commit to GitHub
- ✅ Update README with new status
- ✅ Cleanup source files

**Optional Monthly:**
- Check repository size: `du -sh .git`
- Verify GitHub remote is accessible: `git fetch origin`

## Contact & Questions

- Email: dominick.do.campbell@gmail.com
- Repository: https://github.com/ethos71/cloud-backup
