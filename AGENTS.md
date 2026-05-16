# AGENTS.md

## Cursor Cloud specific instructions

This is a LaTeX Beamer presentation project (academic slide deck). There are no software services, databases, or runtime servers — only document compilation.

### Building

Compile the presentation with:

```
cd /workspace && pdflatex -interaction=nonstopmode main.tex
```

Run twice for correct cross-references and PDF outlines:

```
pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

Output: `main.pdf` (13-page Beamer slide deck).

### Dependencies

Requires TeX Live with: `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-fonts-extra`, `texlive-pictures`, `lmodern`. These are installed via the update script.

### Key files

| File | Purpose |
|---|---|
| `main.tex` | Main Beamer presentation source |
| `beamerthemesimple.sty` | Custom Beamer theme (styling) |
| `transcript.tex` | Speaker notes/transcript |
| `references.bib` | Bibliography (currently empty) |

### Notes

- There is no `Makefile`, no CI, no linter, and no automated tests — the "test" is a successful `pdflatex` compilation with exit code 0.
- Check for errors with: `grep -c "^!" main.log` (should be 0).
- The `transcript.tex` file is currently commented out in `main.tex` (line `%\include{transcript}`).
