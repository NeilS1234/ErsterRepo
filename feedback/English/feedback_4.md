# Feedback 4 — October 13, 2026

## Review scope

Retrospective mentor feedback written on October 19 for Tuesday, October 13. The learning plan has no calendar dates; the work recorded on this date concerns Day 8 — Data Cleaning.

## Submission record

**Status: Substantial implementation submitted on a branch; not reproducible from its final committed input and not integrated into main.**

The `data-cleaning` branch contains three commits dated October 13: [44ae294](https://github.com/NeilS1234/ErsterRepo/commit/44ae294efc807789667a08b0fcdc466fee5d80d7), [0490e50](https://github.com/NeilS1234/ErsterRepo/commit/0490e5078142488832923f59870a1b2daccc3da8), and [5b8e244](https://github.com/NeilS1234/ErsterRepo/commit/5b8e2446a766096d3f1755dbd36df4606792e8ad). The assignment is in `Aufgabe_Tag_8/`. The earlier PR #10 merged the practice exercise on October 8; it does not include these later assignment commits. No subsequent PR for these commits is present in the reviewed PR list.

## What you did well

- You added the cleaning script, original input, cleaned output, and a separate cleaning report.
- Input and output locations use `Path(__file__).parent`, making this application more portable than the practice script.
- The code removes an exact duplicate, standardizes text, converts numbers and dates, flags a negative salary as missing, and renames columns.
- The report records corrections, reasons, and counts. The committed result contains 10 rows after removing one duplicate from the original 11 records.
- Invalid dates are converted to missing values instead of guessing a replacement date.

## What to improve

1. **Repair the committed input first.** The final commit adds the PowerShell wrapper `@'` and a trailing `Set-Content` command inside `messy_dataset.csv`. These are shell instructions, not CSV content. A local run using the exact committed files fails with `KeyError: 'alter'`. Commit only the CSV header and records, then regenerate both outputs. The existing outputs do not prove that the final input works.
2. The age 150 remains in the cleaned output. Define a justified validity range and document whether out-of-range values are flagged, removed, or left missing.
3. Replacing an unknown age with 21 invents a value. Explain why this rule is acceptable for the exercise, or preserve the missing value with a suitable nullable type. Do not treat an arbitrary default as a verified fact.
4. The originally missing salary for David is still missing but has no separate report entry. Distinguish original missing values from values made missing by validation, and document their treatment.
5. The column-renaming entry reports two under “Affected Records,” although it counts columns. Label the unit correctly. Add post-cleaning checks for row counts, duplicate counts, types, and remaining invalid or missing values.
6. Avoid silently creating replacement source data when an input is missing. Keep sample-data creation separate from processing so an incorrect input path is visible.
7. Add assignment-specific setup/run instructions, a learning summary, resources used, and questions or blockers. The Day 8 topic/resources section on main was added on October 14, so it is not evidence of Tuesday's documentation.

## Git and GitHub feedback

The dedicated branch is useful, but the full assignment still needs its own PR. A previous merged PR does not automatically include later branch commits. Explain the input repair in a meaningful commit message, and request review before merging.

## Required next actions

1. Remove the PowerShell wrapper from the CSV and rerun the committed application.
2. Resolve and document the remaining age and missing-salary issues; regenerate the output and report together.
3. Add post-cleaning verification and the daily learning notes.
4. Open a PR containing the complete Day 8 assignment.

This is a clear improvement over the practice exercise: you now have an application and an audit report. The remaining priority is to ensure that the committed inputs actually reproduce the submitted results.

## Evidence and validation

Reviewed [the final dated branch revision](https://github.com/NeilS1234/ErsterRepo/tree/5b8e2446a766096d3f1755dbd36df4606792e8ad/Aufgabe_Tag_8), its script, both CSV datasets, report, commit diffs, and PR history. The exact Day 8 script/input was executed in an isolated copy and failed as described. The checked-in output and report were inspected separately. No passing Ruff, mypy, Flake8, or full test-suite result is claimed.
