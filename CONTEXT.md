# Satellite Collision Watch

Replays real satellite close approaches from the ESA Collision Avoidance Challenge dataset, showing each warning as it would have arrived, so an operator can see how the picture changed and decide what to do.

## Events and reports

**Event**:
One close approach between a protected satellite and another object, described by all reports sharing an `event_id`.
_Avoid_: Encounter, conjunction, case

**Report**:
One warning message about an event, issued at one moment before closest approach; one row in the dataset.
_Avoid_: CDM, row, update, alert, warning report

**TCA**:
Time of closest approach: the moment the two objects in an event are nearest each other.

**Time to TCA**:
Days left between a report being issued and TCA. Slightly negative for reports issued just after closest approach.
_Avoid_: Countdown, lead time

**Final report**:
The last report issued for an event: the one with the smallest time to TCA.
_Avoid_: Last CDM, outcome, truth

## Risk

**Risk**:
A report's estimate of the chance of collision, as a base-10 logarithm (−4 means 1 in 10,000).
_Avoid_: Probability, danger, score

**Negligible risk**:
A risk at the dataset's floor of −30, meaning the chance is too small to estimate, not literally 1 in 10^30.
_Avoid_: Zero risk, no risk

## Replay

**Replay time**:
The point on the timeline the demo is showing, measured as time to TCA. The demo starts at 2 days (48 hours).
_Avoid_: Now, current time, slider value

**Visible report**:
A report issued at or before the replay time, so its time to TCA is greater than or equal to the replay time.
_Avoid_: Available, known

**Current report**:
The latest visible report: the visible report with the smallest time to TCA.
_Avoid_: Latest, newest

**Replayable event**:
An event with at least one report issued 2 or more days before TCA, so it has a current report when the demo starts.

**Scored event**:
A replayable event whose final report was issued less than 2 days before TCA, so newer information arrived after the 48-hour mark. Only scored events count in the accuracy check.
