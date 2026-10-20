# Feedback 6 — October 15, 2026

## Review scope

Retrospective mentor feedback written on October 19 for Thursday, October 15, covering the Day 10 combining/visualizing exercises available at that date.

## Submission record

**Status: Practice exercises submitted; the complete Day 10 assignment is not yet evidenced by this date.**

[PR #16](https://github.com/NeilS1234/ErsterRepo/pull/16) merged five exercise scripts on October 15. The final analysis, merged dataset, three chart files, and findings were added in [PR #17](https://github.com/NeilS1234/ErsterRepo/pull/17), dated October 16. That later progress belongs in Friday's feedback.

## What you did well

- You demonstrate `merge()` with an ID key and `join()` with matching indexes.
- You use `concat(..., ignore_index=True)` to combine monthly records.
- The bar-chart exercise supplies a title and labels for both axes.
- A separate exercise calculates a mean, minimum, and maximum.
- The work was submitted through a dedicated branch and pull request.

These are useful individual demonstrations of the Day 10 learning topics.

## What is still required

The PDF assignment asks for two related datasets combined into one analysis, one merged dataset, three meaningful charts, five findings supported by the data, and a short explanation of limitations. The five practice scripts do not yet provide that complete deliverable:

- The examples use separate small in-memory datasets rather than one integrated analysis.
- The chart exercise displays one bar chart with `plt.show()`; it does not save three chart outputs.
- The three printed statistics are not five interpreted findings.
- A consolidated findings/limitations report and reproducible execution instructions are not present in the dated submission.

This is an incomplete assignment at Thursday's cutoff, not a claim that the final assignment is missing from the repository today.

## What to improve

- Choose a question that can be answered by joining two related datasets, and explain the join key and join type.
- Check key uniqueness and row counts before and after merging, and identify unmatched rows.
- Select three charts that answer different questions. Save them with clear labels, units, and relevant dates.
- Support each finding with a number or a specific observation and state important limitations.
- Add the dependencies, exact run command, resources used, learning summary, and questions or blockers. The main README's Day 10 section was committed on October 16, so it is not credited to Thursday.
- Rename `Writing_Data_Driven_Conclusions .py` to remove the space before the extension and use consistent descriptive filenames.

## Required next actions

1. Combine the exercises into a complete, reproducible analysis.
2. Submit the merged dataset, three saved charts, five findings, and limitations together.
3. Explain the merge checks and add daily learning notes.
4. Keep the complete assignment in a focused PR and request review.

You have shown the building blocks. The next step is to connect them into one analysis whose conclusions can be traced back to the combined data.

## Evidence and validation

Reviewed [the October 15 main revision](https://github.com/NeilS1234/ErsterRepo/tree/dba58439ba644da20868d87bbd73df07d9099f91/day_10_Combining_and_Visualizing_Data), the five scripts, PR #16, and the subsequent PR #17 timestamps. This assessment is based on source and history inspection. The GUI chart exercise and live API analysis were not executed, and no passing automated quality checks are claimed.
