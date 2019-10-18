
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- pipenv
- clarified class names for web services (rather than template views)
  - OpenBaseView -> OpenService
  - AuthBaseView -> AuthService
- mypy static type checking
- isort import sorting
- autoflake removing unused import


## [0.1.0] - 2019-05-04

### Added

- refactored common functionality to decorators
- added `wrapt` dependency

## [0.0.2] - 2019-03-07

### Added

- refactor to `OpenBaseView` and `AuthBaseView` base classes
- `execute_on_request`

## [0.0.1] - 2019-03-03
- Conception!

[Unreleased]: https://github.com/iancleary/responder-base-classes/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/iancleary/responder-base-classes/releases/tag/v0.1.0
[0.0.2]: https://github.com/iancleary/responder-base-classes/releases/tag/v0.0.2
[0.0.1]: https://github.com/iancleary/responder-base-classes/releases/tag/v0.0.1
