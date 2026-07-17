# Stoic Edu · Economics Academy — Claude Code Context

This file is read automatically at the start of every Claude Code session in this
repository. It tells you what this project is, and exactly what to check before
producing any teaching material (slide, game, worksheet, card, brochure).

---

## 🔴 NON-NEGOTIABLE RULES (apply to EVERY material, no exceptions)

1. **All teaching materials are written in ENGLISH.** Every piece of student-facing content —
   slide text, titles, captions, quiz questions, game prompts, feedback messages, worksheets,
   cards — is **English only**. (You may still converse with the owner/intern in Korean, but
   nothing produced *inside a lesson file* is in Korean.)
2. **There is NO Stoic Edu logo file.** Never reference, embed, or fabricate a logo image,
   seal, or emblem. Header attribution is a **plain text wordmark only**: `Prepared by · STOIC EDU`.
   No `logo.png`, no base64 logo, no invented "STE" seal graphic.

These two rules override anything in the skills or references if they ever conflict.

---

## What this repository is

A Pre-IGCSE / Pre-IB Economics curriculum for Stoic Edu, a children's financial-education
platform. 18 lessons, built on a **3-layer architecture**: one conceptual SPINE, delivered
through two thinking TIERS (Tier 1 "Draw the Map", ages 10-12 / Tier 2 "Read the Map",
ages 13-15), topped by a swappable exam ADAPTER (IGCSE or IB). Verified against Cambridge
IGCSE 0455 (2027-29) and the IB DP Economics Guide (2022).

Two people work in this repo: the owner (curriculum design, edits `scripts/build.py` only)
and an intern (materials creation, works only inside `lessons/`). See "Division of labour"
below — respect it even if not explicitly reminded in a given session.

---

## BEFORE producing any material — read these, in this order

### 1. The lesson spec (what to make)
```
outputs/economics-academy-llm-wiki.md
```
This is the production manual, auto-generated from the course-map Excel. Always open it
and read:
- **§0 Prime Directives** — 7 rules that apply to every single material, no exceptions.
- **§6, the specific lesson's spec** (find it by ID, e.g. `M2L1`) — Core Concepts, Essential
  Questions, Core content (priority-ordered bullets with `[ENRICH]`/`[LOW]`/`(!)` flags),
  Key diagrams, Exam-skill focus, and the Tier 1 / Tier 2 delivery descriptions.
- **§7 the drip map row for that lesson** if the material touches exam technique — never
  invent exam content; it must come from that lesson's row.
- **§8 the Bridge** if the material needs to motivate a concept's IGCSE->IB payoff.

If the wiki looks stale (doesn't match a recent verbal instruction about the curriculum),
say so — it may need regenerating from `scripts/build.py` (see below) before you proceed.

### 2. The skill (how to make it — format, layout, brand rules)
```
.claude/skills/<relevant-skill>/SKILL.md
```
Two skills live in this repo:
| Making a... | Use skill |
|---|---|
| Interactive HTML slide deck | `stoic-slide` (also read its `references/base-css.md` and `references/template-structure.md`) |
| Game / simulation design | `finance-game-designer` |

Read the whole SKILL.md (and, for slides, both reference files) — they define exact
dimensions (960×540 fixed frame for slides), fonts, CSS variables, and structure. Never
freehand a layout the skill already defines.

If a request needs a format neither skill covers (e.g. a PDF brochure, an Instagram card,
a class-note PDF), say so plainly rather than improvising — that skill hasn't been added
to this repo yet and should be requested from the owner.

### 3. Sibling materials already in the lesson folder (consistency check)
```
lessons/<LESSON_ID>/shared/      ← spine content shared by both tiers — check tone match
lessons/<LESSON_ID>/tier1-draw/  ← if building tier2, glance at tier1 for the same lesson
lessons/<LESSON_ID>/tier2-read/  ← if building tier1, likewise
```
If material for the *other* tier of the same lesson already exists, keep vocabulary and
the concept-promotion arc consistent with it (same topic, different verbs — see Prime
Directive 2).

### 4. Brand assets (visual reference, as needed)
```
assets/architecture-3-layer.pdf   ← the 3-layer design principle poster
assets/bridge-igcse-to-ib.pdf     ← the IGCSE→IB concept bridge poster
```
Useful for tone/visual-language reference, not usually read directly for a single lesson
slide — the SKILL.md's own design tokens take priority for actual styling.

---

## Where the finished file goes

```
lessons/<LESSON_ID>/<tier1-draw | tier2-read | shared>/<LESSON_ID>_<tier>_<short-name>.html
```
Example: `lessons/M2L1/tier1-draw/M2L1_tier1_currency-game.html`

Never write into `outputs/` (generated only) or `scripts/` (owner-only, the spine).

---

## Division of labour (do not cross without being asked)

| Area | Who edits | Notes |
|---|---|---|
| `scripts/build.py` | Owner only | The spine. All curriculum data lives here. |
| `outputs/*.xlsx`, `outputs/*.md` | Nobody by hand | Generated — see regeneration command below. |
| `lessons/**` | Intern (and owner reviewing) | Teaching materials. Safe to create freely. |
| `.claude/skills/**` | Either, rarely | Only when a skill itself needs improving. |

If asked to change curriculum content (add/remove/reprioritize a bullet, change a flag,
adjust a diagram requirement), that is a **spine change**: edit `scripts/build.py`, then run

```bash
python3 scripts/build.py && python3 scripts/gen_wiki.py
```

to regenerate both the Excel and the wiki before continuing. Do not hand-edit the xlsx or
the wiki.md — they will be overwritten on the next regeneration and are binary/generated
respectively (the xlsx especially cannot be merged by git).

---

## Prime Directives quick-reference (full text lives in the wiki §0)

1. Three layers, never mixed — spine / tiers / adapter stay in their lane.
2. Same topic, different verbs — Tier 1 feels it, Tier 2 judges it.
3. Tiers are entry points, not a sequence — never imply Pre-IGCSE must precede Pre-IB.
4. Honour the flags — bullets are priority-ordered; `[ENRICH]`/`[IB SL CORE]`/`[LOW]`/`(!)`
   constrain what belongs in core vs. optional material.
5. Nothing outside the current syllabuses is ever taught as core (hard boundaries: XED,
   deflation, fixed/managed FX, market-failure D/S diagrams, AD-AS at IGCSE, the formal
   comparative-advantage model and multiplier at IB SL — all enrichment-only, if included).
6. Single-point updates — new cases/hooks attach to spine content, not forked per tier.
7. All questions must be original — never reproduce past-paper items from either board.

When in doubt, the wiki's full §0 wins over this summary.
