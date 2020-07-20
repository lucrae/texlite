TODO:
- unordered lists
- ordered lists
- equations
- unnumbered headings (# *heading)
- footnotes
- scanning for unsupported commands
- more meta options (fontsize, margin)


dependency on pdflatex

https://www.markdownguide.org/cheat-sheet/

Note that TeXLite utilises just an essential set of Markdown's syntax/elements, for example horizontal rules aren't used in standard LaTeX and so won't be parsed as anything special in TexLite. Still, TeXLite uses the .md format so you don't have to put in any extra effort to get syntax highlighting in your editor.

For anything LaTeX-specific, all standard LaTeX control sequences can be used seemlessly. (E.g.: This was written on: \today{}.)


<!-- # Install LaTeX engine dependencies

`sudo apt-get install latexmk`

# Issues

- PyLaTeX compilation failing with latexmk because of "lastpage.sty" not found -->
