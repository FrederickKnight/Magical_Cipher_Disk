# Changelog

## [2.1.0] - 27-07-2025

### Added
- Added validations for each model using pydantic.

### Changed

- Migrated to Pydantic for model construction and validation.
- Introduced a getter method for splits in Disk class, to return a safe copy. This was early on but it was removed.
  
### Removed

- Disk
  - Removed custom from_dict and to_dict methods in favor of model_dump and **data unpacking.
  - Removed property methods for seed and splits; now handled directly as fields.


## [2.0.1] - 22-07-2025

### Fixed:
- Error with the build of the package, Stones Files now are being added correctly to the package

## [2.0.0] - 20-07-2025

### Added

- The version of the package is now in the log of the Cipher.
- Warning for the bug of the special characters in the Cipher.

### Changed

- Stones are now called by functions in the StoneHolder, to enhance readability and repeatability.
- **Breaking**: Applying Stones:
  - Stones now apply even if it's the first letter.
  - A simple change occurs if the letter wasn't changed with the stones.
- **Breaking**: Cipher is now ignoring the spaces for the position in the message.
- **Breaking**: Cipher is now ignoring the special characters for the position in the message. Special Characters mean the chars that are now in the source alphabet.

### Fixed:

- Special Chars in entry text makes the encription incorrect or inconsistent. Such as ? or , in the entry text if these are not in the source alphabet, but are in the target alphabet. The cipher does not correctly skip or handle them. A patch is planned.


## [1.0.0] - 14-07-2025

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
