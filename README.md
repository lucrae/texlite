<p align="center">
  <img src="docs/images/texlite.png" />
</p>

[![PyPI version](https://badge.fury.io/py/texlite.svg)](https://badge.fury.io/py/texlite) ![Ubuntu](https://github.com/lucrae/texlite/workflows/Ubuntu/badge.svg) ![macOS](https://github.com/lucrae/texlite/workflows/macOS/badge.svg)

TeXLite is a lightweight open-source tool for writing standard LaTeX/TeX documents in clean, Markdown-style syntax. With TeXLite, it's easy to write **good-looking documents with minimal overhead**.

<p align="center">
  <img width="100%" src="docs/images/demo.png" />
  <p align="center"><i>A demo of writing a simple document in an editor and compiling it to a PDF with TeXLite</i></p>
</p>

# Get Started

## Install

**STEP 1**: Install and upgrade with [pip](https://pip.pypa.io/en/stable/quickstart/).

```
$ pip install --upgrade texlite
```

**STEP 2**: Install (if not already installed) a [distribution of TeX](https://www.latex-project.org/get/). Recommendations:
- On Ubuntu, *TeX Live* can be installed with `sudo apt-get install texlive`.
- On MacOS, *MacTeX* can be installed with `brew cask install mactex`.
- On Windows, *MikTeX* can be installed from [its official downloads page](https://miktex.org/download).

You should now be able to compile your documents into PDFs with:

```
$ texlite my_document.md
```

(Or alternatively `$ python -m texlite my_document.md`).

Use `texlite --help` for options and information. If you have any issues installing, refer to [Installation Fixes](#installation-fixes).

## Usage

All the info you need on writing with TeXLite is in this [this concise guide](https://github.com/lucrae/texlite/blob/documentation/docs/guide.md).

# Contributing

TeXLite is still in development and has plenty of features and fixes yet to come! If you can help with that, no matter to what degree, contributers are very welcome.

If you have any issues/bugs/requests, or want to know what code is in need of writing, please go to the [Issues](https://github.com/lucrae/texlite/issues) page.

If you're new to contributing, that's okay! Refer to [this great guide](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/) on how to get started.

# Other

## License

TeXLite is licensed under [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html). You are essentially free to use this software in any way you want (privately, commercially, with modifications, etc.) on the condition that distributions stay open-source and stick to the license.

## Installation Fixes

If you're having issues with installing TeXLite, here are some fixes to possible problems:

- **Wrong Python**: If `pip install texlite` is not working, you may be using Python 2.7, which has reached its end of life. Use `pip3 install --upgrade pip` and then `pip3 install texlite` to ensure that you are using Python 3.

- **TeX Live Missing Packages**: If *TeX Live* is installed and working but the document TeX cannot be compiled, it may because of missing plugins. You can ensure your *TeX Live* has all the plugins with `sudo apt-get install texlive-full`.

- **MikTeX Missing Packages**: When first running *MikTeX* on Windows, you may still need to install LaTeX packages. To easily install all that are missing, run `texlite` and wait for a prompt. In the prompt there's a checkbox to do this automatically, which may require you to wait but then it should fix your problems.

- **Not added to Windows PATH**: On Windows PowerShell, Pip will not automatically add programs to your PATH (meaning that TeXLite can't be executed with `$ texlite`). You can fix this either by adding texlite to your PATH, or by calling TeXLite instead with `python -m texlite` or `python3 -m texlite`.
