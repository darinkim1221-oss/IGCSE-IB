# -*- coding: utf-8 -*-
"""
verify_sync.py — confirms the Excel course map and the LLM wiki are in sync
with scripts/build.py (the spine), and with each other.

Run this before every commit that touches scripts/build.py, scripts/gen_wiki.py,
or outputs/. Exits non-zero (and prints a clear diff) if anything is out of sync,
so it is also safe to wire into a pre-commit hook or a CI check later.

Usage (from the repository root):
    python3 scripts/verify_sync.py
"""
import subprocess
import sys
import re
import difflib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI_PATH = ROOT / "outputs" / "economics-academy-llm-wiki.md"
BUILD = ROOT / "scripts" / "build.py"
GEN_WIKI = ROOT / "scripts" / "gen_wiki.py"

DATE_LINE = re.compile(r"^_Auto-generated from .* on \d{4}-\d{2}-\d{2}\.")

def normalize(text):
    """Strip the auto-generated date line so a same-day-vs-different-day rerun
    doesn't get flagged as a content mismatch."""
    if text is None:
        return None
    lines = text.splitlines()
    return "\n".join(DATE_LINE.sub("_Auto-generated from <workbook> on <date>.", l) for l in lines)

def read_text(path):
    if not path.exists():
        return None
    # Always read as UTF-8 regardless of OS default, matching the fixed writer.
    return path.read_text(encoding="utf-8")

def run(script):
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"[FAIL] {script.name} exited with an error:\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def main():
    print("Checking that outputs/*.xlsx and outputs/*wiki.md match scripts/build.py ...")
    print()

    if not BUILD.exists() or not GEN_WIKI.exists():
        print("[FAIL] scripts/build.py or scripts/gen_wiki.py not found. "
              "Run this from the repository root: python3 scripts/verify_sync.py")
        sys.exit(1)

    before = read_text(WIKI_PATH)
    if before is None:
        print(f"[INFO] No committed wiki found at {WIKI_PATH.relative_to(ROOT)} yet — "
              "this will be its first generation.")
        before = ""

    print("1. Rebuilding the Excel course map from scripts/build.py ...")
    print("   " + run(BUILD))

    print("2. Regenerating the wiki from the freshly-built Excel ...")
    print("   " + run(GEN_WIKI))

    after = read_text(WIKI_PATH)

    print()
    if normalize(before) == normalize(after):
        print("[OK] outputs/*.xlsx and outputs/*wiki.md are IN SYNC with scripts/build.py.")
        print("     (Only the auto-generated date stamp may have changed — that's expected.)")
        print("     Safe to commit as-is (or nothing meaningful to commit).")
        sys.exit(0)
    else:
        print("[MISMATCH] The committed wiki did NOT match what scripts/build.py "
              "actually produces.")
        print("           Both files have now been regenerated to the correct, current state.")
        print("           Review the diff below, then git add + commit the updated outputs/.")
        print()
        diff = difflib.unified_diff(
            before.splitlines(keepends=True),
            after.splitlines(keepends=True),
            fromfile="outputs/economics-academy-llm-wiki.md (before)",
            tofile="outputs/economics-academy-llm-wiki.md (after, regenerated)",
        )
        diff_text = "".join(diff)
        # keep console output readable — cap very long diffs
        lines = diff_text.splitlines()
        if len(lines) > 200:
            print("\n".join(lines[:200]))
            print(f"\n... ({len(lines) - 200} more diff lines omitted) ...")
        else:
            print(diff_text)
        sys.exit(1)

if __name__ == "__main__":
    main()
