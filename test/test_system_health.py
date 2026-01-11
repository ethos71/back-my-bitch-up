#!/usr/bin/env python3
"""
System Health Tests

These tests validate the basic structure and functionality of the 
back-my-bitch-up project to ensure the system is working correctly.
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_folder_structure():
    """Test that required folders exist"""
    required_folders = [
        'scripts',
        'docs',
        'docs/robots',
        'data',
        'test',
        '.github/agents',
        '.github/prompts'
    ]
    
    for folder in required_folders:
        folder_path = project_root / folder
        assert folder_path.exists(), f"Required folder missing: {folder}"
        assert folder_path.is_dir(), f"Path is not a directory: {folder}"


def test_required_files():
    """Test that required files exist"""
    required_files = [
        'README.md',
        'scripts/create_yearly_archives.py',
        'docs/robots/README.md',
        'docs/robots/decisions.md',
        'docs/robots/procedures.md',
        'docs/robots/troubleshooting.md',
        '.github/agents/back-my-bitch-up.md',
        '.github/prompts/back-my-bitch-up.md'
    ]
    
    for file in required_files:
        file_path = project_root / file
        assert file_path.exists(), f"Required file missing: {file}"
        assert file_path.is_file(), f"Path is not a file: {file}"


def test_scripts_executable_content():
    """Test that scripts have proper shebang lines"""
    script_files = [
        'scripts/auto_commit.sh',
        'scripts/sync_from_gdrive.sh'
    ]
    
    for script in script_files:
        script_path = project_root / script
        if script_path.exists():
            with open(script_path, 'r') as f:
                first_line = f.readline().strip()
                assert first_line.startswith('#!'), f"Script missing shebang: {script}"


def test_python_scripts_syntax():
    """Test that Python scripts have valid syntax"""
    import py_compile
    
    python_scripts = [
        'scripts/create_yearly_archives.py'
    ]
    
    for script in python_scripts:
        script_path = project_root / script
        if script_path.exists():
            try:
                py_compile.compile(str(script_path), doraise=True)
            except py_compile.PyCompileError as e:
                assert False, f"Syntax error in {script}: {e}"


def test_docs_robots_content():
    """Test that docs/robots files have content"""
    docs_files = [
        'docs/robots/README.md',
        'docs/robots/decisions.md',
        'docs/robots/procedures.md',
        'docs/robots/troubleshooting.md'
    ]
    
    for doc in docs_files:
        doc_path = project_root / doc
        assert doc_path.exists(), f"Documentation missing: {doc}"
        
        content = doc_path.read_text()
        assert len(content) > 100, f"Documentation too short: {doc}"
        assert content.startswith('#'), f"Documentation should start with heading: {doc}"


def test_agent_config_references_robots():
    """Test that agent config references docs/robots"""
    agent_config = project_root / '.github/agents/back-my-bitch-up.md'
    content = agent_config.read_text()
    
    assert 'docs/robots' in content or 'robot' in content.lower(), \
        "Agent config should reference docs/robots for memory system"


def test_prompt_references_test_requirement():
    """Test that system prompt includes test requirement"""
    prompt_file = project_root / '.github/prompts/back-my-bitch-up.md'
    content = prompt_file.read_text()
    
    # Should mention tests or testing
    assert 'test' in content.lower(), \
        "System prompt should reference testing requirements"


def test_data_folder_structure():
    """Test that data folder has proper structure"""
    data_path = project_root / 'data'
    assert data_path.exists(), "data/ folder must exist"
    
    # These may not exist yet but structure should be documented
    expected_structure = ['takeout', 'gdrive_backup']
    
    # Just verify data folder exists for now
    # Subfolders are created as needed during actual backup operations


def test_readme_has_status():
    """Test that README contains status information"""
    readme = project_root / 'README.md'
    content = readme.read_text()
    
    # Should have status tracking
    status_indicators = [
        'Last Full Year Archived',
        'Total Archives',
        'Total Size'
    ]
    
    for indicator in status_indicators:
        assert indicator in content, f"README missing status indicator: {indicator}"


if __name__ == '__main__':
    # Allow running directly for quick checks
    import pytest
    pytest.main([__file__, '-v'])
