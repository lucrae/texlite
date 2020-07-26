<p align="center">
  <img src="docs/images/texlite.png" />
</p>

[![PyPI version](https://badge.fury.io/py/texlite.svg)](https://badge.fury.io/py/texlite) ![Ubuntu](https://github.com/lucrae/texlite/workflows/Ubuntu/badge.svg) ![macOS](https://github.com/lucrae/texlite/workflows/macOS/badge.svg)

TeXLite is an easy-to-use open-source tool for writing standard LaTeX/TeX documents in clean, Markdown-style syntax. With TeXLite, it's easy to write **good-looking documents with minimal overhead**.

# Install

**STEP 1**: Install and upgrade with [pip](https://pip.pypa.io/en/stable/quickstart/).

```
$ pip install --upgrade texlite
```

**STEP 2**: Install (if not already installed) a [distribution of TeX](https://www.latex-project.org/get/). Recommendations:
- On Ubuntu, *TeX Live* can be installed with `sudo apt-get install texlive`.
- On MacOS, *MacTeX* can be installed with `brew cask install mactex`.
- On Windows, *MikTeX* can be downloaded and installed from [here](https://miktex.org/download)

You should now be able to compile documents with:

```
$ texlite my_document.md
```

Use `texlite --help` for options and information. If you have any issues installing, refer to [Installation Fixes](##Installation-Fixes).

## Installation Fixes

- If `pip install texlite` is not working, you may be using Python 2.7, which has reached its end of life. Use `pip3 install --upgrade pip` and then `pip3 install texlite` to ensure that you are using Python 3.

- If *TeX Live* is installed and working but the document TeX cannot be compiled, it may because of missing plugins. You can ensure your *TeX Live* has all the plugins with `sudo apt-get install texlive-full`.

- When first running *MikTeX* on Windows, you may still need to install LaTeX packages. To easily install all that are missing, run `texlite` and wait for a prompt. To make this quicker, select the "
