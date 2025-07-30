# Cursor Prompt Library

This directory contains an aggregated `prompt_library.json` file that can be imported into [Cursor](https://www.cursor.so/) as a personal prompt library. The file is generated from the markdown agent definitions in this repository.

## Generating the Library

Run the script from the repository root:

```bash
python3 scripts/build_cursor_prompt_library.py
```

The script scans all `.md` files (except `README.md`), extracts basic front‑matter fields (`name`, `description`, `color`, `tools`), and bundles the full agent prompt text. The resulting JSON is written to `cursor/prompt_library.json`.

## Using in Cursor

1. Open Cursor and navigate to **Settings → Prompt Library**.
2. Choose **Import** and select the generated `prompt_library.json` file.
3. The agents will appear under your **Personal** library as reusable prompts.

   Open the library with `Cmd`/`Ctrl`+`Shift`+`L` (or use the quick search `/` dialog)
   and start typing an agent's name. Selecting the entry inserts the full
   system prompt so you can run it in any project.

   Example uses:
   - **rapid-prototyper** in a new JavaScript repo to scaffold an MVP
   - **tiktok-strategist** while drafting marketing plans

You can regenerate the file whenever agent definitions change.
