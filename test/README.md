# Test Suite

This directory contains tests that validate the back-my-bitch-up system functionality.

## Running Tests

### All Tests
```bash
cd /home/dominick/workspace/back-my-bitch-up
python3 -m pytest test/ -v
```

### Specific Test File
```bash
python3 -m pytest test/test_system_health.py -v
```

### With Coverage
```bash
python3 -m pytest test/ --cov=. --cov-report=term
```

## Test Files

- `test_system_health.py` - Validates folder structure, required files, and basic system health
- `test_integration.py` - Tests integration between components and documentation consistency

## Requirements

```bash
pip3 install pytest
```

## Test Requirements

**CRITICAL:** All tests must pass before reporting a task as complete or fixed.

The agent MUST:
1. Run all tests after making any changes
2. Fix any failing tests
3. Re-run tests to verify fixes
4. Only report completion when all tests pass

## Adding New Tests

When adding new features:
1. Create corresponding tests in this directory
2. Follow naming convention: `test_*.py`
3. Use descriptive test function names: `test_<what_is_being_tested>()`
4. Add docstrings explaining what the test validates
5. Update this README to document new test files

## Test Philosophy

- Tests should be fast and reliable
- Focus on critical functionality
- Validate structure and integration points
- Catch common mistakes early
- Document expected behavior through tests
