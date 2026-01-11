# Troubleshooting Guide

## Common Issues

### Archive Processing

**Issue:** Archives are too large (>100MB)
**Solution:**
1. Edit `scripts/create_yearly_archives.py`
2. Reduce `MAX_SIZE = 95 * 1024 * 1024` to smaller value (e.g., 80MB)
3. Re-run the script

**Issue:** Files categorized to wrong year
**Solution:**
1. Check filename patterns in `scripts/create_yearly_archives.py`
2. Add new pattern to `extract_year_from_filename()` function
3. Re-run the script

### Git Operations

**Issue:** Push fails due to large file size
**Solutions:**
- Commit and push in smaller batches (e.g., by year)
- Verify files are under 100MB: `find data/takeout/archives -name "*.zip" -size +100M`
- Consider GitHub LFS for files >50MB (requires setup)

**Issue:** Push fails with timeout
**Solutions:**
- Push fewer files at once
- Check network connection
- Try: `git config http.postBuffer 524288000`

### Testing

**Issue:** Tests fail unexpectedly
**Solutions:**
1. Check if all dependencies are installed: `pip3 install pytest`
2. Verify file paths are correct
3. Check if test data exists
4. Run with verbose output: `python3 -m pytest test/ -v -s`

**Issue:** Import errors in tests
**Solutions:**
1. Ensure you're running from repository root
2. Check Python path includes the repository
3. Install any missing dependencies

## Getting Help

1. Check this troubleshooting guide first
2. Review relevant documentation in `docs/robots/`
3. Check agent configuration in `.github/agents/back-my-bitch-up.md`
4. Review git history for similar issues: `git log --all --grep="<keyword>"`
