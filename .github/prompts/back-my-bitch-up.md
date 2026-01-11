# Back My Bitch Up - System Prompt

You are assisting with the "Back My Bitch Up" project - a Google Takeout backup system that stores yearly archives on GitHub.

## Key Behaviors

- Use alias **`bmbu`** to reference this project
- Focus on yearly backup workflows and archive management
- Enforce GitHub's 100MB file size limit (archives max 95MB)
- Maintain year-based organization (2014-2024+)
- Guide annual Google Takeout download → process → commit cycle

## Primary Commands

- `python3 scripts/create_yearly_archives.py` - Process takeout data into yearly archives
- Archive verification and size checks
- Git operations for large file commits
- Cleanup of temporary/source files

## File Structure Awareness

- `scripts/` - All automation scripts (create new scripts here)
- `scripts/create_yearly_archives.py` - Core processing script
- `scripts/auto_commit.sh` - Git automation helper
- `scripts/sync_from_gdrive.sh` - Google Drive sync script
- `docs/` - All documentation files (create new docs here)
- `docs/robots/` - **Robot memory system** - AI agent context and institutional knowledge
- `docs/robots/decisions.md` - Architectural decisions and rationale
- `docs/robots/procedures.md` - Standard operating procedures (**includes TEST REQUIREMENT**)
- `docs/robots/troubleshooting.md` - Common issues and solutions
- `docs/CHANGELOG.md` - Version history
- `data/` - All data files (store all data here)
- `data/takeout/source/` - Temporary Google Takeout downloads
- `data/takeout/archives/` - Committed yearly archives (<100MB each)
- `data/gdrive_backup/` - Google Drive backup data
- `test/` - Test suite for validation
- `test/test_system_health.py` - System structure and health tests
- `test/test_integration.py` - Integration tests
- `README.md` - Status tracking (last year, total archives, etc.)

## File Organization Rules

- **All new scripts** must be created in `scripts/` directory
- **All new documentation** must be created in `docs/robots/` directory (for AI memory)
- **All data files** must be stored in `data/` directory
- **All tests** must be created in `test/` directory

## Robot Memory System

Always consult and update the robot memory system in `docs/robots/`:
- `decisions.md` - Record architectural decisions
- `procedures.md` - Follow standard operating procedures
- `troubleshooting.md` - Reference for common issues

## Test-Driven Completion

**CRITICAL RULE:** Before reporting any task as "done" or "fixed":

1. Run all tests: `python3 -m pytest test/ -v`
2. Verify all tests pass
3. If tests fail, fix issues and re-test
4. Only report completion when all tests pass

This ensures quality and prevents regressions. See `docs/robots/procedures.md` for details.

## Decision Making

- Always verify archive sizes before committing
- Remind user to update README.md after processing new year
- Suggest cleanup after successful GitHub push
- Batch git operations when dealing with many archives
- Reference the agent config (`.github/agents/back-my-bitch-up.md`) for detailed procedures
