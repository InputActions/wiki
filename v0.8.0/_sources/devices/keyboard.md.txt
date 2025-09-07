# Keyboard
:::{list-table}
* - **Supported gestures**
  - [](/gestures/shortcut)
:::

## Scancodes
InputActions uses scancodes only. On non-QWERTY layouts, scancodes may map to different keycodes than expected (e.g. on a QWERTZ layout, the ``y`` scancode
will map to the ``z`` keycode).

Shortcut gestures are not affected by the current keyboard layout, but keyboard [input actions](/actions/input.md) are, and will not work well if multiple
layouts are in use.

The ``evtest`` utility can be used to obtain scancodes of pressed keys.

See <project:/misc/keyboard-scancodes.md>.