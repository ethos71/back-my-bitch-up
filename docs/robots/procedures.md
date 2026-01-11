# Standard Operating Procedures

## Test-Driven Completion Protocol

**CRITICAL:** Before reporting any task as "done" or "fixed", the agent MUST:

1. Run all existing tests in the `test/` directory
2. Verify all tests pass
3. If tests fail, fix the issues and re-test
4. Only report completion after all tests pass

### Running Tests

```bash
# Run all tests
cd /home/dominick/workspace/back-my-bitch-up
python3 -m pytest test/ -v

# Or run individual test files
python3 -m pytest test/test_system_health.py -v
```

### Test Requirements

- Tests must be in the `test/` directory
- Test files must be named `test_*.py`
- Tests should validate core functionality
- Tests should be fast and reliable

## Documentation Updates

When creating new features or making changes:

1. Create or update documentation in `docs/robots/`
2. Update agent config if behavior changes
3. Update system prompt if new conventions are established
4. Add tests to validate the changes
5. Run tests before reporting completion

## Code Review Checklist

Before committing changes:

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] File organization follows conventions (scripts/, docs/, data/)
- [ ] No secrets or credentials in code
- [ ] README.md updated if user-facing changes
