# Packaging guidelines
InputActions should be packaged into the following packages:
- ``inputactions-ctl``- Control tool

  Repository: [InputActions/ctl](https://github.com/InputActions/ctl)

- ``inputactions-kwin`` - KWin plugin implementation

  Repository: [InputActions/kwin](https://github.com/InputActions/kwin)<br>
  Dependencies: ``inputactions-ctl``

- ``inputactions-standalone`` - Standalone implementation

  Repository: [InputActions/standalone](https://github.com/InputActions/standalone)<br>
  Dependencies: ``inputactions-ctl``

  The package must create an ``inputactions`` system group. ``inputactions-client`` must be owned by that group and have the setgid bit.

As GitHub does not include submodules in release tarballs, every release starting from v0.9.0 will have a manually generated one that does include them.