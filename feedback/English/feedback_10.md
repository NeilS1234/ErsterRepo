# Feedback 10 — October 22, 2026

## Review scope

Follow-up to feedback 8 and 9, comparing the previous feedback publication [99c51e8](https://github.com/NeilS1234/ErsterRepo/commit/99c51e823cc765ab90a9ac3d3fbb704333e38b52) with main at [e518e21](https://github.com/NeilS1234/ErsterRepo/commit/e518e21194cda664a94d4c40ce9d098b4dfeb964). Reviewed all 12 current branches, open and closed issues, milestones, pull requests, and the repository tree on October 22.

**Status:** New documentation submitted; the practical Day 14 assignment is not yet demonstrated by the accessible evidence. This is an evidence assessment, not a claim that no work occurred elsewhere. Learning-plan days are not fixed calendar dates.

## Submission record

- Commit e518e21, dated October 21 at 13:29:48 Europe/Berlin, adds the Day 14 section to the main README.
- It includes learning topics, an assignment description, and four YouTube links.
- This is the only new commit on main since the previous feedback publication. Only README.md changed; all other branch heads remain at their previous revisions.
- No new pull request appears after PR #28 on October 20.
- The issues endpoint returns 28 pull requests and **zero ordinary issues**, including closed issues.
- The repository has **zero milestones**, including closed milestones.
- Project-board verification is unavailable: the current GitHub credential lacks the required `read:project` scope. No board link is included in the new README section, so board existence and contents remain unverified.

## What you did well

- You continued documenting the next learning topic and recorded four resources.
- Your description identifies the intended workflow: milestone, at least five issues, labels, board status, and a PR linked to a completed issue.
- The commit message identifies Day 14 and the README update.

## What is still required

The learning plan requires a milestone, at least five issues, appropriate labels, a project board, and one completed issue linked to a pull request. Describing that workflow does not demonstrate its execution.

| Requirement | Verified assessment |
|---|---|
| One milestone | None currently returned by GitHub |
| At least five issues | No ordinary open or closed issues currently returned |
| Appropriate labels | Application to assignment issues is not demonstrated because no such issues are present |
| Project board | Not verified due to access limitations; supply a viewable link |
| Completed issue linked to a PR | Not demonstrated; no ordinary issues or new PRs |
| Documentation of actual actions and results | README describes intended actions, without issue numbers, milestone/board links, commands, or observed outcomes |

Do not treat the existing PR numbers as the five required task issues: GitHub exposes PRs through the issues API, but they are different deliverables for this exercise.

## Required next improvements

1. Create one milestone with a clear goal and completion criteria.
2. Create at least five concrete issues, each with a description and acceptance criteria. Suitable topics include the Day 12 import/mypy problem, style corrections, Day 13 conflict documentation, setup instructions, and this project-management exercise.
3. Apply useful labels and assign the issues to the milestone.
4. Add them to a project board with clear statuses such as Todo, In progress, and Done. Include a board link that your mentor can view.
5. Complete one real issue through a dedicated branch and PR. Link it with a closing reference such as `Closes #<issue-number>`, then verify the issue state after merging.
6. Document the actual issue numbers, labels, milestone and board links, commands or UI steps, PR link, and observed result. Add your learning summary and open questions, or state that none remain.
7. Configure your real Git author name and email for future commits; the new commit still uses “Dein Name” and a placeholder email. Preserve shared history.

## Earlier feedback and validation

No new Python changes or evidence resolving feedback 8 and 9 were submitted in this comparison. Those findings remain open; the previous test results are historical and were not rerun for this documentation-only review.

This review checked remote commit history, branch heads, the file comparison, issues, milestones, PRs, and feedback numbering. Python checks were not rerun because neither the student update nor this feedback changes Python implementations. Project-board access remains the explicit verification limit.

Your next step is to turn the documented plan into inspectable GitHub work items and one completed, linked change.
