# Feedback 3 — October 12, 2026

## Review scope

Retrospective mentor feedback written on October 19, 2026, for Monday, October 12. This is the first missing daily entry for October 12–16; Feedback 2 ends on October 6. The PDF learning plan numbers learning days but does not assign calendar dates. This review follows dated repository evidence rather than assuming that every calendar day corresponds to the next learning day.

## Submission record

**Status: No new submission evidence found for this date.**

No commit dated October 12 was found in the histories of the 11 branches available at review time, and no pull request was opened or merged on that date. The latest main-branch work before the cutoff is [PR #10, merged October 8](https://github.com/NeilS1234/ErsterRepo/pull/10), containing the Day 8 practice exercise.

This is a gap in the recorded evidence. It does not establish that you did no work, were absent, or missed an agreed deadline. Local work, deleted branches, and availability arrangements cannot be established from the current repository.

## What you did well

- The existing Day 8 practice demonstrates missing-value handling, duplicate removal, type conversion, string cleanup, date conversion, and column renaming.
- You had already used a dedicated branch and PR #10 for that practice.

## What still needs evidence

- The practice script only prints the result. It does not save a new cleaned CSV or document each issue, its correction, the reason, and the affected-record count, as required by the Day 8 assignment.
- In the practice input, Anna and David each occur with differences in spaces or capitalization. Because duplicates are removed before names are normalized, these equivalent records remain after cleanup. Normalize the relevant text before checking duplicates, and document which fields define a duplicate.
- The rename mapping uses `vorname` and `alter`, while this practice CSV already contains `Name` and `Alter`; that mapping has no effect.
- The absolute Windows input path prevents another person from running the script unchanged.
- A daily learning summary and questions or blockers for October 12 are not identifiable.

## Required next actions

1. Record what you worked on that day, or note an agreed non-working day if applicable. Do not invent a completed assignment to fill the history.
2. Submit the full Day 8 cleaning application with a separate output CSV and an issue-by-issue report.
3. Add portable execution instructions and a brief learning summary, including unresolved questions or an explicit statement that there are none.
4. Use one focused branch and pull request for the complete assignment.

You have demonstrated the individual cleaning operations. The next step is to make the whole cleaning process reproducible and explain the decisions behind it.

## Evidence and validation

Reviewed the [pre-cutoff main revision](https://github.com/NeilS1234/ErsterRepo/tree/be85a1b79251d3df119eea7f0b20e877ad01beaf), including [the practice script](https://github.com/NeilS1234/ErsterRepo/blob/be85a1b79251d3df119eea7f0b20e877ad01beaf/data_cleaning_ordner/data_cleaning_testground.py) and its CSV, plus the dated histories of all currently listed branches and PRs. Code observations here are from source inspection; no successful execution or quality-check result is claimed. Work first recorded after October 12 is not credited to this date.
