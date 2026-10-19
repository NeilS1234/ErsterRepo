# Feedback 7 — October 16, 2026

## Review scope

Retrospective mentor feedback written on October 19 for Friday, October 16. This entry covers the completed Day 10 submission and the initial Day 11 maintainability project. The PDF learning days are not fixed calendar dates.

## Submission record

| Work | Dated evidence | Assessment |
|---|---|---|
| Day 10 analysis and outputs | PRs [#17](https://github.com/NeilS1234/ErsterRepo/pull/17) and [#18](https://github.com/NeilS1234/ErsterRepo/pull/18), merged October 16 | Required artifacts present; numerical findings reproduced; methodology and reproducibility need improvement |
| Day 11 project | [PR #19](https://github.com/NeilS1234/ErsterRepo/pull/19), merged October 16 | Useful structure demonstration; required refactoring of an earlier assignment is not demonstrated |
| Day 11 project README | [58a15ab](https://github.com/NeilS1234/ErsterRepo/commit/58a15abde61323160560d204c3464cff9b7a8074), dated October 16 on the learning branch; PR #20 merged October 19 | Documentation work exists, but was not integrated into main by Friday |

The Day 12 submission and PRs #20–23 recorded on October 19 are outside last week's implementation assessment. The date of PR #20 is used only to clarify the README integration.

## Day 10 — What you did well

- You combine World Bank GDP-per-person and life-expectancy data using country code and year.
- The script saves a merged dataset, a scatter plot, a time-series chart, a horizontal bar chart, and a findings report. The renamed outputs are committed under `output_Day_10/`.
- A dependency file lists pandas, Matplotlib, and requests.
- The saved dataset contains **6,098 rows**, and its country-code/year keys have no duplicates.
- All five reported numerical findings match recalculation from that saved dataset, after the same rounding: **0.62** correlation in 2023; **65.0** and **81.3** years for the low/high GDP quartiles; median life expectancy **69.1** in 2000 and **73.8** in 2023; Monaco at approximately **$256,800** GDP per person in 2023.
- The report acknowledges missing data, limitations of GDP, and the difference between correlation and causation.

## Day 10 — What to improve

- The three-character-code filter does not restrict the data to countries. The submitted CSV also contains aggregates such as **World, Arab World, and European Union**. Exclude aggregate entities using source metadata and regenerate the country comparisons. Until then, the calculations are reproducible but the descriptions as country-only comparisons are inaccurate.
- Explain that the quartiles are defined by GDP per person, the correlation uses raw GDP values even though the scatter axis is logarithmic, and the annual median is unweighted over the available entities. Missing observations can change the sample between years.
- The program still writes to `output/`, while the committed folder is `output_Day_10/`. Choose one documented location so a rerun does not create a competing set of results.
- Document the working directory, installation and run commands, indicator IDs, retrieval date, and a way to reproduce the analysis from saved inputs. A future live API response may change.
- Add response-schema and pagination checks, unique-key validation before merging, unmatched-row counts, and useful handling of connection failures or empty data.
- Put execution behind a `main()` entry point so importing the module does not trigger network requests and file writes.

## Day 11 — What you did well

- `my_project_day_11/src/main.py` has a source directory, typed `add()` and `main()` functions, an Args/Returns docstring, and a guarded entry point.
- Calculation and printing are separated. Executing this exact file in an isolated copy prints **5**.
- The branch README describes the addition example and lists what you learned.

## Day 11 — What is still required

The plan asks you to refactor **an earlier assignment**, preserving its behavior in a structured project. A new two-number addition example demonstrates structure but does not establish that requirement. Refactor the transaction, CSV-cleaning, or pandas assignment into small typed functions, document them, and retain the original behavior.

The Friday main revision has an empty project README; the documented branch version was merged on October 19. Credit is due for writing that README, but it needs the project structure and a clear working-directory instruction: run `python src/main.py` from inside `my_project_day_11/`, or provide the full repository-relative command.

## Git, documentation, and follow-up

- Dedicated branches and PRs are now routine. No submitted reviews are present on PRs #17 and #19; a merge alone does not demonstrate independent review.
- Use one coherent assignment PR with meaningful commit messages and the previously requested company branch convention, for example `feature/day11Refactor`.
- Python cache files are still tracked, and no root `.gitignore` is present in the reviewed main tree. This request from Feedback 2 remains open.
- Resource links and copied task descriptions do not replace your own learning summary and questions. The Day 11 branch README is a start; add what was difficult, how you solved it, and what remains unclear.

## Required next actions

1. Repair and submit the unmerged Day 8 application described in Feedback 4.
2. Correct the Day 10 population definition and output-path mismatch, then regenerate and explain the results.
3. Refactor an earlier assignment for Day 11 and complete its execution documentation.
4. Remove tracked caches, add ignore rules, and record successful quality checks for the revised project.
5. Add daily learning notes and obtain review before merging.

You have progressed from isolated pandas exercises to an analysis with data, charts, and a written report. The next priority is to make the methodological choices accurate and to apply maintainable structure to a real earlier assignment.

## Evidence and validation

Reviewed [Friday's main revision](https://github.com/NeilS1234/ErsterRepo/tree/5e323eaf3a53f3a1585d7f6c3c2fdcd04636ddca), the Day 10 script, requirements, saved CSV and findings, Day 11 source, the dated branch README, and relevant PR metadata. Recalculated all five findings from the committed CSV and executed the small Day 11 program. Chart files were verified as present; their visual rendering and a fresh World Bank download were not validated. Ruff, mypy, Flake8, and a full test suite were not run; earlier feedback's check counts are not presented as current results.
