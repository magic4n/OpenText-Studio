# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-01-01

### Added
- Initial public release by magic4n.
- 5×5 bitmap font with Latin, Cyrillic, digits and punctuation.
- ANSI Shadow font for block-letter banners.
- Boxed panel renderer.
- 16 ANSI colors and 4 gradients (`fire`, `ocean`, `forest`, `rainbow`).
- 11 animation types: `typewriter`, `pulse`, `rainbow_sweep`, `fade_in`,
  `slide_left`, `blink`, `row_by_row`, `wave`, `sparkle`, `gradient_cycle`,
  `logo_animated`.
- Automatic output folder naming (5 random digits) with `text/` and `anim/`
  subfolders.
- Windows 10+ ANSI (VT) auto-enable.
- UTF-8 output reconfiguration for Cyrillic on all platforms.
- Runnable / embeddable animation modules with `animate(**kwargs)` entry point.
