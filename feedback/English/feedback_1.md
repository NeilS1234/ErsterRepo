# Feedback 1 — Day 1 and Day 2

## Overall assessment

You have made a good start. The main Python programs for Day 1 and Day 2 both run successfully, and the Day 2 solution demonstrates that you understand lists, tuples, dictionaries, loops, and `len()`.

**Status:** The core assignment requirements are completed, with some improvements needed in documentation, code style, and the GitHub workflow.

## Day 1 task

The task was to create the `python-apprenticeship` repository, add a README, write a Python program that prints a welcome message and basic personal information, and push the work to GitHub.

### What you did well

- You created a GitHub repository and added a README.
- `first_project.py` runs without errors.
- The program prints a welcome message and the requested personal information.
- Your commit history shows that you experimented, corrected files, and practised Git commands.

### What to improve

- The README still contains template placeholders such as “An in-depth paragraph about your project.” Replace these with a real project description.
- Complete the README sections for running the program and getting help. Include an example command such as `python first_project.py`.
- Correct spelling mistakes such as `ptoject`, `requiered`, and `git` when you mean Git.
- Add the YouTube resources you used, a short summary of what you learned, and any remaining questions. These are part of the daily submission requirements.
- Use f-strings when displaying values, for example: `print(f"Name: {name}")`.

## Day 2 task

The task was to store information about five employees or products, use at least three data structures, display all records, show the total number of records, select information from every record, and print a formatted summary.

### What you did well

- `second_project.py` runs without errors.
- You created exactly five employee records.
- You used three requested data structures: a tuple, dictionaries, and a list.
- You displayed all records and calculated the correct total with `len()`.
- You used a loop to display each employee's name and job.
- You added comments that make the learning intention easy to follow.

### What to improve

- Create the employee list directly instead of first creating five numbered variables. This is shorter and easier to extend.
- Connect each employee to a department. At the moment, the department tuple is printed but is not related to any employee record.
- Use f-strings for the employee and summary output, for example: `print(f"{employee['name']} — {employee['job']}")`.
- Display all records with a loop instead of printing the raw list. This will make the output more readable.
- In `training_field.py`, `bool("False")` evaluates to `True` because every non-empty string is truthy. Make sure you can explain the difference between the string `"False"` and the Boolean value `False`.
- Add the videos used, learning summary, and open questions for Day 2.

## Code-quality results

- All three Python files execute successfully.
- mypy reports no issues.
- Ruff reports no issues with its current default rules.
- Flake8 reports style problems, including one line longer than 79 characters, trailing whitespace, excessive blank lines, and a blank line at the end of a file.

These style findings do not stop the programs from working, but cleaning them up will make the code more professional and easier to review.

## Git and GitHub feedback

- You have created 19 commits, which shows regular Git practice.
- Some commit messages, such as `commit` and `second_project.py`, do not explain what changed. Prefer messages such as `feat: add employee summary assignment` or `docs: complete project instructions`.
- The repository currently has only the `main` branch and no pull requests. For the next assignment, create a separate branch, push it, open a pull request, and merge it after review.
- Avoid committing incomplete experiments to `main`. A learning or feature branch gives you a safe place to practise.

## Required next improvements

1. Replace all README placeholders with real project information and execution instructions.
2. Add the learning resources, learning summary, and questions for Days 1 and 2.
3. Refactor `second_project.py` into one list of employee dictionaries, including a department for each employee.
4. Use f-strings and improve the formatting of the output.
5. Fix all Flake8 findings.
6. Submit the next assignment through a branch and pull request.

You have completed the important functional part of both assignments. Your next step is to make the repository as clear and professional as the working code.
