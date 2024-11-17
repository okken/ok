# Changelog

All notable changes to this project should be documented in this file.

<!--
## [Unreleased] - yyyy-month-dd

### Added
- nothing so far

### Removed
- nothing so far

### Fixed
- nothing so far

### Changed
- nothing so far
-->

## [Unreleased] - 2024-Aug-25


## [0.1.1] - 2024-Nov-16

- break fork with pytest
- add docs/adr for Architectural Decision Records
- remove logging support
- switch to a more sane version scheme
  - not tracking pytest anymore, so having the version we forked from doesn't really help anyone

## [0.832.5] - 2024-Aug-25

### Removed
- pdb support

## [0.832.3] - 2024-Aug-24

### Removed
- doctest support
- pastebin support

## [0.832.2] - 2024-Aug-23

### Removed
- unittest support

## [0.832.1] - 2024-Aug-23

### Corresponding pytest
- This initial version of `ok` is branched from pytest 8.3.2
- Thus the "sort of makes sense" version of 0.832.1
- For now, keeping the middle digit of the version corresponding
  to the pytest version seems to make sense

### Added
- _version - hopefully temporary hack, as setuptools-scm is not used, 
  but some parts of the system refer to it.

### Removed
- removed folders .githbub, doc, bench, extra, changelog, scripts
- removed all top level .rst files
- removed some other stuff. Nothing functional yet.

### Changed
- CHANGELOG, README, CONTRIBUTING - all changed and now .md files
- pyproject.toml - version is static now, and 0.832.0
- test_config.py - needed mods to minversion since our version changed.
- test_entry_points.py - remove py.test, add ok

### Test status
- tox -e py312 passes on my mac
- no CI set up yet
