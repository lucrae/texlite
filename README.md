<p align="center">
  <img src="docs/images/texlite.png" />
</p>

[![PyPI version](https://badge.fury.io/py/texlite.svg)](https://badge.fury.io/py/texlite) ![Ubuntu](https://github.com/lucrae/texlite/workflows/Ubuntu/badge.svg) ![MacOS](https://github.com/lucrae/texlite/workflows/MacOS/badge.svg)

TeXLite is an easy-to-use open-source tool for writing standard LaTeX/TeX documents in clean, Markdown-style syntax. With TeXLite, it's easy to write **good-looking documents with minimal overhead**.

# Install

**Step 1**: Install TeXLite with [pip](https://pip.pypa.io/en/stable/quickstart/).

```
pip install texlite
```

**Step 2**: Install (if not already installed) a [distribution of TeX](https://www.latex-project.org/get/).
- For Ubuntu, *TeX Live* can be installed with `sudo apt-get install texlive`.
- For MacOS, *MacTeX* can be installed with `brew cask install mactex`.

You should now be able to compile documents with:

```
texlite my_document.md
```

Use `texlite --help` for options and information.
