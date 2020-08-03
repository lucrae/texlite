# Writing with TeXLite

This is a concise guide to using TeXLite v1.1.0.

- [Introduction](#introduction) provides an overview of TeXLite.
- [Usage](#usage) provides information on how to run TeXLite.
- [Features](#features) covers the features of TeXLite, with examples included with all components.

## Introduction

TeXLite *(pronounced `teck-lite`)* is a lightweight open-source tool for writing standard LaTeX/TeX documents in clean, Markdown-style syntax. With TeXLite, it's easy to write **good-looking documents with minimal overhead**.

Standard writing in TeXLite is done with [basic Markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). More complex writing, such as maths, can be done with [LaTeX commands](https://www.latex-project.org/). TeXLite extends LaTeX/TeX, so standard in-line commands in LaTeX will be standard in-line commands in TeXLite.

The "meta" specifications of a document such as titles, authors, margins, font sizes, etc. can be specified at the start of the document. For example, writing in `:title: My Document` will set the document title to "My Document". More information in this can be found under [Document Setup](#document-setup).

## Usage

For instructions on installation, refer to [Installation](https://github.com/lucrae/texlite/blob/master/README.md#install) in the README.

General usage of TeXLite is as follows:

1. Write your document in a text editor, and save it as a Markdown (`.md`).
2. In the command-line, enter `texlite path/to/document` (or `python -m texlite path/to/document`) and TeXLite will generate a PDF beside the document.

You can `cd` to the location of your document, or specify the path. Use `texlite --help`for more information.

Note that writing in TeXLite has features beyond Markdown, but source files are still accepted as `.md` so that you don't have to do any extra work to get nice syntax highlighting in your editor.

## Features

### Section headings

Section headings are written using the hash character.

```
# This the heading of a section
## This is the heading of a subsection
### This is the heading of a subsubsection
```

Section headings will be automatically numbered. If you want unnumbered section headings, add an asterix after the hash.


```
#* This the heading of an unnumbered section
##* This is the heading of a unnumbered subsection
###* This is the heading of a unnumbered subsubsection
```

### Text

Text is written simply by writing without special prefixes. Paragraphs are created with line-breaks.

```
Here is some text. Here is some more text.

Here is some text that will be in another paragraph.
```

Text can be formatted using [basic Markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), using asterisks for italics and double asterisks for bold. You can even do in-line code (monospace font) with backticks.

```
Here is a word in *italics*, a word in **bold**, and some `in-line code`.
```

### Lists

Unordered lists can be created very intuitively with Markdown syntax.

```
Here is a list:
- This is an item
- This is another item
- Here is another one
```

You can use a variety of characters for list items.

```
You can use the following characters for list items:
- Hyphens
+ Addition Signs
* Asterixes
```

Ordered lists can be created by using a number/letter and a period.

```
My ordered list has:
1. A first item
2. A second item
3. A third item
```

Lists can also be nested using indentation, and use both ordered/unordered items.

```
Here is a list:
1. This is the first item
	a. Here is a subitem
	b. Here is another subitem
2. Here is the second main item
	- This is an unordered item
	- This is another.
```

*Note that indentation is done with 4 spaces, for the sake of consistency.*

### Equations

In-line equations can be done with dollar signs, writing maths with [LaTeX maths formatting](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols).

```
Did you know that $E = mc^2$
```

Full-line, multi-lined, and aligned equations can be written between triple dollar signs.

```
$$$
	y &= x + 4
	x &= 2
	\therefore y &= 6
$$$
```

Note here we are using the ampersand before the equals sign to specify alignment.

### Figures

Figures are specified in the same way that images are specified in Markdown.

```
![The Universe](graphics/universe.jpg)
```

This will get the image `universe.jpg` from the directory `graphics`, and add the caption "The Universe". Note that the path to images are relative (located in relation to where the source .md file is) and in POSIX format (using "/" to denote location) no matter the platform.

### Hyperlinks

Although not as popular in most LaTeX documents, hyperlinks can be specified in the same way that they are in Markdown.

```
[TeXLite](https://github.com/lucrae/texlite)
```

This will create a link labelled "TeXLite" that goes to the address `https://github.com/lucrae/texlite`.

### Document Setup

Specifiying document setup options can actually be done anywhere in the document, but makes the most sense to do at the top. Here is an example of specifying the document details for the heading:

```
:title: Solution to the Riemann Hypothesis
:author: Lucien Rae Gentil
:date: July 11, 2038
```

The lines above would set the document title to "Solution to the Riemann Hypothesis" with the author "Lucien Rae Gentil" and the date "July 11, 2038". Note that because in-line LaTeX commands can be used, you can write `\today{}` to automatically provide the current date.

More specifications are planned to be added, but here is the list so far:

- `:title:` Sets the document title.
- `:author:`. Sets the document author.
- `:date:`. Sets the document date, typically can be used with `\today{}`.
- `:abstract:`. Adds an 'abstract' section to the start of the document comprising whatever text is specified.
- `:fontsize:`. Sets the size of the font. Default is `10pt`. Options are: `8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, 20pt`. Remember to include the `pt`.
- `:margin:`. Sets the size of the margins. Default is `1.6in`. Unit must be included, and can be any one of `mm, cm, pt, in`.
- `:linespread:`. Sets the proportional spacing between lines. Default is `1.0`. One-and-a-half spacing is `1.3` and double spacing is `1.6`.
- `:usepackages:`. Includes specified packages to be used in the document. Multiple packages seperated by commas, for example: `:usepackages: hyperref, xcolor`. Note that these packages must be installed in you TeX distribution; if they're not TeXLite will not be able to compile.

## Conclusion

Hopefully this concise guide provides some useful information on what you can do with TeXLite. If you have any issues or suggestions, please add them to the [Issues](https://github.com/lucrae/texlite/issues) page on GitHub. Thank you for reading :)
