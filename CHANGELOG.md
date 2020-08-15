# Changelog

### v1.1.4 (2020-08-10)

- Added link to repo in command-line `--help` for more information.
- Greatly improved codebase readability and internal documentation for future development.
- Cleaned up documentation.

### v1.1.3 (2020-08-04)

- Solved critical config issue with reading in default packages.

### v1.1.1 (2020-08-04)

- Cleaned up some capitalisation inconsistency.
- Decreased distribution build size by excluding some unnecessary files.

### v1.1.0 (2020-08-03)

- Added 'abstract' meta specification, e.g.: `:abstract: Abstract goes here`.
- Added 'usepackages' meta specification, e.g.: `:usepackages: xcolor, hyperref`.
- Added command-line option `--default-packages F` to use a text (.txt) file to specify a custom set of default packages to use (one line per package name). Default is in `texlite/config/default_packages.txt`.
- Added the ability to create nested lists using (4 space) indentation.

### v1.0.5 (2020-07-29)

- Added guide (docs/guide.md) that provides instructions on TeXLite's features.
- Updated README.md to include guide as well as other useful information.
- Fixed issue with Windows paths for graphics, so figures now work on all platforms.

## [Unreleased]

Versions of TeXLite in development.

### v1.1.5

- Decreased distribution build size by removing unneeded files from MANIFEST.in.
- Simplified the --help output.
- Updated README with more details on usage.
