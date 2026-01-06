# Installation
For [Hyprland](/getting-started/installation/hyprland.md) and [Plasma Wayland](/getting-started/installation/kwin.md), the compositor plugins are
recommended, as currently they are the most reliable. It is necessary to rebuild them on every compositor update.

For other environments (including those mentioned above) there is a [standalone](standalone) implementation that operates at evdev level. It is still a work
in progress.

## Feature comparison
This table only lists features that are not available in all implementations.

:::{list-table}
:header-rows: 1

* -
  - GNOME
  - Hyprland
  - Plasma (Wayland)
  - Plasma (Wayland, X11)
  - Other (Wayland)
  - Other (X11)

* - InputActions implementation
  - [Standalone](/getting-started/installation/standalone.md) + extension
  - [Hyprland](/getting-started/installation/hyprland.md) (compositor plugin)
  - [KWin](/getting-started/installation/kwin.md) (compositor plugin)
  - [Standalone](/getting-started/installation/standalone.md) + script
  - [Standalone](/getting-started/installation/standalone.md)
  - [Standalone](/getting-started/installation/standalone.md)

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **General**
  -
  -
  -
  -
  -
  -

* - Multi-session support
  - ✅<sup>[1]</sup>
  - ✅
  - ✅
  - ✅<sup>[1]</sup>
  - ✅<sup>[1]</sup>
  - ✅<sup>[1]</sup>

* - Compatibility with other input tools
  - ?<sup>[2]</sup>
  - ✅<sup>[3]</sup>
  - ✅<sup>[3]</sup>
  - ?<sup>[2]</sup>
  - ?<sup>[2]</sup>
  - ?<sup>[2]</sup>

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **[InputAction](/actions/input.md)**
  -
  -
  -
  -
  -
  -

* - Keyboard text action
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **Touchpad**
  -
  -
  -
  -
  -
  -

* - Accelerated gestures
  - ✅
  - ❌
  - ❌
  - ✅
  - ✅
  - ✅

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **Touchscreen**
  -
  -
  -
  -
  -
  -

* - Support
  - ✅
  - ❌
  - ✅ (6.5+)
  - ✅
  - ✅
  - ✅

* - Window under fingers info (``window_under_fingers_`` variables)
  - ❌
  - ❌
  - ✅
  - ❌
  - ❌
  - ❌

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **[Variables](/variables.md)**
  -
  -
  -
  -
  -
  -

* - ``cursor_shape``
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - ``plasma_overview_active``
  - ❌
  - ❌
  - ✅
  - ❌
  - ❌
  - ❌

* - pointer position variables
  - ✅
  - ✅
  - ✅
  - ✅
  - ❌
  - ❌

* - ``screen_name``
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **Windows**
  -
  -
  -
  -
  -
  -

* - Active window info
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window under pointer info
  - ✅
  - ✅
  - ✅
  - ✅
  - ❌
  - ❌

* - Window resource class (``window{_under_pointer}_class`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window resource name (``window{_under_pointer}_name`` variable)
  - ✅
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌

* - Window fullscreen state (``window{_under_pointer}_fullscreen`` variable)
  - ✅
  - ❌
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window maximized state (``window{_under_pointer}_maximized`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window title (``window{_under_pointer}_title`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌
:::

1. Each virtual terminal has its own InputActions session.

2. InputActions will conflict with any program that grabs input devices and creates virtual ones. Virtual input devices created by InputActions need to be
   blacklisted in such tools if possible. InputActions can be configured to ignore and not grab specific devices in order to let other tools process their
   events first.

3. InputActions blocks input events in the compositor. Event generation also occurs in the compositor and tools operating at evdev level do not receive such
   events.

```{toctree}
:maxdepth: 1
:hidden:

Hyprland <hyprland>
KWin <kwin>
Standalone <standalone>
```
