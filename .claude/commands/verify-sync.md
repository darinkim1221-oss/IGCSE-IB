Run the spine-sync verification for this repository and report the result clearly.

Steps:
1. Run `python3 scripts/verify_sync.py` from the repository root.
2. Read its output carefully.
3. If it reports `[OK] IN SYNC`:
   - Tell the user in one short sentence that the Excel course map and the wiki are
     confirmed in sync with `scripts/build.py`, and that there is nothing to fix.
4. If it reports `[MISMATCH]`:
   - Explain in plain language what changed (summarize the diff it printed — do not
     just paste the raw diff, translate it into "the wiki previously said X, the spine
     now says Y").
   - Confirm that `outputs/Economics-Academy-Course-Map-v3.xlsx` and
     `outputs/economics-academy-llm-wiki.md` have already been regenerated correctly
     (the script does this automatically as part of the check).
   - Stage and commit only `outputs/` (plus `scripts/build.py` or `scripts/gen_wiki.py`
     if those were the files that changed) with a clear commit message describing what
     changed in the spine — do not commit unrelated files.
   - Ask the user before pushing, unless they have already indicated they want you to
     push automatically.
5. If the script itself errors out (not a `[MISMATCH]`, but a Python traceback or a
   `[FAIL]` message), do not attempt to commit anything. Show the user the exact error
   and diagnose it — common causes are: the Excel file is currently open in Excel
   (locked, shows as a `~$...xlsx` file), a missing dependency (`pip install openpyxl
   --break-system-packages`), or being run from the wrong directory (this command must
   be run from the repository root, not from inside `scripts/`).

Never hand-edit `outputs/Economics-Academy-Course-Map-v3.xlsx` or
`outputs/economics-academy-llm-wiki.md` yourself to "fix" a mismatch — the only correct
fix is editing `scripts/build.py` (the spine) and letting `verify_sync.py` regenerate
both files from it.
