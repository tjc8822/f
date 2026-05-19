# AGENTS.md

## Cursor Cloud specific instructions

This is a LaTeX/Beamer academic presentation project (not a software application). The only "build" output is a compiled PDF.

### Build

```bash
latexmk -pdf main.tex
```

### Lint

```bash
chktex main.tex
```

Note: `chktex` reports style warnings (not errors) for existing math notation patterns in the document — these are expected and not regressions.

### Clean

```bash
latexmk -c          # remove auxiliary files, keep PDF
latexmk -C          # remove auxiliary files AND PDF
```

### Required system packages

The following Ubuntu packages must be installed (handled by the update script):
- `texlive-latex-recommended` (core LaTeX + Beamer)
- `texlive-latex-extra` (soul, booktabs, etc.)
- `texlive-fonts-recommended` + `texlive-fonts-extra` (lmodern, ccicons)
- `texlive-science` (additional math packages)
- `latexmk` (build automation)
- `chktex` (linting)

### Notes

- The project originated from Overleaf. `references.bib` is empty so bibtex/biber is not needed.
- `beamerthemesimple.sty` is a custom theme in the repo root; no external theme installation needed.
- `transcript.tex` contains speaker notes but is not included in the default build (the `\include{transcript}` line is commented out in `main.tex`).
