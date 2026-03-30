---
sidebar_position: 3
description: What ASJudge does, who uses it, and what students can see.
---

# ASJudge Overview

**ASJudge** is the competition-day platform for Aerospace Jam. It brings judging, scheduling, student access, and public displays into one place so staff do not need to juggle separate spreadsheets, timers, and score calculators all day long.

## What ASJudge handles

On competition day, ASJudge is responsible for nearly everything that has to be coordinated digitally. Staff use it to sign in by passphrase, teams use it to sign in with their six-digit access codes, judges use it to enter rubric-based scores, and facilitators use it to keep the arena timing accurate. It also handles safety warning tracking, award assignments and voting, congeniality voting, the public and team-facing scoreboards, the schedule page, and the projector views used during the event and awards ceremony.

## Who uses it

Different roles land on different dashboards after login. Admins create staff accounts, import teams, control visibility settings, manage the schedule, and oversee awards. Judges score the rubrics they have been assigned and, when needed, submit award votes. Facilitators control arena timing for a specific arena, while queuers see who to grab next and where to take them. The safety officer logs warnings and keeps track of deduction thresholds. Teams, meanwhile, use the team portal to view their own status, public standings, and congeniality voting when that window is open.

## What students and mentors should know

Students do not see the full staff side of ASJudge, but they do interact with several important parts of it. At check-in, each team receives a **six-digit team access code**, and that code opens the **team portal**. If public scores are enabled, that portal can show the team's current scores and rank. It also shows their next arena appearance, queue time, and current status. When congeniality voting is open, teams can nominate up to **five other teams**, and the public homepage can show top standings, the full scoreboard, and the live schedule.

For students and mentors, the most important thing to understand is that queue and arena times are **live estimates**. As facilitators log real starts and ends, later teams may shift a little.

## The core staff workflow

On event day, ASJudge usually follows a fairly natural rhythm. Admins begin by importing or verifying teams, printing credentials, and creating staff accounts. Judges sign in and confirm they can see the correct dashboard, while facilitators and queuers begin working from the live arena schedule. Throughout the day, judges save scores as teams complete pit or arena judging, safety warnings are logged if needed, and the public-facing displays shift from schedule to scores to awards as the event progresses. Near the end of the day, award votes are reconciled and the automatic awards are checked one last time.

## Judge scoring model

ASJudge stores scores by team, judge, rubric, and scoring item. That matters because multiple judges can score the same rubric independently, and the standings use the **average score per rubric across the judges who scored it** rather than one giant combined sheet. If a judge marks a team as a **no-show** for a rubric, ASJudge records that in the judge note for that team and rubric.

## Arena timing model

The arena side of ASJudge is built around a small set of statuses: `scheduled`, `queued`, `active`, `completed`, and `no_show`. The facilitator is the role that changes those statuses. In practice, `Queue` means the team should be coming toward the arena, `Start` means the run has actually begun, `End` means the run has actually ended, `No Show` closes the slot without a run, and `Reset` clears the timing if the wrong action was logged.

Because the public schedule, team portal, and queuer dashboard all depend on those statuses, the facilitator's button presses affect much more than one screen.

## Safety and penalties

The safety officer can log warnings by team, and after **more than three warnings**, ASJudge automatically applies a **10-point deduction to navigation** in the calculated standings. That is important for both staff and students to understand, because the warning log is not just a note-taking tool. Once the threshold is crossed, it directly changes score calculations.

## Awards in ASJudge

ASJudge supports two kinds of awards: **automatic awards**, which are calculated from rubric scores or congeniality votes, and **manual awards**, which are decided by assigned judges through award voting. That means some awards update automatically throughout the day, while others depend on judges actually submitting their decisions.

## What can be hidden from teams and the public

Admins can control two major visibility settings: whether **congeniality voting** is open and whether **public scores** are visible. If public scores are hidden, the public scoreboard becomes unavailable to non-staff, team-facing score displays are hidden, and projector score views are blocked as well.

## Common operational rules

No matter which role you are in, the same few habits keep the event running smoothly. Use the dashboard for the role you were assigned rather than sharing one account across unrelated jobs. Save scores while the interaction is still fresh. Do not guess when correcting mistakes; if an entry looks wrong, ask the head admin. Treat live timing as operational data rather than a rough suggestion, and put safety ahead of schedule whenever the two are in tension.

## Role guides

After this page, continue with the guide for the role you are actually performing: [Admin Guide](/for-staff/admin-guide), [Arena Judges](/for-staff/arena-judges), [Pit Judges](/for-staff/pit-judges), [Facilitators](/for-staff/facilitators), [Queuers](/for-staff/queuers), or [Safety Officer](/for-staff/safety-officer).
