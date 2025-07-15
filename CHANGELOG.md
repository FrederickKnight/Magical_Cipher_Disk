# Changelog

## Unreleased

### Added

- Ability to reconstruct `Disk` and other components from JSON-like sources.
- Support for more `Stone` colors.
- New encryption methods.

### Changed

- *(To be Added)*

### Removed

- *(To be Added)*


## 1.0.0 - 14-07-2025

### Added

- Stones: `Yellow`, `Blue` and `Red-Green`.
- CipherIO: Handles the saving and logging of the `Cipher`.
- StoneHolder: Applies `Stones` and keep record of the steps.

### Changed

- `Stone` class is now `BaseStone`.
- The `Stones` are now extended clases of `BaseStone`, each can have its own behaviour.
- The behavior of `Stones` is now handled by `StoneHolder`.
- Refactor of `Disk`.
- Refactor of `Cipher`.

### Removed

- Removed support for "Series" in `Disk` (now deprecated).