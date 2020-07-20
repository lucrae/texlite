title: Using \TeX{}Lite
author: Lucien Rae Gentil

# Standard writing

Standard writing and headings can all be done in markdown syntax. For example here is some **bold text** and a word in *italics*. You can even do `in-line code snippets`.

# Beyond standard writing

If you want to do anything beyond markdown, all standard in-line \LaTeX{} commands can be used seamlessly. For example I'm writing this on \today{}.

## Maths

In-line maths can be written just how you'd expect, for example $c^2 = a^2 + b^2$.

## Extra notes

Some things that are a bit fiddly in LaTeX are cleaned up, things like "automatically-directioned double quotation marks" are all taken care of.

# Specifying document details

Document detail options are specified at the top of the document in the format "`<option>: <specification>`", with one line for each option. For example, the line "`title: My Awesome Paper`" will set the document title to "My Awesome Paper".

# More Markdown

Note that \TeX{}Lite utilises just an essential set of Markdown's syntax and elements, so some features in the extended syntax (such as custom heading IDs, fenced code blocks, and definition lists as of writing this) don't have special meaning. \TeX{}Lite still uses the `.md` format so you don't have to put any extra effort to get nice syntax highlighting in your editor.

## Unordered lists

Unnordered lists are:
- Written using hypens
- Really easy to create

## Ordered lists

Ordered lists are:
1. Written using numbers
2. Also really easy
3. Just the same as in Markdown

## Horizontal rules

Horizontal rules, written in Markdown with three hyphens, don't really have a place in standard LaTeX. In \TeX{}Lite they can instead be used for paragraph spacing, equivalent to the "medskip" command.