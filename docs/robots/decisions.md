# Architectural Decisions

This document records important decisions made in the project.

## 2026-01-11: Robot Memory System

**Decision:** Create `docs/robots/` folder for AI agent memory and documentation.

**Rationale:**
- Provides persistent context across AI sessions
- Centralizes project-specific knowledge
- Makes it easier to maintain consistent behavior
- Documents decisions and their reasoning for future reference

**Implementation:**
- All new documentation goes in `docs/robots/`
- Agent and prompt configurations reference this folder
- Tests validate system functionality before reporting completion

## 2024-12: Folder Structure Reorganization

**Decision:** Organize repository into `scripts/`, `docs/`, and `data/` top-level folders.

**Rationale:**
- Clear separation of concerns
- Easier to navigate and maintain
- Follows common conventions
- Prevents clutter in root directory

**Implementation:**
- `scripts/` - All automation and processing scripts
- `docs/` - All documentation files
- `data/` - All data files (takeout, gdrive backups)
