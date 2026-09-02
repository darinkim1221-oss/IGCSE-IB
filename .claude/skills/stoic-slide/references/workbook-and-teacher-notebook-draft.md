# Student Workbook & Teacher Notebook format

> **Status: canonical.** M1L1 (`lessons/M1L1/tier1-draw/M1L1_tier1_workbook.html`,
> `M1L1_tier1_teacher-notes.html`, `lessons/M1L1/tier2-read/M1L1_tier2_workbook.html`,
> `M1L1_tier2_teacher-notes.html`) is the **default template** for every other lesson's
> workbook and teacher notebook, in both tiers. When building or revising any other
> lesson's workbook/teacher-notes, open the matching M1L1 file side by side and match its
> section list, question types, sentence length, and answer-key tone directly — don't
> improvise a new structure per lesson.

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

## 🔴 Concise-by-default — the M1L1 rule

Both notebooks must stay **concise and simple**. Concretely, match M1L1's shape:

- **No padding sections.** If a section doesn't teach something the tutor/student needs
  in the next 45 minutes, cut it. M1L1's teacher notes do NOT have "Extension Activities,"
  "Key Takeaways," or a "Think Like an Economist" reflection slot, and Tier 2's does NOT
  have a separate "Exam Adapter Slot" section (that content now lives in the slide deck's
  own Exam Adapter slide — see `stoic-slide/SKILL.md`'s fixed 9-slide structure).
- **Prose becomes bullets.** Detailed Teaching Notes is a short bulleted list, one bold
  lead phrase + one sentence per bullet — never a wall of paragraphs.
- **Key Concepts & the IB Lens** is just the concept chip row (`.kc-chip`) — no paragraph
  underneath explaining the spine link.
- **Visuals & Diagrams** is 1–2 short `.diagram-note` callouts, no "tip" box.

## Student Workbook (`*_workbook.html`)

Sourced from the wiki's §6 lesson spec (Core content) for that lesson/tier — never
invented content beyond what the spec licenses.

1. Cover strip: title, one-line "what you'll practise", concepts chip row (reuse
   `.cc-chip` style from slide cover), question-count pill.
2. **Tier 1** (match `M1L1_tier1_workbook.html`): **8 questions**, mixed types (circle-
   the-answer, fill-in-the-blank, matching table, short-explain, fact/opinion-style
   sort, one simple graph-drawing question, one "which would you choose + one reason"
   question), plus one family-discussion mission. No exam framing, no command-term
   jargon. Every question must have a single, clean answer format — don't ask for "ONE
   reason" but leave two answer lines (match the number of lines to what's asked).
   **Tier 2** (match `M1L1_tier2_workbook.html`): **4–5 short questions** (Easy → Medium →
   Challenging, with `[n marks]` shown) plus **one** extended-response exam-style question
   worth 5–6 marks. Do not pad with more than 5 short questions — M1L1's tier 2 workbook
   is short and sharp, not a full past paper.
3. Answer space: ruled lines / boxed graph grid (for diagram questions) sized to the
   question — a workbook must be usable as a fill-in document, not just a question bank.
4. Answer key: on a clearly separated final section (`<div class="answer-key">`,
   page-break-before in print), full solutions — child-friendly for Tier 1, mark-scheme
   annotated for Tier 2.
5. No timer/score JS needed — this is a paper-analog artifact. Light JS only for
   optional "reveal answer" `<details>` toggles is fine.

## Teacher Notebook (`*_teacher-notes.html`)

The reference document a tutor opens before/during class. Match
`M1L1_tier1_teacher-notes.html` / `M1L1_tier2_teacher-notes.html` section-for-section:

1. Header strip + one-line suggested-flow strip. **Tier 2's suggested flow is a vertical
   numbered list** (`<ol>`), not a horizontal arrow chain — easier to scan mid-lesson.
2. **Learning Objectives** — short "I can…" bullets (Tier 1) or AO-tagged bullets
   (Tier 2). 4–6 bullets max, one clause each — not full sentences with sub-clauses.
3. **Key Concepts & the IB Lens** — just the `.kc-chip` row. No paragraph underneath.
4. **Detailed Teaching Notes** — a bulleted list (`<ul class="list">`), one `<strong>`
   lead phrase + one short sentence per bullet, pulled from the wiki's Tier 1/Tier 2
   delivery description for that lesson. Cut connective prose ("Unlike Tier 1...",
   "this is deliberately...") — state the teaching move, not the rationale.
5. **Visuals & Diagrams** — 1–2 `.diagram-note` callouts (icon + one short instruction).
   No tip box.
6. **Worked Example** — one short worked scenario with the model answer, 2–4 sentences.
7. **Common Misconceptions** — 2–3 `.warn-box` callouts (misconception → one-line fix).
8. **Teaching Resources** — a short glossary table only (exam-precise for Tier 2,
   child-friendly for Tier 1). No Key Takeaways box.

Do not add an Exam Adapter Slot section to the teacher notebook — that content is a
slide (see the fixed 9-slide structure in `stoic-slide/SKILL.md`), not a notebook
section, to avoid duplicating the same content in two files.
