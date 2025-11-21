# Packaging guidelines
InputActions should be packaged into the following packages:
- ``inputactions`` - Standalone implementation

  Build flags: ``-DINPUTACTIONS_BUILD_STANDALONE=ON``

  Dependencies: ``inputactions-ctl``
- ``inputactions-ctl`` - Control tool

  Build flags: ``-DINPUTACTIONS_BUILD_CTL=ON``
- ``inputactions-kwin`` - KWin plugin

  Build flags: ``-DINPUTACTIONS_BUILD_KWIN=ON``

  Dependencies: ``inputactions-ctl``