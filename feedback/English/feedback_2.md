# Feedback 2 — Days 3 to 6

## Review scope

This review covers the work committed after Feedback 1 through October 6, 2026. It evaluates the assignments for Days 3, 4, and 5, the current progress on Day 6, the improvements requested in Feedback 1, and the Git/GitHub workflow.

## Submission record

| Working date | Expected work | Repository activity | Status |
|---|---|---:|---|
| October 1, 2026 | Day 3 | 13 commits, including merges | Submitted |
| October 2, 2026 | Day 4 | 7 commits, including merges | Submitted |
| October 5, 2026 | Day 5 | 10 commits | Submitted |
| October 6, 2026 | Day 6 | 3 commits at the time of review | In progress |

There is no working day without a commit in this review period. October 3 and 4 were weekend days and are not counted as missing submissions.

## Follow-up from Feedback 1

### Improvements completed

- The README now contains a real project description and documents the learning days.
- You added YouTube learning resources for several days.
- `second_project.py` now uses one list of employee dictionaries.
- Departments are now connected to individual employee records.
- You added f-strings to the Day 2 solution.
- You created branches and successfully merged six pull requests.

### Improvements still open

- Display the employees with a loop instead of accessing positions `0` to `4` individually.
- Add clear execution instructions to the README.
- Add a short learning summary and open questions for every day, not only resource links.
- Remove the remaining template text from the Author and Acknowledgments sections.
- Resolve the outstanding mypy, Ruff, and Flake8 findings.

## Day 3 — Conditions and Loops

### What you did well

- `day3.py` runs successfully.
- The program classifies every transaction as large or small.
- It identifies transactions that meet the condition.
- It calculates the correct total of 245 euros.
- The solution demonstrates a `for` loop and conditional statements.
- You practised branches and pull requests for this assignment.

### What to improve

- The condition `transaction >= 50` is checked twice. Store the result or combine the related output to avoid duplicated logic.
- Use f-strings to make the output clearer and consistent with the previous learning topic.
- Use more descriptive commit messages. Messages such as `updat...` do not explain what changed.
- List the exact videos watched rather than saying that following videos from the series were also watched.

**Assessment:** Completed. The functional requirements are met.

## Day 4 — Functions and Modules

### What you did well

- `day4.py` runs successfully and produces the expected result.
- The Day 3 logic was separated into functions for validation, calculation, classification, and formatting.
- The function names describe their responsibilities clearly.
- The functions return values instead of placing all logic directly inside print statements.

### What to improve

- `calculate_total()` does not use the validation logic. An invalid item would be skipped during display but could still break the total calculation.
- Put the program execution inside a `main()` function and call it with `if __name__ == "__main__":`.
- Add type hints and short docstrings so each function's expected input and output are clear.
- Use an f-string in `format_output()` instead of string concatenation.
- The “modules” part of the learning topic is not demonstrated. As a next step, move reusable functions into a separate module and import them into the main program.

**Assessment:** Completed, with a few structural improvements recommended.

## Day 5 — Files and Error Handling

### What you did well

- `aufgabe_tag_5/aufgabe_5.py` reads data from a CSV file and writes a result file.
- It checks for missing values, invalid numbers, and unreasonable ages.
- It counts valid and invalid records and prints a useful summary.
- It handles a missing input file.
- The program works when executed and generates five valid records from the current input file.
- Additional practice files demonstrate CSV, JSON, exceptions, dataclasses, and imports.

### What to improve

- The committed `result.csv` contains only four records, while the current input contains five valid records. Regenerate output files whenever the input or processing logic changes.
- Split the CSV processing into functions for reading, validation, summarizing, and writing.
- Add a `main()` entry point instead of executing everything at module level.
- Handle missing CSV columns gracefully instead of assuming that `Name`, `Alter`, and `Stadt` are always present.
- The converted age is not written back to the record, so it remains a string in `valid_records`.
- Add a Python `.gitignore`. A compiled file, `data/__pycache__/person.cpython-313.pyc`, is currently tracked and should not be committed.
- Add a dependency file if external packages are required. At minimum, document that the Day 5 program uses only the Python standard library.
- `data/main.py` opens its output in append mode and writes the header every time, which can create duplicate headers and repeated records.

**Assessment:** Completed. The central assignment works, but the repository hygiene and output consistency need attention.

## Day 6 — NumPy Fundamentals

### Current progress

- NumPy is imported correctly.
- A Python list is converted to a NumPy array.
- The program demonstrates vectorized multiplication and compares it with a list comprehension.
- It demonstrates an explicit NumPy integer data type.

### Work still required

The Day 6 assignment is not yet complete at the time of review. It still needs to calculate:

- Sum
- Mean
- Median
- Minimum and maximum
- Standard deviation
- Percentage difference of each value from the mean

Use NumPy operations for these calculations and label every output clearly. Also add the Day 6 YouTube resources, learning summary, and open questions to the README.

**Assessment:** In progress as of October 6, 2026.

## Code-quality results

- `day3.py`, `day4.py`, the Day 5 assignment, and the current NumPy program execute successfully.
- mypy reports 4 errors in `data/person.py` and `training_field.py`.
- Ruff reports 2 issues: a redefined function and an import placed below executable code.
- Flake8 reports 60 style findings across the repository. Most concern whitespace, blank lines, indentation, line length, and missing final newlines.

The most important correctness-related findings are:

- `Person.from_dict()` may pass missing values or a string age into fields declared as `str` and `int`.
- `say_hello()` is defined twice in `training_field.py`.
- `data/main2.py` places an import after executable code.

## Git and GitHub feedback

- You responded well to the previous feedback by using branches and pull requests.
- Six pull requests have been merged, which demonstrates the complete GitHub collaboration workflow.
- Several pull requests were opened for the same small transaction program. Try to keep one assignment in one focused branch and pull request unless a separate fix is genuinely needed.
- Many commit messages remain too general, including variations of `update_readme`, `training_save`, and `numpy_test`.
- Prefer semantic, action-based messages such as `feat: complete day 5 CSV validation` or `docs: add day 6 learning resources`.
- Use the company branch format for future work, for example `feature/day6NumpyAnalysis` or `bugfix/day5ResultSync`.

## Required next actions

1. Complete all Day 6 calculations using NumPy.
2. Regenerate and commit the correct Day 5 `result.csv`.
3. Add `.gitignore` and stop tracking Python cache files.
4. Fix all mypy and Ruff errors, then work through the Flake8 findings.
5. Add exact learning resources, a learning summary, and open questions for each day.
6. Keep each future assignment in one focused branch and pull request with clear commit messages.

You are progressing well and have clearly applied several points from Feedback 1. The next improvement should be moving from code that works to code that is consistently structured, checked, and reproducible.
