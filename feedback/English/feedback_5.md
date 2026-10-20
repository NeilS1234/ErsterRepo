# Feedback 5 — October 14, 2026

## Review scope

Retrospective mentor feedback written on October 19 for Wednesday, October 14, covering the Day 9 filtering/grouping exercises and sales-report assignment recorded that day.

## Submission record

**Status: The Day 9 report's core calculation requirements are implemented; portability and daily documentation remain incomplete.**

PRs [#11](https://github.com/NeilS1234/ErsterRepo/pull/11), [#12](https://github.com/NeilS1234/ErsterRepo/pull/12), [#13](https://github.com/NeilS1234/ErsterRepo/pull/13), and [#14](https://github.com/NeilS1234/ErsterRepo/pull/14) merged the exercises and final report into main. [PR #15](https://github.com/NeilS1234/ErsterRepo/pull/15) synchronized main back into the learning branch; it is not an additional assignment.

## What you did well

- The main report groups revenue by both `Region` and `Kategorie`.
- It calculates grouped totals and averages and identifies the best and worst groups.
- It creates `Preis_pro_Stueck` and a revenue pivot table.
- Recalculation from the submitted 12-row sales CSV gives total revenue of **€8,700**, total quantity **40**, and average revenue per row **€725**.
- The strongest group is **West / Technik (€2,200)**; the weakest is **Nord / Moebel (€400)**.
- The practice script separately demonstrates Boolean filtering, ascending/descending sorting, aggregations, and calculated columns.
- The README now includes Day 8 and Day 9 topics and learning-resource links.

These calculations address the central Day 9 end-of-day requirements in the PDF plan.

## What to improve

- Replace the absolute Windows CSV paths in both scripts with paths relative to the script or a documented input argument. As committed, another reviewer cannot run them unchanged on another machine.
- The practice `pivot_table()` result is discarded, followed by `print(df)`. Assign and print the pivot result so the exercise actually displays it.
- The main sales report does not itself filter or sort the data, although the README describes those steps. The practice demonstrates both. Integrate a meaningful filter and ranking into the report if that README description is intended to describe the submitted application.
- Label the €725 value as average revenue per input row, rather than implying it is average unit price. If you want a group unit price, use group revenue divided by group quantity.
- Explain why West / Technik performs best and what the pivot reveals. Printed tables are useful, but a short interpretation makes the report more informative.
- Validate required columns and handle empty input, missing revenue, and zero quantities before division or `idxmax()`/`idxmin()`.
- The README lists topics, assignments, and resources, but does not clearly record your own daily learning summary or unresolved questions. Add those in your own words.

## Git and GitHub feedback

Using branches and PRs is consistent progress. Four forward PRs for one small assignment make the review fragmented; use one focused PR unless changes need separate review. Replace messages such as `csv_datei_vergessen` with a clear description of the change. No submitted review is present on PR #14, so its merge is evidence of integration, not independent approval.

## Required next actions

1. Make both CSV paths portable and show the practice pivot output.
2. Add a short interpretation and appropriate input validation to the report.
3. Document the execution command, dependency installation, learning summary, and questions.
4. Keep future assignments in one coherent PR and obtain review before merging.

You have implemented the main pandas reporting operations correctly for the supplied data. Focus next on making the result easy for someone else to run, interpret, and review.

## Evidence and validation

Reviewed the [dated main revision](https://github.com/NeilS1234/ErsterRepo/tree/b6c95d2ba532d500192e0bcdd04d80b66eb22c9c), [sales report](https://github.com/NeilS1234/ErsterRepo/blob/b6c95d2ba532d500192e0bcdd04d80b66eb22c9c/day_9_main_task/Sales_Report.py), its input CSV, practice script, README changes, and PRs #11–15. The numerical results above were independently recalculated from the committed CSV. The original scripts were not executed unchanged because of their local Windows paths. Ruff, mypy, Flake8, and a full test suite were not run for this documentation review.
