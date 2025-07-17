# Changelog

## Unreleased

### Added

- *(To be Added)*

### Changed

- Stones are now called by functions in the StoneHolder, to enhance readability and repeatability.
- **Breaking**:Applying Stones:
  - Stones now apply even if it's the first letter.
  - A simple change occurs if the letter wasn't changed with the stones.

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
