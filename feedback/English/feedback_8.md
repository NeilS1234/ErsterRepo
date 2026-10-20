# Feedback 8 — October 19, 2026

## Review scope

Reviewed on October 20 against the four-week learning plan. This entry covers Day 12 and the Day 11 README integration. Day 12 was already present at the previous review and explicitly excluded from feedback 7; it is not new work pushed after that review.

## Submission record

- [PR #20](https://github.com/NeilS1234/ErsterRepo/pull/20) integrated the Day 11 project README on October 19.
- [PR #22](https://github.com/NeilS1234/ErsterRepo/pull/22) merged the Day 12 calculator and tests on October 19. PR #23 synchronized main back into the testing branch.
- Reviewed files: `day12-testing-debugging/src/calculator.py`, `tests/test_calculator.py`, and `pyproject.toml` within that project.

**Status:** Useful testing practice; the assignment is partially complete. The plan requires tests for the refactored earlier assignment and successful pytest, mypy, Ruff, and Flake8 results.

## What you did well

- You wrote seven automated tests covering addition, averages, negative numbers, zero, a single value, and an empty list.
- The empty-list test checks both the exception type and its message.
- The functions have type hints and Google-style docstrings.
- You added configuration for pytest, strict mypy, and Ruff, and listed Day 12 learning resources in the main README.
- The Day 11 README is now integrated into main; this resolves the earlier integration gap described in feedback 7.

## Reproduced quality checks

Checks ran on October 20 in an isolated copy of the exact three submitted text files, from the Day 12 project directory. The available runtime was Python 3.14, not the configured Python 3.11; these results do not establish Python 3.11 validation.

| Check | Result |
|---|---|
| `python -m pytest -q` | 7 passed |
| `pytest -q` | Collection fails: `ModuleNotFoundError: No module named 'src'` |
| `mypy src tests` | Fails: calculator found under both `calculator` and `src.calculator` |
| `ruff check src tests` | Fails: I001 import formatting in the test file |
| `ruff format --check src tests` | Both files need formatting |
| `flake8 src tests` | Fails: W291, E302, E265, and W391 |

Do not describe all quality checks as successful until they pass from a documented clean setup.

## What to improve

1. Connect the tests to the earlier assignment refactored for Day 11. A separate calculator demonstrates testing techniques but does not establish that the original assignment's behavior is preserved.
2. Use a consistent package/import setup so pytest and mypy resolve the same module. Document the working directory and exact commands.
3. Fix import formatting, trailing whitespace, blank lines, and comment spacing; rerun all four required tools and save the results.
4. Document Python and dependency versions, installation steps, your actual learning summary, and unresolved questions.
5. Remove tracked Python caches in a future cleanup and add suitable ignore rules. Cache files are not test-result evidence.
6. Use descriptive commit and PR titles and the previously requested branch convention, for example `feature/day12Tests`.

## Next submission

Provide the tested refactored assignment, reproducible setup instructions, and successful pytest, mypy, Ruff, and Flake8 output. Keep the working seven tests while correcting project integration and style.
