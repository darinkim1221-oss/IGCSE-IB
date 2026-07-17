# Stoic Edu · Economics Academy — Curriculum Repository

Pre-IGCSE / Pre-IB Economics foundation curriculum (18 lessons, 3-layer architecture).
Verified against **Cambridge IGCSE 0455 (2027–2029)** and the **IB DP Economics Guide (2022)**.

---

## The one rule that matters

> **`scripts/build.py` is the single source of truth.**
> The Excel course map and the LLM wiki are *generated* from it. Never hand-edit the files
> in `outputs/` — your edits will be overwritten on the next build, and binary `.xlsx`
> files cannot be merged by git anyway. Edit the Python, regenerate, commit both.

This is Design Commitment 5 ("one spine, single-point updates") applied to the repo itself.

---

## Repository layout

```
economics-academy/
├── scripts/
│   ├── build.py        ← THE SPINE. All curriculum data + Excel builder. Edit here.
│   └── gen_wiki.py     ← Converts the built xlsx into the LLM wiki.
├── outputs/            ← Generated artifacts (committed for convenience, never hand-edited)
│   ├── Economics-Academy-Course-Map-v3.xlsx
│   └── economics-academy-llm-wiki.md
├── lessons/            ← Teaching materials, one folder per lesson (M1L1 … M3L6)
│   └── M1L1/           ← slides, games, worksheets for that lesson (both tiers)
├── assets/             ← Brand posters (3-layer architecture, IGCSE→IB bridge)
└── README.md
```

## Setup (once)

```bash
git clone <repo-url>
cd economics-academy
pip install openpyxl
```

## Regenerate after editing the spine

```bash
python3 scripts/build.py       # rebuilds outputs/…xlsx
python3 scripts/gen_wiki.py    # rebuilds outputs/…wiki.md from the xlsx
git add -A && git commit -m "spine: <what changed>"
```

(Tip: run both with `python3 scripts/build.py && python3 scripts/gen_wiki.py`.)

---

## Collaboration workflow (owner + intern)

**Division of labour — designed to avoid merge conflicts:**

| Area | Owner | Intern |
|---|---|---|
| `scripts/build.py` (the spine: lessons, priorities, flags) | ✅ edits | reads only |
| `lessons/M#L#/` (slides, games, worksheets) | reviews | ✅ creates |
| `outputs/` | regenerates & commits | never touches |

Because the spine is one file owned by one person, and each lesson folder is
independent, two people almost never edit the same file — git stays painless.

**Intern's daily loop:**
```bash
git pull                                  # get the latest spine + wiki
# open outputs/economics-academy-llm-wiki.md → find your lesson spec (e.g. M2L1)
# create materials in lessons/M2L1/  (follow the Prime Directives in the wiki §0)
git add lessons/M2L1 && git commit -m "M2L1: tier-1 currency game v1"
git push
```

**Owner's loop:** pull, review the intern's lesson folders, edit the spine when the
curriculum itself changes, regenerate, push.

**If you both might touch the same lesson:** use branches —
`git checkout -b m2l1-tier1-game`, push, and open a Pull Request for review.
For this team size, direct pushes to `main` with the division of labour above is fine.

---

## Creating materials with an LLM

`outputs/economics-academy-llm-wiki.md` is the production manual. Attach it (or add it
as Project Knowledge in Claude) and reference lessons by ID:

> "Using the wiki, create the Tier 1 lesson package for **M2L1**
> (the invent-your-own-currency game) as HTML slides."

The wiki's §0 Prime Directives enforce the architecture automatically: tier separation,
priority ordering, syllabus boundaries ([ENRICH]/[LOW] flags), and the exam-adapter rules.

---

## Naming & versioning

- Lesson material files: `M2L1_tier1_slides_v1.html`, `M2L1_tier2_worksheet_v1.pdf`
- Curriculum versions are tagged: `git tag v3` after a spine change is verified.
- Syllabus watch: IGCSE 0455 is fixed for 2027–29 exams; IB Economics (2022 guide) is
  not in the 2027 update cycle. Re-verify both when a new syllabus cycle is announced.
