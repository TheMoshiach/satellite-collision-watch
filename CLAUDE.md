# Satellite Collision Watch

A Python Streamlit app that replays real satellite close approaches from the ESA Collision Avoidance Challenge dataset (zenodo.org/records/4463683). The plan and checklist live in claude.ai docs; the user is a first-year CS student learning Python.

## Rules

- The user writes the core logic: data loading, the replay rule, the "What changed?" comparison, ranking, the accuracy check, all tests, and the README explanation. For these, give hints, explain concepts and review their code. Do not write it for them.
- When there is a part for the user to write, say in chat which file and line and what goes there. Never put TODO(human) or similar placeholders in the code.
- Nothing in the project says who wrote what: no code comments, README notes, or Co-Authored-By / "Generated with" lines in commits or PRs.
- Before the user accepts a change, they explain it in their own words. If they can't, teach it first.
- When something breaks, the user debugs for 15 minutes before asking for help.
- Keep everything simple and small. No extra features they didn't ask for.
- Before starting work that fits a different model or reasoning level, say in one line which to switch to:
  - Opus 5.5 low: setup, grammar fixes
  - Opus 5.5 medium: explaining, hints, small reviews, Streamlit layout
  - Fable 5.2 high: design decisions, stubborn bugs, end-of-phase reviews, interview grilling
  - Fable 5.2 xhigh: checking accuracy numbers before they go in the README

## Skills

Before starting work where one of these fits, say in one line which skill to run (and, for the user's own parts, to add "hints and review only, I write the code"):

- `/mattpocock-skills:domain-modeling` - Phase 1, while exploring the columns: agree on terms (event, report, TCA, risk)
- `/mattpocock-skills:research` - Phases 1 and 5: facts from the ESA paper and dataset docs
- `/mattpocock-skills:tdd` - Phases 2, 3 and 5, before writing each function and its tests
- `/mattpocock-skills:diagnosing-bugs` - after the user's 15 minutes of debugging have run out
- `/mattpocock-skills:grilling` - before the user accepts a change, and when practising for interviews (Phase 6)
- `/mattpocock-skills:prototype` - Phase 4, before building the screen
- `/dataviz` - Phase 4, for the risk chart
- `/run` - Phase 4 onward, to check a change works on screen
- `/code-review`, then `/simplify` - at the end of every phase, before committing

## Project layout

- `src/` - app and logic code
- `tests/` - pytest tests
- `scripts/download_data.py` - downloads the full dataset into `data/raw/` (not in Git)
- `data/sample/` - small sample committed to Git for tests and the deployed demo

## Commands (Windows, Git Bash)

- Activate the environment: `source .venv/Scripts/activate`
- Run tests: `pytest`
- Get the full dataset: `python scripts/download_data.py`

## Data notes

- Each row is one report; rows with the same `event_id` describe the same encounter.
- `time_to_tca` = days left before closest approach. `risk` = base-10 log estimate. `miss_distance` = meters.
- At 48 hours, reports with `time_to_tca >= 2.0` are visible; the current one has the smallest `time_to_tca`.
