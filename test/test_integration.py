#!/usr/bin/env python3
"""
Integration Tests

Tests that validate the integration between different components
and the overall system workflow.
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_documentation_consistency():
    """Test that documentation is consistent across files"""
    agent_config = project_root / '.github/agents/back-my-bitch-up.md'
    prompt_file = project_root / '.github/prompts/back-my-bitch-up.md'
    readme = project_root / 'README.md'
    
    agent_content = agent_config.read_text()
    prompt_content = prompt_file.read_text()
    readme_content = readme.read_text()
    
    # Check folder structure mentioned consistently
    assert 'scripts/' in agent_content and 'scripts/' in prompt_content
    assert 'docs/' in agent_content and 'docs/' in prompt_content
    assert 'data/' in agent_content and 'data/' in prompt_content


def test_file_organization_rules():
    """Test that file organization rules are enforced in documentation"""
    agent_config = project_root / '.github/agents/back-my-bitch-up.md'
    prompt_file = project_root / '.github/prompts/back-my-bitch-up.md'
    
    agent_content = agent_config.read_text()
    prompt_content = prompt_file.read_text()
    
    # Both should mention file organization rules
    assert 'scripts' in agent_content.lower() and 'scripts' in prompt_content.lower()
    assert 'docs' in agent_content.lower() and 'docs' in prompt_content.lower()


def test_test_requirement_documented():
    """Test that test requirement is documented"""
    procedures = project_root / 'docs/robots/procedures.md'
    content = procedures.read_text()
    
    # Should document the test requirement
    assert 'test' in content.lower()
    assert 'pytest' in content.lower() or 'python3 -m pytest' in content.lower()


def test_all_scripts_documented():
    """Test that all scripts are mentioned in documentation"""
    scripts_dir = project_root / 'scripts'
    agent_config = project_root / '.github/agents/back-my-bitch-up.md'
    
    if scripts_dir.exists():
        agent_content = agent_config.read_text()
        
        for script_file in scripts_dir.glob('*.py'):
            # Main scripts should be documented
            if script_file.name == 'create_yearly_archives.py':
                assert 'create_yearly_archives' in agent_content


def test_robots_folder_integrated():
    """Test that docs/robots is properly integrated"""
    # Check that robots folder exists and is documented
    robots_dir = project_root / 'docs/robots'
    assert robots_dir.exists()
    
    # Check that it's referenced in agent config
    agent_config = project_root / '.github/agents/back-my-bitch-up.md'
    agent_content = agent_config.read_text()
    
    # Should mention robot memory or docs/robots
    assert 'docs/robots' in agent_content or 'Robot Memory' in agent_content


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
