# Changelog

### v1.0.5

- Added guide (docs/guide.md) that provides instructions on TeXLite's features.
- Updated README.md to include guide as well as other useful information
- Fixed issue with Windows paths for graphics, so figures now work on all platforms.

## [Unreleased]

Versions of TeXLite in development.

### v1.1.0

- Added 'abstract' meta specification, e.g.: `:abstract: Abstract goes here`.
- Added 'usepackages' meta specification, e.g.: `:usepackages: xcolor, hyperref`
- Added command-line option `--default-packages F` to use a text (.txt) file to specify a custom set of default packages to use (one line per package name). Default is in `texlite/config/default_packages.txt`.
- Added the ability to create nested lists using (4 space) indentation.
