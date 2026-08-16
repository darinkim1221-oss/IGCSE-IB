# DRAFT — Student Workbook & Teacher Notebook format

> **Status: non-canonical, first draft.** Neither format has an owner-approved skill yet.
> This note exists only so materials produced under this draft stay consistent with each
> other. Treat it as a starting point to refine, not a locked spec — flag to the owner if
> it should be promoted to a real `.claude/skills/` skill or replaced.

Both formats reuse stoic-slide's brand tokens (colors, fonts, "no logo — text wordmark
only" rule, English-only rule) but are **document-style** (scrollable/printable), not the
960×540 fixed slide frame — homework and teacher prep are read top-to-bottom, not clicked
through.

## Shared page shell (both formats)

- Single self-contained HTML file, CSS inline, same Google Fonts link as stoic-slide
  (Bebas Neue / Noto Sans KR / Space Mono), same `:root` color variables.
- `max-width: 840px` centered content column, white page background, `#f5f7fa` page
  backdrop, generous padding — reads well both on screen and printed (`@media print`
  removes the backdrop margin and page-break avoids mid-question).
- Header: text wordmark `Prepared by · STOIC EDU` (top-right, small, navy) + lesson
  meta strip (Module · Lesson ID · Title · Tier · estimated time).
- Section headers use `.section-tag` (Space Mono, gold, uppercase) + `.big-title`
  (Bebas Neue), same as slide decks, for visual family resemblance.
- Footer: lesson ID + "Economics Academy · Stoic Edu" text line, no logo.

## Student Workbook (`*_workbook.html`)

Sourced from the wiki's §4 rows 7 (Practice Questions) and 10 (Homework) for that
lesson/tier — never invented content beyond what those rows + the lesson spec license.

1. Cover strip: title, one-line "what you'll practise", concepts chip row (reuse
   `.cc-chip` style from slide cover).
2. **Tier 1**: shorter question set, game/mission-formatted phrasing, plus one
   "family discussion mission" (a take-home conversation prompt, not a written answer).
   No exam framing, no command-term jargon.
   **Tier 2**: full mixed-difficulty set (Easy → Medium → Challenging) plus one
   exam-style extended question in that lesson's drip-map format (§7 row), with mark
   allocations shown exactly like the real paper (e.g. "[4 marks]").
3. Answer space: ruled lines / boxed graph grid (for diagram questions) sized to the
   question — a workbook must be usable as a fill-in document, not just a question bank.
3. Answer key: on a clearly separated final section (`<div class="answer-key">`,
   page-break-before in print), full solutions — child-friendly for Tier 1, mark-scheme
   annotated for Tier 2 (matches §4 row 8 tone split).
4. No timer/score JS needed — this is a paper-analog artifact. Light JS only for
   optional "reveal answer" `<details>` toggles is fine.

## Teacher Notebook (`*_teacher-notes.html`)

The reference document a tutor opens before/during class. Compiles the *teaching*
content of the wiki's lesson template (never the student-facing slide script verbatim)
sections 2,3,4,5,9(Tier2 only),11,12.

1. Header strip as above, plus a one-line lesson-flow summary (which slide maps to
   which minute, roughly).
2. **Learning objectives** — 'I can' statements (T1) or AO1–4 tagged (T2), §4 row 2.
3. **Key concepts & KC lens** — the nine-key-concept link, §4 row 3 / wiki §3.
4. **Detailed teaching notes** — the story/analogy/discussion-prompt prose from §4 row
   4, written as prose a tutor can read from, not just bullets copied from the wiki.
5. **Visuals & diagrams** — how to draw it, common student mistakes, §4 row 5.
6. **Worked examples** — full reasoning, §4 row 6.
7. **Exam Adapter Slot (Tier 2 only)** — content taken verbatim in spirit from §7's row
   for that lesson (shared skill / IGCSE element / IB element) — never invented.
8. **Misconceptions box** — gold-left-border callout, reused from slide skill's tip box.
9. **Extension activities** — §4 row 11.
10. **Teaching resources** — glossary (exam-precise for T2, child-friendly for T1),
    key takeaways, formula/reference box where relevant, §4 row 12.
11. Optional: a simple anchor-link mini table of contents at the top since this is a
    reference doc meant to be jumped around in, not read start-to-front every time.
