title: Overview of \TeX{}Lite
author: Lucien Rae Gentil
linespread: large

# Standard writing

Standard writing and formatting can all be done using markdown syntax. For example here is some **bold text** and a word in *italics*. You can even do `in-line code snippets`.

# Beyond standard writing

If you want to do anything beyond markdown, all standard in-line \LaTeX{} commands can be used seamlessly. For example, I'm writing this on \today{} and here are some words in \textsc{small caps}.

## In-line maths

In-line maths is written between dollar signs (\$). Did you know that $e^{\pi i} + 1 = 0$?

## Equations

I am working on this.

# Document details

Document detail options are specified at the top of the document in the format "`<option>: <specification>`", with one line for each option. For example, the line "`title: My Great Paper`" will set the document title to "My Great Paper".

# Sections

Like Markdown headings, sections are denoted using the hash (\#) character, using more hashes for deeper section levels (section, subsection, subsubsection).

###* Unnumbered sections

Unnumbered sections can be done simply by adding an asterix directly next to the hash. For example, \texttt{\#* }is equivalent to \texttt{section*} in LaTeX.

# More Markdown

Note that \TeX{}Lite utilises just an essential set of Markdown's syntax and elements, so some features in the extended syntax (such as custom heading IDs, fenced code blocks, and definition lists as of writing this) don't have special meaning. \TeX{}Lite still uses the `.md` format so you don't have to put any extra effort to get nice syntax highlighting in your editor.

## Unordered lists

Unnordered lists can be written using:
- Hyphens
+ Addition signs
* Asterixes

## Ordered lists

Ordered lists are:
1. Written using numbers
2. Just the same as in Markdown

## Hyperlinks

Using the `hyperref` LaTeX package, hyperlinks can be used just as they are in Markdown. For example, here is a link to [my website](https://lucienrae.com/).

## Horizontal rules

Horizontal rules, written in Markdown with three hyphens, don't really have a place in standard LaTeX. In \TeX{}Lite they can instead be used for paragraph spacing, equivalent to the "medskip" command.

# Extra notes

Some things that are a bit fiddly in LaTeX are cleaned up, things like "automatically-directioned double quotation marks" are all taken care of.