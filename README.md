# POPL-Parser-Project

This repository contains an ANTLR v4 grammar and Python helpers for a small,
lightweight subset of the Python language (assignments, arithmetic, lists,
strings, numbers, variables, simple if/else). The project was used to
generate a parse tree image for a provided sample input.


## Team Members

- Alasdair Orr
- Elias Nelson
- Sean McEfresh
- Ethan Darling
- Dion Burns

---

## Requirements & Environment

- Java (JRE) 11 or newer — required to run the ANTLR generator (when regenerating parsers).
- Python 3.10+ (3.13 was used during development on the author machine).
- ANTLR tool version: 4.13.2 (recommended when regenerating the parser files used here).
- Python runtime: `antlr4-python3-runtime==4.13.2` (must match the generated parser version).
- Optional: `Pillow` (Python imaging library) to render the textual parse tree to a JPEG.

---

## Setup (Windows PowerShell)

1. Install Java (if you plan to regenerate the parser): download and install a JDK/JRE (11+).
2. Install Python 3.10+ and ensure `python` is on your PATH.
3. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install the required Python packages:

```powershell
python -m pip install --upgrade pip
python -m pip install antlr4-python3-runtime==4.13.2 Pillow
```

5. (Only if you need to regenerate the parser from the grammar) Download the ANTLR jar
   (example filename: `antlr-4.13.2-complete.jar`) from the ANTLR website and run:

```powershell
java -jar C:\path\to\antlr-4.13.2-complete.jar -Dlanguage=Python3 -o pd2 pd2\python_pd2.g4
```

Notes:

- Keep the generated parser/runtime versions matched. If the generated parser header says
  it was produced by ANTLR 4.13.2, install `antlr4-python3-runtime==4.13.2` to avoid runtime warnings.
- If the grammar file contains a UTF-8 BOM or duplicate headers, ANTLR may fail — save the `.g4`
  file without a BOM and ensure there are no duplicate grammar declarations.

---


## How to run the parser

- Print a compact parse tree and a pretty textual tree to the console (uses the provided `pd2/main.py`):

```powershell
python .\pd2\main.py
```

- Produce a parse-tree image (if `Pillow` is installed) using the generator helper:

```powershell
python .\pd2\gen_tree_image.py
```

This will save `pd2/parse_tree.jpg` (or `pd2/parse_tree_from_main.jpg` depending on which helper you run).

If you prefer to capture the exact console output from `pd2/main.py` and render it to an image,
run the capture script (if present):

```powershell
python .\pd2\gen_tree_image_from_main.py
```

### Does this apply to `pd3`?

Yes — the same setup and run steps apply to the `pd3` folder. Differences to check when running `pd3`:

- Use the `pd3` filenames instead of `pd2` (`pd3/main.py`, `pd3/gen_tree_image.py`, etc.).
- Ensure the generated parser files in `pd3/` (e.g. `python_pd3Parser.py`, `python_pd3Lexer.py`) exist and
  that the installed `antlr4-python3-runtime` version matches the ANTLR version used to generate them
  (check the header comment in `pd3/python_pd3Parser.py`).
- Run from the repository root so the `pd3` package imports resolve correctly:

```powershell
python .\pd3\main.py
python .\pd3\gen_tree_image.py
```
---
