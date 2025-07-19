# Changelog

## Unreleased

### Added

- The version of the package is now in the log of the Cipher.

### Changed

- Stones are now called by functions in the StoneHolder, to enhance readability and repeatability.
- **Breaking**: Applying Stones:
  - Stones now apply even if it's the first letter.
  - A simple change occurs if the letter wasn't changed with the stones.
- **Breaking**: Cipher is now ignoring the spaces for the position in the message.
- **Breaking**: Cipher is now ignoring the special characters for the position in the message. Special Characters mean the chars that are now in the source alphabet.

### Removed

- *(To be Added)*

### Fix:

- Special Chars in entry text makes the encription incorrect or inconsistent. Such as ? or , in the entry text if these are not in the source alphabet, but are in the target alphabet. The cipher does not correctly skip or handle them. A patch is planned.


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
